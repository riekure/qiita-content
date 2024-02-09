---
title: 'JavaプログラマがPythonを勉強してみた。(for, if, while文)'
tags:
  - Java
  - Python
  - 初心者
  - Python3
private: false
updated_at: '2019-07-19T16:11:16+09:00'
id: be9d37557fb55a8258b5
organization_url_name: null
slide: false
ignorePublish: false
---
# なぜPythonを勉強しようと思った？
~~Qiita週一投稿のネタが尽きたから。未経験なプログラミング言語なら何でもよかった。~~
先週くらいに「プログラミング言語ランキングでPythonついにJavaを抜く」というニュースが話題になった。
そのときに何気なくPythonのソースコードを見たが、
「今まで経験してきたJavaやPHP、C#と形式がぜんぜん違うじゃん…読めねぇ…」
「でもいま流行りの人工知能と言ったらPython、、、興味はあるし基本構文くらいは勉強してみるか…」
となった。
Qiitaのタグ・ランキングでも週間・月間で常に1位だし、勉強しておいて損はないと思ったのもあるので。

n番煎じだと思うが、 ~~Qiita週一投稿の目標のため~~ Javaと比較しながら勉強してみた。

## 動作確認環境
- java 1.8.0
- Python 3.5.2

# Hello World!
最初はやはり「Hello World!」
出力イメージは

```
Hello World!
```

Javaだと、

```java:HelloWorld.java
System.out.println("Hello World!");
```

Pythonだと、

```python:HelloWorld.py
print("Hello world!")
```

~~ここで区切り文字であるセミコロン（;）が不要ということを理解した。~~
コメントにて教えていただきました。
> Pythonにもセミコロン（;）があり、1行に複数の文を書くときに使います。

```python
x = 10; y = 20; z = 30;
# 上の一緒の動作
x, y, z = 10, 20, 30
```

というわけで試してみました。

```python:HelloWorld.py
print("Hello world!");print("Hello world!!")
```
実行結果

```
Hello world!
Hello world!!
```
セミコロン書けました！
せっかく教えていただいたので、Pythonにおけるセミコロンについて調べてみました。

[Google Python スタイルガイド](http://works.surgo.jp/translation/pyguide.html)を見てみると、下記のように書いてあるらしい。

> 行をセミコロンで終了、また 2 つの命令を同じ行内に書くためにセミコロンは使用しません。

Javaと同じで、2つの命令を同じ行内に書くのはダメとのこと。
あと、行をセミコロンで終了させるのもダメらしい。

Pythonにおいては、**「セミコロンは使わないようにコーディングしよう」**という感じなんだろうなぁと解釈。

それ以外のスタイルルールは、自分が今までやってきたJavaと同じかな～という感じ。


# for文
次にfor文を書いてみた。
出力イメージは、

```
0
1
2
3
4
```

Javaだと下のようなコードになるものを、

```java:ForDemo.java
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}
```

見よう見まねでPythonで書いてみて、

```python:ForDemo1.py
for i in range(0, 5):
print(i)
```

実行する！

```
IndentationError: expected an indented block
```

＼(^o^)／
ここは「Python 構文」でGoogle検索！（遅い
[先頭に出てきた検索結果](http://www.tohoho-web.com/python/syntax.html)を見てみる。
リンク先のインデントの項目より抜粋


> Perl や PHP では文を { ... } で囲むことでブロック(複文)を構成しますが、Python ではインデント(行頭の空白文字の数)が重要な意味を持ち、同じ数の空白でインデントされた文がブロックとみなされます。
> {中略}
> インデントには通常、4個の空白文字を使用します。タブ文字は、インデントが8の倍数になるように1～8個の空白文字とみなされます。


インデントがブロックの役割をしているから、{}で囲まなくていいとのこと。
自分みたいな初心者がPython書いたとしても、インデントが揃うようになっているのは良いことなのかも。

ということでさっきのエラー出た構文にprint(i)の前にインデントをいれて

```python:ForDemo2.py
for i in range(0, 5):
    print(i)
```

実行すると、

```
0
1
2
3
4
```

ちゃんと出た。
また、inのあとに文字列を指定してもOK。

```python:ForDemo3.py
for c in 'Hello':
    print(c)
```

実行結果は1行に1文字ずつ出力される形で、

```
H
e
l
l
o
```

ここで疑問が生まれた。

## for hoge in 配列としたらどうなる？

1行に1文字ずつ出力するのか、1行に1単語ごとに出力するのか検証してみる。

```python:ForDemo4.py
list = ['Hello', 'World']
for c in list:
    print(c)
```

実行結果は、

```
Hello
World
```

1行に1単語ごとに出た。
じゃあ2重でfor文を書けば、1行に1文字ずつ出力するのか。

```python:ForDemo5.py
list = ['Hello', 'World']
for c1 in list:
    for c2 in c1:
        print(c2)
```

実行結果は、

```
H
e
l
l
o
W
o
r
l
d
```

# if文

次に条件分岐にはかかせないif文について。
Javaで書いたコードをpythonで書いてみる。

```java:IfDemo1.java
String str = "blue";
if ("blue".equals(str)) {
    System.out.println("青信号です。");
} else if ("yellow".equals(str)) {
    System.out.println("黄信号です。");
} else {
    System.out.println("赤信号です。");
}
```

if文も、いろいろなサンプルコードを拝見してから書いてみる。

```python:ifDemo1.py
str = "blue"
if str == "blue":
    print("青信号です。")
elif str == "yellow":
    print("黄信号です。")
else:
    print("赤信号です。")
```

実行してみると、

```
青信号です。
```

正常に動いた。
~~最初は、elifをelse ifって書いてエラー出た。~~
Pythonプログラマの方は、elifをなんて読んでいるんでしょうか？
自分が書いているときはエリフって心の中で読みながら書いてました。
エルフの剣士みたいでカッコイイと思う。(うるさい

※ コメントにて教えていただきました。
elif = 「**エルイフ**」と読むのが一般的なようです。
エリフと読まないように注意！！

## OR, AND, NOTは？

複雑な条件分岐を書くためにはOR, AND, NOTの存在は欠かせない。

```java:IfDemo2.java
int i = 0;
if (i == 0 || i < 0) {
    System.put.println("0以下");
} else if (50 <= i && i <= 100) {
    System.out.println("50以上かつ100以下");
} else if (!i == 0) {
    System.out.println("0じゃないです");
}
```

またまた、いろいろなサンプルコードを拝見してから書いてみる。

```python:IfDemo2.py
i = 0
if i == 0 or i < 0:
    print("0以下")
elif 50 <= i and i <= 100:
    print("50以上かつ100以下")
elif not i == 0:
    print("0じゃないです。")
```

実行結果は、

```
0以下
```
コメントにて教えていただきましたが、elifの部分を下記のように記載することも可能。
入力文字数も少なく、パッと見でどういう内容の条件が把握できるのでかなり良い。

```python:IfDemo3.py
i = 50
if i == 0 or i < 0:
    print("0以下")
elif 50 <= i <= 100::
    print("50以上かつ100以下")
elif not i == 0:
    print("0じゃないです。")
```

実行結果

```
50以上かつ100以下
```

次に、Pythonは{}によるブロック定義が不要なので、
条件式を()で括っていいのか分からなかったので試してみた。

```python:IfDemo4.py
i = 1
if (i == 1) or (i >= 2 and i < 3):
    print("OK！")
```


実行結果は、

```
OK！
```

()をつけることができました。
条件分岐に関しても、優先順位をつけるとかJavaと同じ考えが通用しそう。

# while文

ループ処理の基本といえば、for文とwhile文だと思うので、while文も書いてみた。
出力イメージはfor文と同じで、

```
0
1
2
3
4
```

Javaで書いてみると、

```Java:WhileDemo.java
int i = 0;
while(i < 5) {
    System.out.println(i);
    i++;
}
```

早速Pythonでもサンプルコードの見よう見まねで書いてみる。

```python:WhileDemo1.py
i = 0
while i < 5:
    print(i)
    i++
```

i++の箇所でエラーが出た。
調べてみると、Pythonには[i++のようなインクリメント演算子がない](https://www.python-izm.com/tips/increment/)らしい。
代わりに、下のように**累積代入**という方法を使用するとのこと。

```python:WhileDemo2.py
i = 0
while i < 5:
    print(i)
    i += 1
```

実行結果は想定通り、

```
0
1
2
3
4
```
インクリメントがないということで、デクリメントもないらしい。
デクリメントもインクリメントと同様な形式で、

```python:WhileDemo3.py
i = 4
while 0 <= i:
    print(i)
    i -= 1
```

実行結果

```
4
3
2
1
0
```

# やってみての感想
{}で囲まないため、}だけの行が存在しない。なので、ソースコードの行数がかなり少ない。
else ifをelifと書く印象からすると、入力文字数も少ないのかなと思う。
これで機械学習だけでなく、Webアプリもゲームも作ることができるんだから需要ありますよね！

ただ、区切り文字であるセミコロン（;）が不要というのが慣れない。
どうしても勢いでセミコロンをつけてしまう。

[「PYPL PopularitY of Programming Language」](http://pypl.github.io/PYPL.html
)の結果をちゃんと見てみると、
PHPの下がり幅がすごいので、PHPは捨ててPythonにシフトしたほうがいいのかなぁという印象。
Javaの今後がさっぱり分からず非常に不安。

Pythonを使って具体的に作りたいものがあるわけではないので、今後もPythonを勉強していくか悩み中…
