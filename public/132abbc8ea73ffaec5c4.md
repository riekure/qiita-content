---
title: >-
  【Unity】UnityEditor.BuildPlayerWindow+BuildMethodExceptionが発生してAndroidビルドできないときの対処方法
tags:
  - Unity
  - 初心者
private: false
updated_at: '2019-06-28T11:43:58+09:00'
id: 132abbc8ea73ffaec5c4
organization_url_name: null
slide: false
ignorePublish: false
---
# 背景

スマホ向けVRアプリを作成中です。
そのとき、Android用にビルドしようとしてもうまくいかず、かなり解決に時間がかかってしまいました。
対処方法として、いくつか試したので、紹介しようと思います。

発生したエラーは以下のとおりです。

```
UnityException: No Android devices connected
Make sure your device is plugged in.
If you are sure that the device is attached then it might be USB driver issue, for details please check 'Android environment setup' section in Unity manual.
UnityEditor.BuildPlayerWindow:BuildPlayerAndRun()
```

```
Build completed with a result of 'Failed'
UnityEditor.BuildPlayerWindow:BuildPlayerAndRun()
```

```
UnityEditor.BuildPlayerWindow+BuildMethodException: 2 errors

  at UnityEditor.BuildPlayerWindow+DefaultBuildMethods.BuildPlayer (UnityEditor.BuildPlayerOptions options) [0x00242] in C:\buildslave\unity\build\Editor\Mono\BuildPlayerWindowBuildMethods.cs:194 

  at UnityEditor.BuildPlayerWindow.CallBuildMethods (System.Boolean askForBuildLocation, UnityEditor.BuildOptions defaultBuildOptions) [0x0007f] in C:\buildslave\unity\build\Editor\Mono\BuildPlayerWindowBuildMethods.cs:97 
UnityEditor.BuildPlayerWindow:BuildPlayerAndRun()
```

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/1211fa5a-8ff4-e41a-6536-acf509dd045b.png)


# 環境

- Windows 10
- Unity 2019.1.5f1
- Android Studio Version 3.2.1

# 1. Unityを管理者として実行＆ビルド（効果なし）

Unityを「右クリック」→「管理者として実行」をクリックして、該当するプロジェクトを開きます。
そして、Build And Runします。
エラー内容変わらず。

# 2. Unityをバージョンアップする（効果なし）

Unityを最新バージョンにアップデートします。
エラー内容変わらず。

# 3. Unityをダウングレードする（効果なし）

Unity 2018.3.1f1にダウングレードしてビルドしてみました。
エラー内容変わらず。

# 4. Windows 10の更新プログラム（効果なし）

設定→更新とセキュリティ→Windows Update で更新プログラムを確認。
とくに更新するものもなく、状況は変わらず。

# 5. C:\Users\[name]\Documentsフォルダにビルドする（効果なし）

いままで C:\Users\[name]\Desktop にapkを作成しようとしていたので、Documentsフォルダ配下に変更しました。
エラー内容変わらず。

# 6. Minimum API Levelを下げる（効果なし）

Android 7.1（API Level 25）から、Android 5.0（API Level 20）に下げてみました。
エラー内容変わらず。

# 7. プロジェクトのフォルダ内の.slnファイルを削除する（効果なし）

.slnファイルをゴミ箱へ。
エラー内容変わらず。
（必ずバックアップをとっておき、作業が終わったら戻してください。）

# 8. AndroidをUSBデバッグをONにする

使用していたAndroidがデバッグモードになっていませんでした。
下記が非常に参考になります。
[[Android]  アプリを実機でデバッグするためのUSB ドライバーを設定する](https://akira-watson.com/android/nexus7-usb-driver.html)

USBデバッグをONにしたら、無事ビルドすることができました。

# あとがき

AndroidのUSBデバッグをOFFにしたことを完全に忘れていました。
てっきりUnityをアップデートしたことが原因かと思い、ずっと的外れな対処を試していました。
Unityに関するエラー調査力がまだまだだと痛感しました。

# 参考文献

[Unityがビルドできない｜teratail](https://teratail.com/questions/139998)
[Unable to build my projects in 2018.2.0b7 after receiving fatal build error](https://forum.unity.com/threads/unable-to-build-my-projects-in-2018-2-0b7-after-receiving-fatal-build-error.535810/)
