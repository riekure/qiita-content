---
title: '【Unity】Scene／GameObject／Component とは何か '
tags:
  - Unity
  - 初心者
private: false
updated_at: '2021-02-09T22:38:24+09:00'
id: 376fc0f7af45eaa247fb
organization_url_name: null
slide: false
ignorePublish: false
---
# 初めに

人に説明する場合、どうすればいいのか考えたときに、うまく言葉が出てこなかったので、自分なりに整理したものです。
公式ドキュメント見れば分かる！という方は、こちら

- https://docs.unity3d.com/ja/2019.4/Manual/CreatingScenes.html
- https://docs.unity3d.com/ja/2019.4/Manual/GameObjects.html
- https://docs.unity3d.com/ja/2018.4/Manual/UsingComponents.html

# 一言で言うと…

Scene：空間、世界
GameObject：物
Component：振る舞い

# Scene

空間や世界です。
Scene は、物を配置して構成します。（物 = GameObject）
言い換えると、 Scene には複数の GameObject が配置されることで構成されているということです。

卓球で例えると、試合会場です。

# GameObject
「Scene中にある物」です。
GameObject 自身に何かする機能はありません。
キャラクターや環境、特殊な効果として働かせるためには、 Component を追加（アタッチ）する必要があります。

卓球で例えると、卓球台やラケット、ボール、照明に電子掲示板、フェンスなど全て GameObject といえます。

# Component
GameObject の振る舞い。
「画面中に物体として移す」ということは Component によって定義されます。
基本的な振る舞いは Unity が提供されています。　例）物体の形、色、重さ、音が出るなど
C# スクリプトを追加することで、独自の振る舞いを提供することもできます。

GameObject に light Component をアタッチすれば、光を放つ GameObject になります。
Mesh Filter と Mesh Renderer, Box Collider をアタッチすれば、箱型の GameObject になります。

卓球のラケットで例えると、ラケットの形、色、ボールが当たったときの反発などは Component が担当しています。

#終わりに

まとめようと思ったら、めちゃくちゃ短くなりました。
もっとより良い文章が書けたら、追記します。


