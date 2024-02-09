---
title: JavaプログラマがPythonを勉強してみた。(デコレータについて）
tags:
  - Java
  - Python
  - 初心者
  - Python3
private: false
updated_at: '2018-08-26T12:15:09+09:00'
id: 383e7e2378c0f6854ff8
organization_url_name: null
slide: false
ignorePublish: false
---
Javaでの投稿ネタが尽きたので、勢いでPythonの勉強を始めたJavaプログラマです。

今回は、前回理解できずに省略してしまったデコレータについて勉強します。
過去の勉強記事はこちら。
[if,for,while文について](https://qiita.com/riekure/items/be9d37557fb55a8258b5)
[型について](https://qiita.com/riekure/items/57f306500636727bc125)
[(関数(メソッド)について](https://qiita.com/riekure/items/218a08868f4531ef6588)

# デコレータとは？

[侍エンジニア塾](https://www.sejuku.net/blog/25130)には次のように書かれていました。

> デコレータとは、すでにある関数に処理の追加や変更を行う為の機能です。
> 
> デコレータを使うことによって、既存の関数の中身を直接変更することなく、それらに機能を追加したり変更したりすることが出来るようになります。
> 
> たとえば、ある関数があって処理によって関数の動作を変更させていときにデコレータを定義しておけば、わざわざ処理ごとに似たような関数を作る手間が省けます。

Javaで例えると、オーバーライドでしょうか？
オーバーライドはメソッドの再定義もしくは再作成みたいな印象なので、追加や変更とはちょっと違う？

# 使い方は？
基本構文は、

```python
@デコレータ名
```

という形で、Javaだとアノテーションみたいに@を使用します。
サンプルコードをいくつか見ましたが、でれも関数(def)の上に定義していました。

以下が、[こちら](https://www.sejuku.net/blog/25130)のサンプルコードを真似して作りました。

```python
def decorateSample(myfunc):
    print("Hello Decorator")
 
@decorateSample
def myfunc():
    print("Test")
```

これを実行すると、「Hello Decorator」と出力されました。
ちなみに「Test」は出力されません。
デコレータを使用する関数名を引数に設定するのがポイントです。

passは「何もしない」という意味です。Javaで表現すると「;」や「return;」でしょうか。

これは、シンタックスシュガー(糖衣構文)という構文のひとつです。
~~美味しそうな名前ですね。~~
自分はシンタックスシュガーという単語を初耳だったので、ちょっと脱線しますが調べました。

### シンタックスシュガーってなに？

[Wikipedia](https://ja.wikipedia.org/wiki/%E7%B3%96%E8%A1%A3%E6%A7%8B%E6%96%87)に普通にページがありました。
Python特有の構文の名前かと思いましたが、違いました。

> 複雑でわかりにくい書き方と全く同じ意味になるものを、よりシンプルでわかりやすい書き方で書くことができるもののことである。

省略して書く構文のことらしいです。
なので、Javaで表現すると、

```java
// シンタックスシュガーじゃない書き方
String[] strs = new String[2];
strs[0] = "abc";
strs[1] = "def";
```

```java
// シンタックスシュガーな書き方
String[] strs = {"abc", "def"};
```

ということです。
特に関数を呼び出していないのに「Hello Decorator」が出力されたことが、シンタックスシュガーということになります。
知らなかった自分が恥ずかしい…

# デコレータは内部で何している？

前述したPythonのコードは、結局のところ、

```python
def decorateSample(myfunc):
    print("Hello Decorator")
 
def myfunc():
    print("Test")

myfunc = decorateSample(myfunc)
```

をしているらしいです。


```python
myfunc = decorateSample(myfunc)
```

ここは何をしているんでしょうか？？
myfuncにdecorateSample関数の内容を代入？置換？している感じでしょうか？
だから、「Test」は出力されず、「Hello Decorator」が出力されるということ？
~~自分の理解力のなさにイライラしてきました~~

# Pythonの標準デコレータ

Pythonには、標準なデコレータが用意されています。
よく使われている一般的なデコレータは、以下の3種類だそうです。

- @classmethod
- @staticmethod
- @property

ひとつひとつ見てみます。

### classmethod

参考にさせていただいたのは[こちら](http://st-hakky.hatenablog.com/entry/2017/11/15/155523)。

> クラスメソッドとは、クラス内で定義されたメソッドで、インスタンス化しなくても呼び出すことができるメソッドのことです。
これは、インスタンスではなくて、クラスそのものに対してなんらかの操作をするメソッドを定義するときに用います。

むむ…
調べる前は「Javaのインスタンスメソッド」 = 「Pythonのクラスメソッド」かと思いましたが、違うみたいです。

Pythonで通常のメソッドの書き方は下のようなイメージ（Javaでいうインスタンスメソッド？）

```python
class SampleClass:
    def hello_world(self):
        print("Hello World!")

# インスタンス化してメソッド呼び出し
sample_class = SampleClass()
sample_class.hello_world()
```

selfってなんじゃい！ってなりましたが、どうやらJavaでいう「this」という意味らしいです。
※ [こちら](http://yoshiori.hatenablog.com/entry/20090716/1247720811)を参考にさせていただきました。更新日付はかなり古いですが、分かりやすいです。

ここで、@classmethodを使用すると、上のようにインスタンス化する必要がなく、呼び出すことができます。

```python
class SampleClass:
    
    @classmethod
    def hello_world(cls):
        print("Hello World!")

# そのままメソッド呼び出し
SampleClass.hello_world()
```

selfをclsに変更しているのは、慣例だからです。
通常のメソッドとクラスメソッドで、第一引数の名前が違うので注意です。
（クラスメソッドは第一引数にクラスを受け取るので、clsと命名するらしい…）

classmethod()関数というものを使うことでも、クラスメソッドを実現できるらしいのですが、非推奨とのこと。
なので、今回は省略。

### staticmethod

classmethodと同様で、[こちらのサイト](http://st-hakky.hatenablog.com/entry/2017/11/15/155523)より引用。

> 簡単に特徴を述べると以下のような違いがあります。
    ・staticmethod : こちらは、クラス内に定義されていても、クラスに関係なく動き、受け取った引数のみ考慮します。乱暴に言うと、ただの関数と変わりません。
    ・classmethod : こちらは、クラス自身を引数として受け取り、受け取った引数と共に用いることができます

staticmethodは、インスタンス化は必要ない、引数を受け取らないメソッドということのようです。
「それだけかよ。じゃあ普通の関数でいいじゃん。どんなときに使えばいいんだ？」ってなりました。

どうやら継承クラスでの動きが違うらしい。
以下がまたサンプルコードを真似っこしたコードです。

```python
class ParentClass():
    str = 'Hello, I am Parent Class'
 
    @classmethod
    def class_method(cls):
        print('class_method: ' + cls.str)
 
    @staticmethod
    def static_method():
        print('static_method: '+ ParentClass.str)

class ChildClass(ParentClass):
    str = 'Hello, I am Child Class'

ChildClass.class_method() # 実行結果：class_method: Hello, I am Child Class
ChildClass.static_method() # 実行結果：static_method: Hello, I am Parent Class
```

子クラスがstatic_method()を呼んでも、親クラスを呼んでいます。
classmethodは、継承が行われると参照先まで変わる。
staticmethodは、子クラスでも動作が変わらないときに使いたい。
というものらしいです。

Javaにもstaticメソッドという名前はありますが、継承した際の挙動が違うので注意が必要そうですね。

### property

また[参考サイト](https://www.sejuku.net/blog/25130)から引用。

> Pythonのクラスは通常、プロパティ（属性）に直接読み書きを行う事が可能です。
クラス作成時に実行される__init__メソッドの引数としてselfが設定されていますよね、
プロパティとは「self.〜」の形の変数のことです。
@propertyを使うとこのデコレータで装飾された関数はgetterという読み取りしかできないプロパティになります。
読み取ることしかできないということは、新たに値を変更することなどができないということです。

は？(´・ω・｀)？
と思って、5回くらい読み直しました。

getterにしか使わないデコレータということ？
getterってJavaでいう

```java
public String getter() {
  return this.hoge;
}
```

みたいなやつのこと？
え？じゃあsetterのデコレータは？

__init__メソッドってなんじゃい！と思って調べたら、**コンストラクタ**でした。なるほど。

というわけで、また見よう見まねで、

```python
class SampleClass(object):
    def __init__(self, hoge):
        self.__hoge = hoge
    
    @property
    def getter(self):
        return self.__hoge

# インスタンス化してメソッド呼び出し
sample_class = SampleClass(1234)
x = sample_class.getter

print(x) # 実行結果：1234
```

それで、気になっていたsetterはというと、

```python
class SampleClass(object):
    def __init__(self, hoge):
        self._hoge = hoge
    
    @property
    def hoge(self):
        return self._hoge
    
    @hoge.setter
    def hoge(self, hoge):
        self._hoge = hoge

# インスタンス化してメソッド呼び出し
sample_class = SampleClass(1234)
x = sample_class.hoge

print(x) # 実行結果：1234

sample_class.hoge = 5678
x = sample_class.hoge

print(x) # 実行結果：5678
```

getterである@propertyを付与しているほうと、メソッド名を合わせることが重要。
（それが分からずかなりハマった…）
@プロパティ名.setterといった名前で作成しましょう。

# 感想
概念としては理解できたけど、いまいち使い道というか、上手な使い方が分からない状況。
たぶん詳細な挙動も理解できていないことが原因だろうなと思っています。

Javaに似たような機能がないと、どうしても理解度が落ちるのが悩み。
PHPやC#だとあまり苦労しなかったのでちょっと悔しい…というかイライラする…

AmazonでIT専門書フェアやっているので、Python本をどれか良さげなのを買います。
今のところ、「WEBアプリかゲームプログラミングなら読みやすいのかなぁ」とか思ってます。

「それは止めておけ！」とか、
「本なんていらね！WEBサイトだけで十分だ！」とか、
「初心者なら絶対この本だ！」などの意見がありましたら、教えていただけるとありがたいです。

# 参考サイト
https://www.sejuku.net/blog/25130
http://st-hakky.hatenablog.com/entry/2017/11/15/155523
https://kiwamiden.com/how-to-use-property-decorator
http://nametake-1009.hatenablog.com/entry/2015/10/21/222829
