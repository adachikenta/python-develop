"""単体テスト"""
import sys
import os
import pytest

# プロジェクトルートをパスに追加
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import greet, calculate_sum


class TestGreet:
    """greet関数のテスト"""

    def test_greet_default(self):
        """デフォルト引数でのテスト"""
        result = greet()
        print(f"\n実行結果: {result}")
        assert result == "Hello, World!"

    def test_greet_with_name(self):
        """名前を指定したテスト"""
        result1 = greet("Python")
        result2 = greet("Test")
        print(f"\n実行結果1: {result1}")
        print(f"実行結果2: {result2}")
        assert result1 == "Hello, Python!"
        assert result2 == "Hello, Test!"


class TestCalculateSum:
    """calculate_sum関数のテスト"""

    def test_positive_numbers(self):
        """正の数の加算"""
        assert calculate_sum(10, 20) == 30
        assert calculate_sum(5, 15) == 20

    def test_negative_numbers(self):
        """負の数の加算"""
        assert calculate_sum(-10, -20) == -30
        assert calculate_sum(-5, 10) == 5

    def test_zero(self):
        """ゼロを含む加算"""
        assert calculate_sum(0, 0) == 0
        assert calculate_sum(10, 0) == 10
