---
title: git revertの基本的な使い方
tags:
  - Git
private: false
updated_at: '2018-11-09T22:23:23+09:00'
id: 05b547c102701feb8222
organization_url_name: null
slide: false
ignorePublish: false
---
# revertコマンドとは

すでにpushされているcommitを打ち消す(もとに戻す)コマンドの事。
取り消したいコミットを打ち消すようなコミットを新しく作成する。

# 使い方

1回revertするたびに自動的にcommitされる。
実行したときに、コミットメッセージを編集するためのエディタが起動する。

```
$ git revert <commit ID>
```
※ ```<commit ID>``` には、commitのハッシュ値を指定する。git logを叩くと出力される値。

## commitせずにrevert

commitしない方法は、-nを指定する。
複数のcommitを戻して、1つのcommitとしてpushする場合に便利。

```
$ git revert <commit ID> -n
```


## コミットメッセージを編集しない場合

コミットメッセージを編集しなくていいときは `--no-edit` を使用する。

```
$ git revert --no-edit <commit ID>
```

その場合は、

```
This reverts commit <commit ID>.
```
というようなメッセージが設定されてcommitされる。

# 雑感

めったに使用することはないので、毎回忘れてしまうのでメモ書き。

