import pandas as pd
import requests

# CSVファイルを読み込む
df = pd.read_csv('sample_employees.csv')

# 'employee_id'と'temp_password'の列だけを取り出す
df = df[['employee_id', 'onetime_code']]

# DataFrameを辞書のリストに変換する
dict_list = df.to_dict('records')

# アクセストークンを取得するためのメソッド
def get_access_token():
  url = "http://host.docker.internal:8080/realms/master/protocol/openid-connect/token"
  params = {
    "client_id": "admin-cli",
    "username": "admin",
    "password": "admin",
    "grant_type": "password"
  }
  response = requests.post(url, data=params)
  data = response.json()
  return data['access_token']

access_token = get_access_token()

# ユーザーを作成するためのメソッド
# ユーザを表すパラメータは以下の通り
# '{ "username": "username", "enabled": "true", "credentials": [{"type": "password", "value": "onetime_code", "temporary": true }]}
def create_user(employee_id, onetime_code, access_token):
  url = "http://host.docker.internal:8080/admin/realms/plain/users"
  user_json = {
    "username": employee_id,
    "enabled": "true",
    "credentials": [{"type": "password", "value": onetime_code, "temporary": True}]
  }
  # post user
  headers = {"Authorization": f"Bearer {access_token}"}
  response = requests.post(url, json=user_json, headers=headers)
  if response.status_code != 201:
    print(f"Failed to create user {employee_id}. Status code: {response.status_code}")
  else:
    print(f"Successfully created user {employee_id}")

# ユーザーを作成する
for user in dict_list:
  create_user(user['employee_id'], user['onetime_code'], access_token)  