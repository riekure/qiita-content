---
title: WindowsにWindows Subsystem for Linux（WSL）を入れてfish導入するまで
tags:
  - Windows
  - fish
  - WSL
private: false
updated_at: '2021-01-18T10:33:10+09:00'
id: a42186a8b1905cd4d4a3
organization_url_name: null
slide: false
ignorePublish: false
---
# 環境
Windows 10 バージョン1909
# WSLを入れる

スタートボタンを右クリック
「アプリと機能(F)」を押す
プログラムと機能を押す
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/a938e6d2-acce-6414-22dc-8558ca8071fe.png)
Windows の機能の有効化または無効化
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/9be03398-f994-5008-21c5-df6b12a974f4.png)
Linux 用 Windows サブシステム にチェックを入れてPCを再起動
（他の記事にあるWindows Subsystem for Linuxはなかった）
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/103c895b-a1a8-717c-57b5-5385cdab4914.png)
Microsoft Storeを開く
検索窓にUbuntuと入力して検索
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/5f87dd55-718c-527b-16c8-c5fd1440c79a.png)
どの Ubuntu を選択しても良いと思うが、今回は「Ubuntu 20.04 LTS」をインストール

Ubuntu を起動して、少し待つとユーザー名とパスワードを入力する
Linux 経験者なら慣れていると思いますが、不慣れな人でも英語が読めれば大丈夫。
英語が読めなければ、コピペしてGoogle翻訳なりDeepL翻訳に突っ込んで頑張りましょう。
コピペは、範囲選択して右クリックです。

このような画面が表示されればOK
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/f8f33db8-acea-bcd6-d32b-5e51275a17e5.png)

Ubuntuをインストールしたら、下記のコマンドを実行してパッケージを最新化しましょう。

```shell
sudo apt-get update
```

# fish をインストール
fish shell をインストールしましょう。

```shell
sudo apt-add-repository ppa:fish-shell/release-2
sudo apt-get install fish
```

ちゃんとインストールできたか確認するために、バージョンを確認するコマンドを実行しましょう。

```shell
fish --version
```

デフォルトで使用するシェルを fish に変更します。

```shell
chsh -s /usr/bin/fish
```

```fish, version 3.1.0``` のようにバージョン情報が返ってくればOKです。

# fisher をインストール

fisher をインストールしましょう。
fish 用のパッケージマネージャです。
fish を色々とカスタマイズするために必要です。

```shell
curl https://git.io/fisher --create-dirs -sLo ~/.config/fish/functions/fisher.fish
```

これで色々カスタマイズできるようになりました。
下のリンクから好みのカラーテーマを入れてみましょう。
https://github.com/oh-my-fish/oh-my-fish/blob/master/docs/Themes.md
自分は、例として「bobthefish」をいれてみます。

```shell
fisher install oh-my-fish/theme-agnoster
```

# 終わりに
慣れていないせいか、すごく使いづらい。
