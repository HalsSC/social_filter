import os
import urllib.request
import json
from COTOHA_API import CotohaApi

DEVELOPER_API_BASE_URL = "https://api.ce-cotoha.com/api/dev/nlp/"
ACCESS_TOKEN_PUBLISH_URL = "https://api.ce-cotoha.com/v1/oauth/accesstokens"
CLIENT_ID = "XXXXXXXXXXXXXXXXXXXXXXXXXx"
CLIENT_SECRET = "xxxxxxxxxxxxxxxxxx"

meow = "にゃーん"

if __name__ == '__main__':
    # COTOHA APIインスタンス生成
    cotoha_api = CotohaApi(CLIENT_ID, CLIENT_SECRET,DEVELOPER_API_BASE_URL, ACCESS_TOKEN_PUBLISH_URL)

    # 解析対象文を入力
    sentence = input("input>")
    sen_old = sentence

    # 固有表現解析API実行
    result = cotoha_api.ne(sentence)

    # 固有名詞の除去
    for res in result['result']:
        if res['class'] != "OTH":
            sentence = sentence.replace(res['form'], meow)

    # 感情分析API実行
    result = cotoha_api.sentiment(sentence)

    # マイナス(Negative)な表現の除去
    for emo in result['result']['emotional_phrase']:
        if emo['emotion'] in ["怒る", "悲しい", "不安", "恥ずかしい", "嫌", "N"]:
            sentence = sentence.replace(emo['form'], meow)

    # 整形して表示
    print("\noutput>{}\n".format(sentence))
