# PyMCPAutoGUI 🖱️⌨️🖼️ - GUI Automation via MCP

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Supercharge your AI Agent's capabilities!** ✨ PyMCPAutoGUI provides a bridge between your AI agents (like those in Cursor or other MCP-compatible environments) and your computer's graphical user interface (GUI). It allows your agent to see the screen, control the mouse and keyboard, and interact with windows, just like a human user!

Stop tedious manual GUI tasks and let your AI do the heavy lifting. Perfect for automating repetitive actions, testing GUIs, or building powerful AI assistants.

## 🤔 Why PyMCPAutoGUI?

*   **🤖 Empower Your Agents:** Give your AI agents the ability to interact directly with desktop applications.
*   **✅ Simple Integration:** Works seamlessly with MCP-compatible clients like the Cursor editor.
*   **🚀 Easy to Use:** Start the server with a simple command.
*   **🖱️⌨️ Comprehensive Control:** Offers a wide range of GUI automation functions from [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) and [PyGetWindow](https://pygetwindow.readthedocs.io/en/latest/).
*   **🖼️ Screen Perception:** Includes tools for taking screenshots and locating images on the screen.
*   **🪟 Window Management:** Control window position, size, state (minimize, maximize), and more.
*   **💬 User Interaction:** Display alert, confirmation, and prompt boxes.

## 🛠️ Supported Environments

*   **Operating Systems:** Windows, macOS, Linux (Requires appropriate dependencies for `pyautogui` on each OS)
*   **Python:** 3.11+
*   **MCP Clients:** Cursor Editor, any client supporting the [Model Context Protocol (MCP)](https://microsoft.github.io/language-server-protocol/specifications/mcp/)

## 🚀 Getting Started

### 1. Installation

It's recommended to install PyMCPAutoGUI in a dedicated virtual environment.

```bash
# Create and activate a virtual environment (example using venv)
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS / Linux bash
source .venv/bin/activate

# Install using pip (assuming the package is published on PyPI)
# Or install directly from the source directory if developing
pip install pymcpautogui # Or pip install .
```

*(Note: `pyautogui` might have system dependencies like `scrot` on Linux for screenshots. Please refer to the `pyautogui` documentation for OS-specific installation requirements.)*

### 2. Running the MCP Server

Once installed, you can run the PyMCPAutoGUI server from your terminal:

```bash
# Make sure your virtual environment is activated
python -m pymcpautogui.server
```

The server will start and listen for incoming MCP connections (defaulting to port 6789). You should see output indicating the server is running.

```
INFO:     Started server process [XXXXX]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:6789 (Press CTRL+C to quit)
```

Keep this terminal window open while you want the server to be available.

## ✨ Integration with Cursor Editor

You can easily connect PyMCPAutoGUI to the Cursor editor (@ symbol) for seamless GUI automation within your coding workflow.

1.  **Open Cursor Settings:** Go to `File > Preferences > Settings` (or `Ctrl+,`).
2.  **Search for MCP:** Search for "MCP".
3.  **Edit `settings.json`:** Find the `cursor.mcpConfigs` setting and click "Edit in settings.json".
4.  **Add PyMCPAutoGUI Configuration:** Add the following configuration to your `settings.json` file within the `cursor.mcpConfigs` object. Adapt the `cwd` and `command` paths if necessary (e.g., if not running Cursor from the project root or using a different Python path).

    ```json
    {
        // ... other settings ...
        "cursor.mcpConfigs": {
            // ... other MCP server configs ...
            "PyMCPAutoGUI": {
                // English: Set the working directory. Use ${workspaceFolder} if running Cursor from the project root,
                // or specify the directory where 'pymcpautogui' is installed if running globally.
                // Japanese: 作業ディレクトリを設定します。プロジェクトルートからCursorを実行する場合は ${workspaceFolder} を使用し、
                // グローバルに実行する場合は 'pymcpautogui' がインストールされているディレクトリを指定します。
                "cwd": "${workspaceFolder}", // Or path to site-packages or installation directory

                // English: Command to run the server. Use 'python' if it's in PATH and the correct venv is active,
                // or specify the full path to the Python executable in the virtual environment.
                // Japanese: サーバーを実行するコマンド。PATH にあり、正しい仮想環境がアクティブな場合は 'python' を使用し、
                // そうでない場合は仮想環境内の Python 実行可能ファイルへのフルパスを指定します。
                "command": "python", // Or ".venv\\Scripts\\python.exe" or full path

                // English: Arguments to run the server module.
                // Japanese: サーバーモジュールを実行するための引数。
                "args": ["-m", "pymcpautogui.server"]
            }
            // ... other MCP server configs ...
        },
        // ... other settings ...
    }
    ```

5.  **Save `settings.json`**.
6.  **Use in Cursor:** Now you can invoke the PyMCPAutoGUI tools directly in Cursor using the `@PyMCPAutoGUI` handle!

    *Example:*
    `@PyMCPAutoGUI move_to(x=100, y=200)`
    `@PyMCPAutoGUI write(text='Hello from Cursor!', interval=0.1)`
    `@PyMCPAutoGUI screenshot(filename='screenshot.png')`
    `@PyMCPAutoGUI activate_window(title='Calculator')`

## 🛠️ Available Tools

PyMCPAutoGUI exposes most functions from `pyautogui` and `pygetwindow` as MCP tools. Here are some examples:

*   **Mouse:** `move_to`, `click`, `move_rel`, `drag_to`, `drag_rel`, `scroll`, `mouse_down`, `mouse_up`, `get_position`
*   **Keyboard:** `write`, `press`, `key_down`, `key_up`, `hotkey`
*   **Screenshots:** `screenshot`, `locate_on_screen`, `locate_center_on_screen`
*   **Windows:** `get_all_titles`, `get_windows_with_title`, `get_active_window`, `activate_window`, `minimize_window`, `maximize_window`, `restore_window`, `move_window`, `resize_window`, `close_window`
*   **Dialogs:** `alert`, `confirm`, `prompt`, `password`
*   **Config:** `set_pause`, `set_failsafe`

Refer to the `src/pymcpautogui/server.py` file or use `@PyMCPAutoGUI list_tools` (if supported by the client) for a full list and function signatures.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
