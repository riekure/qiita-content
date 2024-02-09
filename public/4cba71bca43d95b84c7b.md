---
title: Unity + Visual Studio CommunityでC#をデバッグ実行する
tags:
  - C#
  - VisualStudio
  - Unity
  - 初心者
private: false
updated_at: '2019-03-11T19:11:51+09:00'
id: 4cba71bca43d95b84c7b
organization_url_name: null
slide: false
ignorePublish: false
---
記事で間違いなどありましたら、コメントや編集リクエストで教えていただけると幸いです。

# 動作確認環境

- Windows 10
- Unity 2018.3.1f1
- Visual Studio Community 2017

# 1. ブレイクポイントを設定する
※ 「2. Unity デバッガーのアタッチ」と順番が前後しても問題ありません。

Unityから、任意のC#スクリプトを選択し、Visual Studio Community(以下、VSと表記)を起動します。

VSにブレイクポイントを設定するため、行数表示の左部をクリックまたはF9ボタンを押下します。
そうすると、下の画像のように、赤い点？丸？が表示されます。

![vs02.png](https://qiita-image-store.s3.amazonaws.com/0/233011/84c09ed2-d0e7-d696-413a-b945cfa5cf4d.png)

# 2. Unity デバッガーのアタッチ
※ 「1. ブレイクポイントを設定する」と順番が前後しても問題ありません。

![vs03.png](https://qiita-image-store.s3.amazonaws.com/0/233011/ae681231-d036-9a06-64e9-add2aa12760e.png)

「デバッグ」→「Unity デバッガーのアタッチ」をクリックします。
そうすると、下の画像のようなポップアップが表示されます。

デバッグしたい任意のプロジェクトを選択し、OKボタンを押下します。

画像では、1つのプロジェクトしか起動していなかったため、1つのプロジェクトしか表示されていません。
もし、複数のUnityプロジェクトを同時起動していれば、複数のプロジェクトから選択することになります。

![vs04.png](https://qiita-image-store.s3.amazonaws.com/0/233011/2ad8f562-ce37-217b-7a7a-9617a4cde389.png)

OKボタンを押すと、下の画像のようになります。

![vs05.png](https://qiita-image-store.s3.amazonaws.com/0/233011/89e236f9-6e97-5a2c-3ec0-877376c3d2d0.png)

# 3. Unity側でPlayボタンを押下する

Unity側でPlayボタン（再生ボタン？）を押下して、ブレークポイントで実行が止まればOKでず。

![vs06.png](https://qiita-image-store.s3.amazonaws.com/0/233011/3bf6f962-143a-ac77-387d-b1df23859507.png)

# 終わりに（雑記）

この記事書きながら、VSではなくVisual Studio Code（以下、VSCodeと表記）を使ってもよいのでは？と思い始めました。
調べた限り、VSCodeでもデバッグできるようです。

VSとVSCodeの機能の違いを調査して、移行しても問題なさそうだったら、使い慣れているVSCodeに移行しようと思います。


