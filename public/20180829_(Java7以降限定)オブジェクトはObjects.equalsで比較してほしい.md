---
title: (Java7以降限定)オブジェクトはObjects.equalsで比較してほしい
tags:
  - Java
  - java7
private: false
updated_at: '2018-08-29T01:37:42+09:00'
id: 7348a600e18b7d6d0f72
organization_url_name: null
slide: false
ignorePublish: false
---
# Java 7より前の比較

オブジェクトを比較する際に、未だに下のようなコードを書いてしまう人（自社の人）がいる。
NullPointerExceptionを回避するために、定数から先に書いてみたり、

```java
if ("hoge".equals(hoge)) {
	// NullPointerExceptionになることはない
}
```

nullチェックを先にやってから、比較していたりする。

```java
if (hoge != null && hoge.equals("hoge")) {
	// hogeがNULLだった場合、後続のString.equalsは実行されない
}
```

# Java7以降の比較

Java 7以降を使っているならば、ぜひ```java.util.Objects.equals(Object a, Object b)```を使ってほしい。
これの場合、nullを考慮した比較を行ってくれる。

```java
if (Objects.equals(hoge, "hoge")) {
	// 処理
}
```

オブジェクトのポインタ(メモリ上の番地)が違っていても、
ちゃんと格納されている値同士で比較してくれるので安心。

```java
String hoge1 = "hoge";
String hoge2 = new String("hoge");

System.out.println(hoge1 == hoge2);               // false
System.out.println(hoge1.equals(hoge2));          // true
System.out.println(Objects.equals(hoge1, hoge2)); // true
```

# おまけ

この記事を書くにあたり、 java.util.Objectsについて、改めて調べてみました。
これは知らなかった！というものを書いてみます。

### toString

String型に変換するメソッド。
変換対象がnullだった場合、nullという文字列に変換される。

```java
Object obj = null;
String str = Objects.toString(obj);
System.out.println(Objects.equals(str, "null")); // true
System.out.println(Objects.equals(str, null));   // false 
```

null回避できるのは非常に良いことだが、nullという文字列に変換されるのは困る場面があると思う。
そんなときは、第2引数に文字列を設定すると、nullの場合に返す値を変更することができる。

```java
Object obj = null;
String str = Objects.toString(obj, "NULLです！");
System.out.println(str); // 出力結果：NULLです！
```

toStringメソッドは知っていたが、第2引数を設定できることを知らなかった。

### isNull／nonNull

isNullは引数がNULLの場合、 trueを返すメソッド。
nonNullは引数がNULLの場合、falseを返すメソッド。

```java
Object obj = null;
System.out.println(Objects.isNull(obj));  // true
System.out.println(Objects.nonNull(obj)); // false
```
```obj == null```よりは、スタイリッシュに見えます。
（```obj == null```や```obj != null```の挙動の違いは分かりませんでした…）

### requireNonNull

対象がNULLかどうかチェックするメソッド。
NULLだった場合は、NullPointerExceptionが発生する。

```java
Object obj2 = Objects.requireNonNull(obj1);
```
このメソッドを使わないでNULLチェックを行おうとすると、

```java
if (obj1 == null) {
	throw new NullPointerException();
} else {
	Object obj2 = Objects.requireNonNull(obj1);
}
```

となる。
地味な便利メソッドだと思う。


# 参考文献
[Objects (Java Platform SE 7)](https://docs.oracle.com/javase/jp/7/api/java/util/Objects.html)
[今までの書き方はもう古い！？ java.util.Objectsが便利すぎる](https://amg-solution.jp/blog/11164)
