---
title: 【Unity】Standard AssetsがImport Packageに表示されていないときの対処方法
tags:
  - Unity
  - 初心者
private: false
updated_at: '2019-02-21T14:50:20+09:00'
id: 96ad0dda78852da1bc9e
organization_url_name: null
slide: false
ignorePublish: false
---
# 背景

[Unity5 3D/2Dゲーム開発 実践入門 作りながら覚えるスマートフォンゲーム制作（吉谷 幹人） \| 書籍 本 | ソシム](http://www.socym.co.jp/book/967)の本で勉強しているときに、「Assets」→「Import Package」から、Standard Assetsを選択してください。的な操作がありました。
しかし、自分のUnityは、Custom Packageしか表示されていません。

![import_package.png](https://qiita-image-store.s3.amazonaws.com/0/233011/397bf2e8-c214-49b1-dd89-24f88889728d.png)


# 動作確認環境

- Windows 10
- Unity 2018.3.1f1

# 解決方法

「Window」→「Asset Store」を開いて、Standart Assetsと入力して検索してください。
次に、画像の一番上にあるUnity Technologiesと書いてあるタブをクリックしてください。

![standard_assets2.png](https://qiita-image-store.s3.amazonaws.com/0/233011/d997dc12-9488-44b7-fb24-e47b56d1246c.png)

ピンクのImportボタンを押下してください。
Importしたいものにチェックを入れて、Importボタンを押下すればStandard Assetsを使用することができます。

![standard_assets.png](https://qiita-image-store.s3.amazonaws.com/0/233011/bf851b24-629c-3e58-3687-24fca37d344a.png)


# 終わりに

~~おそらくUnityが日々バージョンアップしていくなかで、Standard AssetsはAssets Storeからインストールするものになったのだと思います。~~
下の追記をご覧ください！

ググり能力が低いせいか、なかなか解決できませんでした。
忘れては困ると思ったので、自分の備忘録がてら記事にしました。

# 2019/2/21に追記

コメントにて教えていただきました。

2018年7月10日の公式ブログより、Standard Assets の差し替えが発表されていました。
[Unity 2018.2 リリース – Unity Blog](https://blogs.unity3d.com/jp/2018/07/10/2018-2-is-now-available/)より引用

> Unity 2018.2 では 5.0 バージョンの Standard Assets がインストーラーから削除されました。旧プロトタイピング用パッケージ各部の差し替えパッケージの作成が進行中です。最初のパッケージ（Standard Assets: Characters）はプレビュー版として Unity 2018.2 のリリース後、近日中に入手可能となります。これには First-Person および Third-Person Controller が Cinemachine と統合されて含まれているほか、Probuilder でビルドされたプロトタイピング環境も含まれます。詳細は近日公開予定のブログ記事をご覧ください。 旧 5.0 パッケージはアセットストアで引き続き入手可能です

2019年2月21日現在は、差し替え中なのでアセットストアから入手して使用するしかないようです。
おそらく、新しいStandart Assetsの開発が完了すれば、今まで通りUnityのインストーラーに含まれるのではないかと思います。

[GitHub - Unity-Technologies/Standard-Assets-Characters: Unity Standard Asset Controllers](https://github.com/Unity-Technologies/Standard-Assets-Characters)で、Character Package(BETA)を開発中のようです。
