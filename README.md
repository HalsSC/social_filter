# にゃーん(social_filter)
社会性フィルターをCOTOHA APIを使って適用する

## にゃーん(COTOHA_API.py)
COTOHA APIの操作ライブラリ
+ 具体例:以下のようにすることで固有表現の解析ができる
~~~
from COTOHA_API import CotohaApi

DEVELOPER_API_BASE_URL = "https://api.ce-cotoha.com/api/dev/nlp/"
ACCESS_TOKEN_PUBLISH_URL = "https://api.ce-cotoha.com/v1/oauth/accesstokens"
CLIENT_ID = "XXXXXXXXXXXXXXXXXXXXXXXXXx"
CLIENT_SECRET = "xxxxxxxxxxxxxxxxxx"

cotoha_api = CotohaApi(CLIENT_ID,CLIENT_SECRET,DEVELOPER_API_BASE_URL,ACCESS_TOKEN_PUBLISH_URL)
result = cotoha_api.ne(sentence)
print(result['result'])
~~~

## にゃーん(social_filter.py)
社会性フィルターを適用するプログラム
+ 手順
1. 固有表現を抽出し「その他」と判断されたもの以外すべて"にゃーん"に置きかえる
2. 感情分析によりNegativeと判断した部分を"にゃーん"に置き換える
3. 結果を出力
