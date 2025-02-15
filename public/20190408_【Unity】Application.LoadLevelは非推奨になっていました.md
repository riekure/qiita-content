---
title: 【Unity】Application.LoadLevelは非推奨になっていました
tags:
  - C#
  - Unity
  - 初心者
private: false
updated_at: '2019-04-08T20:21:56+09:00'
id: c593e6b31449927cf21c
organization_url_name: null
slide: false
ignorePublish: false
---
# 背景

[Unity5 3D/2Dゲーム開発 実践入門 作りながら覚えるスマートフォンゲーム制作（吉谷 幹人） \| 書籍 本 | ソシム](http://www.socym.co.jp/book/967)の本に書いあるコードを写経していたら、他のシーンを呼び出す```Application.LoadLevel```は非推奨ですと警告されました。

![loadlevel.png](https://qiita-image-store.s3.amazonaws.com/0/233011/b9ccad74-1e0c-ad28-9a82-668cd921d96d.png)


# 修正案

Visual Studioが親切に、Use```SceneManager.LoadScene```と教えてくれたので、言われた通りに修正すると、想定どおりに「ゲームタイトルのシーン⇔メインゲームのシーン」に遷移できました。

![loadscene.png](https://qiita-image-store.s3.amazonaws.com/0/233011/f7709abb-e006-c085-a9ed-63bd447c66a0.png)


# 終わりに

どうやらUnity 5.3（2015年12月16日リリース）の頃から、```Application.LoadLevel``` が非推奨になったようです。
自分がギリギリUnityを触ってた頃だったのですが、知らなかったので記事にしました。

他にも、自分が過去に使っていた```Application.LoadLevelAdditive```（遷移前のシーンを残して、他のシーンを呼び出す）も非推奨になっていました。
同じく```Application.LoadLevel```を使用すると、警告は消えます。

まとめると、下のような感じです。

```C#
        // 他のシーンを呼び出す
        Application.LoadLevel("Main"); // 非推奨
        SceneManager.LoadScene("Main"); // OK

        // 遷移前のシーンを残して、他のシーンを呼び出す
        Application.LoadLevelAdditive("Main"); // 非推奨
        SceneManager.LoadScene("Main", LoadSceneMode.Additive); // OK

        // 現在読み込んでいるシーンを再読込
        Application.LoadLevel(Application.loadedLevel); // 非推奨
        SceneManager.LoadScene(SceneManager.GetActiveScene().name); // OK
```

