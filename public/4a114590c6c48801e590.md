---
title: MyBatisのSQLで不等号の比較演算子を使う
tags:
  - Java
  - MyBatis
private: false
updated_at: '2018-05-01T11:40:17+09:00'
id: 4a114590c6c48801e590
organization_url_name: null
slide: false
ignorePublish: false
---
# 初めに
MyBatisはXMLファイルにSQL文を定義して使用するが、XMLなので<や>は使えない。
それに気づかずエラー吐いて、
なんでや！コンソールでこのSQL叩いたら正常に実行できたのに！と小一時間悩んだ。

## 実行環境
- MyBatis 3
- Java 8 

# エラーになる例
```xml
<select id="hoge" resultType="hoge">
    SELECT
        *
    FROM
        HOGE
    WHERE
        HOGE.HOGE_DATE < SYSDATE
</select>
```
不等号を使っているWHERE句がダメと怒られる。
## エラー内容
```
Cause: org.xml.sax.SAXParseException; lineNumber: XX; columnNumber: XX; 要素のコンテンツは、整形式の文字データまたはマークアップで構成されている必要があります。 
```
# 改善策①
不等号を使っている箇所を<![CDATA[・・・]]>で囲んでしまうという方法。  

```xml
<select id="hoge" resultType="hoge">
    SELECT
        *
    FROM
        HOGE
    WHERE
        HOGE_DATE <![CDATA[ < ]]> SYSDATE
</select>
```

# 改善策②
下の例のようにSELECT句全体を囲んでも良かった。
こっちのほうが可読性は高い。（気がする。）

```xml
<select id="hoge" resultType="hoge">
<![CDATA[ 
    SELECT
        *
    FROM
        HOGE
    WHERE
        HOGE_DATE < SYSDATE
]]>
</select>
```
# 改善策③
コメントにて教えていただいたエンティティ参照を使用する方法です。
少し調べたところ、以下の5種類があるようです。

| 文字 | エンティティ参照 |
|:-----------|:------------|
|<|\&lt;|
|>|\&gt;|
|&|\&amp;|
|'(シングルクォーテーション)|\&apos;|
|"(ダブルクォーテーション)|\&quot;|


エンティティ参照を使用して記載すると、下のようになります。

```xml
<select id="hoge" resultType="hoge">
    SELECT
        *
    FROM
        HOGE
    WHERE
        HOGE_DATE &lt; SYSDATE
</select>
```

# 終わりに
MyBatisに初めて触っているが、動作確認済のSQLをコピペして、呼び出すだけで使えるので便利。
MyBatis公式ドキュメントが日本語化されており、情報量も豊富なので使いやすい。
if、choose、foreachなどの動的SQLについても後日まとめる予定。

# 参考文献
[MyBatis – MyBatis 3 | Mapper XML ファイル](http://www.mybatis.org/mybatis-3/ja/sqlmap-xml.html)
[文字参照とエンティティ参照[XML標準]](https://msdn.microsoft.com/ja-jp/library/ms256190(v=vs.120).aspx)
