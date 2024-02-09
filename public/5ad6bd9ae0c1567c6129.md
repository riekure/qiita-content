---
title: 【Unity】Androidアプリでバックグラウンドに移行する方法
tags:
  - Android
  - Unity
private: false
updated_at: '2021-01-04T09:59:56+09:00'
id: 5ad6bd9ae0c1567c6129
organization_url_name: null
slide: false
ignorePublish: false
---
# 初めに

Unity で実装した Android アプリの話です。
Unity 側でアプリをバックグラウンドに移動させたかっただけなのですが、調べるのに時間がかかったので記事にすることにしました。

# 動作確認環境

- Unity 2019.4.13f1

# コード

```c#
AndroidJavaObject activity = new AndroidJavaClass("com.unity3d.player.UnityPlayer").GetStatic<AndroidJavaObject>("currentActivity");
activity.Call<bool>("moveTaskToBack", true);
activity.Dispose();
```

# 簡単な解説

初めに、Android ネイティブの機能を使うので、`Activity` を取得します。
`Activity` を取得するには、 `AndroidJavaClass` を使用してUnityPlayerクラスを取得し、そのクラスを使って `currentActivity` を`AndroidJavaObject` として取得します。

あとは、`Activity#moveTaskToBack(true)` メソッドを呼ぶだけです。

最後は、状況によりますが `AndroidJavaObject` を `Dispose()` します。
`AndroidJavaObject` は `IDisposable` インターフェイスが実装されているので、アンマネージドリソースになります。
使い終わったら解放しましょう。
`using` で囲んでもよいかもしれません。

```c#
using(AndroidJavaObject activity = new AndroidJavaClass("com.unity3d.player.UnityPlayer").GetStatic<AndroidJavaObject>("currentActivity"))
{
    activity.Call<bool>("moveTaskToBack", true);
}
```

# 参考文献
[アプリケーションを終了させる - NO_NAME](http://t-tech.hatenablog.com/entry/2012/02/03/111722)
[【Unity】Androidのネイティブの機能を使う](https://marunouchi-tech.i-studio.co.jp/2405/)
[【Unity,C#】外部リソースを使用する時の注意【メモ】 - Blue_Breath_Blog](https://hi-network.sakura.ne.jp/wp/2020/03/25/post-1098/)
