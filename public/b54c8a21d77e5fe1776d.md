---
title: 【Oracle】テーブルのカラム情報をSQLで取得する方法
tags:
  - SQL
  - oracle
  - Oracle11g
private: false
updated_at: '2019-03-23T11:48:00+09:00'
id: b54c8a21d77e5fe1776d
organization_url_name: null
slide: false
ignorePublish: false
---
# 背景

普段の開発中の場合、SQLクライアント（GUIツール？）を使用していれば、カラム情報の取得は困らないと思います。
GUIでぱぱっと表示できます。

しかし、SQLを使って、カラム情報を取得したい状況があるかもしれません。
そんな状況があったので、せっかくなので記事に残そうと思いました。

# 動作確認環境

- Oracle 11g
- SQL Developer

# SQL

```sql
SELECT
  column_name
  , data_type
  , data_length
FROM
  all_tab_columns 
WHERE
  owner = 'HOGE'
  AND table_name = 'FUGA'
ORDER BY
  column_id; 
```

カラム情報を確認するには、all_tab_columnsを参照します。
上の例で、WHERE句は、HOGEスキーマが所有しているFUGAテーブルを指定しています。
ORDER BY句は、項目の順番（column_id）を指定します。

SELECT句はそれぞれ、

- column_name → 列名（カラム名）
- data_type → 列のデータ型
- data_length → 列の長さ

を表しています。

その他にも取得できる情報はたくさんあります。
詳しくは、[ALL_TAB_COLUMNS（Oracle公式）](https://docs.oracle.com/cd/E16338_01/server.112/b56311/statviews_2103.htm)を参考にするとよいかと思います。

# 終わりに

MySQLの場合は、```DESCRIBE テーブル名``` で取得できます。
MySQLに比べると、OracleはSQLが長くなってしまい微妙だなぁ…という印象です。

