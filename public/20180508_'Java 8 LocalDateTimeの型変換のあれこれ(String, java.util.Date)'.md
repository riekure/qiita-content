---
title: 'Java 8 LocalDateTimeの型変換のあれこれ(String, java.util.Date)'
tags:
  - Java
  - java8
private: false
updated_at: '2018-05-08T20:47:14+09:00'
id: d83d4ea5d8a19a267453
organization_url_name: null
slide: false
ignorePublish: false
---
Java 8 LocalDateTimeの型変換のあれこれ(String, java.util.Date)
# はじめに
Javaの日付型はDateやCalendarクラスなどが使用されてきたが、Java 8以降は新しくLocalDateTime/ZonedDateTimeクラスなどを使用することが推奨されている。

今回は、LocalDateTimeクラスを使用する機会があったので、勉強してみた。
一発で変換できるメソッドが用意されているわけでなく、手軽に型変換できないことが分かった。

今回は、String⇔LocalDateTimeと、java.util.Date⇔LocalDateTimeについて自分なりに整理した。

# String → LocalDateTime

## SimpleDateFormatクラスを使用した場合
String→SimpleDateFormat→Date→LocalDateTimeという流れで変換する。

```java
    public static LocalDateTime toLocalDateTime(String date, String format) throws ParseException {
        SimpleDateFormat sdf = new SimpleDateFormat(format);
        Date formatDate = sdf.parse(date);
        return LocalDateTime.ofInstant(formatDate.toInstant(), ZoneId.systemDefault());
    }
```

使い方例

```java
    public static void main(String args[]) {
        // 実行結果：2018-05-07T00:00
        System.out.println(toLocalDateTime("2018/05/07", "yyyy/MM/dd"));
    }
```

## DateTimeFormatterクラスを使用した場合
DateTimeFormatterクラスは、SimpleDateFormatと違い、newしなくて良い。
生成時にofPatternメソッドで日付パターンを決める必要がある。

String→DateTimeFormatter→LocalDateTimeという流れで変換する。
SimpleDateFormat使うより短くできる。

```java
    public static LocalDateTime toLocalDateTime(String date, String format) {

        DateTimeFormatter dtf = DateTimeFormatter.ofPattern(format);
        return LocalDateTime.parse(date, dtf);
    }
```

使い方例

```java
    public static void main(String args[]) {
        // 実行結果：2018-05-07T10:00
        System.out.println(toLocalDateTime("2018/05/07 10:00:00","yyyy/MM/dd HH:mm:ss"));
    }
```

ただ、日付と時刻を持つLocalDateTimeなので、時刻を指定しないとエラーになってしまう。

```java
    public static void main(String args[]) {
        // 実行結果：DateTimeParseException
        System.out.println(toLocalDateTime("2018/05/07","yyyy/MM/dd"));
    }
```

なので、日付のみで良いならLocalDateを返すようにしてみるか、

```java
    public static LocalDate toLocalDate(String date, String format) {

        DateTimeFormatter dtf = DateTimeFormatter.ofPattern(format);
        return LocalDate.parse(date, dtf);

    }
```

LocalDateに変換してから、0時を付け足してLocalDateTimeにするかになる。
※ コメントにて教えていただきました。

```java
    public static LocalDateTime toLocalDateTime(String date, String format) {

        DateTimeFormatter dateTimeFormatter = DateTimeFormatter.ofPattern(format);
        return LocalDate.parse(date, dateTimeFormatter).atTime(LocalTime.MIN);

    }
```


# LocalDateTime → String
~~これはparseメソッドを使用すれば一発で変換できる。~~すみません嘘です。
formatメソッド + DateTimeFormatterで変換することができる。

```java
    public static String toStr(LocalDateTime localDateTime, String format) {

        DateTimeFormatter dateTimeFormatter = DateTimeFormatter.ofPattern(format);
        return localDateTime.format(dateTimeFormatter);

    }
```

使い方例

```java
    public static void main(String args[]) {
        // 実行結果：2018/05/07
        System.out.println(toStr(LocalDateTime.now(), "yyyy/MM/dd"));
    }
```

# LocalDateTime → java.util.Date
LocalDateTime→ZonedDateTime→Instant→java.util.Dateという流れで変換する。

```java
    public static Date toDate(LocalDateTime localDateTime) {
        ZoneId zone = ZoneId.systemDefault();
        ZonedDateTime zonedDateTime = ZonedDateTime.of(localDateTime, zone);
        Instant instant = zonedDateTime.toInstant();
        return Date.from(instant);
    }
```

使い方例

```java
    public static void main(String args[]) {
        // 実行結果：Mon May 07 19:59:32 JST 2018
        System.out.println(toDate(LocalDateTime.now()));
    }
```

# java.util.Date → LocalDateTime

Date→Instant→LocalDateTimeという流れで変換する。

```java
    public static LocalDateTime toLocalDateTime(Date date) {
        Instant instant = date.toInstant();
        return LocalDateTime.ofInstant(instant, ZoneId.systemDefault());
    }
```

使い型例

```java
    public static void main(String args[]) {
        // 2018-05-07T19:59:32.139
        System.out.println(toLocalDateTime(new Date()));
    }
```

# 最後に
LocalDateTimeの扱いは難しい。（小並感）
LocalDateとLocalTimeをうまく使い分けていくのがよいのかも。
（自分にとって）分かりやすいように1行ずつ変数宣言しているが、コメントにて教えていただいた1行で全てやっちゃうのほうがもちろん良い。

```java
public static void main(String args[]) {
    // String→LocalDateTime
    System.out.println(LocalDate.parse("2018/05/07", 
                           DateTimeFormatter.ofPattern("uuuu/MM/dd"))
                       .atTime(LocalTime.MIN));
}
```

## 疑問点
SimpleDateFormatとDateTimeFormatterの違いを把握しきれていないので、後日じっくり調べる。
