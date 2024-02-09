---
title: 【Unity】Unity Hub から Unity インストールするときに「不完全または破損したダウンロードファイル」と出たときの対処方法
tags:
  - Unity
private: false
updated_at: '2020-05-11T09:53:32+09:00'
id: 4719b4fc7d3509fdc29c
organization_url_name: null
slide: false
ignorePublish: false
---
# 現象

Unity 2019.2.9f1 のインストールしている途中に、「不完全または破損したダウンロードファイル」と表示され、インストールに失敗しました。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/528219b8-9d9f-371d-9a7a-4601f7c9ca82.png)

そのときに行った対処方法まとめです。
結論から言うと、 **Unity Hub を経由せずに、公式サイトからインストーラーをダウンロードして、直接 Unity をインストールするのが一番はやいです。**

# 環境

- Windows10
- Unity Hub 2.3.1
- インストールできなかった Unity Version は 2019.2.9f1



# やったこと

- proxy を使用していないか確認
- システム要件を確認
- インストールしていた Unity を全てアンインストール
- Unity Hub を再インストール
- インストール中に Unity Hub をアクティブウィンドウから動かさない

## proxy を使用していないか確認

proxy を使用している場合は、設定を OFF にしてください。
確認方法は[こちら。](https://pasokatu.hateblo.jp/entry/2017/07/04/111147)」

proxy の設定なんてしていないので、問題なし。

## システム要件を確認

[Unity のシステム要件](https://docs.unity3d.com/Manual/system-requirements.html) を確認しました。
もちろん要件を満たしていたので、問題なし。

## インストールしていた Unity を全てアンインストール

インストールしたい Unity 2019.2.9f1 以外を全てアンインストールしました。
もちろんこんなことしても解決しませんでした。

## Unity Hub を再インストール

Unity Hub が壊れた説をかけて、再インストールしました。
もちろん改善しませんでした。

## インストール中に Unity Hub をアクティブウィンドウから動かさない

インストールが終わるまで、インストール画面を選択して状態で、他の作業を何もしない。
もちろん改善しませんでした。

# いろいろやった結果

諦めて Unity Hub を経由せずに Unity をインストールしてください。

# 終わりに

Unity Hub からインストールすれば、いろいろな Unity の Version を一元管理できます。
アンインストール、 Android, iOS などのモジュールを加えることもできます。
ただ、 Unity Hub を経由せずに、直接インストールした Version は、 Unity Hub からアンインストールもモジュールも追加することができません。

こうなると面倒なので、時間かけて頑張りました。
意味ありませんでしたが。

# 参考文献

[インストールがうまくいかない場合 – ユニティ・テクノロジーズ](https://helpdesk.unity3d.co.jp/hc/ja/articles/219377968-%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%8C%E3%81%86%E3%81%BE%E3%81%8F%E3%81%84%E3%81%8B%E3%81%AA%E3%81%84%E5%A0%B4%E5%90%88)
