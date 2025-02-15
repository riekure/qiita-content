---
title: 【Unity】Prefab／Nested Prefabs／Prefab Variant の違いについてまとめる
tags:
  - Unity
private: false
updated_at: '2022-12-03T16:49:33+09:00'
id: 48b24e84cc8850621176
organization_url_name: null
slide: false
ignorePublish: false
---
# 初めに

Preafab Variant という名前は知っているが、使ったことないので Prefab 全体について勉強した内容をまとめた記事です。

# Prefab とは？

作成済みの GameObject をテンプレートとして保存し、複製して使用することができる機能です。

例えば、体力や攻撃力などをスクリプトなどで設定した Enemy オブジェクトを作成したとします。
そして Enemy オブジェクトを Prefab 化します。

そうすると、 Enemy オブジェクトを簡単に複製することができます。（インスタンス化という。）
もちろん何個でも複製可能です。

インスタンス化したオブジェクトは、スクリプトなどで設定した値を変更することも可能です。

## Prefab 化する方法

作成した GameObject を Hierarchy から Project にドラッグ&ドロップすれば作成できます。
![Prefab化.gif](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/88450ee4-63e9-4208-0f4e-120c4a4c51b8.gif)

## Prefab をインスタンス化する方法
Project から Hierarchy にドラッグ&ドロップすればインスタンス化できます。
![インスタンス化.gif](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/e086bf82-dce3-d200-6f6f-94d83ceb03aa.gif)

## インスタンスから Prefab を上書きする方法

インスタンス化したオブジェクトから、Prefab に対して上書き（Override）することができます。

Override するには、 まずインスタンスの Inspector から編集します。
そのあとは、二種類の上書き方法があります。

**1. Override したプロパティを右クリック → "Apply to Prefab 'Prefab名'"**
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/0d26cc35-22d0-56e3-0482-3d5d5686d341.png)
**2. Overridesドロップダウンから Override したプロパティを選択して Apply ボタンを押下**
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/6b3e3085-e819-3a27-4ed5-57bd35181f24.png)
**3. Overridesドロップダウンから Apply All ボタンを押下**

※ 言葉通り、上2つとは異なり、変更したプロパティの全てを上書きします。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/6dd46f2a-adda-34ed-73e6-b8d1137aba77.png)


### インスタンスで上書きできるもの

- プロパティの値の変更
- コンポーネントの追加／削除
- GameObjectの追加

### インスタンスで上書きできないもの

- GameObjectの削除
- 階層構造を変更できない
  - Open Prefab から直接編集する必要がある

変更しようとすると ↓ のダイアログが表示される。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/a269bacd-afa7-923f-72f8-9239b653e615.png)

## 直接 Prefab を編集する

Hierarchy から編集する方法の他に、 Prefab モードから編集することもできます。
Preafab モードを表示する方法は、2種類あります。

**1. Project から Prefab を選択 → Open Prefab ボタンを押下**
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/bed957d1-4804-07a2-ff5a-2c8b7474c057.png)
**2. Hierarchy から Prefab を選択 → 「＞」を押下**
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/14717799-4298-625d-c4fb-64d72a99782d.png)

Prefab モードでの変更は、 Auto Save にチェックが付いていれば、自動で保存されます。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/02e07659-f67e-9ffb-0ae1-22be469a9a14.png)
チェックが付いていなければ、自分で Save ボタンを押すことで保存できます。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/dc56dd48-dabf-edad-dbb2-44d0fb3c1e67.png)

# Nested Prefabs とは？

名前の通りですが、 Prefab は入れ子にすることができます。
Prefab の階層内に別の Prefab が存在している状態です。

スクショは、 "Enemy1" Prefab に "Enemy2" Prefab が入れ子になっています。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/a4187a1f-0a93-6464-715a-4267e37a2eaa.png)

この状態で、 Apply All ボタンを押下すると、以下のように、Prefab の中に Prefab が入っている状態で Prefab 化することができます。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/85cf6eeb-a1cc-578a-502d-04855399dc95.png)

# Prefab Variant とは？

Unity 公式には、

> プレハブバリアントは、一揃いの事前定義されたプレハブのバリエーションを使用したい場合に便利です。

どういうことかというと、「構成はほぼ一緒だが、一部の設定だけがベースの Prefab と異なる」といった場合に便利ということです。
例えば、 BaseEnemy という Prefab から、HPと攻撃力が異なる様々な種類の敵オブジェクトを作りたいときなど便利です。

Unity 2018.3からの新機能らしいです。

実際に使ってみます。

## 例
今回は HP と Attack というプロパティを持つ BaseEnemy (Prefab) を元に、以下の Prefab Variant を作成するという例でやってみます。

- 名前：シャドウ（ザコ敵）
  - HP: 10
  - Attack: 2
- 名前：ギガース（そこそこ強い敵）
  - HP: 20000
  - Attack: 5000

### BaseEnemy (Prefab) を用意

上で記載した Prefab 化を元に、BaseEnemy という名前の Prefab を用意します。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/29a7e5eb-6fcc-78e2-6e8b-56b0f61cd742.png)
EnemyManager の内容は以下です。
（例なので最小限しか書いておらず、特に機能はないです。hp と attack を定義しているだけです。）

```EnemyManager.cs
using UnityEngine;

public class EnemyManager : MonoBehaviour
{
    [SerializeField] int hp;
    [SerializeField] int attack;
}
```

### Preafab Variant でザコ敵のシャドウを作成

Prefab 化した BaseEnemy を Hierarchy から Project にドラッグ&ドロップします。
そうすると、新しい Prefab を作成するか、 Prefab Variant を作成するかダイアログで問われます。
今回は Prefab Variant を選択します。
![プレファブバリアント.gif](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/1965c71c-e650-5a1c-20b8-2e891cd77e51.gif)
あとは、 Prefab を変更するように、 Prefab Variant を編集します。
名前は "ShadowVariant" 、HP = 10とAttack = 2に変更します。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/53e27ed3-5ecf-df9c-5b4d-660aa7ebc49e.png)
ちなみに、 Prefab Variant に適用した変更を Prefab にも上書きしたい場合は、 Prefab と同じ手順で上書きすることができます。

### Preafab Variant でそこそこ強い敵ギガースを作成

せっかくなので上とは違う Prefab Variant の作成方法でやってみます。
Prefab を右クリック > Create > Prefab Variant で作成できます。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/db62931c-b6ce-5bf1-dc35-1e852794398a.png)
名前は "GigasEnemy"、HP = 20000とAttack=5000に変更します。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/9fcd2baa-c8e1-d799-e242-ff75ccb40032.png)

# Prefab とのインスタンスの接続解除

インスタンス化したが、 Prefab との紐付けを解除する方法もあります。
右クリック > Unpack Prefab で、紐付けを解除できます。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/233011/e29de1b0-dda1-3754-37db-9b9e6ea4c1b4.png)

ちなみに Prefab Variant を Unpack Prefab すると、 Prefab になり、
Prefab を Unpack Prefab すると、全ての Prefab の紐付けを解除できます。

Prefab Variant を Unpack Prefab Completely すると、一気に全ての紐付けを解除できます。
また、子階層に Prefab がいる場合も、 Unpack Prefab Completely すると、一気に紐付けを解除できます。

# 終わりに

最初は Prefab Variant について知りたくて、調べていました。
そのついでに Prefab とか改めて調べ直したのですが、結構新しいことを知ることができてよかったです。
Unity の基礎をもう少し深堀りしてもいいかなーと思いました。

ちなみに、敵の元ネタはキンハーです。


# 参考文献

https://dkrevel.com/makegame-beginner/prefab-nested/
https://light11.hatenadiary.com/entry/2019/01/20/205726
https://docs.unity3d.com/ja/2018.4/Manual/PrefabVariants.html
