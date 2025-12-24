"""Application"""

def greet(name="World"):
    """挨拶メッセージを返す"""
    return f"Hello, {name}!"

def calculate_sum(a, b):
    """2つの数値の合計を返す"""
    return a + b

###################################################
# アプリケーション起動
###################################################
if __name__ == "__main__":
    print(greet())
    print(f"Sum: {calculate_sum(10, 20)}")
