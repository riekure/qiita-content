---
title: 【Python】マイページからいいね（LGTM）順が消えたので Qiita API 使って取得する
tags:
  - Qiita
  - Python
  - QiitaAPI
  - Python3
private: false
updated_at: '2020-06-28T14:24:13+09:00'
id: 166abfefed095fefe00a
organization_url_name: null
slide: false
ignorePublish: false
---
# 初めに

いいね順が見れなくなったので、コードを書くことにしました。
消されたということは、需要がなかったんですかね…

# 動作環境
- Windows 10
- Python3.7.1(Anaconda)

# コード

USER_ID を変更すれば、別ユーザーの投稿一覧も取得できると思います。

```python
import http.client
import json
import math

CONN = http.client.HTTPSConnection('qiita.com', 443)
USER_ID = 'riekure'
PER_PAGE = 100

class Api:
    # リクエスト結果をJSON形式で返す
    @staticmethod
    def request(http, url) :
        CONN.request(http, url)
        res = CONN.getresponse()
        data = res.read().decode('utf-8')
        return json.loads(data)

    # 投稿数とからページ番号を計算する
    @staticmethod
    def page_count(items_count) :
        return math.floor(items_count / PER_PAGE) + 1

# 投稿数を取得
items_count = Api.request('GET', '/api/v2/users/' + USER_ID)['items_count']
page = Api.page_count(items_count)

# 投稿記事を全て取得
all_article = {}
for i in range(page) :
     article = Api.request('GET', '/api/v2/users/' + USER_ID + '/items?page=' + str(i+1) + '&per_page=' + str(PER_PAGE))
     for j in range(PER_PAGE) :
         try :
             all_article[article[j]['title']] = article[j]['likes_count']
         except IndexError :
             break


# いいね（LGTM）の降順にソート
# items() を使用するので tuple になる
tuple_items = sorted(all_article.items(), key=lambda x:x[1], reverse=True)

# markdown の表形式で表示
print('| 記事タイトル | いいねカウント |')
print('|------------|--------------|')
for title, likes_count in tuple_items:
    print('| ' + title + ' | ' + str(likes_count) + ' |')
```

# 実行結果

2020年6月2日現在の結果

| 記事タイトル | いいねカウント |
|------------|--------------|
| UnityでVisual Studio Codeを使用できるようにするまでの手順 | 61 |
| [Windows 10] 矢印キーに指を伸ばすエンジニアはザコ！とバカにされた（Change KeyとAutoHotkeyの導入） | 54 |
| 10ヶ月勉強してもAWS認定ソリューションアーキテクト-アソシエイト-に合格できないので、勉強方法を振り返る | 42 |
| 1年かけてAWS認定ソリューションアーキテクト-アソシエイト-に合格できたので、勉強法を振り返る | 29 |
| クソコード量産プロジェクトを撲滅するためのESLint導入物語 | 29 |
| Amazon Linux 2でmysql-serverがインストールできないときの対処方法 | 27 |
| Java 8 LocalDateTimeの型変換のあれこれ(String, java.util.Date) | 22 |
| MyBatisのSQLで不等号の比較演算子を使う | 22 |
| 表で対策するAWS 認定ソリューションアーキテクト - アソシエイト(SAA) ※ 随時更新 | 20 |
| JavaプログラマがPythonを勉強してみた。(型について） | 19 |
| AWS認定ソリューションアーキテクトアソシエイトを合格するまで更新するのをやめないッ！ | 19 |
| AWS認定ソリューションアーキテクトアソシエイト(SAA)不合格体験記 | 18 |
| ログインできないユーザでコマンドを実行する方法＋おまけ | 17 |
| 条件式が複数ある三項演算子に混乱した話 | 17 |
| [初心者]AWSを月数百円くらいの範囲で使っていると思ったら、2000円くらい請求された話 | 15 |
| EclipseからIntelliJ IDEAに移行する人のためのショートカット比較(Windows) | 15 |
| Javaでファイルをバイト配列に変換する方法 | 15 |
| 【Unity】Standard AssetsがImport Packageに表示されていないときの対処方法 | 14 |
| git revertの基本的な使い方 | 14 |
| (Java7以降限定)オブジェクトはObjects.equalsで比較してほしい | 12 |
| 【Unity】Unity-Chan!（ユニティちゃん）でCS0234エラーが発生したときの調査結果と解決方法 | 9 |
| 下位10%のダメなエンジニアにだけ解けないパズルを解いた結果、下位10%のダメなエンジニアだと判明した | 9 |
| Windows10のノートPC内蔵キーボードはJIS配列、Bluetooth接続のキーボードはUS配列にする設定方法 | 9 |
| JavaプログラマがPythonを勉強してみた。(for, if, while文) | 9 |
| 【Java】 (list == null  list.size() == 0)でNULL／空チェックしている事が気に入らない | 8 |
| [MyBatis]大量データをマッピングするときはCursorを使おう | 8 |
| [Java] ファイル書き込みは何を使えばいいのか | 7 |
| JavaプログラマがPythonを勉強してみた。(関数(メソッド)について） | 7 |
| SimpleDateFormatとDateTimeFormatterの違いってなんだ？？ | 7 |
| Javaで英数記号・ひらがな・カタカナ・JIS第一／第二水準漢字以外をエラーにするチェック処理を実装してみた | 6 |
| 【VSCode】言語ごとにインデント幅、タブとスペースどちらを使うか設定する | 5 |
| 【Unity】git addしたときのopen("Temp/UnityLockfile"): Permission deniedの原因と対処方法 | 5 |
| 【Java】StringBuilderの末尾から指定した文字数分を削除する | 5 |
| [Java 8]コーディングテストで使える標準入力をリストまたは配列に変換するまで | 5 |
| [Java 8]コーディングテストで使えるアルファベット順、文字列長順のソート方法 | 5 |
| Oracle SQL(11g)でMySQLのLIMIT OFFSET句を再現したい | 5 |
| 【Unity】プロジェクトをOculus Go用にビルドするまでに個人的に詰まったところまとめ | 4 |
| 【Unity】Windows 10で起動時に応答なしになるとき | 4 |
| 特定のファイルをrmコマンドなどで削除できないようにする方法(chattr、lsattrコマンド) | 4 |
| 特定のポート番号を使用しているプロセスの見つけ方 | 4 |
| 【Unity】非同期処理を理解する〜コルーチン編〜 | 3 |
| 【Unity】Application.LoadLevelは非推奨になっていました | 3 |
| Unity + Visual Studio CommunityでC#をデバッグ実行する | 3 |
| Oculus RiftはSurface Book 2で動かせないから気をつけて！ | 3 |
| .bash_profileの設定を間違えて、どんなコマンドも"command not found"になってしまったときの解決方法 | 3 |
| JavaプログラマがPythonを勉強してみた。(デコレータについて） | 3 |
| 【Git】fatal: protocol error: bad line length character: usag の解消方法 | 2 |
| 【Ruby】Ruby初心者がよく使うと思う配列のメソッド | 2 |
| 【Ruby】コーディングテストで使える？標準入力から値を受け取る方法 | 2 |
| AWS Innovate Online Conference 「試験対策セッション5：運用上の優秀性（オペレーショナル・エクセレンス）を備えたアーキテクチャを定義する」をまとめてみた | 2 |
| AWS Innovate Online Conference 「試験対策セッション4：コスト最適化アーキテクチャを設計する」をまとめてみた | 2 |
| AWS Innovate Online Conference 「試験対策セッション1：回復性の高いアーキテクチャを設計する」をまとめてみた | 2 |
| [Python] Qiita APIを使って投稿一覧を取得する + 2018年の振り返り | 2 |
| 下位20%のダメなエンジニアにだけ解けないパズルを解いた | 2 |
| [Java]過去の自分が作成した機能をjava.io.FileからNIO.2で書き直し | 2 |
| Oracle SQLでDB接続中のセッションを特定＆強制終了(KILL) | 2 |
| Aurora(MySQL)でCREATE VIEWしたらエラーが出た | 2 |
| 【Unity】コンポーネントの有効化/無効化をボタン押下で切り替える | 1 |
| 【Ruby】二次元配列の宣言を間違えて、要素の変更が想定通りにできなかった原因と反省 | 1 |
| 【Unity】Unity Editorかスマホ実機か判別して処理を分ける | 1 |
| 【Unity】UnityEditor.BuildPlayerWindow+BuildMethodExceptionが発生してAndroidビルドできないときの対処方法 | 1 |
| AWS Innovate Online Conference 「試験対策セッション3：セキュアなアプリケーションおよびアーキテクチャを規定する」をまとめてみた | 1 |
| AWS Innovate Online Conference 「試験対策セッション2：パフォーマンスに優れたアーキテクチャを定義する」をまとめてみた | 1 |
| ほとんどのエンジニアには解けるパズル３を解けませんでした | 1 |
| [Unity]"Can't add script behavior XXXX.The script needs to derive from MonoBehaviour"の改善方法4つ | 1 |
| 【Unity】非同期処理を理解する〜async/await編〜 | 0 |
| 【Unity】Unity Hub から Unity インストールするときに「不完全または破損したダウンロードファイル」と出たときの対処方法 | 0 |
| 時間がない人のためのスクラム開発用語集 | 0 |
| 【Slack】Slack API を使用してメッセージを飛ばすまでの手順 | 0 |
| 【Katalon Studio】ダークテーマ（黒背景）にする方法 | 0 |
| 【Katalon Studio】デフォルトのブラウザを変更する方法 | 0 |
| THETA Web API v2.1 を curl コマンドで実行する方法 | 0 |
| ChromeでAWS Cloud9に接続できないときの対処方法 | 0 |
| 【Oracle】テーブルのカラム情報をSQLで取得する方法 | 0 |

# 終わりに

だいたい気合を入れて書いた記事は LGTM 貰えないのに、雑に書いた記事のほうが LGTM 貰えるのはなぜなんでしょうかね？
