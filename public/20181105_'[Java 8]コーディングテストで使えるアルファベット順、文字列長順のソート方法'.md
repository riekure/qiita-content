---
title: '[Java 8]コーディングテストで使えるアルファベット順、文字列長順のソート方法'
tags:
  - Java
  - java8
private: false
updated_at: '2018-11-05T10:05:00+09:00'
id: 79df368a4cbc6be1dda2
organization_url_name: null
slide: false
ignorePublish: false
---
# 背景

最近、転職活動のWEBコーディングテストで落ちまくっています。
慣れるしかないと思って、paiza.ioで練習しています。
時間に追われて焦って解くと、後日ソースを見て、吐き気がするクソコードを量産してしまいます。

今回は、List<String>に格納したあとにソートする手法について、まとめてみます。

# 動作環境

- java 1.8.0_191

※Comparatorを使用しているので、Java 7以前では動作しないので注意してください。
```java.util.Comparator;```をインポートしていると思ってください。

# アルファベット順

```java
List<String> list = Arrays.asList("ABC", "DEFGH", "IJKL", "abc", "defgh", "ijkl");

// アルファベット順の昇順（大文字、小文字を区別しない）
// 出力結果：ABC,abc,DEFGH,defgh,IJKL,ijkl
list.sort(String.CASE_INSENSITIVE_ORDER);

// アルファベット順の降順（大文字、小文字を区別しない）
// 出力結果：IJKL,ijkl,DEFGH,defgh,ABC,abc
list.sort(String.CASE_INSENSITIVE_ORDER.reversed());

// アルファベット順の昇順（大文字→小文字で区別）
// 出力結果：ABC,DEFGH,IJKL,abc,defgh,ijkl
list.sort(Comparator.naturalOrder());

// アルファベット順の降順（大文字→小文字を区別）
// 出力結果：ijkl,defgh,abc,IJKL,DEFGH,ABC
list.sort(Comparator.reverseOrder());
```

# 文字列長順

```java
List<String> list = Arrays.asList("ABC", "DEFGH", "IJKL", "abc", "defgh", "ijkl");

// 文字列長の昇順
// 出力結果：ABC,abc,IJKL,ijkl,DEFGH,defgh
list.sort(Comparator.comparingInt(String::length));

// 文字列長の降順
// 出力結果：DEFGH,defgh,IJKL,ijkl,ABC,abc
list.sort(Comparator.comparingInt(String::length).reversed());
```

# おまけ
文字列長 → アルファベット順でソート

```java
list.sort(Comparator.comparingInt(String::length).thenComparing(Comparator.naturalOrder()));
```

Integerをソートする方法。

```java
List<Integer> list = Arrays.asList(1, 3, 2);

// 昇順
Collections.sort(list);

// 降順
Collections.reverse(list);
```

# 終わりに

Lambdaでも実現できるのですが、個人的にComparatorのほうが可読性が高いと感じているため、割愛しました。
これくらいは調べずに、パッと出てくるようになりたいです。

コーディングテストでは、こういうソートが必要なことが多いから覚えたほうがいい！
こっちのほうが可読性が高いぞ！といったご意見、間違いとかありましたら教えてください。
