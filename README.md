# aws-elastic

S3へファイルをアップロードしたときににイベントを発行して、lambdaで処理してElasticsearchへデータを格納する。

```
S3 --> Lambda --> ElasticSearch 
```

## ElasticSerachでの設定

タイムスタンプの形式: `YYYY-MM-dd HH:mm:ss`

## Lambdaへのデプロイ

```
cd work
pip install requests -t .
pip install requests_aws4auth -t .
zip -r ../lambda.zip .
```

## TODO

- timestampの設定を行う
- geoipプラグインを使ったマッピング
- X-Packによるトリガーイベント発行

