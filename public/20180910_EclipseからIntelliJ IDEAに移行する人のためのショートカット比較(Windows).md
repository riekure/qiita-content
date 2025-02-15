---
title: EclipseからIntelliJ IDEAに移行する人のためのショートカット比較(Windows)
tags:
  - Java
  - Eclipse
  - IntelliJ
  - IntelliJIdea
private: false
updated_at: '2018-09-10T11:12:18+09:00'
id: ade81d045cf75d9ae3e0
organization_url_name: null
slide: false
ignorePublish: false
---
# EclipseからIntelliJ IDEAに乗り換え中

最近、Eclipseから卒業したくて、IntelliJ IDEAに乗り換えようとしています。

理由は、Eclipseが重い、すぐ壊れる、なんか使いづらいとか色々とあります。
いちいち設定しなくても動作してくれることは気に入っていましたが、昔に比べるとEclipseを使うメリットをあまり感じなくなりました。
VSCodeで頑張っていた頃もあったのですが、補完機能が弱くて断念。

IntelliJ IDEAは、Jetbrains製にも関わらず、Communityだと無料で使用することができます。
評判に良いので、せっかくなので使ってみようと思いました。

そこで、Eclipseのショートカットでいうあれは、IntelliJ IDEAだとどうやるのか？をまとめました。
自分が知っている、よく使うショートカットしか書いていません。
新しいショートカットが分かったら、随時追記していこうと思います。

# 動作環境
Windows 10

# 入力補完機能(sysout, main)

| 機能 | Eclipse | IntelliJ IDEA |
| :-- | :------ | :------------ |
| System.out.prinln | sysout | sout |
| public static void main | main | psvm |

# 編集機能

| 機能 | Eclipse | IntelliJ IDEA |
| :-- | :------ | :------------ |
| 行の削除 | Ctrl + D | Ctrl + L |
| 行の入れ替え | [Alt] + ↑ or ↓ | [Alt] + [Shift] + ↑ or ↓ |
| カーソルがある行を削除 | [Ctrl] + d | [Ctrl] + y |
| カーソルがある行を複製 | [Ctrl] + [Alt] + ↑ or ↓ | [Ctrl] + d |
| コメント化 |  [Ctrl] + / |  [Ctrl] + / |
| 検索 |  [Ctrl] + f |  [Ctrl] + f |
| 置換 |  [Ctrl] + f |  [Ctrl] + r |
| コードフォーマット | [Ctrl] + [Shift] + f | [Ctrl] + [Shift] + l |
| 自動補完 | [Ctrl] + [Space] | [Ctrl] + j |
| ファイル検索 | [Ctrl] + h | [Ctrl] + [Shift] + f |
| ファイル名検索 | [Ctrl] + [Shift] + r | [Ctrl] + [Shift] + n |
| 呼び出し階層 | [Ctrl] + [Alt] + h | [Ctrl] + [Alt] + h |
| 定義部分に移動 | F3 | [Ctrl] + b |
| 移動前の箇所に戻る | [Alt] + ← or → | [Ctrl] + [Alt] + ← or → |
| エディタのタブを閉じる | [Ctrl] + w | [Ctrl] + F4 |
| インポート編成 | [Ctrl] + [Shift] + o | [Ctrl] + [Alt] + o |

# デバッグ
| 機能 | Eclipse | IntelliJ IDEA |
| :-- | :------ | :------------ |
| ステップイン | F5 | F7 |
| ステップオーバー | F6 | F8 |
| プログラム再開 | F8 | F9 |
| 関数の呼び出し結果を見る | [Ctrl] + [Shift] + i | [Ctrl] + [Alt] + F8 |
