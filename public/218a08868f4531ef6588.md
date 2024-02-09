---
title: JavaプログラマがPythonを勉強してみた。(関数(メソッド)について）
tags:
  - Java
  - Python
  - 初心者
  - Python3
private: false
updated_at: '2019-07-19T16:15:59+09:00'
id: 218a08868f4531ef6588
organization_url_name: null
slide: false
ignorePublish: false
---
Javaでの投稿ネタが尽きたので、勢いでPythonの勉強を始めたJavaプログラマです。
[前々回の「if,for,while文」の勉強記事はこちら。](https://qiita.com/riekure/items/be9d37557fb55a8258b5)
[前回の「型について」の勉強記事はこちら。](https://qiita.com/riekure/items/57f306500636727bc125)

AWSの資格勉強をそっちのけで、Pythonを勉強するのはどうかと思ってきている今日このごろ。
やっぱりコーディングって楽しいですよね。（言い訳
今週は本気出す。（たぶん出ない

今回は関数(メソッド)について、勉強してみます。

## 参考サイト
- [Python-izm](https://www.python-izm.com)
- [Python入門(tohoho)](http://www.tohoho-web.com/python/index.html)
- [Python 3.6.5 ドキュメント](https://docs.python.org/ja/3/)

## 動作確認環境
- java 1.8.0
- Python 3.5.2


# 関数とメソッド

まずは、基本的な関数(メソッド)の形を確認してみます。
Javaだと、

```java:HelloMethodDemo1.java
static void hello() {
    System.out.println("Hello World!");
}
public static void main(String[] args) {
    hello();
}
```
Pythonだと、

```python:HelloMethodDemo1.py
def hello():
    print('Hello World!')
hello()
```

実行結果はいつもの、

```
Hello World!
```

ちなみにreturnするパターンで書いてみると、

```java:HelloMethodDemo2.java
static String hello() {
    return "Hello World!";
}
public static void main(String[] args) {
    System.out.println(hello());
}
```

```python:HelloMethodDemo2.py
def hello():
    return 'Hello World!'
print(hello())
```

Pythonがスタイリッシュすぎて、Javaが冗長なダメ言語に見えます。
3年以上お世話になったJavaより、Pythonのほうが早く書けます。
Javaを勉強してきた意味を失いそうです。（言い過ぎ

### 関数とメソッドの違い

モジュール内で定義されているものが関数、クラス内に定義されているものがメソッドになるとのこと。
というわけで、上で書いているのは、関数になります。
メソッドは、

```python:HelloMethodDemo3.py
class TestClass:
    # メソッド
    def hello(self):
        print('Hello World!')
```
こうなっているものを言います。

# 引数

関数（メソッド）には、やはり引数を渡して処理したいときは多いです。
Javaだと、

```java:AddDemo.java
static int add(int a, int b) {
    return a + b;
}
public static void main(String[] args) {
    System.out.println(add(1, 2));
}
```

Pythonだと、

```python:AddDemo.py
def add(a, b):
    return a + b
print(add(1, 2))
```

Javaとの違いは型宣言の有無くらいなので、引数ありパターンも問題なく理解できました。

### 引数の初期値
今回参考にさせていただいた[サイト(Python-izm)](https://www.python-izm.com/advanced/function_method/)に、
引数に初期値を設定できる旨の記載がありました。
以下、参考サイトより抜粋。

> 引数は初期値を指定すると、関数を呼び出す際に省略する事が可能です。

なるほど。というわけで実際に書いてみた。

```python:AddDemo2.py
def add(a, b=2):
    return a + b
print(add(1)) # 実行結果：3
print(add(1, 3)) # 実行結果：4
```

ちなみに第一引数に設定すると、エラーで落ちました。
最後の引数にしか、初期値は設定できませんでした。

```python:AddDemo3.py
# エラーになる例
def add(a=1, b):
    return a + b
print(add(2))
```

※ 2018年6月14日追記
コメントにて教えていただきました。
上記のエラーを回避するためには、こういう場合は両方にデフォルト値を設定すれば大丈夫です。

```python
def add(a=1, b=2):
    return a + b
```

この機能はJavaにはありません。
（PHP、C++、C#とか他の言語なら結構ある機能でした。PHPとC#を使ったことあるのに見たことなかった…）
これ・・・どんなときに使うのがベストなんですかね・・・？？？
Java脳が役立つ場面が本当になくてツライ・・・

### 引数に可変長(タプル)を設定したいとき

引数にはタプルなどを設定することもできます。具体的には*(アスタリスク)を使います。

```python:ArgsDemo.py
def variable(*args):
    print(args)
variable('a', 'b', 'c')
```

実行結果は、

```
('a', 'b', 'c')
```

# グローバル変数とローカル変数

Pythonでは、
関数外で定義された変数は**グローバル変数**、
関数内で定義された変数は**ローカル変数**と呼びます。
~~※ Javaと同じ~~

※ 2018年6月14日追記
コメントにて教えていただきました。
Pythonのグローバル変数 = Javaのクラス変数(public)に相当します。
また、Pythonでは classの直後に書いた変数がクラス変数になるとのことです。

関数内でグローバル変数に代入するときは、global宣言してから実行すること。
参照だけの場合は、global宣言は不要です。

というわけで、見よう見まねでコードで書いてみました。
Javaでのイメージだと、

```java:IncrementsDemo.java
public class Main {
    public static int count = 1;
    
    void increments() {
        System.out.println(count);
        count++;
        System.out.println(count);
    }
    public static void main(String[] args) throws Exception {
        Main main = new Main();
        main.increments();
    }
}
```

実行結果は、

```
1
2
```

これをpythonで書いてみました。

```python:IncrementsDemo.py
count = 1

def increments():
    print(count)
    global count
    count += 1
    print(count)

increments()
```

では実行してみます。

```
Main.py:5: SyntaxWarning: name 'count' is used prior to global declaration
  global count
```

エラーではなくワーニングですが＼(^o^)／
まぁこういうのをググったりすることで、新しいことを覚えていくわけですよ。（言い訳2回目

というわけでGoogle検索して[最初に出てきたサイト](http://d.hatena.ne.jp/artgear/20120202/1328176677)より抜粋。
（サンプルコード見る限り、Python 2系ですが、、、）

> 注意点があり、global文でグローバル変数であると指示する名前は同じコードブロック内で先にローカル変数として使ってはいけません。一つの関数内で同じ名前のローカル変数とグローバル変数があってはいけないということですね。

へぇ～_〆(・∀・*)
というわけで今回は、関数の直後にprintでcountを参照したあと、global宣言していることがダメっぽいです。

なので、下のように修正してみました。

```python:IncrementsDemo.py
count = 1

def increments():
    global count
    count += 1
    print(count)
    
print(count)
increments()
```

改めて実行

```
1
2

```

ふむ、できました。
関数内でグローバル変数を使用するときは、代入するときはglobal宣言する。
グローバル変数を参照するときは不要。
ということを覚えておいたほうが良さそうです。

※ 2018年6月14日追記
コメントにて教えていただきましたコードが下になります。
上で書いた自分作成コードは、Javaでのイメージを再現できていないので無視してください…

```python
class Main:
    def __init__(self):
        self.count = 1

    def increments(self):
        print(self.count)
        self.count += 1
        print(self.count)

    @staticmethod
    def main():
        main = Main()
        main.increments()

Main.main()
```

せっかくなので、上のコードから学んだことをメモしておきます。

### 関数に使用するアンダーバーの意味は？

関数名に使用されているアンダーバーは、ちゃんとした意味があります。
参考サイトは[こちら。](https://teratail.com/questions/41277)

アンダーバー2つで定義されている場合は、外部からの参照を受けないもの。(Javaでいうprivate?)
アンダーバー1つで定義されている場合は、外部から参照しないように慣習的につけているが、本当はアクセスできる。

使い分けに関しても参考サイトに書いてあります。
個人的に慣れるまで上手く使い分けられないかも…という印象です…

### @staticmethodってなに？
これはデコレータと呼ばれるものです。
後に出てくる感想にも書きましたが、色んなサイトを読んでみても、しっかり理解できていないので、ここで書くのは止めておきます…

# ラムダ式
続きましてラムダ式について。
Javaだと8から採用されています。

ちなみにJavaだと、こんな感じの形をしています。

```java:LambdaDemo.java
Hoge hoge = (name) -> {
  return "Hello " + name + "!";
};
```

自分はあまりラムダ式を使いこなすことができていないクソ雑魚ナメクジなので、ラムダ式をマスターしたい…

話を戻すと、Pythonにもラムダ式は存在します。
見よう見まねで使った結果がこちら。

```python:LambdaDemo.py
output = lambda name: 'Hello' + name + '!'
print(output('lambda'))
```

実行結果は、

```
Hello lambda!
```

Javaよりは読みやすい？ような気はします。
ただ、応用編みたいなサンプルコードをいくつか見ましたが、さっぱり分かりませんでした。
あとで、もっとしっかり勉強したほうが良さそうです…

# イテレータ
Javaで言うと、MapやListなどで要素を順番に処理していくインターフェースです。
next()とかhasNext()とかremove()とか使うやつです。

Pythonの場合は、リストやタブル、辞書などの要素を順番に処理する場合に使うらしいです。

考え方は、Javaと一緒のようです。
ただ、Javaで明示的に「Iterator」と書くときなんてほぼないです。（自分だけですかね…）
ましてや、Java 8でStream APIが追加されているので、ますます使う機会がないのでは？と思います。

Javaだと、下のような形で書くことが多い気がします。

```java::IteratorDemo.java
List<String> list = new ArrayList<>();
Collections.addAll(list, "Sun.", "Mon.", "Tues.", "Wed.", "Thurs.", "Fri.", "Sat.");

Iterator<String> iterator = list.iterator();
while(iterator.hasNext()) {
  System.out.println(iterator.next());
}
```

※ 2018年6月14日追記
拡張for文で書いてみると、

```java::IteratorDemo.java
List<String> list = new ArrayList<>();
Collections.addAll(list, "Sun.", "Mon.", "Tues.", "Wed.", "Thurs.", "Fri.", "Sat.");

for(Iterator<String> iterator = list.iterator(); iterator.hasNext(); ) {			 
    System.out.println(iterator.next());
}
```
（Listのまま拡張for文回せよ！って感じですね。。。）

実行結果

```
Sun.
Mon.
Tues.
Wed.
Thurs.
Fri.
Sat.
```

Pythonだとどうなるかというと、


```python:IteratorDemo.py
week = ['Sun.', 'Mon.', 'Tues.', 'Wed.', 'Thurs.', 'Fri.', 'Sat.']
iter_week = iter(week)

for i in iter_week:
    print(i)
```

この圧倒的な入力文字数の少なさ！
for文を使用すると、次のイテレータに進んでくれるのはかなり便利だと思います。

※ 2018年6月14日追記
コメントにて教えていただきました。
そもそも自分でiterしなくても、for文書けます。もっとスッキリします。
それがこちら。

```python
week = ['Sun.', 'Mon.', 'Tues.', 'Wed.', 'Thurs.', 'Fri.', 'Sat.']
for i in week:
    print(i)
```

ちなみにJavaと同じように、next関数も使用可能です。

```python:IteratorDemo.py
week = ['Sun.', 'Mon.', 'Tues.', 'Wed.', 'Thurs.', 'Fri.', 'Sat.']
iter_week = iter(week)

print(next(iter_week))
print(next(iter_week))
print(next(iter_week))
print(next(iter_week))
print(next(iter_week))
print(next(iter_week))
print(next(iter_week))
```

これでも、上の実行結果と同じ挙動になります。
ちなみに最後の要素で、もう一度next関数を使用すると、**StopIteration**という例外が発生しました。

まだ学習はしていないですが、try~except構文もあるようです。
※ try~catchではないらしい。

# ジェネレータ
Javaにはないやつです。
イテレータの親戚で、反復できるオブジェクトらしいです。
ジェネレータ関数とジェネレータ式があり、ジェネレータ関数のほうをジェネレータと呼ばれています。
ジェネレータ関数は、yieldキーワードを使用することで実現できます。
正直言ってサッパリ分からんので、実際に書いてみました。

[Python-izm](https://www.python-izm.com)のサンプルを真似しています。

```python:YieldDemo.py
def func():
    yield('おはよう')
    yield('こんにちは')
    yield('こんばんは')

f = func()
print(next(f))
print(next(f))
print(next(f))
```

実行結果は、

```
おはよう
こんにちは
こんばんは
```

ちなみにもう一回、next関数を使用すると**StopIteration**という例外が発生しました。

リストと似ているなぁという印象です。

下記は、[Python-izm](https://www.python-izm.com)の解説より抜粋させていただきました。

> forなどでループ処理を行うことができますが、リストなどで反復処理を行う場合と異なる点は、その都度必要な分だけ値を生成して返す点にあります。

ということは、リストよりジェネレータのほうがメモリ消費は少ないという利点がありそうです。
また、大量データを使用するときは、リストよりジェネレータを使用したほうが良さそうです。
（自分はクソ雑魚プログラマなので、当分はお世話になりそうがないですね…）

# 感想
今回は関数(メソッド)について勉強しました。
イテレータとかジェネレータは、かなり奥が深そうです。
たぶん実際に使ってみようとすると、かなり手こずりそうだなぁという印象を受けました。

ほかにも、デコレータ(@)の紹介があったので、解説を読む＋分からない点はググりました。
結果、何を言っているのかさっぱり理解できなかったので、今回はデコレータについて書くのを止めました。（おい
理解できるようになったら、本記事に追記 or 新しい記事として投稿しようかと思ってます。

※ 2018年6月14日追記
> あと、Pythonの内包表記とJavaのStreamのforEach処理+ラムダの比較もあると良いかも。

コメントいただきました。
内包表記？？？って思い調べましたが、「なにこれ…内包？外延？どう動きするか分からぬ…」と見事に混乱しました。
Python使ってて内包表記も書けないやつはダメらしいです。本当かどうか知りません（おい
こちらもデコレータと合わせて、本記事に追記 or 新しい記事として投稿しようかと思ってます。
