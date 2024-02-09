---
title: 特定のファイルをrmコマンドなどで削除できないようにする方法(chattr、lsattrコマンド)
tags:
  - Bash
  - Linux
  - CentOS
private: false
updated_at: '2018-12-12T10:36:02+09:00'
id: 6def7f813ebe03dd5850
organization_url_name: null
slide: false
ignorePublish: false
---
# 背景
例外処理のテストパターン消化のために必要になりました。
後輩にどうやれば実現できるのか、間違った説明をしてしまったので、戒めとして書きます。

# 動作環境

- Amazon EC2
- Cent OS 7

# ファイル権限000でも削除できてしまう

ファイルの権限を ```chmod 000``` としていたとしても、特定の条件を満たしていれば削除できます。
それは、**ファイルを配置しているディレクトリに対する書き込み権限**があることです。
ディレクトリに対する書き込み権限があれば、ディレクトリ直下にあるファイルは削除できます。
たとえ、読み込み／書き込み／実行権限がなくてもです。

# じゃあどうするか

## 1. ディレクトリの書き込み権限をなくす

chmodコマンドでディレクトリの書き込み権限をなくせばいいです。
chmodコマンドについては、調べればたくさん参考文献が出てくるので、省略します。

でも、ディレクトリの書き込み権限をなくしたら困る！という場合もあると思います。
そんなときは```chattr``` コマンドを使用しましょう。

## 2. chattrコマンドを使用する

下記のようなコマンドを実行すると、削除することができなくなります。

```
$ chattr +i 対象ファイル
```

実際にやってみると、下のようになります。

```
$ cd /tmp
$ ls -al
合計 XX
drwxrwxr-x. 2 riekure riekure  4096 12月 12 09:45 .
drwxrwxr-x. 3 riekure riekure    19 11月 19 16:32 ..
-rw-rw-r--. 1 riekure riekure     0 12月 12 09:45 temp.txt
$ chattr +i temp.txt
$ rm -f temp.txt
rm: `temp.txt' を削除できません: 許可されていない操作です
```

また削除できるようにするためには、 ```-i``` オプションを指定してください。

```
$ chattr -i 対象ファイル
```

削除できなくなっているかは、```lsattr``` コマンドで確認することができます。

```
$ lsattr
----i----------- ./temp.txt
```

全てがハイフンならば、ファイルの属性は変更されていません。

以下、[参考文献](https://kazmax.zpp.jp/cmd/c/chattr.1.html)より、変更できるファイル属性の一覧です。

| 属性 | 効果 |
| :--- | :--- |
| a | 追加のみ許可 (append only) |
| c | 圧縮 (compressed) |
| i | 変更不可 (immutable) |
| j | データのジャーナリング (data journalling) |
| s | 安全な削除 (secure deletion) |
| t | 末尾マージをしない (no tail-merging) |
| u | 復活可能 (undeletable) |
| A | atime を更新しない |
| D | ディレクトリの同期更新 (synchronous directory updates) |
| S | 同期更新 (synchronous updates) |
| T | ディレクトリ階層のトップ |

# 参考文献
[chattr - コマンド (プログラム) の説明 - Linux コマンド集 一覧表](https://kazmax.zpp.jp/cmd/c/chattr.1.html)
[あんまり知られてないコマンドオブザイヤー「lsattr」と「chatter」のお話 - 美徳という名の背徳](https://blog.hyec.jp/2013/09/06/lsattrchatter/)
