---
title: 【Slack】Slack API を使用してメッセージを飛ばすまでの手順
tags:
  - Slack
  - slack-api
private: false
updated_at: '2020-04-27T21:47:07+09:00'
id: e2165c5a30eac498f345
organization_url_name: null
slide: false
ignorePublish: false
---
# App を新規作成

https://api.slack.com/apps にアクセス。
**Create an App** ボタンを押します。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/35d101fe-a9a9-b7d4-a6ff-3f67d13557b4.png)


**App Name** は 適切なアプリ名をつけてください。
今回は「SlackMessageTest」と名付けています。

**Development Slack Workspace** は、紐付ける Slack のワークスペースを指定してください。
今回は「RiekureAlone」を指定しています。

入力が終わったら **Create App** ボタンを押します。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/e39e6fd7-18dd-b672-fced-f4092fc982ff.png)

そして下のような画面に遷移します。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/6c5b329f-ad10-f8c2-1fa4-d5f9e487bc0e.png)

# API でメッセージを送信できる権限を追加

**Permissions** を押します。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/0ffb5234-863a-a0cb-eff4-a1ed11a3cc97.png)

下にスクロールして、 **Scope** の **Add on OAuth Scope** を押します。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/ad16e791-8e34-f8bd-94ad-667abc2ae77d.png)

**chat::write** を選択します。 
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/1fd6866e-1dbd-8e6c-f7ab-cb7029284084.png)

選択したらこんな画面になります。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/090cbf7c-db41-179f-5988-7b87572003e3.png)

# ワークスペースにインストール

ページの先頭の **Install App to Workspace** を押します。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/2775ab5b-b84a-ee24-0149-d1b6f652142b.png)

**許可** を押します。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/79f8f252-7da5-8e9a-5110-303079525def.png)

成功すると、 **Access Token** が発行されるので、メモしておきます。
（スクショで黒く塗りつぶしているところです。）
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/d4b79bb7-61fe-b305-3b64-4886614f8ee9.png)

# チャンネルに対して App を追加

App を追加したいチャンネルを選択して、 **アプリを追加する** を押します。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/09b4adf7-af2f-9c0c-84d7-63bbe6dcec7f.png)

作ったアプリを選択します。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/50963933-f12f-553c-b429-c6e548bfc86e.png)

# 動作確認

https://api.slack.com/methods/chat.postMessage/test
で正常にメッセージを送信できるか確認します。

とりあえず Arguments で Required に設定されている項目を埋めます。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/686ea688-d145-271b-5e02-2ff8a8538345.png)

入力したら、下にスクロールして **Test Method** を押します。
うまくできたら、 Slack にメッセージが飛ぶことを確認してください。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/783e5cb7-ddc7-75e9-6fe5-2065cb053e06.png)




