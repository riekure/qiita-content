---
title: Aurora(MySQL)でCREATE VIEWしたらエラーが出た
tags:
  - MySQL
  - AWS
private: false
updated_at: '2018-04-10T09:28:36+09:00'
id: 0b32174fced2533da4ab
organization_url_name: null
slide: false
ignorePublish: false
---
# 初めに
Auroraを使って環境構築したときにビューを作成しようとして失敗した。
解決にかなり時間がかかってしまったので、今後忘れないようにメモ書き。  
# 状況  
前環境の構築に使ったCREATE VIEWを実行すると、以下のエラーが出て失敗した。
(権限がないと怒られた…)   
## 怒られたSQL
```sql
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`192.0.2.0:80` SQL SECURITY DEFINER VIEW `example_view` AS ~
```
## エラーメッセージ
```
Access denied; you need (at least one of) the SUPER privilege(s) for this operation
```
# 原因と対処方法  
元々のSQLではユーザの後にIPアドレスを指定していた。
Auroraの場合は、IPアドレスではなく、\`%`を指定する必要があった。
## 実行すべきだったSQL
```sql
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `example_view` AS ~
```
AWSの知識はもちろん、SQLの知識も不足しすぎてて調査に無駄に時間がかかった。
Amazon RDSでのMySQLでは、rootユーザでもSUPER権限を持っていないらしい。
今までAWSをまともに触ったことがなかったので、ちょっと勉強になった。  
