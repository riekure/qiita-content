---
title: 【Unity】Windows 10で起動時に応答なしになるとき
tags:
  - Unity
  - Windows10
private: false
updated_at: '2019-01-14T11:34:17+09:00'
id: 247f7cd11c26b753b42b
organization_url_name: null
slide: false
ignorePublish: false
---
# Unity Editorを起動した瞬間応答なし

ある日、PCを起動してUnityを起動したところ、Unity Editorをロード中に固まってしまう事象が発生しました。
そのときにやった対処法をまとめてみます。

# 環境
- Windows 10
- Unity 2018.2.X

# やったこと
1. Unityのバージョンアップ（効果なし）
2. Windows 10の更新プログラム（効果なし）
3. PC自体をオフライン環境にしてUnityを起動（効果なし）
4. セキュリティソフトを停止させた状態で起動（効果なし）
5. Unity自体を一度アンインストールした後に再度インストールからの起動（効果なし）
6. 最近インストールしたソフトウェアを削除

# 1. Unityのバージョンアップ（効果なし）

最新バージョンを使用していないならば、公式サイトから最新版を取得しましょう。
[Unity Store](https://store.unity.com/ja)

# 2. Windows 10の更新プログラム（効果なし）

設定→更新とセキュリティ→Windows Update で更新プログラムのチェックを行いましょう。
もし、更新プログラムがあればインストールしましょう。
「最新の状態です」と表示されていればOKです。

![windows update.PNG](https://qiita-image-store.s3.amazonaws.com/0/233011/f75b5bbe-8b68-50e3-f702-b37364916c5b.png)

# 3. PC自体をオフライン環境にしてUnityを起動（効果なし）

Wi-FiをOFFにしてUnityを起動します。
LANケーブルを刺しているならば、抜いて起動しましょう。

# 4. セキュリティソフトを停止させた状態で起動（効果なし）

自分の場合は、セキュリティソフト = Windows Defenderでした。
下記のページが非常に分かりやすかったです。
[Windows 10 の Windows Defender を無効に、または削除する方法](https://support.kaspersky.co.jp/common/windows/13341#block0)

# 5. Unity自体を一度アンインストールした後に再度インストールからの起動（効果なし）

Unityをアンインストールして、Unity関連のキャッシュファイルを片っ端から削除しました。
そして、再度インストールしました。

# 6. 最近インストールしたソフトウェアを削除

アプリと機能で、最近インストールしたソフトウェアを上から削除していきました。
自分の場合は、「Duet Display」というiPadを外部ディスプレイとして使用できるソフトウェアでした。
これで起動するようになりました。

# 終わりに

この事象の解決で、貴重な休日が1日なくなりました。
治らなさすぎて、買ったPCが1ヶ月でぶっ壊れたのかと思いました。

# 参考文献
[WindowsでUnityEditorがうまく起動しない – ユニティ・テクノロジーズ・ジャパン合同会社](https://helpdesk.unity3d.co.jp/hc/ja/articles/219447788-Windows%E3%81%A7UnityEditor%E3%81%8C%E3%81%86%E3%81%BE%E3%81%8F%E8%B5%B7%E5%8B%95%E3%81%97%E3%81%AA%E3%81%84)
