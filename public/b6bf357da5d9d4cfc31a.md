---
title: 【Ruby】Ruby初心者がよく使うと思う配列のメソッド
tags:
  - Ruby
  - 初心者
private: false
updated_at: '2019-08-11T23:35:42+09:00'
id: b6bf357da5d9d4cfc31a
organization_url_name: null
slide: false
ignorePublish: false
---
# はじめに
いま、Rubyプログラマに勧めてもらった[チェリー本](https://www.amazon.co.jp/dp/B077Q8BXHC/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)を使って学習を進めています。
Rubyの勉強を開始してから1週間くらいしか経っていない初心者が、覚えておきたい配列のメソッドを調べました。
個人的な振り返りメモも兼ねています。
ぜひ間違えていたら、コメントや編集リクエストで教えていただけると嬉しいです。

# 参考文献
[プロを目指す人のためのRuby入門 言語仕様からテスト駆動開発・デバッグ技法まで Software Design plus \| 伊藤 淳一 | コンピュータ・IT | Kindleストア | Amazon](https://www.amazon.co.jp/dp/B077Q8BXHC/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)
[start_with? (String) - Rubyリファレンス](https://ref.xaio.jp/ruby/classes/string/start_with)
[class Array (Ruby 2.6.0)](https://docs.ruby-lang.org/ja/latest/class/Array.html#I_EACH)
[Rubyのeachでindexを取得する：each_with_index \| UX MILK](https://uxmilk.jp/23853)
[【Ruby】each_with_indexは知ってたけどeach.with_indexは知らなかった… - 訳も知らないで](https://shirusu-ni-tarazu.hatenablog.jp/entry/2012/11/04/173513)
[class Enumerator (Ruby 2.6.0)](https://docs.ruby-lang.org/ja/latest/class/Enumerator.html#I_WITH_INDEX)

# 動作確認環境

- Windows 10
- ruby 2.5.5p157

# eachメソッドでループする

今回勉強に使わせてもらっている[チェリー本](https://www.amazon.co.jp/dp/B077Q8BXHC/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)によると、for文ではなく、eachメソッドを使用することが多いとのことです。

```ruby
arr = ['Spring', 'Summer', 'Autumn', 'Winter']
arr.each do |n|
  puts n
end
```

実行結果

```
Spring
Summer
Autumn
Winter
```

# eachメソッドでindex（添字）を取得したい
Enumerableモジュールのメソッドの一つである```each_with_index```を使用します。

```ruby
arr = ['Spring', 'Summer', 'Autumn', 'Winter']
arr.each_with_index do |n, index|
  puts "#{index}, #{n}"
end
```

実行結果

```
0, Spring
1, Summer
2, Autumn
3, Winter
```

# index（添字）の始まりの値を設定したい

Enumeratorクラスのメソッドの一つである```with_index```メソッドを使用します。
サンプルは、2からindexを開始するという意味です。

```ruby
arr = ['Spring', 'Summer', 'Autumn', 'Winter']
arr.each.with_index(2) do |n, index|
  puts "#{index}, #{n}"
end
```

実行結果

```
2, Spring
3, Summer
4, Autumn
5, Winter
```

# 配列同士を比較したい

サンプルコード

```ruby
arr = ['Spring', 'Summer', 'Autumn', 'Winter']
arr_compare = ['Spring', 'Summer', 'Autumn']
puts arr.eql?arr_compare   # false
arr_compare.push('Winter') # 要素を追加してから比較
puts arr.eql?arr_compare   # true
```

# 配列が空かどうか確認

```ruby
arr = ['Spring', 'Summer', 'Autumn', 'Winter']
arr_empty = []
puts arr_empty.empty? # true
puts arr.empty?       # false
```

# 指定した範囲の配列要素を取得する

サンプルコード

```ruby
arr = ['Spring', 'Summer', 'Autumn', 'Winter']
p arr[1...3] # 3を含まない
p arr[1..3]  # 3を含む
```

実行結果

```
["Summer", "Autumn"]
["Summer", "Autumn", "Winter"]
```

# 条件に一致する要素を取り出して新しい配列を作る

サンプルコード

```ruby
arr = ['Spring', 'Summer', 'Autumn', 'Winter']
# 文字列の先頭がSの要素を抽出
p arr.select { |n| n.start_with?("S") }
```

実行結果

```
["Spring", "Summer"]
```

# 条件と不一致の要素を取り出して新しい配列を作る

サンプルコード

```ruby
arr = ['Spring', 'Summer', 'Autumn', 'Winter']
# 文字列の最後尾がrの要素を抽出
p arr.reject { |n| n.end_with?("r") }
```

実行結果

```
["Spring", "Autumn"]
```

# 全要素に対してブロック内で評価した結果で新しい配列を作る

```ruby
p arr.map { |n| n.start_with?("S") }
```

実行結果

```
[true, true, false, false]
```

# 条件に一致する最初の要素を返す

サンプルコード

```ruby

# uを含む文字列を検索
p arr.find { |n| n.index("u")}
```

実行結果

```
"Summer"
```

# おわりに（おまけ）

実は[チェリー本](https://www.amazon.co.jp/dp/B077Q8BXHC/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)を購入する前に、
この記事の下書きを作っていたのですが、
だいたい（もしかしたら全部）チェリー本に書いていました。

まとめた意味がなくなってしまい、すごく悲しくなりました。

