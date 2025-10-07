# repo12

FastAPIを使用して現在の日時を返すAPIアプリケーション

## セットアップ

```bash
pip install -r requirements.txt
```

## サーバーの起動

```bash
uvicorn main:app --reload
```

## APIエンドポイント

### GET /datetime

現在の日時を返します。

**レスポンス例:**
```json
{
    "datetime": "2025-10-07T09:00:00.000000",
    "timestamp": 1759827600.0
}
```

## テストの実行

```bash
pytest test_main.py -v
```