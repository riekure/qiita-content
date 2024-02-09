---
title: 【Unity】リソースデータ (Resources/StreamingAssets/AssetBundle) 読み込みについてまとめてみた
tags:
  - C#
  - Unity
private: false
updated_at: '2024-01-22T21:57:43+09:00'
id: 8ca8d7cedffa7f734c1f
organization_url_name: null
slide: false
ignorePublish: false
---
# リソースデータについて

- Unity プロジェクトに「画像」「3Dモデル」「音声」「動画」など、ファイルサイズが大きいアセットが含まれる
- ユーザーに届ける方法は大きく分けると2つ
    - 全アセットをビルドに含める
    - DLC（ダウンロードコンテンツ）としてゲーム内（アプリ内）でダウンロードさせる


# Resources 

- 旧来の Unity 開発で頻繁に利用されていたアセットの動的読み込みを行うための仕組み
    - `Resources` という名前がついたフォルダは、ビルド時にアプリのバイナリに同梱される
    - `Resources.Load("path/to/asset")` といったAPIから読み込みが行える
- 現在は**非推奨**
    - メモリ管理が難しくなる
    - アプリの起動時間が長くなる
    - リソースを特定のプラットフォームにのみ配信するなどの対応ができない

## Resources を使ってもよいケース

- プロトタイプ開発時
- アプリが立ち上がっている間常駐するリソース
- メモリをあまり使わない場合
- プラットフォーム間でリソースを切り替える必要がない場合

# StreamingAssets

- アセットを変換しないでそのままアプリに持っていく仕組み
    - バイナリとして保存するのでデシリアライズが必要
- プラットフォームごとに配置されるフォルダは異なり、 `Application.streamingAssetsPath` で取得できる
    - Unity Editor、Windows、Linux、PS4、Xbox、Switch は `Application.dataPath + "/StreamingAssets"`
    - macOS は `Application.dataPath + "/Resources/Data/StreamingAssets"`
    - iOS は `Application.dataPath + "/Raw"`
    - Android は圧縮された APK/JAR ファイル `"jar:file://" + Application.dataPath + "!/assets"`
- Android の場合は `UnityWeRequest` を使ってロードする

## StreamingAssets を使ってもよいケース

- ビルド済みの AssetBundle を格納する
    - AssetBundle は変更しなければビルドし直し不要のため、ビルド時間の削減
    - ビルド前処理に buildTarget に指定されたプラットフォームの AssetBundle のみを StreamingAssets に配置する必要がある
- プラットフォームごとに変換が不要なアセットの読み込み

# AssetBundle

- Import済アセットのバイナリデータを固めたモノ
    - DLCとしてダウンロードすることで、ビルドに含まれないリソースを追加読み込みできる
- AssetBundle として使えるアセットは
    - 画像
    - オーディオファイル
    - フォント
    - Scene
    - Prefab
    - フォルダ
        - C#スクリプトを固めることはできない
- 通常の AssetBundle と Streamed AssetBundle(Streamed Scene AssetBundle) に分類できる

## 通常の AssetBundle

- Scene を除く任意の Asset を固めた AssetBundle のこと
    - 1つ以上の Asset が固められたバイナリデータをファイルとして出力したもの
        - 内部的には Lz4 などの圧縮アルゴリズムを用いて圧縮されたファイル

## Streamed Scene AssetBundle

- Scene そのものを AssetBundle として固めたもの
    - Scene 内の GameObject から参照されているアセットも一緒に固められる
- 圧縮などの仕組みは通常の AssetBundle と変わらない
- AssetBundle を Load した時点で SceneManager からアクセス可能になる

## AssetBundle でできること

- DLC としてアセットを動的ロードする
- バリエーションを持たせる
    - 複数のプラットフォーム、国、地域に配信するときなど、リソースデータにバリエーションをもたせたい
    - AssetBundle Variants 機能を使う
- 任意の粒度でまとめる
    - 設定した AssetBundle Name 単位でグルーピングされる
    - APIを叩いてグルーピング可能
- 依存関係を構築する

## Addressable Asset System

- アドレスを指定することでリソースデータをロードできる機能
    - アドレスは Asset ごとに付けることができる任意の名前
- ローカルのデータか、リモートから AssetBundle をロードするか設定ひとつで変更できる
    - 呼び出し側は同じインターフェースでロードできる

## 使い方

- Unity2019.3以上ならば Package Manager から Addressables をインストールすることで使用可能
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/3fd822ef-8caf-7afd-4588-f748247e5ab9.png)
- Window > Asset Management > Addressables > Settings を選択すると。 `AddressableAssetsData` フォルダが作成される
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/e5d0b28e-ffc6-c499-c100-0956d9c37e91.png)
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/5d2b7c3c-e351-8606-b87f-b5ce079f9f8a.png)
- Addressable にチェックを入れることで、Addressable の管理対象になる
    - Addressables Group に追加される
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/f4d00a92-80c8-29f8-4ea7-b6342d21b04d.png)
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/0ba3eea2-78bd-8c9b-8692-5dbdc46bf52a.png)

### フォルダ構成

|アセット|内容|
|:--|:--|
|AddressableAssetSettings.asset|・プロジェクトのAddressableの設定が保存されている|
|AssetGroups/|・Groupに属しているアセットのGUIDやLabel情報などを管理|
|AssetGroups/Built In Data.asset|・Resources や Scene in Buildに関わる情報を管理|
|AssetGroups/Default Local Group.asset|・Playerビルドに含めるアセットを管理<br>・初期状態に作成される|
|Schemas/|・Groupの詳細な設定を管理<br>・GroupごとにSchemasが配置される|
|AssetGroupTemplates/|・Groupの新規作成時につかうテンプレ<br>・新規でGroup Templeteを作成したときは AddressableAssetSettings に追加しなければならない|
|DataBuilders/|・ビルド、エディタ再生時に使用される設定<br>・AssetBundleのビルド方法を定義したScriptableObjectが配置される|
|DefaultObject.asset|・AddressableAssetSettings.assetの場所を示すScriptableObject|

※ DataBuilders や AssetGroupTemples はあまり編集しない

## AssetBundle をビルドする

- 新規の場合h AddressableGroups で、 Build > New Build > Default Build Script を選択する
    - すでにビルド済みの AssetBundle を更新する場合は Update a Previous Build
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/cc4ce0f0-add5-7fbe-c84c-888852024f83.png)
- Build される場所は以下で設定できる
    - LoadBuildPath: `Library/com.unity.addressables/[BuildTarget]`(デフォルト)
        - Playerビルド時に一時的に StreamingAssets にコピーされることで Player ビルドに同梱される
    - RemoteBuildPath: `ServerData/[BuildTarget]`(デフォルト)
        - プロジェクトルート直下に作成される `ServerData` 以下に作成された AssetBundle を RemoteLoadPath のURLに対応するようにアップロードする必要がある
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/3194a82b-60f3-162e-77a0-6ac328d03bca.png)

## AssetBundle を読み込む

- 通常はアプリ起動時に自動的に Addressable の初期化処理が実行される
- 何らかの理由でスクリプトから初期化、実体化したい場合は
    - `Addressables.LoadAssetAsync()` してから `Instantiate()` する
    - 直接 `Addressables.InstantiateAsync()` する

```c#
// Load してから Instatiate()
var gameobject = await Addressables.LoadAssetAsync<GameObject>("Assets/Prefabs/Cube.prefab");
var obj = Instantiate(go);

// 直接 Instatiate()
Addressables.LoadAssetAsync<GameObject>("Assets/Prefabs/Cube.prefab");
```

# 参考文献

https://www.borndigital.co.jp/book/22432.html

https://learn.unity.com/tutorial/assets-resources-and-assetbundles?uv=2017.3

https://light11.hatenadiary.com/entry/2020/07/29/202755

https://docs.unity3d.com/ja/2019.4/Manual/StreamingAssets.html

https://robamemo.hatenablog.com/entry/2021/01/08/195415

