---
title: 【Unity】Android アプリでスクショや画面録画などを禁止する
tags:
  - Android
  - Unity
private: false
updated_at: '2021-01-13T10:27:39+09:00'
id: 22378919e597b492f748
organization_url_name: null
slide: false
ignorePublish: false
---
# 背景

アプリによっては、セキュリティやコンテンツ的にスクショや画面録画を禁止したいときがあると思います。
そのとき Android の機能である `WindowManager.LayoutParams.FLAG_SECURE` を Activity の `OnCreate()` で呼ぶ必要があります。

しかし、Unity だとどうするのか分からなかったので調べてまとめた記事になります。

# FLAG_SECURE を設定するとどうなるか

- スクショを無効化
- 画面録画（スクリーンレコーディング）をすると、録画した画面が真っ黒になる
- タスク画面・タスク一覧で、アプリ画面を真っ白にできる

# 動作確認環境

- Unity 2018.4.22f1

※ Unity2018.2以前のバージョンを使っている場合は、以下の手順とは異なるかと思いますので、ご注意ください。

# 手順

Unity + Android で実現するためには、

1. `UnityPlayerActivity` を拡張して新しい Activity を定義する
2. 新しい Activity が使用されるように `AndroidManifest.xml` を修正する
3. 新しい Activity の `OnCreate()` に `FLAG_SECURE` を設定する

という手順が必要です。

## 1. `UnityPlayerActivity` を拡張する

自分が作業中の Unityプロジェクトの `Assets/Plugins/Android` 配下に新しい Activity を作成します。
例として、 `OverrideExample` クラスを作成します。

ちなみに、 package name 以外のファイル内容は、Unity公式からそのままコピペしています。
[UnityPlayerActivity Java コードの拡張 - Unity マニュアル](https://docs.unity3d.com/ja/2018.4/Manual/AndroidUnityPlayerActivity.html)
package name は、自分が設定した名前に置き換えてください。

```OverrideExample.java
package com.DefaultCompany.ExtendUnityPlayerActivity;
import com.unity3d.player.UnityPlayerActivity;
import android.os.Bundle;
import android.util.Log;

public class OverrideExample extends UnityPlayerActivity {

  protected void onCreate(Bundle savedInstanceState) {

    // UnityPlayerActivity.onCreate() を呼び出す
    super.onCreate(savedInstanceState);

    // logcat にデバッグメッセージをプリントする
    Log.d("OverrideActivity", "onCreate called!");
  }

  public void onBackPressed()
  {
    // UnityPlayerActivity.onBackPressed() を呼び出す代わりに、Back ボタンイベントを無視する
    // super.onBackPressed();
  }
}
```

## 2. `AndroidManifest.xml` を修正する

Activity と同様に `Assets/Plugins/Android` に `AndroidManifest.xml` を配置します。
`android:name` の部分は、`1.` で作成したクラス名に合わせてください。

```AndroidManifest.xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="com.company.product">
  <application android:icon="@drawable/app_icon" android:label="@string/app_name">
    <activity android:name=".OverrideExample"
             android:label="@string/app_name"
             android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen">
        <intent-filter>
            <action android:name="android.intent.action.MAIN" />
            <category android:name="android.intent.category.LAUNCHER" />
        </intent-filter>
    </activity>
  </application>
</manifest>
```

この状態で、Androidビルドして問題なくアプリが使用できるか確認してください。
特に、 package name を間違えるとアプリがクラッシュしたりするので、注意してください。

## 3. FLAG_SECURE を設定する

`onCreate()` で `FLAG_SECURE` を設定します。

```OverrideExample.java
package com.DefaultCompany.ExtendUnityPlayerActivity;
import com.unity3d.player.UnityPlayerActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.WindowManager;

public class OverrideExample extends UnityPlayerActivity {

  protected void onCreate(Bundle savedInstanceState) {

    // UnityPlayerActivity.onCreate() を呼び出す
    super.onCreate(savedInstanceState);

    // logcat にデバッグメッセージをプリントする
    Log.d("OverrideActivity", "onCreate called!");

    //FLAG_SECUREの設定
    getWindow().setFlags(WindowManager.LayoutParams.FLAG_SECURE, WindowManager.LayoutParams.FLAG_SECURE);
  }

  public void onBackPressed()
  {
    // UnityPlayerActivity.onBackPressed() を呼び出す代わりに、Back ボタンイベントを無視する
    // super.onBackPressed();
  }
}
```

これで作業は完了です。
Androidビルドして、問題なければスクショや画面録画ができなくなっていると思います。

# 参考文献

[UnityPlayerActivity Java コードの拡張 - Unity マニュアル](https://docs.unity3d.com/ja/2018.4/Manual/AndroidUnityPlayerActivity.html)
[Androidアプリでキャプチャーをされたくないときにする方法](http://buchi.hatenablog.com/entry/2015/10/09/184456)
