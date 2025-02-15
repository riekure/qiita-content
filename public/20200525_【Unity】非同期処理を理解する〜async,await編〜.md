---
title: 【Unity】非同期処理を理解する〜async/await編〜
tags:
  - C#
  - Unity
  - 非同期処理
private: false
updated_at: '2020-05-25T10:19:37+09:00'
id: ce243baeb0c78743526b
organization_url_name: null
slide: false
ignorePublish: false
---
# async/await とは

- C# の機能として用意されている
    - C# 5.0の新機能
    - Unity 2018 から C# 6.0 に対応した（それまでは C# 4.0 でした。）
    - Task クラスに対して使うものという軽い認識（本当は `INotifyCompletion` インターフェースの `IsCompleted` と `GetResult` ）
- Unity で `.NET 4.x` を選択すれば使用可能
- async = asynchronous = 非同期
    - await を使うメソッドにつけなければならないキーワード
    - async をつけただけでは普通のメソッドと挙動は変わらない
- await
    - 非同期メソッドを呼び出し、完了するまで実行を中断するキーワード
- 戻り値を取得できる（コルーチンは無理）
- 並列処理だけど、普通のメソッドの呼び出しと同じようにかける = 可読性が上がる

基本的な構文は、

```
async 戻り値の型 メソッド名(引数)
{
    await ~~~~
}    
```

戻り値は、基本的に ```Task / Task<T>``` 型と考えて問題ないかと思います。
（といいながら、サンプルは ```void``` で書いたりしています…）

# 機能

## Task.Delay(Int32 millisecondsDelay)

引数で指定されたミリ秒待機します。

```c#
using System.Threading.Tasks;
using UnityEngine;


public class Test : MonoBehaviour
{
    void Start()
    {
        AsyncSample1();
    }

    async void AsyncSample1()
    {
        Debug.Log("AsyncSample1 Start.");
        await Task.Delay(1000);
        Debug.Log("AsyncSample1 End.");
    }
}
```

今回のサンプルでは、**1000ミリ秒 = 1秒** 待機するようにしたので、実行結果は以下のようになります。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/577e2c4c-829c-e133-b59f-e6e764e62f14.png)

## ContinueWith

直列処理できます。
非同期処理のメソッドも、`ContinueWith` でつなぐことで、直列化することができます。

ちなみに `ContinueWith` を**使わず**に、普通に並列的に処理にしたければ、下のようになイメージになります。

```c#
using System.Threading.Tasks;
using UnityEngine;


public class Test : MonoBehaviour
{
    void Start()
    {
        AsyncSample1();
        AsyncSample2();
    }

    async void AsyncSample1()
    {
        Debug.Log("AsyncSample1 Start.");
        await Task.Delay(1000);
        Debug.Log("AsyncSample1 End.");
    }

    async void AsyncSample2()
    {
        Debug.Log("AsyncSample2 Start.");
        await Task.Delay(1000);
        Debug.Log("AsyncSample2 End.");
    }
}
```

並列なので、
1. `AsyncSample1 Start.`
2. `AsyncSample2 Start.`
3. `AsyncSample1 End.`
4. `AsyncSample2 End.`
という結果になります。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/a184abe6-ae1a-d17e-578c-809b4d25d9d9.png)

`ContinueWith` を使って直列処理（**AsyncSample1** を実行完了後、 **AsyncSample2** を実行）するサンプルは、

```c#
using System.Threading.Tasks;
using UnityEngine;


public class Test : MonoBehaviour
{
    void Start()
    {
        AsyncSample1().ContinueWith(_ => AsyncSample2());
    }

    async Task AsyncSample1()
    {
        Debug.Log("AsyncSample1 Start.");
        await Task.Delay(1000);
        Debug.Log("AsyncSample1 End.");
    }

    async Task AsyncSample2()
    {
        Debug.Log("AsyncSample2 Start.");
        await Task.Delay(1000);
        Debug.Log("AsyncSample2 End.");
    }
}
```
注意点は、メソッドの返り値の型が Task になっていることくらいです。

1. `AsyncSample1 Start.`
2. `AsyncSample1 End.`
3. `AsyncSample2 Start.`
4. `AsyncSample2 End.`
という結果になります。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/90a50316-0dcb-7ab3-0e25-4563a03433d8.png)

## Task.Run()

引数として与えられた処理を別スレッドで実行します。
用途として、重い処理を非同期にしたいときに使います。

ちょっと良い例が思いつかないので、超簡単なサンプルだけ書きます。

```c#
Task.Run(()  =>  Debug.Log("重い処理..."));
```

## Task.WhenAll()

指定された Task が全て完了してから Task を実行することができます。

```c#
using System.Threading.Tasks;
using UnityEngine;


public class Test : MonoBehaviour
{
    async void Start()
    {
        await Task.WhenAll(AsyncSample1(), AsyncSample2());
        Debug.Log("All Completed.");
    }

    async Task AsyncSample1()
    {
        Debug.Log("AsyncSample1 Start.");
        await Task.Delay(1000);
        Debug.Log("AsyncSample1 End.");
    }

    async Task AsyncSample2()
    {
        Debug.Log("AsyncSample2 Start.");
        await Task.Delay(1000);
        Debug.Log("AsyncSample2 End.");
    }
}
```

`AsyncSample1()`, `AsyncSample2()` の実行が完了したら、 `All Completed.` を出力するようなサンプルです。
実行結果は、
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/bf20342a-a9a5-0f68-4f92-1d40dc034865.png)


## Task\<T>

戻り値が欲しい場合は `Task<T>` を使います。

```c#
using System.Threading.Tasks;
using UnityEngine;


public class Test : MonoBehaviour
{
    async void Start()
    {
        var str = await AsyncSample1();
        Debug.Log(str);
    }

    async Task<string> AsyncSample1()
    {
        Debug.Log("AsyncSample1 Start.");
        await Task.Delay(1000);
        return "AsyncSample1 End.";
    }
}
```

`AsyncSample1()` の結果が返ってくるまで、`Debug.Log` されると困るので、 `await` する必要があります。
（待ち受けするイメージです。）
結果は、
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/cb0e7b7b-790e-bf6b-c16e-b26be989c49e.png)

# 終わりに

Unity 初心者なので、間違いがあったら教えてくれるとありがたいです。
Unity で Task 使うなら、 UniTask 使おう。(理由はいまいち知らない…）
理由は UniTask の記事を書くときに、調べたいと思います。

# 参考文献
https://docs.microsoft.com/ja-jp/dotnet/api/system.threading.tasks.task?view=netcore-3.1
https://torikasyu.com/?p=1554
https://docs.microsoft.com/ja-jp/dotnet/api/system.threading.tasks.task.whenall?view=netcore-3.1
https://www.slideshare.net/UnityTechnologiesJapan/unite-tokyo-2018asyncawait
