---
title: 【Unity】PlayerPrefs の使い方やメリット/デメリットなどをまとめてみた
tags:
  - C#
  - Unity
private: false
updated_at: '2022-02-13T22:24:22+09:00'
id: 3fd4526b13d8e89a7fc6
organization_url_name: null
slide: false
ignorePublish: false
---
# PlayerPrefs とは？

- UnityEngine が提供しているゲームデータのセーブ・ロードを行う機能
- ゲームが終了しても保持しておきたいデータを保存することができる
- - キー・バリュー形式で端末内に保存する
    - 個人設定（コンフィグの設定等）のような外部に保存する必要がないデータや通信できないときに一時保存するときに使える

# データをセーブする

- 対応している型は…
    - `float`
    - `int`
    - `string`
- 同じキー名でセーブしたら、値は上書きされる


```c#:使用例
// Health というキー名に float 型で 50.0f という値を保存
PlayerPrefs.SetFloat("Health", 50.0F);

// Score というキー名に int 型で 20 という値を保存
PlayerPrefs.SetInt("Score", 20);

// Player Name というキー名に string 型で Foobar という値を保存
PlayerPrefs.SetString("Player Name", "Foobar");
```

# データをロードする

- キー名を指定してデータをロードする
    - キー名に対応するデータがなかった場合は `defaultValue` の値を返す
        - `defaultValue` の指定がなかったら `GetFloat`, `GetInt` の場合は0, `GetString` の場合は空文字を返す

```c#
public static float GetFloat (string key);
public static float GetFloat (string key, float defaultValue);
public static int GetInt (string key);
public static int GetInt (string key, int defaultValue);
public static string GetString (string key);
public static string GetString (string key, string defaultValue);
```

```c#:使用例
// Health というキー名のデータをロード.キーが存在しなかったら 50.0f を返す.
var health = PlayerPrefs.GetFloat("Health", 50.0f);

// Score というキー名のデータをロード.キーが存在しなかったら 20 を返す.
var score = PlayerPrefs.GetInt("Score", 20);

// Player Name というキー名のデータをロード.キーが存在しなかったら Foobar を返す.
var playerName = PlayerPrefs.GetString("Player Name", "Foobar");
```

# データを削除する

- キー名を指定してキーとデータを削除
- 全てのキーとデータを削除

```c#:使用例
// 全てのキーとデータを削除
PlayerPrefs.DeleteAll();

// Health というキーとデータを削除
PlayerPrefs.DeleteKey("Health");
```

- PlayerPrefs で値を保存する実装ができる
- PlayerPrefs でどこに値が保存されてるか（どの程度セキュアか）理解している
- PlayerPrefs 以外で値を保存する手法について理解している


# データが保存される場所

| 端末 | 場所 |
| :-- | :-- |
| **macOS** | `~/Library/Preferences` フォルダー内の `unity.[会社名].[製品名].plist` というファイル |
| **Windows** | レジストリの `HKCU\Software\[company name]\[product name]` に保存される| 
| **Linux** | `~/.config unity3d[CompanyName]/[ProductName]` に保存される |
| **Windows Store Apps** | `%userprofile%\AppData\Local\Packages\[ProductPackageId]>\LocalState\playerprefs.dat` に保存される |
| **Android** | SharedPreferencesに保存<br>`/data/data/pkg-name/shared_prefs/pkg-name.xml`に保存<br>C#/JavaScript, Android Java, ネイティブコードは全てアクセス可能 |
| **iOS** |  UserDefaults に保存<br>`/Library/Preferences/[bundle identifier].plist` に格納される |

# メリット/デメリット

#### メリット
- 端末がオフライン状態でも使用できる
- 端末内に保存するのでサーバやDBが不要
 
#### デメリット
- 保存できるデータ型が限られている
    - 大容量のデータ保存に向かない
- 端末内に保存されるのでユーザーもアクセスが容易
- 複数のデータを一括で保存できない

# 代替案

- 外部アセットを使用（EasySaveなど）
    - 簡単にセーブ＆ロード&暗号化が実装できる
    - int や string だけでなく、List や Vector3 などの型も保存可能
        - PlayerPrefs より多機能
- 外部ファイルとして保存（CSV, JSON, XML）
    - 大量のデータを保存するときに PlayerPrefs よりおすすめ
- サーバに保存
    - ユーザーが変更できないようにサーバ上にデータを保管する = セキュリティ対策


# 参考文献

https://docs.unity3d.com/ja/current/ScriptReference/PlayerPrefs.html

https://blog.unity.com/ja/technology/persistent-data-how-to-save-your-game-states-and-settings

https://kan-kikuchi.hatenablog.com/entry/EasySave
