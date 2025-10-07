from fastapi.testclient import TestClient
from datetime import datetime
import pytest
from src.main import app

client = TestClient(app)


def test_get_current_datetime():
    """現在の日時を返すAPIのテスト"""
    response = client.get("/datetime")
    
    # ステータスコードが200であることを確認
    assert response.status_code == 200
    
    # レスポンスがJSONであることを確認
    data = response.json()
    
    # 必要なキーが含まれていることを確認
    assert "datetime" in data
    assert "timestamp" in data
    
    # datetimeがISO形式の文字列であることを確認
    assert isinstance(data["datetime"], str)
    # ISO形式として解析できることを確認
    parsed_datetime = datetime.fromisoformat(data["datetime"])
    assert isinstance(parsed_datetime, datetime)
    
    # timestampが数値であることを確認
    assert isinstance(data["timestamp"], (int, float))
    
    # timestampが現在時刻に近いことを確認（5秒以内）
    current_timestamp = datetime.now().timestamp()
    assert abs(data["timestamp"] - current_timestamp) < 5


def test_datetime_response_format():
    """日時レスポンスのフォーマットをテスト"""
    response = client.get("/datetime")
    data = response.json()
    
    # datetimeフィールドにTが含まれていることを確認（ISO 8601形式）
    assert "T" in data["datetime"]
