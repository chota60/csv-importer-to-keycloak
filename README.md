# これは
なんかツール類を保存しとく

# ユーザのインポート
- input: csv
- plain realm に入れる

雑だが　python によってalt shell を作る

## 設計イメージ
- csv 読み込み
- リストにしておく
    - username, password
- ユーザの数だけループ
    - token 取得
      - token を変数へ
    - ユーザ登録
      - username, password , token を利用して HTTP request を送る

これで終わる感じがする

