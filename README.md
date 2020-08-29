### コンテナデプロイ

```bash
$ heroku login
$ heroku container:login
$ heroku container:push web -a [Herokuアプリ名]
$ heroku container:release web -a [Herokuアプリ名]
```

### コンテナ削除

```bash
$ heroku container:rm web -a [Herokuアプリ名]
```
