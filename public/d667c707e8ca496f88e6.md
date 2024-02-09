---
title: Amazon Linux 2でmysql-serverがインストールできないときの対処方法
tags:
  - MySQL
  - AWS
  - EC2
  - AmazonLinux
private: false
updated_at: '2018-10-01T08:12:57+09:00'
id: d667c707e8ca496f88e6
organization_url_name: null
slide: false
ignorePublish: false
---
# 背景

AWSの勉強中、DBサーバ用のEC2インスタンスを用意しました。
1年間無料で使い放題とのことだったので、OSはAmazon Linux2です。
その際に、mysqlがインストールできず、苦戦しました。
そのときの解決方法です。

# 動作環境
OS：Amazon Linux 2

# 事象

下記のように、「パッケージ mysql-serverは利用できません。」というメッセージが出力されてしまいました。

```
$ sudo yum -y install mysql-server
読み込んだプラグイン:extras_suggestions, langpacks, priorities, update-motd
amzn2-core                                               | 2.4 kB     00:00     
amzn2extra-docker                                        | 1.3 kB     00:00     
(1/4): amzn2-core/2/x86_64/updateinfo                      |  47 kB   00:00     
(2/4): amzn2extra-docker/2/x86_64/primary_db               |  29 kB   00:00     
(3/4): amzn2-core/2/x86_64/primary_db                      |  22 MB   00:00     
(4/4): amzn2-core/2/x86_64/group_gz                        | 2.4 kB   00:00     
パッケージ mysql-server は利用できません。
エラー: 何もしません
```

# 解決方法

どうやら、デフォルトで入ってるmariaDBと競合する場合があるということで、下記のコマンドを実行。

```
$ sudo yum remove mariadb-libs
$ sudo yum localinstall http://dev.mysql.com/get/mysql57-community-release-el7-7.noarch.rpm
$ sudo yum -y install mysql-community-server
```

バージョン確認のコマンドを実行して、正常に出力されればOKです。

```
$ mysqld --version
```



# 参考文献
[第10回　yum, rpmインストールにおけるMySQL 5.6とMySQL 5.7の違い](http://gihyo.jp/dev/serial/01/mysql-road-construction-news/0010)
[CentOS7 mysqlがインストールできない](http://americandog1993.hatenablog.jp/entry/2017/07/22/013708)
