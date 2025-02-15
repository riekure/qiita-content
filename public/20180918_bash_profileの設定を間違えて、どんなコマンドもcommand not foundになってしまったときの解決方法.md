---
title: .bash_profileの設定を間違えて、どんなコマンドも"command not found"になってしまったときの解決方法
tags:
  - Bash
  - Linux
  - CentOS
private: false
updated_at: '2018-09-18T13:40:00+09:00'
id: 673e255e6a143fc4ef7d
organization_url_name: null
slide: false
ignorePublish: false
---
# はじめに
サーバの設定をいろいろと変更しているときに、Linuxの環境変数を触っていました。
そのときに失敗してしまい、```ls```とか```vi```とか、標準的なコマンドを入力しても"command not found"になってしまいました。
その際に、実施した復旧方法を記載しています。

# 環境
- EC2
- Cent OS 7

# 対処方法①：rootユーザに切り替える

rootユーザに切り替えて、間違えて編集してしまった.bash_profileを修正する方法です。

```
$ su -
```

あとは使いたいコマンドのパスが通っているか確認します。

```
$ which ls
$ which vi
```

あとは、ゆっくり.bach_profileを修正します。

```
$ vi .bash_profile
```

編集し終わったら、.bash_profileを再読込します。

```
$ source .bash_profile
```

# 対処方法②：exportで各種コマンドを実行できるようにする

exportコマンドで$PATH（パス）を通します。

```
$ export /bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:/home/(ユーザ名)/bin
```

上記のコマンドを実行すると、各種コマンドが使用できるようになっているはずです。
あとは、ゆっくり.bash_profileを修正し直します。

# あとがき

AWSの勉強中にやらかしました。
インスタンス削除して一からやり直さないといけないのか…？ってめっちゃ焦りました。

他にも方法はありそうですが、今回実施した2つの方法を記載しました。

