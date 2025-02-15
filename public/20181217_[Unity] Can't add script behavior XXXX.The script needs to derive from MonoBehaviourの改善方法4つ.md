---
title: >-
  [Unity]"Can't add script behavior XXXX.The script needs to derive from
  MonoBehaviour"の改善方法4つ
tags:
  - C#
  - Unity
  - 初心者
private: false
updated_at: '2018-12-17T10:10:29+09:00'
id: 90cc2aa26460daf1d75a
organization_url_name: null
slide: false
ignorePublish: false
---
# 背景

3年弱ぶりにUnityを触った初心者です。
間違いがあったらご指摘いただければありがたいです。

# 事象

オブジェクトに対してスクリプトをアタッチしようとしたときに、下記のメッセージがポップアップで表示されることがあります。

![error_message.png](https://qiita-image-store.s3.amazonaws.com/0/233011/8b588e92-7c5a-1a12-a91f-854b397a0a7c.png)


# 環境
- Windows 10
- Unity 2018.2.19

# 1. ファイル名とクラス名が一致していない

これが一番起こりやすい事象です。
下記イメージでは、命名を誤ってしまい「Shooter.cs.cs」というファイル名で、クラス名は「Shooter」としています。

![scripts.png](https://qiita-image-store.s3.amazonaws.com/0/233011/67fb4a16-b1c9-e2a6-d1c7-27a7dfc5bd01.png)

この場合、ファイル名「Shooter.cs」に変更することで、アタッチすることが出来るようになります。

# 2. コードの中に全角スペースがある

スクリプトファイルのコード内に全角スペースがあると、発生することがあります。
全角スペースがないか確認し、存在する場合は半角スペースに置換しましょう。

# 3. Reimport Allする

ファイル名とクラスが一致している、コード内に全角スペースがないにもかかわらず、
正常にアタッチできない場合は、Reimport Allを試してみましょう。
Projectから右クリックして、下から5番目くらいにあります。

![reimport.png](https://qiita-image-store.s3.amazonaws.com/0/233011/7822fbad-9ae7-124d-56fe-d66cd4b073ed.png)

言葉の通り、プロジェクトを1からインポートしてくれます。

# 4. Unityのバージョンを変更する

[Unity Issue Tracker - [2018.1] &#39;Can&#39;t add script behaviour VisualContainerAsset&#39; error when adding script to GO with mismatched file and class name](https://issuetracker.unity3d.com/issues/2018-dot-1-cant-add-script-behaviour-visualcontainerasset-error-when-adding-script-to-go-with-mismatched-file-and-class-name)
のように、もしかしたらUnityのバグかもしれません。

最新バージョンを使用していない場合は、アップデートをしてみましょう。

# 終わりに（雑記）

学生時代に触って以来、Unityを触りました。
当時はUnity 4系を使っていました。
uGUIが追加されて、「なにこれすごい」って1人テンション上がっていたことを思い出します。

3年くらいたって、ちょっと知らない設定とか増えていましたが、UIは当時のままで安心しました。
当時は、UnityとVisual Studioでたまに固まってしまっていましたが、今はかなりサクサクでした。
（自分のPCスペックが上がった影響なだけかもしれませんが…）

あと、昔Unity 4系で作ったProjectをImportしたら、エラー吐きまくって悲しくなりました。
