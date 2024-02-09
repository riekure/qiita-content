---
title: 【Unity 2019以上】UnityでVisual Studio Codeを使用できるようにするまでの手順
tags:
  - Windows
  - Unity
  - 初心者
  - VSCode
private: false
updated_at: '2023-12-20T22:44:32+09:00'
id: ec35feeef553637a4113
organization_url_name: null
slide: false
ignorePublish: false
---
:::note
本記事はUnity 2019以上のバージョンが対象です。
Unity 2018以下のバージョンの使っている方はこちらの記事を参考にしてください。
[【Unity 2018以下】UnityでVisual Studio Codeを使用できるようにするまでの手順](https://qiita.com/riekure/items/c45868f37a187f8e1d69)
:::

:::note warn
今回導入する C# Dev Kit は、個人やオープンソースプロジェクト、商用でも最大5人のチームの場合は無料で利用できます。
上記以外の場合は Visual Studio Professional 以上のライセンスが必要ですので注意してください。
https://code.visualstudio.com/docs/csharp/cs-dev-kit-faq#_who-can-use-c-dev-kit
:::

# 動作確認環境
- Windows11
- Unity Hub 3.6.1
- Unity 2022.3.10f1

#### 導入するVSCodeの拡張機能

- [C#](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp)
- [C# Dev Kit](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit)
- [IntelliCode for C# Dev Kit](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.vscodeintellicode-csharp)
- [.NET Install Tool](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.vscode-dotnet-runtime)
- [Unity for Visual Studio Code](https://aka.ms/vscode-unity)

:::note warn
今回インストールする [Unity for Visual Studio Code](https://aka.ms/vscode-unity) は2023年12月20日現在 preview 版です。
そのため、正式版がリリースされたら、本記事の手順から変更される場合があります。
:::

# Unity Hubをインストールする

Unity Hub とは Unity のバージョンを管理してくれるアプリです。
Unity 本体ではありません。
基本的には Unity Hub と Unity はセットで使います。
Unity Hub は下記ページから、ダウンロード→インストールしてください。
https://unity.com/ja/download

# Unity 2019以降のバージョンをインストールする

Unity Hub を起動して、左メニューの「インストール」を選択します。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/c4921dec-56a7-696c-ca08-2131c432e366.png)
「エディターをインストール」を選択します。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/89cb33e6-7d02-1ba5-1b5c-57bf67d5e399.png)
任意のバージョンの「インストール」を選択します。
特に事情がなければ、長期サポート(LTS)のバージョンをインストールすると良いと思います。
今回は `2022.3.10f1` をインストールします。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/2f63b3df-b266-0c3b-7ffb-9947879153c5.png)

インストールするモジュールを選択します。
作成するアプリ、ゲームに合わせて「プラットフォーム」にチェックを入れます。
自分は Android 向けアプリを作るので「Android Build Support」にチェックのみ入れます。
必要な方は「日本語」にもチェックを入れましょう。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/dc8c4229-eb09-a1b2-71ba-668b0b5c8d1e.png)

利用規約に同意して、インストールします。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/c2b9af25-ec47-b3fb-b86b-e2ec37788a3d.png)

インストール完了するまで待ちます…
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/84d1f788-a276-d6aa-a474-d172acf80c3e.png)


# VSCodeをインストールする
Visual Studio CodeをOSのバージョンに合わせてインストールします。
[Download Visual Studio Code - Mac, Linux, Windows](https://code.visualstudio.com/download)
今回は、事前にインストールしていたので省略します。

今回は、Windows11 なので赤枠部分のボタンを押して、インストーラーをダウンロードしました。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/3d94b58c-47d5-e10c-6107-ce9dfa116e48.png)

インストーラーを起動します。

ライセンスに「同意する」を選択して「次へ」

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/5269f04d-a347-1c1a-4cdb-64e638b6f52a.png)

インストール先のフォルダを設定してください。
今回はデフォルトから変更せずに「次へ」

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/eeb731e7-76c6-6768-226d-4c76246bf2d0.png)

ショートカットを作成する場所を指定してください。
作成不要な方は「スタートメニューフォルダーを作成しない」にチェックを入れてください。
これもデフォルトから変更せずに「次へ」

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/53b198bd-17d0-1e81-a5ad-4104f341db1d.png)

実行する追加タスクを選択してください。

「エクスプローラーのファイルコンテキストメニューに[Codeで開く]アクションを追加する」にチェックを入れると、エクスプローラーでファイルを選択した状態で右クリックすると、「Codeで開く」を追加することができます。

「エクスプローラーのディレクトリコンテキストメニューに[Codeで開く]アクションを追加する」にチェックを入れると、エクスプローラーでフォルダを選択した状態で右クリックすると、「Codeで開く」を追加することができます。

「サポートされているファイルの種類のエディターとして、Codeを登録する」にチェックを入れると、エクスプローラーでファイルを右クリック > プログラムから開く を選択したときに VSCode が選べるようになります。

「PATHへの追加（再起動後に使用可能）」は、コマンドプロンプトから code と入力すると、VSCode を起動することができるようになります。

今回は、下記の通り「サポートされているファイルの種類のエディターとして、Codeを登録する」以外にチェックを入れて「次へ」
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/49f2e12a-538c-2f75-bf90-de973f032850.png)

確認して問題なかったら「インストール」

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/7f9c5566-ce12-5ab8-9225-be9ff3f3b98e.png)

# VSCode に拡張機能をインストールする

はじめに C# 関連の拡張機能をインストールします。
具体的には下記の4つをインストールします。

- [C#](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp)
- [C# Dev Kit](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit)
- [IntelliCode for C# Dev Kit](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.vscodeintellicode-csharp)
- [.NET Install Tool](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.vscode-dotnet-runtime)

VSCode を起動して、 Extension を開きます。（ショートカットは Ctrl + Shift + x）
`c#` と検索すると、Microsoft 提供の `C# Dev Kit` が表示されるはずです。
`C# Dev Kit` をインストールすると、 [C# Dev Kit](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit)の他に、自動的に [C#](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp),  [IntelliCode for C# Dev Kit](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.vscodeintellicode-csharp), [.NET Install Tool](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.vscode-dotnet-runtime) もインストールされます。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/f25cb502-9724-d7b3-6e4d-a0eb91b508d9.png)

次に Unity の拡張機能をインストールします。

- [Unity](https://aka.ms/vscode-unity)

`Unity`と検索し、Microsoft が発行者である `Unity` が表示されます。
こちらをインストールしてください。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/19886d50-0b99-9555-efaa-585247cb72e5.png)

# Unity の新規プロジェクトを作成する

Unity Hub の右上の「新しいプロジェクト」を押します。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/0220270f-d128-87f2-4219-6d63034e15a2.png)

作成したいゲームに合わせて、テンプレートを選択してください。
プロジェクト名と保存場所も、任意で変更してください。
今回、テンプレートは3Dを選択しました。
「Unity Cloud に接続」と「Unity Version Control を使用する」は、どちらもチェックせずにプロジェクトを作成しました。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/7cc3abe3-e1af-3849-af7e-d2c2107a678a.png)

「プロジェクトを作成」を押すと、Unityプロジェクトが自動的に起動するので待ちましょう…

# Unity の Package Manager から Visual Studio Editor を Import する

Window > Package Manager を選択して、 Package Manager を起動してください。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/36a00a0b-d579-b48a-54db-c1c24d66cf66.png)

Visual Studio Editor を選択、Unlock してください。

:::note warn
Visual Studio Code Editor と間違えないように気をつけてください。
こちらは、現在メンテナンスされていません。
:::

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/448026b2-4734-6134-5196-6804e14604e3.png)

このときバージョンが2.0.20以上であるか確認してください。
自分の環境では 2.0.18 となっており、2.0.20以上ではなかったので Update します。
Version History から 2.0.20以上のバージョンを選択して Update してください。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/d581a421-d875-63c1-04f3-d5f388a7677a.png)

確認ダイアログが表示されるので Yes

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/f7e7b609-92ab-01d9-4d84-fd732a0a5b90.png)

# Unity から開くエディタを VSCode に変更する

Edit > Preferences を選択して Preferences を開きます。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/9fdae79a-7fa0-9756-39e9-2cc08304b10a.png)


External Tools > External Script Editor を Visual Studio Code を選択してください。
このとき、下部に Visual Studio Editor v2.X.X enabled と表示されていることを確認してください。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/b53bb7dd-050f-3b95-d3cc-e9b0ebcf186c.png)

Sign in します。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/88d0b32e-db31-7ce8-bdfa-6f7c0f09f65d.png)

Allow すると、ブラウザに飛ばされるので Microsoft アカウントでログインしてください。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/b2af3868-3c58-6771-51c9-bd84c29a76a4.png)

# トラブルシューティング

自分の場合、プロジェクト内のC#コードを開いたら、VSCode の左下にエラーが表示されていました。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/a68e26d7-c4c7-64d5-9f1c-e250178fc66f.png)

```
[info] It was not possible to find any compatible framework version
The framework 'Microsoft.NETCore.App', version '6.0.0' was not found.
  - The following frameworks were found:
      2.1.9 at [C:\Program Files\dotnet\shared\Microsoft.NETCore.App]
      2.1.15 at [C:\Program Files\dotnet\shared\Microsoft.NETCore.App]
      2.2.4 at [C:\Program Files\dotnet\shared\Microsoft.NETCore.App]
      3.1.1 at [C:\Program Files\dotnet\shared\Microsoft.NETCore.App]

You can resolve the problem by installing the specified framework and/or SDK.

The specified framework can be found at:
  - https://aka.ms/dotnet-core-applaunch?framework=Microsoft.NETCore.App&framework_version=6.0.0&arch=x64&rid=win10-x64

[info] Project system initialization finished. 0 project(s) are loaded, and 1 failed to load.
```

.NETCore のバージョン 6.0.0 をインストールしないといけないようなので、下記のサイトから 6.0.417 のインストーラーをダウンロードしました。
https://dotnet.microsoft.com/ja-jp/download/dotnet/6.0
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/4df52bf3-e2f2-2ac6-97f6-7230a996d171.png)

インストール後は（念のため）Unity と VSCode を起動し直したところ、エラーが消えました。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/510a70dc-bf6e-67f5-e54e-c919ec1ab9c0.png)

# デバッグしてみる

ブレイクポイントを設定します。
設定したい行をクリックすれば、赤い丸が表示されます。

VSCodeのウィンドウ左端にある[デバッグ]アイコンを選択します。
[Attach to Unity]を選択した状態で、▶ボタンを押して Unity の画面に戻ります。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/4266bc47-133b-5439-17a5-912cedf43f0b.png)

初めてデバッグしようとしたら、Unity の画面でダイアログが表示されます。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/709590c9-619f-8f06-f0b9-46796a9e2c6d.png)

```
You are trying to attach a debugger, but Debug Mode is switched off in your project.

When Unity is in Debug Mode, C# performance is reduced, but you can attach a debugger. Switching to Debug Mode also recompiles and reloads all scripts.

You can enable Debug Mode temporarily for this Editor session, switch it on for all projects until further notice, or cancel attaching the debugger.

If you switch it on for all projects, you can change it later in the "Code Optimization on

Startup" setting in the Preferences window.
```

プロジェクトでデバッグモードがOFFになっているよ
デバッグモードにしたら、C#のパフォーマンスが低下するよ
一時的にデバッグを有効にするか、すべてのプロジェクトでデバッグを有効にするか、キャンセルするか選べるよ
すべてのプロジェクトでデバッグをONにしたときは「Code Optimization on Startup」設定で変更できるよ
だそうです。

[Enable debbuing for this session] か [Enable debugging for all projects] を選択します。

最後にUnity側でゲームの再生ボタンを押して、ブレイクポイントで止まって、以下のような画面になればOKです。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/e4eccc8c-c802-71c1-3171-c7501ca5d2b4.png)

# 参考文献

https://code.visualstudio.com/docs/other/unity

https://forest.watch.impress.co.jp/docs/news/1521609.html
