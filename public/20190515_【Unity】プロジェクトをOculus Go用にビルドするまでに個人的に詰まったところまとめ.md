---
title: 【Unity】プロジェクトをOculus Go用にビルドするまでに個人的に詰まったところまとめ
tags:
  - Unity
  - 初心者
  - Oculus
private: false
updated_at: '2019-05-15T09:26:24+09:00'
id: e26b2fa93cfc56ca5da4
organization_url_name: null
slide: false
ignorePublish: false
---
# 背景

「Unity Oculus Go」でググって、3ページほど参考にしながら進めていました。
たぶん自分が悪いのですが、いろいろなところに詰まってしまいました。
なので、トラブルシューティングとしてまとめました。

いろいろ試行錯誤していたので、情報不足感とスクショ不足感が否めませんが、ご了承ください…

# 開発環境

- Windows 10
- Unity 2018.3.1f1
- Android Studio Version 3.2.1

# Oculus Goを開発者モードにする

1. Oculusアプリを起動する
2. 「設定」→「その他の設定」→「開発者モード」をONにする

## 団体登録していない場合
<font color="Red">**1回目のつまづきポイント**</font>
![Screenshot_20190509-233813.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/3b6c07c3-04ba-c4ad-06a1-c533ae07ea37.png)
団体登録をしていないと、上記のような「開発者になろう」というポップアップが表示されます。
作成開始ボタンを押下すると、[Device Setup - Oculus Go](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-device-setup-go/)に遷移します。
（スマホよりPCで先に登録することをオススメします。）

自分は団体登録していなかったので、[Oculus開発者ダッシュボード](https://dashboard.oculus.com/organizations/create/)で新しい団体を作成しました。
なんでもよかったので、「riekure」で登録しました。
![new organiton.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/5b463787-c39f-c47e-853c-e80ab3e1559b.png)

# Android SDK(API Level 25)をインストール

※ Android Studioをインストール済という前提。
<font color="Red">**2回目のつまづきポイント。API 25を入れるべし。**</font>
Oculus GoはAndroidのAPI Level 25で動くので、該当するSDKをインストールします。

1. Android Studioを起動する
![android studio.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/3f374ad6-0b40-1840-bb8c-3757655a4c32.png)
2. 右下にある「Configure」→「SDK Manager」を押下
3. Android 7.1.1（Nougat）をチェックしてApply
4. 時間がかかるので待つ

# Oculus Go ADB Driverをインストール（Windows限定）

<font color="Red">**3回目のつまづきポイント。存在を忘れがち。**</font>

1. https://developer.oculus.com/downloads/package/oculus-go-adb-drivers/ からダウンロード
2. ZIPファイルがダウンロードされるので、解凍する。
3. 解凍したファイル/usb_driver/android_winusb.infというファイルがあるので、右クリック→インストール

# UnityプロジェクトをAndroid用にビルド

1. 「File」→「Build Settings」を押下
2. 「Android」を選択して、「Player Setting」を押下
3. 「other Settings」→「Minimum API Level」をAndroid 7.1 'Nought'（API level 25）を選択 ※もっと下げたほうがいいのかも…？
4. 「XR Settings」→「Virtual Reality Supported」をチェック
5. 「Virtual Reality SDK」で＋ボタンを押下、Oculusを選択
6. 「File」→「Build Settings」→「Build and run」を実行する

<font color="Red">**4回目のつまづきポイント。API Levelを間違いがち。**</font>

初回のAPI Levelを26にして実行したら、下記のような「No compatible Android device found.」というWarningが出力されてしまいました。
![No compatible Android device found.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/6ed1263a-51f6-5e2d-cec1-93764671c50b.png)
Oculus GoはAndroid 7.1.1らしいので、注意しましょう。

# 参考文献
[Unity＋Oculus Go開発メモ - フレームシンセシス](https://framesynthesis.jp/tech/unity/oculusgo/)
[【VR開発入門】Unityで作ったゲームをOculus Goにビルドする方法 \| FREE SWORDER](https://freesworder.net/unity-oculus-go-build/)
[Device Setup - Oculus Go](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-device-setup-go/)
