# PyMCPAutoGUI 🖱️⌨️🖼️ - MCP経由でのGUIオートメーション

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**AIエージェントの能力を最大限に引き出しましょう！** ✨ PyMCPAutoGUIは、AIエージェント（Cursorや他のMCP互換環境のエージェントなど）とコンピュータのグラフィカルユーザーインターフェース（GUI）との間の架け橋を提供します。これにより、エージェントはまるで人間のユーザーのように、画面を見たり👁️、マウス🖱️やキーボード⌨️を操作したり、ウィンドウ🪟と対話したりすることができます！

面倒な手作業によるGUIタスクをやめて、AIに力仕事を任せましょう💪。反復的なアクションの自動化、GUIのテスト、または強力なAIアシスタント🤖の構築に最適です。

## 🤔 なぜPyMCPAutoGUIを選ぶのか？

*   **🤖 エージェントを強化:** AIエージェントにデスクトップアプリケーションと直接対話する力を与えます。
*   **✅ 簡単な統合:** CursorエディタのようなMCP互換クライアントとシームレスに連携します。プラグアンドプレイです！
*   **🚀 使いやすさ:** 簡単なサーバーコマンドで始められます。本当に、*それくらい*簡単です。
*   **🖱️⌨️ 包括的な制御:** 実績のある[PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)と[PyGetWindow](https://pygetwindow.readthedocs.io/en/latest/)からの幅広いGUI自動化機能を提供します。
*   **🖼️ 画面認識:** スクリーンショットの取得や画面上の画像の特定など、エージェントが*見る*ためのツールが含まれています！
*   **🪟 ウィンドウ管理:** ウィンドウの位置、サイズ、状態（最小化、最大化など）を制御します。デスクトップを整理しましょう！
*   **💬 ユーザーインタラクション:** アラート、確認、プロンプトボックスを表示して、ユーザーとコミュニケーションをとります。

## 🛠️ サポートされている環境

*   **オペレーティングシステム:** Windows, macOS, Linux （各OSで`pyautogui`に必要な依存関係があります）
*   **Python:** 3.11+ 🐍
*   **MCPクライアント:** Cursor Editor、その他[Model Context Protocol (MCP)](https://microsoft.github.io/language-server-protocol/specifications/mcp/)をサポートするクライアント

## 🚀 始め方 - とても簡単です！

### 1. インストール (推奨：仮想環境を使用してください！)

仮想環境を使用すると、プロジェクトの依存関係が整理されます。

```bash
# 仮想環境を作成してアクティベートします (venvを使用する例)
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS / Linux bash
source .venv/bin/activate

# pipを使用してインストールします (PyPIまたはローカルソースから)
# 仮想環境がアクティブであることを確認してください！
pip install pymcpautogui # またはローカルソースからインストールする場合は pip install .
```

*(注意: `pyautogui`は、スクリーンショットのためにLinuxで`scrot`のようなシステム依存関係を持つ場合があります。OS固有のインストール要件については、`pyautogui`のドキュメントを参照してください。)*

### 2. MCPサーバーの実行

インストール後、ターミナルからサーバーを実行するだけです：

```bash
# 仮想環境がアクティブであることを確認してください！
python -m pymcpautogui.server
```

サーバーが起動し、接続を待ち受けます（デフォルトはポート6789）。以下の出力が表示されるはずです：

```
INFO:     Started server process [XXXXX]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:6789 (Press CTRL+C to quit)
```

GUIオートメーションの魔法が必要な間、このターミナルを開いたままにしておいてください！ ✨

## ✨ Cursor Editorとのシームレスな統合

PyMCPAutoGUIをCursor（@シンボル）に接続して、コーディングワークフロー内で直接GUIオートメーションを実現します。

1.  **MCP設定を開く:** Cursorで、コマンドパレット（`Ctrl+Shift+P`または`Cmd+Shift+P`）を使用し、「MCP: Open mcp.json configuration file」を検索します。
2.  **PyMCPAutoGUI設定を追加:** この設定を`mcp.json`に追加またはマージします。必要に応じてパスを調整してください（特にCursorをプロジェクトルートから実行していない場合）。

    ```json
    {
        "mcpServers": {
            // ... 他のMCPサーバー設定があれば ...
            "PyMCPAutoGUI": {
                // 作業ディレクトリを設定します。通常は ${workspaceFolder} で正しいです。
                "cwd": "${workspaceFolder}",

                // Pythonを実行するコマンド。Cursorを起動したターミナルでvenvがアクティブであれば 'python' で動作します。
                // そうでない場合はフルパスを指定します。
                "command": "python", // または ".venv/Scripts/python.exe" (Win) や ".venv/bin/python" (Mac/Linux)

                // サーバーモジュールを起動するための引数。
                "args": ["-m", "pymcpautogui.server"]
            }
            // ... 他のMCPサーバー設定があれば ...
        }
    }
    ```
    *(ヒント: `mcp.json`が既に存在する場合は、`mcpServers`オブジェクト内に`"PyMCPAutoGUI": { ... }`の部分を追加するだけです。)*

3.  **`mcp.json`を保存します**。Cursorはサーバーを検出します。
4.  **自動化！** Cursorチャットで`@PyMCPAutoGUI`を使用します：

    *例：*
    `@PyMCPAutoGUI move_to(x=100, y=200)`
    `@PyMCPAutoGUI write(text='AIで自動化！ 🎉', interval=0.1)`
    `@PyMCPAutoGUI screenshot(filename='current_screen.png')`
    `@PyMCPAutoGUI activate_window(title='メモ帳')`

## 🧰 利用可能なツール

PyMCPAutoGUIは、`pyautogui`と`pygetwindow`のほとんどの関数を公開しています。例：

*   **マウス 🖱️:** `move_to`, `click`, `move_rel`, `drag_to`, `drag_rel`, `scroll`, `mouse_down`, `mouse_up`, `get_position`
*   **キーボード ⌨️:** `write`, `press`, `key_down`, `key_up`, `hotkey`
*   **スクリーンショット 🖼️:** `screenshot`, `locate_on_screen`, `locate_center_on_screen`
*   **ウィンドウ 🪟:** `get_all_titles`, `get_windows_with_title`, `get_active_window`, `activate_window`, `minimize_window`, `maximize_window`, `restore_window`, `move_window`, `resize_window`, `close_window`
*   **ダイアログ 💬:** `alert`, `confirm`, `prompt`, `password`
*   **設定 ⚙️:** `set_pause`, `set_failsafe`

完全なリストと詳細については、`pymcpautogui/server.py`ファイルを確認するか、MCPクライアントで`@PyMCPAutoGUI list_tools`を使用してください。

## 📄 ライセンス

このプロジェクトはMITライセンスの下でライセンスされています - 詳細については[LICENSE](LICENSE)ファイルを参照してください。自動化を楽しんでください！ 😄 