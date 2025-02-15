---
title: 【Unity】Unity-Chan!（ユニティちゃん）でCS0234エラーが発生したときの調査結果と解決方法
tags:
  - Unity
  - 初心者
private: false
updated_at: '2019-05-25T20:31:37+09:00'
id: 479406e53d9c6ca137b0
organization_url_name: null
slide: false
ignorePublish: false
---
# 開発環境

- Windows 10
- Unity 2018.3.1f1

# 事象

Asset Storeから、下記の「Unity-Chan! Model」をすべてImportしました。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/9e86d72e-ce1a-546e-e1d2-7a3a4c9730f4.png)
「Assets」→「unity-chan!」→「Unity-chan! Model」→「Prefabs」の「unitychan.prefab」を配置したとき、下記のエラーが発生しました。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/906eee80-76a0-5452-bc50-4f396718388b.png)

```
Assets\unity-chan!\Unity-chan! Model\Scripts\AutoBlink.cs(8,23): error CS0234: The type or namespace name 'Policy' does not exist in the namespace 'System.Security' (are you missing an assembly reference?)
```

該当するソースコードを確認すると、
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/5972e1f5-605c-6cf5-f927-f867aeaf0f3c.png)
```
型または名前空間の名前 'Policy' が名前空間 'System.Security' に存在しません (アセンブリ参照があることを確認してください)。 (CS0234) 
```
メッセージの通りですが、System.SecurityにPolicyが存在しないため、エラーになっています。

# 解決方法
多くの場合、System.Security.Policyのクラスを利用していないため、using節からSystem.Security.Policyを削除することで対処できるとのこと。

実際に消してみると、エラーはなくなりました。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/9efe4328-1160-8852-b18c-3bbeaf846e75.png)
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/cbc8abbd-9deb-3006-16be-12142a7f281a.png)

# 調査してみた&解決方法その2

Unity公式？キャラクターのアセットがエラーしているのは、自分の設定などの問題では？というモヤモヤが消えなかったので、頑張って調べてみました。

とりあえず、Import漏れ、欠落などを疑いましたがそんなことはなさそうでした。
（そもそもスクリプトの問題の時点で、関係なさそうですが…）

「C# System.Security」でググったところ、MS公式のドキュメントが出てきました。
[System.Security Namespace](https://docs.microsoft.com/ja-jp/dotnet/api/system.security?view=netframework-4.8)
ここで、そもそもUnityで.NETのバージョンを意識したことがないことに気が付きました。

「Edit」→「Project Settings」→「Player」の
Other Settings、ConfigurationsのApi Compatibillity Levelが.NET Standard 2.0になっていました。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/6044fee4-2c81-4d67-bce3-c98fdf91fa69.png)
これを.NET 4.xに変更しました。

これでも、エラーが出なくなりました。

# おわりに

自分が調査して見つけた解決方法が正しいのか分かりません。
解決方法が間違っていたら、教えてください…

## 2019年5月25日追記

@KTA552 さんに、コメントにて教えていただきました。

### System.Security.Policyは消しちゃって大丈夫

Unity Japan公式に問い合わせたところ、使っていないので消しちゃって大丈夫との返事をもらったそうです。
そのため、本記事の最初に記載しましたコメントアウト or 削除が最適解ということです。

### ユニティちゃんトゥーンシェーダー Ver.2.X.Xを使用する

また、もう一つ回避方法があるそうです。
それは、[ユニティちゃんトゥーンシェーダー Ver.2.X.X](https://github.com/unity3d-jp/UnityChanToonShaderVer2_Project) リポジトリの配下になる ```AutoBlink.cs``` を適用することです。

方法は簡単で、[unity3d-jp/UnityChanToonShaderVer2_Project](https://github.com/unity3d-jp/UnityChanToonShaderVer2_Project/blob/master/Assets/UnityChan/Scripts/AutoBlink.cs) をダウンロード（もちろんgit cloneしてもOK）して、置き換えるだけです。
差分は、```using System.Security.Policy``` の有無のみです。

ユニティちゃんトゥーンシェーダー Ver.2.X.Xのリポジトリのほうが新しいそうなので、こちらで置き換えてしまうのも手だそうです。

# 参考文献
[Unityちゃんのインポート](https://ja.stackoverflow.com/questions/52819/unity%E3%81%A1%E3%82%83%E3%82%93%E3%81%AE%E3%82%A4%E3%83%B3%E3%83%9D%E3%83%BC%E3%83%88)
["error CS0234: The type or namespace name 'Policy' does not exist in the namespace 'System.Security'" エラーが発生する (Unityプログラミング)](https://www.ipentec.com/document/unity-error-cs0234-the-type-or-namespace-name-policy-does-not-exist-in-namespace-system-security)
