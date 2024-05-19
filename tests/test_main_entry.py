# tests/test_main_entry.py

import pytest
from unittest import mock

def test_main_entry():
    with mock.patch("uvicorn.run") as mock_run:
        from src.main import start
        start()
        mock_run.assert_called_once_with("src.main:app", host="127.0.0.1", port=8000)

if __name__ == "__main__":
    pytest.main()
