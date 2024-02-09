---
title: THETA Web API v2.1 を curl コマンドで実行する方法
tags:
  - curl
  - Theta
private: false
updated_at: '2020-01-14T13:59:29+09:00'
id: e626227e3a8dee6472b3
organization_url_name: null
slide: false
ignorePublish: false
---
# 背景

THETA API の使い方や、レスポンスを知りたかった。
実装する前に、 curl で確認できるようになりたかった。
（Unity + THETA で遊ぶことが目標です。）

# 動作確認環境

- THETA V（ファームウェア：バージョン 3.10.1）
- macOS Calalina バージョン10.15.2

# 参考文献

https://api.ricoh/docs/theta-web-api-v2.1/

# camera.takePicture

https://api.ricoh/docs/theta-web-api-v2.1/commands/camera.take_picture/
静止画を撮影したいときに使用します。

```shell
curl -H "content-type: application/json; charset=utf-8" -X POST http://192.168.1.1:80/osc/commands/execute -d '{"name": "camera.takePicture"}'
```

静止画モードでのレスポンス
( state が done の場合は、ファイル保存先などが返ってくるようです。)

```json
{
	"name": "camera.takePicture",
	"id": "5143",
	"progress": {
		"completion": 0
	},
	"state": "inProgress"
}
```

ちなみに、動画モードで実行すると、エラーが返ってきました。

```json
{
	"error": {
		"code": "disabledCommand",
		"message": "Command executed is currently disabled."
	},
	"name": "camera.takePicture",
	"state": "error"
}
```


# camera.startCapture

https://api.ricoh/docs/theta-web-api-v2.1/commands/camera.start_capture/
動画モードの場合は、`camera.takePicture` ではなく、こちらを使用します。
実行すると、動画の撮影を開始することができます。

```shell
curl -H "content-type: application/json; charset=utf-8" -X POST http://192.168.1.1:80/osc/commands/execute -d '{"name": "camera.startCapture", "parameters" : {}}'
```

レスポンス

```json
{
	"name": "camera.startCapture",
	"state": "done"
}
```

インターバル撮影などを行いたい場合は、 `parameters` に `_mode` を追加してください。

```shell
curl -H "content-type: application/json; charset=utf-8" -X POST http://192.168.1.1:80/osc/commands/execute -d '{"name": "camera.startCapture", "parameters" : {"_mode" : "interval"}}'
```

# camera.stopCapture
https://api.ricoh/docs/theta-web-api-v2.1/commands/camera.stop_capture/
`camera.startCapture` を実行したあと、録画を終了するときに使用します。

```shell
curl -H "content-type: application/json; charset=utf-8" -X POST http://192.168.1.1:80/osc/commands/execute -d '{"name": "camera.stopCapture"}' 
```

レスポンス

```shell
{
	"name": "camera.stopCapture",
	"results": {
		"fileUrls": [
			"http://192.168.1.1/files/150100525831424d42079f84a8a2c300/100RICOH/R0011427.MP4"
		]
	},
	"state": "done"
}
```

# camera.delete

https://api.ricoh/docs/theta-web-api-v2.1/commands/camera.delete/
THETA 内に保存されている静止画／動画を削除したいときに使用します。
例は、全削除を示しています。

```shell
curl -H "content-type: application/json; charset=utf-8" -X POST http://192.168.1.1:80/osc/commands/execute -d '{"name": "camera.delete", "parameters" : {"fileUrls" : ["all"]}}'
```

レスポンス

```json
{
	"name": "camera.delete",
	"state": "done"
}
```

# camera.getOptions

THETA の現在の設定を取得したときに使用します。
`optionNames` に指定された値の内容を返してくれます。
例では、`captureMode`, `fileFormat`, `fileFormatSupport` を取得しています。
取得できる値は、`Options` を参照。

```shell
curl -H "content-type: application/json; charset=utf-8" -X POST http://192.168.1.1:80/osc/commands/execute -d '{"name": "camera.getOptions", "parameters": { "optionNames": [ "captureMode", "fileFormat", "fileFormatSupport" ] }}'
```

レスポンス

```json
{
	"name": "camera.getOptions",
	"results": {
		"options": {
			"captureMode": "video",
			"fileFormat": {
				"_codec": "H.264/MPEG-4 AVC",
				"height": 1920,
				"type": "mp4",
				"width": 3840
			},
			"fileFormatSupport": [
				{
					"_codec": "H.264/MPEG-4 AVC",
					"height": 1920,
					"type": "mp4",
					"width": 3840
				},
				{
					"_codec": "H.265/HEVC",
					"height": 1920,
					"type": "mp4",
					"width": 3840
				},
				{
					"_codec": "H.264/MPEG-4 AVC",
					"height": 960,
					"type": "mp4",
					"width": 1920
				},
				{
					"_codec": "H.265/HEVC",
					"height": 960,
					"type": "mp4",
					"width": 1920
				}
			]
		}
	},
	"state": "done"
}
```

# camera.setOptions

THETA の設定を変更したいときに使用します。
例は `fileFormat` を `"type":"mp4","width":3840,"height":1920, "_codec":"H.264/MPEG-4 AVC"` に変更しています。
変更できる値、設定する値は 各 `Options` を参照。

```shell
curl -H "content-type: application/json; charset=utf-8" -X POST http://192.168.1.1:80/osc/commands/execute -d '{"name": "camera.setOptions", "parameters": { "options": { "fileFormat": {"type":"mp4","width":3840,"height":1920, "_codec":"H.264/MPEG-4 AVC"} } }}'
```

レスポンス

```json
{
	"name": "camera.setOptions",
	"state": "done"
}
```

# 終わりに

使用頻度が高そうなコマンドを一通り書きました。
他にも多くのコマンドがありますが、あとは API リファレンスを見ながら対応できるかと思います。
