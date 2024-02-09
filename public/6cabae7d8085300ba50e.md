---
title: ChromeでAWS Cloud9に接続できないときの対処方法
tags:
  - Chrome
  - AWS
  - 初心者
  - cloud9
private: false
updated_at: '2019-12-13T12:10:59+09:00'
id: 6cabae7d8085300ba50e
organization_url_name: null
slide: false
ignorePublish: false
---
# はじめに

Ruby On Railsの学習のため、AWS Cloud9を使っています。
その学習中にCloud9に接続できなくなってしまいました。

その際に試した対処法をまとめます。

# 環境

- OS：MacOS Mojave バージョン 10.14.6
- ブラウザ：Chrome バージョン76

# 事象

Cloud9を開いていたタブを閉じて、数分後にまたCloud9にアクセスしたときに発生しました。
表示されたメッセージは以下になります。

```
This is taking longer than expected. If you think there might be an issue, contact AWS Support.
It might be caused by VPC configuration issues. Please check documentation.
```

※ スクショはとっていませんでした…

# やったこと

- Chromeのキャッシュを削除（変化なし）
- Chromeのバージョンアップ確認（そもそもバージョンアップなし）
- EC2の再起動（変化なし）
- 使用するブラウザを変更

# 使用するブラウザを変更

Chromeではなく、Safariを使用したら正常にアクセス、使用することができました。
Firefoxでも正常にアクセスできました。

ちなみに、後日Chromeで接続しても、正常にアクセスすることができました。
