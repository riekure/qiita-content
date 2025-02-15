---
title: '[Windows 10] 矢印キーに指を伸ばすエンジニアはザコ！とバカにされた（Change KeyとAutoHotkeyの導入）'
tags:
  - Windows
  - AutoHotkey
  - Keyboard
  - Windows10
private: false
updated_at: '2019-12-11T10:05:31+09:00'
id: 49b941fa5159f9948313
organization_url_name: null
slide: false
ignorePublish: false
---
# 本記事でやること

- Aの左隣のCapsLockキーをCtrlに変更する
- 右AltキーをF13キーに変更する
- F13キー + HJKLキーの組み合わせで矢印キーを実現する

# 検証環境

- Windows 10
- [ThinkPad USキーボード（外付け）](https://www.lenovo.com/jp/ja/landingpage/accessories/thinkaccessories/thinkpad/02/02/)

# 使用ツール

- Chagne Key
- Ctrl2Cap
- AutoHotKey

# 背景① ～なぜバカにされたのか～

皆さんは矢印キーを使っていますか？？
（方向キー、カーソルキー、カーソル移動キーとも言われてるみたいですが、自分は矢印キーと言ってしまうので、この記事では矢印キーでいきます。）
[方向キー - Wikipedia](https://ja.wikipedia.org/wiki/%E6%96%B9%E5%90%91%E3%82%AD%E3%83%BC)

超有名Web企業にお勤めの友人と久しぶりに会話して、なぜかキーボードの話になりました。

友人の会社では、矢印キーに指を伸ばすものならば、「**矢印キーに指を伸ばす奴は雑魚！**（意訳）」と言われるそうです。
矢印キーに指を伸ばすとホームポジションが崩れるかららしいです。なるほど…

超有名Web企業にお勤めの友人は、仕事ではMac(US配列)を使っているそうです。
自分は、しがないSIer勤務なので、仕事はWindows(JIS配列)+外付US配列キーボードを使っています。
（プライベートではWindowsとMac両方使っています。）

超有名Web企業は、当然のようにJIS配列かUS配列が選べるらしいです。
なので、社員の半数以上がUS配列なんだとか。
すごーい！（小並感）

一方、自分の会社では、支給PCにUS配列の選択肢なんてありません。
自分が会社にUS配列キーボードを持ち込んだときは、周りから変人扱いされました。すごい違いです。
~~同じIT企業とは思えないです。悲しい。~~

とりあえず友人には、「俺もMac使うときは矢印キー使わないし…（震え声）」と言っておきました。

# 背景② ～なぜ自分は矢印キーを使うのか～

何を隠そう、自分が会社で使っているキーボードは、矢印キーを使いすぎて印字がなくなっています。
矢印キーを使いまくってしまう最大の理由は、**OfficeおよびExcelです。**

昨今のテキストエディタまたはIDEは、ショートカットを自由に変更できます。
Vim風、Emac風など、自分好みのショートカットを設定できます。
しかも、拡張機能を追加するだけや設定ファイルを書き換えるだけで！！
その影響もあってか、コーディング作業中は矢印キーを使うことは少ないかと思います。

しかしOfficeはそうはいきません。
Excelにショートカットキーを導入するのは厳しいです。
（手法はあるみたいです。ただ設定ファイルを一括で読み込んでOK！とはならない様子）
自分はEmacs派なのですが、Excelでセルを1つ上に移動したいとき、うっかりCtrl + pを押して印刷しようとします。
~~イラッとします。~~

コーディングのお仕事もありますが、 **†Excel方眼紙の使い手†** なので、結果的に矢印キーを多用してしまいます。

# 背景③ ～OSの問題～

MacはCommandキーとControlキーがあるおかげか、UnixライクのOSだからかわかりませんが、
OSレベルでのキーボードショートカットがWindowsに比べて豊富です。

カーソル移動に関しては、Controlキーとの組み合わせで実現できます。

| 組み合わせるキー | 機能           |
|------------|--------------|
| P          | カーソルを上に移動   |
| N          | カーソルを下に移動   |
| B          | カーソルを左に移動   |
| F          | カーソルを右に移動   |
| A          | カーソルを行頭へ移動 |
| E          | カーソルを行末へ移動 |


一方、Windowsにカーソル移動を担当するショートカットはありません。
コーディングはともかく、ブラウザの検索窓に入力するときやメモアプリなんかを使うときは、地味に気になるところです。

# CapslockをCtrlに変更する

手法は2つあります。
他のキーも変更する予定があるならばChange Key、CapslockをCtrlにする変更する以外は何もいじる気がないならばCtrl2Capでも問題ないかと思います。

# Change Keyを使う

## ダウンロード

[「Change Key」非常駐型でフリーのキー配置変更ソフト - 窓の杜](https://forest.watch.impress.co.jp/library/software/changekey/) でダウンロード
解凍すると、**ChgKey.exe**が入っているかと思います。

## capslockをCtrlに変更

Change Keyはインストールという機能はありません。
**ChgKey.exe**を管理者権限で実行します。
管理者権限で実行しない場合は、下記の「レジストリ　管理者権限でオープンできませんでした。カレントユーザー権限でレジストリ情報を設定します。」というワーニングが表示されます。

![image.png](https://qiita-image-store.s3.amazonaws.com/0/233011/61fdf110-f00b-e961-afe0-7c4f2ecaa36a.png)

実行すると、下のように仮想キーボードが出てきます。

![image.png](https://qiita-image-store.s3.amazonaws.com/0/233011/adf522c7-cbd2-e803-f753-77178f12c93d.png)

変えたいキーをクリックします。今回はCaplockをクリックします。
すると、「キーをどのキーに変更しますか？」というポップアップが出てきます。

![image.png](https://qiita-image-store.s3.amazonaws.com/0/233011/fc4c8357-b430-5ac1-be42-10b826b05e76.png)

ここで、Ctrl左をクリックします。
そうすると、下記のように出ますので、タブにある登録(R)→現在の設定内容で登録します(R)を押下してください。
**×で閉じても反映されない**ので注意してください。

![image.png](https://qiita-image-store.s3.amazonaws.com/0/233011/d2712876-528a-a709-66da-896962cbc0a9.png)

あとは再起動すれば、CapslockはCtrlに変更されたはずです。

# Ctrl2Capを使う

## ダウンロード

[Ctrl2cap](https://technet.microsoft.com/ja-jp/sysinternals/bb897578.aspx?f=255&MSPPError=-2147217396) でダウンロード
お好きな場所に展開しましょう。

## インストール

管理者権限でコマンドプロンプトを開きます。
コマンドプロンプトで、先ほど解凍したCtrl2Cap配下にcdコマンドで移動してください。

そして、下記のコマンドを実行してください。

```
ctrl2cap /install
```

「Ctrl2cap successfully installed. You must reboot for it to take effect」と表示されれば成功です。再起動してください。
ちなみにアンインストールしたい場合は、

```
ctrl2cap /uninstall
```

# 右AltキーをF13キーに変更する

自分は右Altキーをあまり使用しないので、F13キーに変更して、新しいショートカットキーに組み合わせるためのキーに変更します。
Capslockキーを変更したときと手順は同じですが、F13キーが選択肢にありません。

![image.png](https://qiita-image-store.s3.amazonaws.com/0/233011/d3a6b928-acd5-dcea-7efc-080453e2b3fa.png)

そんなときは、テンキーの上、「キーを無効にする」の隣のScan Modeを押下してください。
すると、下のように表示されるはずです。

![image.png](https://qiita-image-store.s3.amazonaws.com/0/233011/d5244da6-1667-4ced-898c-2f349f56179d.png)

[ChangeKeyを使用してWindowsキーをF13キーに変更する方法 - 情報科学屋さんを目指す人のメモ（FC2ブログ版）](http://did2.blog64.fc2.com/blog-entry-349.html) によると、0x0064 = F13キーなので、0064と入力してOKを押してください。
タブにある登録(R)→現在の設定内容で登録します(R)を押下してください。
再起動をすると、右AltはF13キーになります。

# F13キー + HJKLキーの組み合わせで矢印キーを実現

## AutoHotKeyをダウンロード／インストール

https://www.autohotkey.com/ からダウンロードしてください。
ダウンロードしたexeファイルを実行して、インストールを行ってください。
[AutoHotKeyのインストールの仕方 - のたり雑記ブログ](https://umada.net/autohotkey_install) がすごく参考になります。

## ahkファイルを作成

インストール先フォルダを開きます。
そこで新規ファイルとして、ahkファイルを作成してください。
例では、「MySettingKey.ahk」とします。

![image.png](https://qiita-image-store.s3.amazonaws.com/0/233011/1aad79ed-fb43-6faf-80e0-b280bcab8d0a.png)

中身は下の内容を書いてみてください。

```
F13 & H::Send,{Blind}{Left}
F13 & J::Send,{Blind}{Down}
F13 & K::Send,{Blind}{Up}
F13 & L::Send,{Blind}{Right}
```

意味は下になります。

| ショートカットキー | 機能           |
|------------|--------------|
| F13 + H          | カーソルを左に移動   |
| F13 + J          | カーソルを下に移動   |
| F13 + K          | カーソルを上に移動   |
| F13 + L          | カーソルを右に移動   |

これによって、矢印キーに手を伸ばさずともホームポジションでカーソル移動できます。
Excelでセル一つ右に移動するときもF13 + Lで可能です。

## ahkファイルを実行する

作成した「MySettingKey.ahk」をダブルクリックするか、右クリック→Run Scriptを押下してください。

![image.png](https://qiita-image-store.s3.amazonaws.com/0/233011/4b093740-234a-3564-1072-eaafdd51debf.png)

コンパイルエラーにならなければ、通知領域に緑のHマークが表示されます。

![image.png](https://qiita-image-store.s3.amazonaws.com/0/233011/1727bdd3-520e-6b1d-dd3e-0aad7bb17962.png)

## 起動時に自動実行する

このままでは、PCを再起動したときにahkファイルが実行されません。
そのため、せっかく自分が定義したショートカットを使用するために、エクスプローラーを開いて、ahkファイルをダブルクリックするという手間ができてしまいます。

PCを起動したときに、自動でahkファイルを実行するようにしましょう。
windowsキー + Rキーを押し、「**shell:startup**」と入力してください。

![image.png](https://qiita-image-store.s3.amazonaws.com/0/233011/7c1cfc6d-21a3-2d5e-4577-c73408d2a35a.png)

そうすると、「C:\Users\{User}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup」のパスでエクスプローラーが起動します。
このパスに置いたファイルはPC起動時に自動的に実行されるようになります。

そこに、自分で作成したahkファイルのショートカットを配置してください。

![image.png](https://qiita-image-store.s3.amazonaws.com/0/233011/437727c3-241f-d0dc-471a-42f17ea2f9f0.png)

上のように配置すれば、PCを起動したときに自動的にahkファイルが自動的に実行されるようになります。

# 終わりに

これで最低限、矢印キーに指を伸ばさないエンジニアになれました。
まぁ、指が慣れてなさすぎて結局矢印キーを使ってしまうんですがね…
他にもfunctionや、Backspaceやdeleteもショートカットで実現できるようにすればかなり作業スピードが上がるかもしれません。
ここで設定した例は、あくまで一例なので、いろいろ試して自分にあったコマンドを見つけてみてください。

# 参考文献

[キーリスト - AutoHotkey Wiki](http://ahkwiki.net/KeyList)
[「AutoHotKey」による作業効率化～その1～基本：That's Done!](https://ch.nicovideo.jp/Jinsichi/blomaga/ar455334)
[AutoHotkeyの使い方1](https://rcmdnk.com/blog/2013/07/28/computer-windows-autohotkey/)
