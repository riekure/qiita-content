---
title: 【Java】StringBuilderの末尾から指定した文字数分を削除する
tags:
  - Java
private: false
updated_at: '2019-02-15T13:02:19+09:00'
id: e3566bc0e3193370d349
organization_url_name: null
slide: false
ignorePublish: false
---
# はじめに

~~StringBuilderの標準メソッドで用意されていると思っていたのですが、どう探しても見つからなかったので自作しました。~~
↑誤解を招く記載でした……

末尾から指定した文字数を消すことに特化したメソッドが用意されていないかと思ったのですが、探しても見つからなかったので自作しました。です。


# 動作確認環境
- java 1.8.0

# サンプルソースコード①

```java
public class Demo {
    public static void main(String[] args) {
    	StringBuilder sb = new StringBuilder("hoge");

        // 末尾から1文字分を削除
    	sb.setLength(sb.length()-1);

        // 実行結果：hog
    	System.out.println(sb);
    }
}
```

```setLength``` は、シーケンスの文字列の長さを設定するものです。


```length()``` で、いま現在の文字列の長さを返します。上の例だと、4が返ってきています。
あとは、```length()``` から自分が削除したい文字数分を減算するだけです。


注意点としては、0未満の文字列長を指定してしまうと、```java.lang.StringIndexOutOfBoundsException``` とエラーが発生してしまう点です。

```java
StringBuilder sb = new StringBuilder("hoge");
sb.setLength(sb.length()-5);
// エラー：java.lang.StringIndexOutOfBoundsException: String index out of range: -1
```

```setLength``` する前に、```StringBuilder``` の長さを確認するほうがよいかもしれません。

```java
// n文字以上ならば、末尾からn文字削除
if (sb.length() >= n) {
	sb.setLength(sb.length()-n);
}
```

# サンプルソースコード②

```delete(int start, int end)``` を使用する方法です。
コメントにて教えていただきました。

自分も最初に思いついたのですが、開始位置と終了位置どちらも指定する必要があり、可読性が低いのでは…と思い、自分の中で却下しました。
```length()``` を2回書く必要があると思ったので…

そもそもlength()を変数に持たせれば1回書くだけで済むじゃん！可読性悪くないじゃん！と思い直しました。
deleteという文字があれば、文字を削除するということも分かりやすいですよね。

```java
StringBuilder sb = new StringBuilder("hoge");

int n = 2;              // 末尾から削除したい文字数
int size = sb.length(); // length()をint型変数に格納

// 末尾から2文字文を削除
sb.delete(size-n, size);

// 実行結果：ho
System.out.println(sb);
```

注意点は、サンプルソースコード①と同様なので、省略します。

# サンプルソースコード③

```deleteCharAt(int index)``` を使用する方法です。
こちらもコメントにて教えていただきました。

この場合は、**末尾から1文字だけ削除**することができます。
**末尾から複数文字数を削除することはできません**ので、ご注意ください。

しかし、こちらは上2つのサンプルソースコードより、（個人的に）可読性が良いと思います。
自分は、偉そうに公式ドキュメントを示しておきながら、全く気づくことができませんでした。
なので、戒めに記載しておきます。

```java
StringBuilder sb = new StringBuilder("hoge");

// 末尾から1文字分を削除
sb.deleteCharAt(sb.length()-1);

// 実行結果：hog
System.out.println(sb);
```

# 終わりに

もっと良い実装があったら教えてください。

# 参考文献

[StringBuilder (Java Platform SE 8)](https://docs.oracle.com/javase/jp/8/docs/api/java/lang/StringBuilder.html)
