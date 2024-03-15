# Mapbox

- 99.9% Chat GPT が出力した Python スクリプト

- Mapbox API を利用して地図を生成する

- Chat GPT に渡したプロンプト

```bash
<instruction>
あなたは地図検索&表示シミュレーターです。
1.推定する地点の入力: 推定したい地点の名称を入力してください。例えば、「東京スカイツリー」などです。

2.最も近い地点の検索: 入力された地点名に対して、最も近い地点を検索します。検索方法については、いくつかの方法があります。たとえば、OpenStreetMapを使用して地点を検索することができます。

3.推定された緯度経度の確認: 検索された地点の緯度経度が正しいかどうかを確認します。誤った場合は、正しい緯度経度を手動で入力することができます。
地図のスタイルを選択する: 地図のスタイルを選択してください。例えば、「light-v10」、「dark-v10」、「outdoors-v11」、「satellite-streets-v11」などがあります。

4.地図のプレビューを生成する: 入力された緯度経度とスタイルに基づいて、Mapboxで地図を生成し、エンコードされたURLを作成します。その後、地図のプレビューを生成し、イメージリンクとソース引用を提供します。下記の形式で表示されます。

YOUR_ACCESS_TOKEN =“---you should put your access token here --”

<output>
![Title of Image](link of image) [Source](link of source)
```

- 初めに Chat GPT が生成したコードはエラーが出たのでエラメッセージと共にエラーが出るよ、と投げたら修正コードを提示してくれた

- 修正コードもそのままでは動かず ``generate_map_preview()`` の URL 生成時に ``{latitude}`` と ``{longitude}`` の順序を手動で入れ替えたら動いた

- Chat GPT すごい

## Usage

- コマンド実行前に ``mapbox.py`` の ``YOUR_MAPBOX_ACCESS_TOKEN`` を自分のアクセストークンで書き換える

- トークンはこちら（[Mapbox - Account]([Account | Mapbox](https://account.mapbox.com/access-tokens/))）から取得

- API 使用料は月間 50,000 アクセスまでは無料なので個人利用なら実質無料

```bash
$ python mapbox.py
```

## Environment

- python 3.x

- ``requests`` パッケージが必要

- もし ``import requests`` でエラーが出たら以下のコマンドでインストールできる

```bash
$ pip install requests
```

- 
