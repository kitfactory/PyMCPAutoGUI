# English: Import the FastMCP class from the mcp.server.fastmcp module.
# Japanese: mcp.server.fastmcp モジュールから FastMCP クラスをインポートします。
from mcp.server.fastmcp import FastMCP

# English: Create a FastMCP server instance named "Echo Server".
# Japanese: "Echo Server" という名前の FastMCP サーバーインスタンスを作成します。
mcp = FastMCP("Demo")

# English: Define a tool named 'echo'.
# Japanese: 'echo' という名前のツールを定義します。
# English: This tool takes a string 'text' as input and returns the same string.
# Japanese: このツールは文字列 'text' を入力として受け取り、同じ文字列を返します。
@mcp.tool()
def echo(text: str) -> str:
    # English: Echo the input text.
    # Japanese: 入力されたテキストをエコーします。
    """Echo the input text"""
    return text

# Add an addition tool
# 加算ツールを追加する
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers
    二つの数を加算する
    """
    return a + b

# Add a dynamic greeting resource
# 動的な挨拶リソースを追加する
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting
    パーソナライズされた挨拶を取得する
    """
    return f"Hello, {name}!" 