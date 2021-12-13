# sync_postgresql_fastapi

FastAPI + SQLAlchemy 同期処理

# API 一覧確認

http://localhost:8000/docs

# 事前準備

## docker 起動

```
docker-compose run --entrypoint "poetry install" demo-app
docker-compose up

```

## マイグレーション実行

```
docker-compose exec demo-app poetry run python -m api.migrate_db
```

## db 確認

1. db の docker コンテナに接続

```
docker container exec -it sync_postgresql_fastapi_db_1 bash
```

2. postgresql にログイン

```
psql -h localhost -p 5432 -U admin -d sync_db
```

3. postgresql のテーブル一覧表示

```
\d
```

# CRUD 動作確認

vscode に REST Client が入っている場合、crud.http ファイルから動作確認可能
