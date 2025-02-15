---
title: SimpleDateFormatとDateTimeFormatterの違いってなんだ？？
tags:
  - Java
  - java8
private: false
updated_at: '2018-05-14T11:26:04+09:00'
id: 935f45b252f9882ab958
organization_url_name: null
slide: false
ignorePublish: false
---
SimpleDateFormatとDateTimeFormatterの違いってなんだ？？

自分が[この前書いた記事](https://qiita.com/riekure/items/d83d4ea5d8a19a267453)で、SimpleDateFormatとDateTimeFormatterを使用した。
どちらも日付時刻フォーマッターで、一体何が違うのか把握できていなかったので、調べてみた。

# インスタンス生成の違い
newするか、用意されているメソッドを使用するかの違いがある。

### SimpleDateFormatの場合
SimpleDateFormatのインスタンス生成は、newして生成する。
スレッドセーフではない。
そのため、マルチスレッド処理の場合、使用する直前で毎回インスタンスを生成することが必要。

```java
SimpleDateFormat sdf = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss.SSS");
```

### DateTimeFormatterの場合
DateTimeFormatterのインスタンス生成は、ofPatternメソッドで生成する。
スレッドセーフ。
SimpleDateFormatと違って、マルチスレッド処理のとき、使うたびにインスタンスを生成するということが必要ない。

```java
DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss.SSS");
```

# parse(解析)
StringをSimpleDateFormatとDateTimeFormatterを使って変換してみる。

### SimpleDateFormatの場合

String → Dateに変換する処理。
parseメソッドにString型を引数として渡すのみ。
ParseExceptionの例外処理が必要だけど、下の例では省略。

```java
SimpleDateFormat sdf = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss.SSS");
Date date = sdf.parse("2018/05/14 12:34:56.123");
// Mon May 14 12:34:56 UTC 2018
System.out.println(date);
```

### DateTimeFormatterの場合

String → TemporalAccessorに変換する処理。

```java
DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss.SSS");
TemporalAccessor ta = dtf.parse("2018/05/14 12:34:56.123");
// {},ISO resolved to 2018-05-14T12:34:56.123
System.out.println(ta);
```
[TemporalAccessor](https://docs.oracle.com/javase/jp/8/docs/api/java/time/temporal/TemporalAccessor.html)ってなに…？ってなった。出力結果も"ISO resolved to ~~"とかついている。
LocalDateTimeの親インターフェースらしい。他にもLocalDate, LocalTime, ZonedDateTimeの親にあたる。
なので、こんなことが可能。
※ 自分で書いておいて「だからなに…？」ってなっていますが、備忘録として記載。

```java
TemporalAccessor tAccessor = LocalDateTime.of(2018, 5, 14, 12, 34, 56);
```

DateTimeFommaterでparseする場合、LocalDateTimeのparseメソッドが使用されているパターンが多いと思われる。
下のようになる。こちらのほうが使用頻度高そうなので覚えておきたい。
（String → LocalDateTimeに変換する処理。）

```java
DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss.SSS");
LocalDateTime date = LocalDateTime.parse("2018/05/14 12:34:56.123", dtf);
// 2018-05-14T12:34:56.123
System.out.println(date);
```

# format(整形)
SimpleDateFormatとDateTimeFormatterをその名の通りフォーマットしてみる。

### SimpleDateFormatの場合

Date→Stringに変換する処理。
formatメソッドにjava.util.Date型を引数として渡す。

```java
SimpleDateFormat sdf = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss.SSS");
Date date = sdf.parse("2018/05/14 12:34:56.123");
// Mon May 14 12:34:56 UTC 2018
System.out.println(date);
        
String str = sdf.format(date);
// 2018/05/14 12:34:56.123
System.out.println(str);
```

### DateTimeFormatterの場合

formatメソッドに[TemporalAccessor](https://docs.oracle.com/javase/jp/8/docs/api/java/time/temporal/TemporalAccessor.html)を引数として渡す。

```java
DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss.SSS");
LocalDateTime date = LocalDateTime.parse("2018/05/14 12:34:56.123", dtf);
// 2018-05-14T12:34:56.123
System.out.println(date);

String str = dtf.format(date);
// 2018/05/14 12:34:56.123
System.out.println(str);
```

# まとめ

だらだらと書いてしまったが、わかったことをまとめると、


||SimpleDateFormat|DateTimeFormatter|
|:-----------|:-----------|:------------|
| 型 | java.util.Dateへの変換 | [TemporalAccessor](https://docs.oracle.com/javase/jp/8/docs/api/java/time/temporal/TemporalAccessor.html)への変換（LocalDateTime, LocalDate, LocalTime, ZonedDateTimeなど）
| インスタンス生成 | `new SimpleDateFormat("yyyy/MM/dd HH:mm:ss.SSS")` | `DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss.SSS")` |
| スレッドセーフ？ | × | ◯ |
| parse | `dtf.parse(str)` <br> java.util.Dateになる。 | `dtf.parse(str)` <br> [TemporalAccessor](https://docs.oracle.com/javase/jp/8/docs/api/java/time/temporal/TemporalAccessor.html)になる。 <br> LocalDateTimeなどのparseメソッドのほうが使いやすい。 |
| format | `sdf.format(date)` | `dtf.format(TemporalAccessor)` |

Javaの日付／時刻の扱いはやっぱり難しい。
PHPはこんなに難しくなったような気がする。
（日付／時刻を扱ったことがあまりないからそう思っているだけかも…）
