---
title: '[MyBatis]大量データをマッピングするときはCursorを使おう'
tags:
  - Java
  - MyBatis
  - java8
  - springframework
private: false
updated_at: '2018-10-15T13:03:31+09:00'
id: 761abcf54c9216db596f
organization_url_name: null
slide: false
ignorePublish: false
---
# はじめに

この間仕事で、大量データを扱っていて、どうしてもレスポンスがでない処理を見直すことなりました。
全体的に、約4分くらいかかる処理でした。
この処理を見直すときに、MappperをListではなく、org.apache.ibatis.cursor.Cursorに修正しました。
その結果、レスポンスを早くすることができました。

せっかくなので、MyBatis3.4以降で追加されたCursorの使い方についてまとめていきます。

# 動作環境

- Java 1.8.0_181
- Spring FrameWork 4.3.16
- MyBatis 3.4.5
- mybatis-spring 1.3.1

※ mybatis-springだけ、プロジェクトによって必要／不必要が分かれると思います。

# 使い方

mapper.xmlは、Listで取得するときと特に変える必要はありません。
大量データを処理するので、fetchSizeでキャッシュのサイズを調整すると、さらに良いと思います。

```mapper.xml
  <select id="getColumns" fetchSize="50000" resultType="java.lang.String">
    SELECT columns FROM table1
  </select>
```

Mapper.javaは、org.apache.ibatis.cursor.Cursorをインポートします。
\<String>の部分は、SQLの戻り値に合わせてください。

```Mapper.java
import org.apache.ibatis.cursor.Cursor;

@Mapper
public interface Mapper {
    public Cursor<String> getColumns();
}
```

Mapperから呼び出す部分です。
Cursor\<T>型に呼び出し結果を格納する以外は、Listと同様です。

また、ループ処理で値を取り出す部分も、Listと同じように書くことができます。
サンプルでは、forEachとIteratorの2種類で書いています。

```Service.java
@Service
public class Service {
    @Autowired
    private Mapper mapper;

    public void getMapper() {
        try (Cursor<String> columnsCorsor = mapper.getColumns()) {

            // ループ処理１
            columnsCorsor.forEach(s -> {
                System.out.println(s);
            });

            // ループ処理２（2回目のループはエラーするので注意！！）
            Iterator<String> iterator = columnsCorsor.iterator();
            while (iterator.hasNext()) {
                System.out.println(iterator.next());
            }

        } catch (Exception e) {
            e.printstacktrace();
        }
    }
}
```

注意しなければならないのは、Listで取得した時とは違い、**Cursor内のデータを全て読み込んだタイミングで**、closeされます。
そのため、1回でも全データを取り出したあとに、もう一度データを取り出しにいくと、下のようなエラーが出ます。

```
java.lang.IllegalStateException: Cannot open more than one iterator on a Cursor
```

基本的な使用方法の場合は、MyBatis側がクローズしてくれるので問題ないと思います。

しかし、途中でエラーが発生した場合、クローズしてくれる保証はありません。
なので、呼び出し元でtry~resource文かfinally句などで、**しっかりとクローズ**してあげましょう。

# 最後に

Cursorのおかげで、レスポンスを4分から2分まで短縮することができました。
（Cursor以外の部分も見直した結果ですが……）
大量データを処理する際は、ぜひCursorを活用してみましょう。


# 雑記
MyBatisって参考資料が少ないので、利用者は少ないのかなと思っています。
DBアクセス系のフレームワークは、何が主流なんでしょうか…？
MyBatisは生SQLをかけるし、良い感じにマッピングしてくれるので、個人的には気に入っているのですが…
~~アノテーションにたまにイラッとすることはありますが~~

# 参考文献
[MyBatis – MyBatis 3 | Mapper XML ファイル](http://www.mybatis.org/mybatis-3/ja/sqlmap-xml.html)
[Cursor | mybatis](http://www.mybatis.org/mybatis-3/apidocs/reference/org/apache/ibatis/cursor/Cursor.html)
[5.2. データベースアクセス（MyBatis3編） — TERASOLUNA Server Framework for Java (5.x) Development Guideline 5.0.1.RELEASE documentation](https://terasolunaorg.github.io/guideline/5.0.1.RELEASE/ja/ArchitectureInDetail/DataAccessMyBatis3.html)
