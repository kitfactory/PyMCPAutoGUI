# PyMCPAutoGUI 🖱️⌨️🖼️ - GUI Automation via MCP

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Supercharge your AI Agent's capabilities!** ✨ PyMCPAutoGUI provides a bridge between your AI agents (like those in Cursor or other MCP-compatible environments) and your computer's graphical user interface (GUI). It allows your agent to see the screen 👁️, control the mouse 🖱️ and keyboard ⌨️, and interact with windows 🪟, just like a human user!

Stop tedious manual GUI tasks and let your AI do the heavy lifting 💪. Perfect for automating repetitive actions, testing GUIs, or building powerful AI assistants 🤖.

## 🤔 Why Choose PyMCPAutoGUI?

*   **🤖 Empower Your Agents:** Give your AI agents the power to interact directly with desktop applications.
*   **✅ Simple Integration:** Works seamlessly with MCP-compatible clients like the Cursor editor. It's plug and play!
*   **🚀 Easy to Use:** Get started with a simple server command. Seriously, it's *that* easy.
*   **🖱️⌨️ Comprehensive Control:** Offers a wide range of GUI automation functions from the battle-tested [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) and [PyGetWindow](https://pygetwindow.readthedocs.io/en/latest/).
*   **🖼️ Screen Perception:** Includes tools for taking screenshots and locating images on the screen – let your agent *see*!
*   **🪟 Window Management:** Control window position, size, state (minimize, maximize), and more. Tidy up that desktop!
*   **💬 User Interaction:** Display alert, confirmation, and prompt boxes to communicate with the user.

## 🛠️ Supported Environments

*   **Operating Systems:** Windows, macOS, Linux (Requires appropriate dependencies for `pyautogui` on each OS)
*   **Python:** 3.11+ 🐍
*   **MCP Clients:** Cursor Editor, any client supporting the [Model Context Protocol (MCP)](https://microsoft.github.io/language-server-protocol/specifications/mcp/)

## 🚀 Getting Started - It's Super Easy!

### 1. Installation (Recommended: Use a Virtual Environment!)

Using a virtual environment keeps your project dependencies tidy.

```bash
# Create and activate a virtual environment (example using venv)
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS / Linux bash
source .venv/bin/activate

# Install using pip (from PyPI or local source)
# Make sure your virtual environment is active!
pip install pymcpautogui # Or pip install . if installing from local source
```

*(Note: `pyautogui` might have system dependencies like `scrot` on Linux for screenshots. Please check the `pyautogui` documentation for OS-specific installation requirements.)*

### 2. Running the MCP Server

Once installed, simply run the server from your terminal:

```bash
# Make sure your virtual environment is activated!
python -m pymcpautogui.server
```

The server will start and listen for connections (defaulting to port 6789). Look for this output:

```
INFO:     Started server process [XXXXX]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:6789 (Press CTRL+C to quit)
```

Keep this terminal running while you need the GUI automation magic! ✨

## ✨ Seamless Integration with Cursor Editor

Connect PyMCPAutoGUI to Cursor (@ symbol) for GUI automation directly within your coding workflow.

1.  **Open MCP Configuration:** In Cursor, use the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) and find "MCP: Open mcp.json configuration file".
2.  **Add PyMCPAutoGUI Config:** Add or merge this configuration into your `mcp.json`. Adjust paths if needed (especially if Cursor isn't running from the project root).

    ```json
    {
        "mcpServers": {
            // ... other MCP server configs if any ...
            "PyMCPAutoGUI": {
                // Sets the working directory. ${workspaceFolder} is usually correct.
                "cwd": "${workspaceFolder}",

                // Command to run Python. 'python' works if the venv is active in the terminal
                // where Cursor was launched, or specify the full path.
                "command": "python", // Or ".venv/Scripts/python.exe" (Win) or ".venv/bin/python" (Mac/Linux)

                // Arguments to start the server module.
                "args": ["-m", "pymcpautogui.server"]
            }
            // ... other MCP server configs if any ...
        }
    }
    ```
    *(Tip: If `mcp.json` already exists, just add the `"PyMCPAutoGUI": { ... }` part inside the `mcpServers` object.)*

3.  **Save `mcp.json`**. Cursor will detect the server.
4.  **Automate!** Use `@PyMCPAutoGUI` in Cursor chats:

    *Example:*
    `@PyMCPAutoGUI move_to(x=100, y=200)`
    `@PyMCPAutoGUI write(text='Automating with AI! 🎉', interval=0.1)`
    `@PyMCPAutoGUI screenshot(filename='current_screen.png')`
    `@PyMCPAutoGUI activate_window(title='Notepad')`

## 🧰 Available Tools

PyMCPAutoGUI exposes most functions from `pyautogui` and `pygetwindow`. Examples include:

*   **Mouse 🖱️:** `move_to`, `click`, `move_rel`, `drag_to`, `drag_rel`, `scroll`, `mouse_down`, `mouse_up`, `get_position`
*   **Keyboard ⌨️:** `write`, `press`, `key_down`, `key_up`, `hotkey`
*   **Screenshots 🖼️:** `screenshot`, `locate_on_screen`, `locate_center_on_screen`
*   **Windows 🪟:** `get_all_titles`, `get_windows_with_title`, `get_active_window`, `activate_window`, `minimize_window`, `maximize_window`, `restore_window`, `move_window`, `resize_window`, `close_window`
*   **Dialogs 💬:** `alert`, `confirm`, `prompt`, `password`
*   **Config ⚙️:** `set_pause`, `set_failsafe`

For the full list and details, check the `pymcpautogui/server.py` file or use `@PyMCPAutoGUI list_tools` in your MCP client.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. Happy Automating! 😄
