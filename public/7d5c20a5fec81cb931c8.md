---
title: '【Git】fatal: protocol error: bad line length character: usag の解消方法'
tags:
  - Git
private: false
updated_at: '2020-03-01T21:56:49+09:00'
id: 7d5c20a5fec81cb931c8
organization_url_name: null
slide: false
ignorePublish: false
---
# はじめに

develop ブランチが更新されたので、pull しようとしたら、
`fatal: protocol error: bad line length character: usag` 
が発生しました。
なかなか解決できず、2時間ほど時間を無駄にしました。

最初に結論からいうと、

###.gitconfig を見直そう！！！！

# 環境

- macOS Catalina バージョン10.15.2
- git 2.21.1

# やったこと

- .bashrc の見直し（効果なし）
- git のアップデート（効果なし）
- 対象のブランチを削除して、取得し直す（効果なし）
- プロジェクトを clone し直す（効果なし）
- 仮想環境で clone してから ローカルに持ってくる（効果なし）
- .gitconfig を見直す

# .bashrc の見直し（効果なし）

参考文献より、

> ググってみると、リモート先のサーバーにsshでログインする時に表示されるメッセージが悪いとか、
> ssh関連で、.bashrcとか.zshrcとかの設定を見なおしたよ、というような内容が多い。

でした。
ただ、自分の Mac の Terminal は fish を使っています。
bash も zsh も使っていません。

念のため、.bashrc を確認しましたが、何も書かれていませんでした。
さらに念のため、.bashrc を消してみましたが、改善しませんでした。

# git のアップデート（効果なし）

git のバグかと思ったので、 git のアップデートしました。
mac で HomeBrew を使用している方は、下記のコマンドでアップデートできます。

```shell
brew update
brew install git
```

XCode の CommandLineTools での git を使っている方は、 which コマンドで path が合っているか確認しましょう。

```shell
which git
# /usr/local/bin/git となっていれば OK
```

これでは改善しませんでした。

# 対象のブランチを削除して、取得し直す（効果なし）

今回は develop ブランチを pull しようとしたときに発生しました。
なので、 develop を削除して、取得し直そうと思いました。

```shell
git checkout master
git branch -D develop
git checkout -b develop origin/develop
```

これでももちろん改善せず。

# プロジェクトを clone し直す（効果なし）

この際ヤケクソです。
プロジェクトを新たに clone することにしました。

```
git clone https://github.com/<ユーザー名>/<プロジェクト名>.git
```

ここでも、`fatal: protocol error: bad line length character: usag` が発生しました。
そこで、git そのものがバグっていると気づきました。

# .gitconfig を見直す

```shell
rm ~/.gitconfig
touch ~/.gitconfig
git config --global user.email example@example.com
git config --global user.name example
```

と、.gitconfig を削除して、name と email を設定し直しました。
これで、エラーが発生しなくなり、clone も pull もできるようになりました。

# 最後に

どのタイミングでバグったのが気になるところですが、無事解消することができました。

# 参考文献

[[エラー] bad line length character: Sysl - KayaMemo](http://kayakuguri.github.io/blog/2014/07/28/git-heroku-error/)
