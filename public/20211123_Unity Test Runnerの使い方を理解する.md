---
title: Unity Test Runnerの使い方を理解する
tags:
  - C#
  - テスト
  - Unity
private: false
updated_at: '2021-11-23T22:44:11+09:00'
id: b0f89280ecfcfa626f7b
organization_url_name: null
slide: false
ignorePublish: false
---
# 動作確認環境

- Windows10
- Unity 2019.4.13f1

# Unity Test Runner とは？

- Unityのテスト実行ツール
- NUnit という.NET用テスティングフレームワークが使われている
- EditMode, PlayMode のテスト実行環境がある

# Unity Test Runner のインストール方法

- Unity2019.1 以前ならば、標準でインストールされているので対応不要
- Unity2019.3 以降ならば、Package Manager から Test Framework と検索してインストールする

# Windowの開き方

- `Window` > `General` > `Test Runner` を選択するとウィンドウを開くことができる
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/35da28d6-b5e1-0805-e0ab-560bde48d629.png)
- 以下のようなウィンドウが開けばOK
  - `Create Playmode Test Assembly Folder` ボタンを押すと、 `Test`フォルダと`Assembly Definition File`が作成される
  - 作成された `Test` フォルダ配下にスクリプトを配置していく
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/ba12485c-5201-e895-b605-3248f42380cb.png)

## EditMode
- プレイモードを経由せずに、Unityエディタで即実行できる
    - すぐ実行できる
    - `Start()` や `Update()` など `MonoBehavior` の関数は呼ばれない
- メソッドに `[Test]` アトリビュートをつけるとテストメソッドと認識される
- スクリプトの配置場所は…
    - `Editor` のチェックを入れた `Assembly Definition File`(.asmdefファイル) を配置したフォルダ配下
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/45e9bbb3-2625-81d5-4159-dfa210d50236.png)

## PlayMode
- Unityエディタのプレイモードで実行できる
    - `MonoBehaviour` を組み合わせたテストができる
- テスト用の `Scene` が生成・実行される
    - Unity エディタがクラッシュすると、 `Scene` ファイルが残ってしまう
- スクリプトの配置場所は…
    - `Create Playmode Test Assembly Folder` ボタンを押して作成したフォルダ
    - `Assembly Definition File`の `Assemply Definition References` の `UnityEditor.TestRunner` を消す（画像の選択部分を消す）
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/d9cf6eb9-a097-ddff-69e3-c1d97e99ac28.png)

## フォルダ構成例

```
Assets/
└ Tests/
  ┝ PlayMode.asmdef
  ┝ TestCodeInPlayMode.cs
  ┝ Editor/
  │ ┝ Editor.asmdef
  │ └ TestCodeInEditorMode.cs
```

# テストの書き方

- 通常は `Test` アトリビュート、コルーチンの場合は `UnityTest` アトリビュートを付けたメソッドを定義
- 判定の書き方は Constraint Model と Classic Model がある

```c#
using System.Collections;
using NUnit.Framework;
using UnityEngine.TestTools;

public class EditorModeExample
{
    [Test]
    public void ExampleTest()
    {
        var a = 10;
        var b = 10;
        Assert.That(a == b);
    }

    [UnityTest]
    public IEnumerator ExampleTestEnumerator()
    {
        Assert.That(1 < 10);
        yield return null;
        Assert.That(2 < 10);
        yield return null;
        Assert.That(3 < 10);
    }
}
```

## Classic Model

- `Assert.True()` や `Assert.AreEqual()` などが使える古い書き方
    - こっちはもう使わない
- 基本的には後述の Constraint Model を使う

## Constraint Model

- `Assert.That()` を使う
- `Assert.That()` には多くのオーバーライドがある

#### Classic Model より Constraint Model を使う理由

- 複雑な条件が来た場合、Classic Model より柔軟に対応できる
- テストコードを結果と期待値を記述するという内容に画一化できる
- 旧モデルはサポートされなくなってきている

# テストの実行方法

- 実行したい関数かクラスを選択して、ダブルクリックもしくは右クリック > Run をクリックする
  - 緑のチェックマークになれば、テスト成功
  - 赤いバツマークになれば、テスト失敗

テスト成功時
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/77eef72a-c4ce-df23-f8e2-eb75556778db.png)
テスト失敗時
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/dabf6262-a285-31ee-c05f-92da21bce01c.png)

# テストの前後処理の書き方

対応するアトリビュートを使用することで可能

| 書き方 | 説明 |
| --- | --- |
| `[SetUp]` | 各テスト実行前に1回ずつ呼ばれる |
| `[TearDown]` | 各テスト実行前に1回ずつ呼ばれる |
| `[UnitySetUp]` | 各テスト実行前に1回ずつ呼ばれる（コルーチン） |
| `[UnityTearDown]` | 各テスト実行前に1回ずつ呼ばれる（コルーチン） |
| `[OneTimeSetUp]` | 最初のテスト実行前に1回だけ呼ばれる |
| `[OneTimeTearDown]` | 最後のテスト実行後に1回だけ呼ばれる |

### コード例

```c#
        // このクラスに定義された各テストが実行される前に、テストごとに一回ずつ呼ばれる
        [SetUp]
        public void Setup()
        {
            Debug.Log("SetUp");
        }

        // このクラスに定義された各テストの実行終了後に、テストごとに一回ずつ呼ばれる
        [TearDown]
        public void TearDown()
        {
            Debug.Log("TearDown");
        }

        // このクラスに定義された各テストが実行される前に、テストごとに一回ずつ呼ばれる（コルーチン）
        [UnitySetUp]
        public IEnumerator UnitySetup()
        {
            Debug.Log("UnitySetup");
            yield break;
        }

        // このクラスに定義された各テストの実行終了後に、テストごとに一回ずつ呼ばれる（コルーチン）
        [UnityTearDown]
        public IEnumerator UnityTearDown()
        {
            Debug.Log("UnityTearDown");
            yield break;
        }

        // このクラスに定義されたテストのうち最初のテストが実行される前に一回呼ばれる
        [OneTimeSetUp]
        public void OneTimeSetUp()
        {
            Debug.Log("OneTimeSetUp");
        }

        // このクラスに定義されたテストのうち最後のテストが実行された後に一回呼ばれる
        [OneTimeTearDown]
        public void OneTimeTearDown()
        {
            Debug.Log("OneTimeTearDown");
        }
```

# 参考文献

https://docs.unity3d.com/ja/2018.4/Manual/testing-editortestsrunner.html

https://www.slideshare.net/UnityTechnologiesJapan002/unite-tokyo-2019unity-test-runner

https://www.hanachiru-blog.com/entry/2020/05/16/120000

https://docs.nunit.org/articles/nunit/writing-tests/assertions/assertion-models/constraint.html
