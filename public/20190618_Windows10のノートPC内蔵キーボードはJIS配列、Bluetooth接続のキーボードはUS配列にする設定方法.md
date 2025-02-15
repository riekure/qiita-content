---
title: Windows10のノートPC内蔵キーボードはJIS配列、Bluetooth接続のキーボードはUS配列にする設定方法
tags:
  - Keyboard
  - Windows10
private: false
updated_at: '2019-06-18T12:03:41+09:00'
id: 7a80ae33ef0a73c3c250
organization_url_name: null
slide: false
ignorePublish: false
---
ノートPC内蔵キーボードと、Bluetooth接続しているキーボードの配列を独立して設定できず苦労しました。
売ってなかったから仕方ないけど、USキーボードのノートPC買えば良かった。

解決策を見つけたので、今後誰かの役に立つと信じて残しておきます。
（おそらく未来の自分の為にはなる。）

## 環境
OS: Windows 10
接続したキーボード：[thinkpad bluetooth ワイヤレス・トラックポイント・キーボード](https://www3.lenovo.com/jp/ja/accessories-and-monitors/keyboards-and-mice/keyboards/KEYBOARD-US-English/p/0B47189)


※ コメントで教えていただいた情報です。
本記事で記載している設定が、
<font color="Red">**Windows10 ver.1809 以降では効かなくなってしまったようです。**</font>
Windows10のバージョン情報を確認してから、本手順を実施するようにしてください。


## 手順1. ハードウェアIDの特定
1. デバイスマネージャーを開く
2. キーボードを開く
3. HIDキーボードデバイスを右クリック（もしかしたら名前が違うかも…）
4. プロパティを開く 

![プロパティ.PNG](https://qiita-image-store.s3.amazonaws.com/0/233011/bc8b4f34-d0b6-b728-f5fb-8e1723632181.png) 

Lenovoと書いてあるので、これだと特定。 
5. 詳細タブを開く
6. プロパティでハードウェアIDを選択
7. 出てきたハードウェアIDをメモる ※ コピペできます


![ハードウェアID.PNG](https://qiita-image-store.s3.amazonaws.com/0/233011/be17bec8-cd5e-e956-f4a3-7645d20f091e.png)



## 手順2. レジストリの変更
1. レジストリエディタを開く（Windows + Rキーを押したあとに、「regedit」と入力する。）
2. コンピュータ → HKEY_LOCALMACHINE → SYSTEM → CurrentControlSet → Enum → HIDとたどっていく
3. HIDの一覧から、Bluetooth接続するキーボードのハードウェアIDを見つける
4. Device Parametersを開いて、右クリック → 新規 → DWORDで設定を追加する
5. PCを再起動

- KeyboardTypeOverride：4
- KeyboardSubtypeOverride：0

![設定内容1.PNG](https://qiita-image-store.s3.amazonaws.com/0/233011/73770e15-0464-69d0-49c6-5eadeed24d97.png)
![設定内容2.PNG](https://qiita-image-store.s3.amazonaws.com/0/233011/a775ceee-7c48-5d68-6d5c-2d95cb4d42a7.png)



## 参考サイト
http://d.hatena.ne.jp/ruby-U/20101110/1289371908

