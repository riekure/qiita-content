---
title: 【Unity】Unity Editorかスマホ実機か判別して処理を分ける
tags:
  - C#
  - Unity
  - 初心者
private: false
updated_at: '2019-07-24T23:41:09+09:00'
id: 8936d755644eeee5da31
organization_url_name: null
slide: false
ignorePublish: false
---
# はじめに

スマホ実機で毎回動作確認するのが面倒だったので、Unity Editorの場合はキーボード操作ができるようにしました。

# サンプルスクリプト1

Main CameraにAttachして使用することを想定したスクリプトです。
Unity Editorの場合は、方向キーで視点移動ができるように、
スマホ実機（Unity Editor以外）の場合は、端末を傾けて視点移動ができるようになっています。

```c#:GyroController1
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GyroController : MonoBehaviour
{
    // キーボード操作用
    private Vector3 rotate;
    void Start()
    {
        // 動作確認用のログ
        Debug.Log("started");

        // Unityエディタと実機で処理を分ける
        if (Application.isEditor)
        {
            rotate = transform.rotation.eulerAngles;
            Debug.Log("no-smartphone");
        }
        else 
        {
            Input.gyro.enabled =true;
        }
    }

    void Update()
    {
        // キーボードで視点変更
        float speed = Time.deltaTime * 100.0f;

        // PCは矢印キーで視点変更
        if (Application.isEditor)
        {
            if (Input.GetKey(KeyCode.LeftArrow))
            {
                rotate.y -= speed;
            }
            if (Input.GetKey(KeyCode.RightArrow))
            {
                rotate.y += speed;
            }
            if (Input.GetKey(KeyCode.UpArrow))
            {
                rotate.x -= speed;
            }
            if (Input.GetKey(KeyCode.DownArrow))
            {
                rotate.x += speed;
            }
            transform.rotation = Quaternion.Euler(rotate);
        }
        // スマホはジャイロで視点変更
        else
        {
            Quaternion gratitude = Input.gyro.attitude;
            gratitude.x *= -1;
            gratitude.y *= -1;
            transform.localRotation = Quaternion.Euler(90, 0, 0) * gratitude;
            
        }
    }
}
```

# サンプルスクリプト2

コメントにて教えていただいた方法です。
コメントそのまま転載させてもらうと、

> 長所=デバッグコマンドなどをapkに埋め込まなくて済みます
> 短所=実機専用コード部分にインテリセンス効かなくなります

書いてみましたが、インデントに自信はありません。

```c#:GyroController2
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GyroController : MonoBehaviour
{
    // キーボード操作用
#if UNITY_EDITOR || UNITY_STANDALONE
    private Vector3 rotate;
#endif

    void Start()
    {
        // 動作確認用ログ1
        Debug.Log("started");
    #if UNITY_EDITOR || UNITY_STANDALONE
        rotate = transform.eulerAngles;
        // 動作確認用ログ2
        Debug.Log("non-smartphone");
    #else
        Input.gyro.enabled = true;
    #endif
    }

    void Update()
    {
        // PCの場合はキーボード、スマホはジャイロで視点変更
    #if UNITY_EDITOR || UNITY_STANDALONE
        float speed = Time.deltaTime * 100.0f;
        if (Input.GetKey(KeyCode.LeftArrow))
        {
            rotate.y -= speed;
        }
        if (Input.GetKey(KeyCode.RightArrow))
        {
            rotate.y += speed;
        }
        if (Input.GetKey(KeyCode.UpArrow))
        {
            rotate.x -= speed;
        }
        if (Input.GetKey(KeyCode.DownArrow))
        {
            rotate.x += speed;
        }
        transform.rotation = Quaternion.Euler(rotate);
    #else
        Quaternion gattitude = Input.gyro.attitude;
        gattitude.x *= -1;
        gattitude.y *= -1;
        transform.localRotation = Quaternion.Euler(90, 0, 0) * gattitude;
    #endif
    }
}
```

# 最後に

Unity初心者なので、より良い方法や間違いがあったら、是非教えてほしいです。

# 参考文献

[Platform dependent compilation](https://docs.unity3d.com/Manual/PlatformDependentCompilation.html)
