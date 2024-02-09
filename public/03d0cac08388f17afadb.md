---
title: Oculus RiftはSurface Book 2で動かせないから気をつけて！
tags:
  - Unity
  - Surface
  - Oculus
  - OculusRift
  - VR
private: false
updated_at: '2019-01-22T00:48:30+09:00'
id: 03d0cac08388f17afadb
organization_url_name: null
slide: false
ignorePublish: false
---
# 結論から

Surface Book 2では、Oculus Riftを動かすことができません。
変換アダプターとか関係なく、ハードウェアのアーキテクチャ的に繋がりません。

## なぜ動かないか

詳細は、 [こちらのYouTube](https://www.youtube.com/watch?v=-vht-2juWh4) の動画が非常にわかりやすいです。

原因は、HDMIケーブルを認識することができないからです。

Surface Book 2の端子は、
① USB3.1 Gen1（フルサイズ）
② SDメモリーカードスロット
③ ヘッドホン出力
④ USB3.1 Gen1 Type-C
⑤ Surface Connect
があります。

HDMI端子がありませんが、USB-C→HDMI変換ケーブルで外部ディスプレイに出力可能です。
CPU内蔵GPU(iGPU)かディスクリートGPU(dGPU)の2つのGPUが内蔵されています。
しかし、USB-CとUSB3.1は、iGPUにしか繋がらず、dGPUにつなぐことができません。
そのため、Oculus RiftはiGPUを使用することになるため、スペックが足りず正常に動作させることができません。

15インチの場合、SteamVRパフォーマンステストでは、十分な性能であることを表わす「VRレディ」というスペックです。
しかし、動作させることができません。
Oculus RiftもHTC Viveも公式による正式サポートしていないため、文句は言えませんが納得行かない…

[Surface Book 2 15インチモデル 詳細レビュー：すべてが最高品質の超ハイエンド2-in-1ノートPC – こまめブログ](https://little-beans.net/review/surface-book2-15/)


# 終わりに

Oculus Questの発売まで待てず、Oculus Riftを買ったのが失敗でした。
セールをやっていたので、ノリで買って失敗しました。

どうやらHTC Viveの場合は動作させることができるようですが、iGPUと繋いだ状態とのことです。

Oculus RiftとHTC Viveが動かないことを知っていたらSurface Book 2を買わなかったです。ちゃんと下調べすればよかったと反省しています。

でもそれ以外は完璧なので、気に入っています。


# 参考文献

 [Would it work?? Oculus rift on surface book 2 15" : virtualreality](https://www.reddit.com/r/virtualreality/comments/7st24r/would_it_work_oculus_rift_on_surface_book_2_15/)
 
 [can you use VR on the Surface Book 2 (rift, vive etc) : Surface](https://www.reddit.com/r/Surface/comments/7f32ya/can_you_use_vr_on_the_surface_book_2_rift_vive_etc/)
 
 [Microsoft Surface Book 2 review: beauty and brawn, but with limits - The Verge](https://www.theverge.com/2017/11/16/16658466/microsoft-surface-book-2-review)
 
