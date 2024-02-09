---
title: Oracle SQLでDB接続中のセッションを特定＆強制終了(KILL)
tags:
  - SQL
  - oracle
private: false
updated_at: '2018-08-21T13:43:04+09:00'
id: 7d49b78c781097aa1704
organization_url_name: null
slide: false
ignorePublish: false
---
# DB接続中のセッションを特定

負荷のかかるSQLを実行した際に、クライアントがフリーズしてしまい、強制終了してしまった。
そのときに、セッションが残っているか確認したいときに使用したSQLです。

```sql
SELECT
    SID, SERIAL#, MACHINE, STATUS, PROGRAM
FROM
    V$SESSION
WHERE
  USERNAME = 'HOGE';
```

HOGEと記載しているところに、ログインしたユーザIDを指定します。
実行すると、下のような結果が出力される。


| SID | SERIAL# | MACHINE | STATUS | PROGRAM |
| :-- | :-- | :-- | :-- | :-- | :-- | 
| 48 | 141 | riekure1 | Active | SQL Developer |
| 139 | 157 | riekure2 | Inactive | A5M2.exe |


各項目の意味については、[Oracle公式](https://docs.oracle.com/cd/E60665_01/db112/REFRN/dynviews_3016.htm)が分かりやすいと思います。

# セッションを強制終了
もし、怪しいセッションが残っていて、強制終了したいときはSIDとSERIAL#を使用します。

```sql
ALTER SYSTEM KILL SESSION '48,141';
```

'SID, SERIAL'(カンマ区切り)で対象セッションを指定します。
ちなみに、自分自身を強制終了できませんでした。地味に親切でした。
