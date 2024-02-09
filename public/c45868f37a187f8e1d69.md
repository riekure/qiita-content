---
title: 【Unity 2018以下】UnityでVisual Studio Codeを使用できるようにするまでの手順
tags:
  - Unity
  - 初心者
  - VSCode
private: false
updated_at: '2023-12-20T22:43:54+09:00'
id: c45868f37a187f8e1d69
organization_url_name: null
slide: false
ignorePublish: false
---
:::note
Unity 2019以降のバージョンを使っている方は、こちらの記事を参考にしてください。
[【Unity 2019以降】UnityでVisual Studio Codeを使用できるようにするまでの手順](https://qiita.com/riekure/items/ec35feeef553637a4113)
:::

# 2023年3月9日追記

本記事で導入している [Debugger for Unity](https://marketplace.visualstudio.com/items?itemName=Unity.unity-debug) が**非推奨**になっています。

非推奨になったことについて、Unity-Technologies が言及していました。
https://github.com/Unity-Technologies/vscode-unity-debug/issues/206
要約すると、お金的にも技術的にも今後サポートする予定がないとのことです。

現在の自分の環境では VSCode で問題なく開発できています。 
しかし今後の Unity や VSCode の更新によって、動かなくなる可能性があります。
今のうちに、 Visual Studio や JetBrains Rider に慣れていくほうが良いかと思います。

上記の現状を踏まえて、「いや！絶対に VSCode を使いたいんだ！」という方だけ、本記事を参考にしてくれると幸いです。

# 動作確認環境
- Windows 10
- Unity 2018.3.1f1 Personal

# Visual Studio Codeとは

- 通称「VSCode」。
- Microsoft社が開発したオープンソースのテキストエディタ。
- 軽量で高速、低消費電力。
- デバッグ機能付き。
- Gitをサポート。
- IntelliSenseをサポート。

# VSCodeをインストールする

Visual Studio CodeをOSのバージョンに合わせてインストールします。
[Download Visual Studio Code - Mac, Linux, Windows](https://code.visualstudio.com/download)
今回は、事前にインストールしていたので省略します。

# スクリプトを開くエディタをVSCodeに変更する

「Edit」→「preferences」→「External Tools」→「External Script Editor」を変更すると、使用したいエディタが起動するようになります。
（変更前のdevenv.exe(Community)は、Visual Studio 2019 Communityです。）
![preferences.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/32971324-79c5-a459-411a-f79f101db8b5.png)
![preferences2.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/f2b10592-7cfa-b8e9-1544-fa83f013a28d.png)
今回は、VSCodeに変更します。
これで、Unityでスクリプトを選択すると、VSCodeが起動するようになります。

# VSCodeでC#を書けるようにする

VSCodeで起動するようになりましたが、入力補完も何もありません。
このままだと開発効率が悪いです。

## C#の拡張機能を導入

C#の拡張機能を導入します。

![vscode_extensionC#.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/1baf53ed-9b56-2ad0-49cf-2147d7a0f473.png)


## .NET CLI toolsをインストール

![vscode_extensionC#2.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/40e0537b-8d54-5bd2-ae44-05b08732f1be.png)
> The .NET CLI tools cannot be located. .NET Core debugging will not be enabled. Make sure .NET CLI tools are installed and are on the path.

というエラーが出ました。
「Get .NET CLI tools」ボタンを押して、.NET CLI toolsをインストールします。
インストールしても、エラーが消えなかったので、PCを再起動しました。
そしたらパスが通ったようでエラーが出なくなりました。

## .NETFramework,Version=v4.5をインストール

<font color="Red">**----------2020/10/24追記ここから----------------**

コメントにて教えていただきました。
本記事では、 Visual Studio から「.NET Framework 4.5 Targeting Pack」をインストールする手順となっています。
[Microsoft公式ページ](https://dotnet.microsoft.com/download/dotnet-framework/net471)から直接ダウンロードしてもよいと思われます。
（申し訳ありませんが、筆者が実際に動作確認したわけではないです…）
詳しい参考記事は下記ページを見てください。

https://code.visualstudio.com/docs/other/unity#_enabling-code-completion-for-recent-versions-of-unity

あくまでVSCodeからインストールしてくださいと怒られた.NETFramewarkのバージョンをインストールするようにしてください。

<font color="Red">**----------2020/10/24追記ここまで----------------**

![vscode_extensionC#3.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/fb55b5f4-1b65-8380-dfca-c0a32cf4f7b8.png)
> フレームワーク ".NETFramework,Version=v4.5" の参照アセンブリが見つかりませんでした。これを解決するには、このフレームワーク バージョンの SDK または Targeting Pack をインストールするか、SDK または Targeting Pack をインストールしているフレームワークのバージョンにアプリケーションを再ターゲットしてください。アセンブリはグローバル アセンブリ キャッシュ (GAC) から解決され、参照アセンブリの代わりに使用されるため、アセンブリが目的のフレームワークに正しくターゲットされない場合もあります。

 が出力されるようになりました。
 これは、 Visual Studioでの作業が必要です。

 「ツール」 →「ツールと機能を取得」をクリックします。
![ツールと機能を取得.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/a0762f44-45ed-278b-b2b4-5bbfef2f2bfc.png)
「.NET Framework 4.5 Targeting Pack」を選択して、インストールしてください。
![net_framework4.5.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/62ea51b6-978b-7f05-9159-25bfb2ae8ed9.png)
これでやっと、入力補完ができたり、参照の検索ができるようになりました。

# VSCodeでデバッグできるようにする

デバッグできないと、これまた開発効率が悪いので、VSCodeでデバッグできるようにします。

## Debugger for Unityの拡張機能を導入

![debuggerForUnity.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/754d039e-df14-d635-8275-1668f0f33fa5.png)
Debugger for Unityの拡張機能を導入します。
C#の拡張機能と同じ方法でインストールします。

## デバッグする方法

ブレイクポイントを設定します。
止めたい行をダブルクリックすれば、設定できます。
![debug.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/a7b38b66-e726-8b3b-d572-4245d644f9fe.png)
プレイクポイントを設定したら、▶ボタンを押します。
最後にUnity側でゲームの再生ボタンを押して、ブレイクポイントで止まればOKです。
![debug2.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/cb446c2f-8526-3827-7639-6bbce93724d1.png)

# Unity 関連のスニペットを使えるようにする

Unity 関連の補完を強くします。
[MonoBehaviour Snippets](https://marketplace.visualstudio.com/items?itemName=zrachod.mono-snippets) という拡張ツールをインストールします。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/f7947445-bf3e-2525-4f8d-b0483a8557c4.png)

https://marketplace.visualstudio.com/items?itemName=zrachod.mono-snippets
の gif が非常に分かりやすいです。

MonoBehavior の関数だけでなく、MonoBehavior を継承したクラスの作成や、Editor の拡張クラス、Debug.Log なども一瞬で書くことができます。
参考文献：[【Visual Studio Code】Unity 関連のスニペットを使えるようにする「Unity Code Snippets」](https://baba-s.hatenablog.com/entry/2018/01/15/133400)

# クラスやメソッドなどのコメントを書きやすくする
[C# XML Documentation Comments](https://marketplace.visualstudio.com/items?itemName=k--kato.docomment) をインストールしてください。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/84ea671c-6bc9-7c9a-b440-d9dad481ea07.png)
クラスやメソッドの1行上で、 スラッシュ3つ（///）と入力すると、 XML 形式のコメントを挿入することができます。

クラスの場合は、

```c#
/// <summary>
/// 
/// </summary>
```

メソッドの場合は、引数や戻り値に合わせて自動的に、

```c#
    /// <summary>
    /// 
    /// </summary>
    /// <param name="x"></param>
    /// <param name="y"></param>
    /// <returns></returns>
```

のようなコメントを自動生成することができます。

# 終わりに

~~Visual Studioに比べて、VSCodeの入力補完が弱い気がしました。~~
~~自分の設定次第かもしれないので、もう少しVSCodeで頑張ってみようと思います。~~

[MonoBehaviour Snippets](https://marketplace.visualstudio.com/items?itemName=zrachod.mono-snippets) のおかげで、少しマシになりました。
EditorConfig for VS Code は、dot-net 系をサポートしていないので省略しています。

他に良い拡張機能があったら教えて下さい。

# 参考文献
 [Visual Studio Codeで「フレームワーク .NETFramework,Version=v4.5 の参照アセンブリが見つかりませんでした。」と表示される時の対処方法 - ニワトリ再生産](https://takubokubird.hatenablog.com/entry/2019/01/06/023155)
 [【Unity】Unity 2018.2で「C# プロジェクト Assembly-Csharpは、このコンピューターにインストールされていない」が出たので、その対処 - テラシュールブログ](http://tsubakit1.hateblo.jp/entry/2018/06/17/030129)
[【Visual Studio Code】Unity 関連のスニペットを使えるようにする「Unity Code Snippets」](https://baba-s.hatenablog.com/entry/2018/01/15/133400)
