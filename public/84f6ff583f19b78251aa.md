---
title: 【Unity C#】DRY原則を勉強する
tags:
  - C#
  - Unity
private: false
updated_at: '2022-03-13T21:00:13+09:00'
id: 84f6ff583f19b78251aa
organization_url_name: null
slide: false
ignorePublish: false
---
# 前置き

書籍を読んだり、ググったりして、自分に分かりやすいようにまとめた記事です。
より詳しく知りたい方は、下記の参考文献を読んでみてください。

# 参考文献

[達人プログラマー ―熟達に向けたあなたの旅― 第2版 | Amazon](https://www.amazon.co.jp/dp/B08T9BXSVD)
[あなたはDRY原則を誤認している？ - Qiita](https://qiita.com/yatmsu/items/b4a84c4ae78fd67a364c)
[本当の問題にたどり着かない――思考の重複を起こさないための「DRY」原則：問題解決力を高めるコツはプログラミングの原則・思考にあり - ＠IT](https://qiita.com/yatmsu/items/b4a84c4ae78fd67a364c)

# DRY原則(Don't Repeat Your Self) とは

- 一言でいうと<font color="Red">**知識を二箇所以上に重複させるな**</font>
- 同じロジックが複数箇所で使われるなら、コピペは厳禁
  - 同じようなコードが複数あると、修正する際に修正漏れする危険性がある
  - 同じようなコードだと思って、修正不要な箇所に誤って手を加えることになる可能性もある  
<br />
- 誤解しがちなところは<font color="Red">**「コードを重複させるな」ではない**</font>
  - 「知識」や「意図」の二重化についての原則
    - 異なった場所に同じことを表現するという問題を避けるための
    - コードだけでなく、データベーススキーマ、テスト計画、ビルドシステムやドキュメントなども含まれる

## コードの二重化

商品情報から消費税を計算したり、値引した価格を求めたりするコード例

```Product.cs
public class Product
{
    public string Name { get; set; }
    public int Price { get; set; }
}
```

```PriceCalculation.cs
public class PriceCalculation
{
    /// <summary>
    /// 商品の10%を求める
    /// </summary>
    /// <param name="product"></param>
    /// <returns></returns>
    public int GetTenPercentPrice(Product product)
    {
        return product.Price * 0.10;
    }

    /// <summary>
    /// 商品の消費税を求める
    /// </summary>
    /// <param name="product"></param>
    /// <returns></returns>
    public int GetConsumptionTax(Product product)
    {
        return product.Price * 0.10;
    }
}
```

### 改善方法

- `GetTenPercentPrice` と `GetConsumptionTax` のどちらも計算内容は同じ = 共通化できる
    - `Product.cs` の内容は同じなので割愛

```PriceCalculation.cs
public class PriceCalculation
{
    /// <summary>
    /// 商品の10%を求める
    /// </summary>
    /// <param name="product"></param>
    /// <returns></returns>
    public int GetTenPercentPrice(Product product)
    {
        return product.Price * 0.10;
    }
}
```

### 本当にこれで良いの？？

- 消費税が10%から8%に変更されたとする
    - `GetTenPercentPrice` を以下のように変更する可能性あり

```PriceCalculation.cs
public class PriceCalculation
{
    /// <summary>
    /// 商品の8%値引きした価格（消費税）を求める
    /// </summary>
    /// <param name="product"></param>
    /// <returns></returns>
    public int GetEightPercentPrice(Product product)
    {
        return product.Price * 0.08;
    }
}
```

- 消費税の計算に関する修正としては問題ないが「10%値引きした価格計算」する処理がなくなった
    - 値引き計算している処理のところでコンパイルエラーや意図しない挙動になってしまう
    - 共通化しすぎかも？？

### 本当の改善方法（例）

- 「値引き価格計算」と「消費税計算」は別々に管理するほうがよいかも
    - 変更する理由を明確に分離できる

```DiscountCalculation.cs
public class DiscountCalculation
{
    /// <summary>
    /// 商品の10%を求める
    /// </summary>
    /// <param name="product"></param>
    /// <returns></returns>
    public int GetTenPercentPrice(Product product)
    {
        return product.Price * 0.10;
    }
}
```

```TaxCalculation.cs
public class TaxCalculation
{
    /// <summary>
    /// 商品の消費税を求める
    /// </summary>
    /// <param name="product"></param>
    /// <returns></returns>
    public int GetConsumptionTax(Product product)
    {
        return product.Price * 0.10;
    }
}
```

## コードのコメントによる二重化

コード例

```Bullet.cs
// 違反例
public class Bullet : MonoBehaviour
{
    /// <summary>
    /// Enemyオブジェクトに衝突したときに発火する
    /// GameObjectに格納している IEnemy の Component を取得
    /// Enemyオブジェクトにダメージを与える
    /// Component が取得できなかったら何もしないで処理を終了する
    /// </summary>
    /// <param name="collision"></param>
    void OnCollisionEnter(Collision collision)
    {
        var hit = collision.gameObject;
        var enemy = hit.GetComponent<IEnemy>();

        if (enemy == null)
            return;

        enemy.ApplyDamage();
    }
}
```

### 良くない点
- コメントとコードで、この関数の情報が2度繰り返されている
    - コードを修正した場合、コメントを修正する必要がある
        - コメント修正を忘れる可能性大
        - 時間が経つと、コードとコメントが乖離していく

### 改善方法
- 変数名、関数名などを工夫することで改善可能
    - 名前で意味や意図、役割を表すようにする
    - コードを読むだけで分かることはコメントに書かない


## データ構造の二重化

縦、横、面積のデータ構造を持つコード例

```Rectangle.cs
// 違反例
public class Rectangle
{
    public int Height { get; set; }
    public int Width { get; set; }
    public int Area { get; set; }
}
```


### 良くない点

- 縦か横の長さが変化すると面積も変わる

### 改善方法

- `Area()` は縦x横で面積を計算するメソッドに変更する

```Rectangle.cs
// 改善例
public class Rectangle
{
    public int Height { get; set; }
    public int Width { get; set; }
    public int Area()
    {
        return Height * Width;
    }
}
```

# 終わりに

SOLID原則に続いてDRY原則をまとめました。
間違いや改善点あれば、ぜひ教えてください。
SOLID原則の記事は以下です。

1. [SOLID原則を勉強する その1～単一責任の原則 (SRP)～](https://qiita.com/riekure/items/904f56713c3e213920fa)
2. [SOLID原則を勉強する その2～オープン・クローズド原則(OCP)～](https://qiita.com/riekure/items/41c891c50a868cfd5939)
3. [SOLID原則を勉強する その3～リスコフの置換原則(LSP)～](https://qiita.com/riekure/items/cfc6f8e160ec975153ba)
4. [SOLID原則を勉強する その4～インターフェース分離の原則(ISP)～](https://qiita.com/riekure/items/8b6b8adf641285e22113)
5. [SOLID原則を勉強する その5～依存性逆転の原則(DIP)～](https://qiita.com/riekure/items/ab6b5deb391399944a15)


