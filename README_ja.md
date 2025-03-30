# PyMCPAutoGUI 🖱️⌨️🖼️ - MCP経由でのGUIオートメーション

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**あなたのAIエージェントの能力を強化しましょう！** ✨ PyMCPAutoGUI は、AI エージェント（Cursor や他の MCP 互換環境のエージェントなど）とコンピューターのグラフィカルユーザーインターフェース（GUI）との間の架け橋を提供します。これにより、エージェントは人間のように画面を見たり、マウスやキーボードを操作したり、ウィンドウと対話したりできるようになります！

退屈な手動 GUI タスクをやめて、AI に面倒な作業を任せましょう。反復的なアクションの自動化、GUI のテスト、強力な AI アシスタントの構築に最適です。

## 🤔 なぜ PyMCPAutoGUI？

*   **🤖 エージェントの強化:** AI エージェントにデスクトップアプリケーションと直接対話する能力を与えます。
*   **✅ 簡単な統合:** Cursor エディタのような MCP 互換クライアントとシームレスに連携します。
*   **🚀 使いやすい:** 簡単なコマンドでサーバーを起動できます。
*   **🖱️⌨️ 包括的な制御:** [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) と [PyGetWindow](https://pygetwindow.readthedocs.io/en/latest/) の幅広い GUI 自動化機能を提供します。
*   **🖼️ 画面認識:** スクリーンショットの撮影や画面上の画像の特定のためのツールが含まれています。
*   **🪟 ウィンドウ管理:** ウィンドウの位置、サイズ、状態（最小化、最大化など）を制御します。
*   **💬 ユーザーインタラクション:** アラート、確認、プロンプトボックスを表示します。

## 🛠️ サポート環境

*   **オペレーティングシステム:** Windows, macOS, Linux (各 OS で `pyautogui` の適切な依存関係が必要です)
*   **Python:** 3.11+
*   **MCP クライアント:** Cursor Editor、その他 [Model Context Protocol (MCP)](https://microsoft.github.io/language-server-protocol/specifications/mcp/) をサポートするクライアント

## 🚀 はじめに

### 1. インストール

PyMCPAutoGUI は専用の仮想環境にインストールすることをお勧めします。

```bash
# 仮想環境の作成と有効化 (venv を使用した例)
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS / Linux bash
source .venv/bin/activate

# pip を使用したインストール (PyPI で公開されている場合)
# または開発中の場合はソースディレクトリから直接インストール
pip install pymcpautogui # または pip install .
```

*注意: `pyautogui` は、スクリーンショット用に Linux の `scrot` のようなシステム依存関係を持つ場合があります。OS 固有のインストール要件については、`pyautogui` のドキュメントを参照してください。*

### 2. MCP サーバーの実行

インストール後、ターミナルから PyMCPAutoGUI サーバーを実行できます:

```bash
# 仮想環境が有効化されていることを確認してください
python -m pymcpautogui.server
```

サーバーが起動し、MCP 接続を待ち受けます（デフォルトはポート 6789）。サーバーが実行中であることを示す出力が表示されるはずです。

```
INFO:     Started server process [XXXXX]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:6789 (Press CTRL+C to quit)
```

サーバーを利用可能にしておきたい間は、このターミナルウィンドウを開いたままにしておきます。

## ✨ Cursor Editor との連携

PyMCPAutoGUI を Cursor エディタ（@ シンボル）に簡単に接続して、コーディングワークフロー内でシームレスな GUI 自動化を実現できます。

1.  **Cursor 設定を開く:** `File > Preferences > Settings` (または `Ctrl+,`) に移動します。
2.  **MCP を検索:** "MCP" を検索します。
3.  **`settings.json` を編集:** `cursor.mcpConfigs` 設定を見つけ、「Edit in settings.json」をクリックします。
4.  **PyMCPAutoGUI 設定を追加:** `settings.json` ファイル内の `cursor.mcpConfigs` オブジェクトに以下の設定を追加します。必要に応じて `cwd` と `command` のパスを調整してください（例: Cursor をプロジェクトルートから実行していない場合や、異なる Python パスを使用している場合）。

    ```json
    {
        // ... その他の設定 ...
        "cursor.mcpConfigs": {
            // ... 他の MCP サーバー設定 ...
            "PyMCPAutoGUI": {
                // 作業ディレクトリを設定します。プロジェクトルートからCursorを実行する場合は ${workspaceFolder} を使用し、
                // グローバルに実行する場合は 'pymcpautogui' がインストールされているディレクトリを指定します。
                "cwd": "${workspaceFolder}", // または site-packages やインストールディレクトリへのパス

                // サーバーを実行するコマンド。PATH にあり、正しい仮想環境がアクティブな場合は 'python' を使用し、
                // そうでない場合は仮想環境内の Python 実行可能ファイルへのフルパスを指定します。
                "command": "python", // または ".venv\\Scripts\\python.exe" やフルパス

                // サーバーモジュールを実行するための引数。
                "args": ["-m", "pymcpautogui.server"]
            }
            // ... 他の MCP サーバー設定 ...
        },
        // ... その他の設定 ...
    }
    ```

5.  **`settings.json` を保存します**。
6.  **Cursor で使用:** これで `@PyMCPAutoGUI` ハンドルを使用して Cursor で直接 PyMCPAutoGUI ツールを呼び出すことができます！

    *例:*
    `@PyMCPAutoGUI move_to(x=100, y=200)`
    `@PyMCPAutoGUI write(text='カーソルからこんにちは！', interval=0.1)`
    `@PyMCPAutoGUI screenshot(filename='screenshot.png')`
    `@PyMCPAutoGUI activate_window(title='電卓')`

## 🛠️ 利用可能なツール

PyMCPAutoGUI は `pyautogui` と `pygetwindow` のほとんどの機能を MCP ツールとして公開しています。以下に例を示します:

*   **マウス:** `move_to`, `click`, `move_rel`, `drag_to`, `drag_rel`, `scroll`, `mouse_down`, `mouse_up`, `get_position`
*   **キーボード:** `write`, `press`, `key_down`, `key_up`, `hotkey`
*   **スクリーンショット:** `screenshot`, `locate_on_screen`, `locate_center_on_screen`
*   **ウィンドウ:** `get_all_titles`, `get_windows_with_title`, `get_active_window`, `activate_window`, `minimize_window`, `maximize_window`, `restore_window`, `move_window`, `resize_window`, `close_window`
*   **ダイアログ:** `alert`, `confirm`, `prompt`, `password`
*   **設定:** `set_pause`, `set_failsafe`

完全なリストと関数のシグネチャについては、`src/pymcpautogui/server.py` ファイルを参照するか、`@PyMCPAutoGUI list_tools` (クライアントがサポートしている場合) を使用してください。

## 📄 ライセンス

このプロジェクトは MIT ライセンスの下でライセンスされています - 詳細は [LICENSE](LICENSE) ファイルをご覧ください。 