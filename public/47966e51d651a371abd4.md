---
title: Oracle SQL(11g)でMySQLのLIMIT OFFSET句を再現したい
tags:
  - SQL
  - oracle
private: false
updated_at: '2018-10-09T22:23:58+09:00'
id: 47966e51d651a371abd4
organization_url_name: null
slide: false
ignorePublish: false
---
# 動作環境
- MySQL 8.0
- Oracle Database 11g

# MySQLの場合

10レコード分取得した場合は、

```sql
SELECT column1 FROM table1 LIMIT 10;
```

10レコード目から20レコード取得した場合、下記のようになります。

```sql
-- MySQLの書き方①
SELECT column1 FROM table1 LIMIT 10 OFFSET 20;

-- MySQLの書き方②
SELECT column1 FROM table1 LIMIT 10 20;
```

②のように、OFFSETを省略して記載することも可能です。
しかし、個人的には、①をよく使っている気がします。

# Oracle SQLの場合


でもOracleだと、LIMITもOFFSETもありません。
Oracleの場合は、疑似列ROWNUMを使用すれば実現できます。

10レコード分取得した場合は、

```sql

SELECT column1 FROM table1 WHERE ROWNUM <= 10;
```

注意しなければならないのは、10レコード目から20レコード取得した場合です。
下記のように書きたくなりますが、これでは取得できません。
（自分はよく忘れて、こう書きます…………）

```sql
-- これでは取得できない！！！
SELECT column1 FROM table1 WHERE ROWNUM <= 10 AND 20 <= ROWNUM;
SELECT column1 FROM table1 WHERE ROWNUM BETWEEN 10 AND 20;
```

最初にfetchされた1行目がROWNUM=1となり、WHERE句の条件を満たすものがないため、レコードを取得できません。
なので、副問合せを使用して、ROWNUMを確定させてから、範囲指定して取得する方法を取る必要があります。

```sql
SELECT
  column1 
FROM
  ( 
    SELECT
      column1
      , ROWNUM AS rn 
    FROM
      table1
  ) 
WHERE
  rn BETWEEN 10 AND 20
```

しかし、ROWNUMには**欠点**があります。
それはORDER BYを使った場合、意図しない順番でデータが取れてしまう場合があることです。
詳細は割愛しますが、ORDER BYする前に、ROWNUMの採番が行われてしまっているためです。

なので、Xレコード目からXレコード分取得する場合は、
ROW_NUMBER()を使用したほうが無難です。

```sql
SELECT
  column1 
FROM
  ( 
    SELECT
      column1
      , ROW_NUMBER() OVER (ORDER BY column1) AS rn 
    FROM
      table1
  ) 
WHERE
  rn BETWEEN 10 AND 20
```

ちなみに、selectする項目にアスタリスク(＊)を使いたい場合は、

```sql
SELECT
  *
FROM
  ( 
    SELECT
      table1.*
      , ROW_NUMBER() OVER (ORDER BY column1) AS rn 
    FROM
      table1
  ) 
WHERE
  rn BETWEEN 10 AND 20
```

テーブル名.＊という形式になります。

# おまけ

## Oracle Database 12cの場合

oracle 12cの場合は、もっと簡潔に記載することができます。

```sql
SELECT column1 FROM table1 ORDER BY column1
OFFSET 10 ROWS FETCH FIRST 10 ROWS ONLY;
```


