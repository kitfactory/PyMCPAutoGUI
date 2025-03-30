# English: Import necessary libraries.
# Japanese: 必要なライブラリをインポートします。
import pyautogui
import pygetwindow as gw # Import pygetwindow
from mcp.server.fastmcp import FastMCP

# English: Create a FastMCP server instance named "PyMCPAutoGUI".
# Japanese: "PyMCPAutoGUI" という名前の FastMCP サーバーインスタンスを作成します。
mcp = FastMCP("PyMCPAutoGUI")

# --- Mouse Tools ---
# --- マウスツール ---

# English: Define a tool to move the mouse cursor to the specified coordinates.
# Japanese: マウスカーソルを指定された座標に移動するツールを定義します。
@mcp.tool()
def move_to(x: int, y: int) -> str:
    """Moves the mouse cursor to the specified X and Y coordinates.
    指定されたX座標とY座標にマウスカーソルを移動します。

    Args:
        x (int): The x-coordinate to move to. 移動先のX座標。
        y (int): The y-coordinate to move to. 移動先のY座標。

    Returns:
        str: A confirmation message. 確認メッセージ。
    """
    try:
        pyautogui.moveTo(x, y)
        return f"Mouse moved to ({x}, {y})."
    except Exception as e:
        return f"Error moving mouse: {e}"

# English: Define a tool to perform a mouse click.
# Japanese: マウスクリックを実行するツールを定義します。
@mcp.tool()
def click(x: int | None = None, y: int | None = None, button: str = 'left') -> str:
    """Performs a mouse click at the specified coordinates or current position.
    指定された座標または現在の位置でマウスクリックを実行します。

    Args:
        x (int | None): The x-coordinate to click at. If None, uses the current position. クリックするX座標。Noneの場合は現在の位置を使用します。
        y (int | None): The y-coordinate to click at. If None, uses the current position. クリックするY座標。Noneの場合は現在の位置を使用します。
        button (str): The mouse button to click ('left', 'middle', 'right'). デフォルトは 'left'。 クリックするマウスボタン ('left', 'middle', 'right')。 Defaults to 'left'.

    Returns:
        str: A confirmation message. 確認メッセージ。
    """
    try:
        pyautogui.click(x=x, y=y, button=button)
        location = f"({x}, {y})" if x is not None and y is not None else "current position"
        return f"{button.capitalize()} click performed at {location}."
    except Exception as e:
        return f"Error performing click: {e}"

# --- Keyboard Tools ---
# --- キーボードツール ---

# English: Define a tool to type a string.
# Japanese: 文字列を入力するツールを定義します。
@mcp.tool()
def write(text: str, interval: float = 0.0) -> str:
    """Types the given text string using the keyboard.
    指定されたテキスト文字列をキーボードで入力します。

    Args:
        text (str): The string to type. 入力する文字列。
        interval (float): The time in seconds to wait between each keypress. デフォルトは 0.0。 各キープレスの間の待機時間（秒）。 Defaults to 0.0.

    Returns:
        str: A confirmation message. 確認メッセージ。
    """
    try:
        pyautogui.write(text, interval=interval)
        return f"Typed: {text}"
    except Exception as e:
        return f"Error typing text: {e}"

# English: Define a tool to press a specific key.
# Japanese: 特定のキーを押すツールを定義します。
@mcp.tool()
def press(key: str) -> str:
    """Presses the specified keyboard key.
    指定されたキーボードのキーを押します。

    See pyautogui documentation for valid key strings.
    有効なキー文字列については、pyautoguiのドキュメントを参照してください。

    Args:
        key (str): The key to press (e.g., 'enter', 'esc', 'f1', 'a', 'ctrl'). 押すキー（例: 'enter', 'esc', 'f1', 'a', 'ctrl'）。

    Returns:
        str: A confirmation message. 確認メッセージ。
    """
    try:
        pyautogui.press(key)
        return f"Pressed key: {key}"
    except Exception as e:
        return f"Error pressing key: {e}"

# --- Additional Mouse Tools ---
# --- 追加のマウスツール ---

# English: Define a tool to move the mouse cursor relative to its current position.
# Japanese: 現在のマウス位置から相対的にカーソルを移動するツールを定義します。
@mcp.tool()
def move_rel(x_offset: int, y_offset: int, duration: float = 0.0) -> str:
    """Moves the mouse cursor relative to its current position.
    現在のマウス位置から相対的にカーソルを移動します。

    Args:
        x_offset (int): The horizontal offset to move. 水平方向の移動オフセット。
        y_offset (int): The vertical offset to move. 垂直方向の移動オフセット。
        duration (float): The time in seconds to spend moving the mouse. Defaults to 0.0. マウス移動にかける時間（秒）。デフォルトは 0.0。

    Returns:
        str: A confirmation message. 確認メッセージ。
    """
    try:
        pyautogui.moveRel(x_offset, y_offset, duration=duration)
        return f"Mouse moved relatively by ({x_offset}, {y_offset})."
    except Exception as e:
        return f"Error moving mouse relatively: {e}"

# English: Define a tool to drag the mouse cursor to the specified coordinates.
# Japanese: マウスカーソルを指定された座標までドラッグするツールを定義します。
@mcp.tool()
def drag_to(x: int, y: int, duration: float = 0.0, button: str = 'left') -> str:
    """Drags the mouse cursor to the specified X and Y coordinates.
    マウスカーソルを指定されたX座標とY座標までドラッグします。

    Args:
        x (int): The x-coordinate to drag to. ドラッグ先のX座標。
        y (int): The y-coordinate to drag to. ドラッグ先のY座標。
        duration (float): The time in seconds to spend dragging. Defaults to 0.0. ドラッグにかける時間（秒）。デフォルトは 0.0。
        button (str): The mouse button to drag with ('left', 'middle', 'right'). Defaults to 'left'. ドラッグに使用するマウスボタン ('left', 'middle', 'right')。デフォルトは 'left'。

    Returns:
        str: A confirmation message. 確認メッセージ。
    """
    try:
        pyautogui.dragTo(x, y, duration=duration, button=button)
        return f"Mouse dragged to ({x}, {y}) using {button} button."
    except Exception as e:
        return f"Error dragging mouse: {e}"

# English: Define a tool to drag the mouse cursor relative to its current position.
# Japanese: 現在のマウス位置から相対的にカーソルをドラッグするツールを定義します。
@mcp.tool()
def drag_rel(x_offset: int, y_offset: int, duration: float = 0.0, button: str = 'left') -> str:
    """Drags the mouse cursor relative to its current position.
    現在のマウス位置から相対的にカーソルをドラッグします。

    Args:
        x_offset (int): The horizontal offset to drag. 水平方向のドラッグオフセット。
        y_offset (int): The vertical offset to drag. 垂直方向のドラッグオフセット。
        duration (float): The time in seconds to spend dragging. Defaults to 0.0. ドラッグにかける時間（秒）。デフォルトは 0.0。
        button (str): The mouse button to drag with ('left', 'middle', 'right'). Defaults to 'left'. ドラッグに使用するマウスボタン ('left', 'middle', 'right')。デフォルトは 'left'。

    Returns:
        str: A confirmation message. 確認メッセージ。
    """
    try:
        pyautogui.dragRel(x_offset, y_offset, duration=duration, button=button)
        return f"Mouse dragged relatively by ({x_offset}, {y_offset}) using {button} button."
    except Exception as e:
        return f"Error dragging mouse relatively: {e}"

# English: Define a tool to scroll the mouse wheel.
# Japanese: マウスホイールをスクロールするツールを定義します。
@mcp.tool()
def scroll(amount: int, x: int | None = None, y: int | None = None) -> str:
    """Scrolls the mouse wheel up or down.
    マウスホイールを上下にスクロールします。

    Args:
        amount (int): The amount to scroll. Positive is up, negative is down. スクロール量。正の値は上、負の値は下。
        x (int | None): The x-coordinate to scroll at. If None, uses current mouse position. スクロールするX座標。Noneの場合は現在のマウス位置を使用。
        y (int | None): The y-coordinate to scroll at. If None, uses current mouse position. スクロールするY座標。Noneの場合は現在のマウス位置を使用。

    Returns:
        str: A confirmation message. 確認メッセージ。
    """
    try:
        pyautogui.scroll(amount, x=x, y=y)
        direction = "up" if amount > 0 else "down"
        location = f"at ({x}, {y})" if x is not None and y is not None else "at current position"
        return f"Scrolled {direction} by {abs(amount)} units {location}."
    except Exception as e:
        return f"Error scrolling: {e}"

# English: Define a tool to press and hold a mouse button down.
# Japanese: マウスボタンを押し下げたままにするツールを定義します。
@mcp.tool()
def mouse_down(x: int | None = None, y: int | None = None, button: str = 'left') -> str:
    """Presses and holds down the specified mouse button.
    指定されたマウスボタンを押し下げたままにします。

    Args:
        x (int | None): The x-coordinate to press down at. If None, uses current position. 押し下げるX座標。Noneの場合は現在の位置を使用。
        y (int | None): The y-coordinate to press down at. If None, uses current position. 押し下げるY座標。Noneの場合は現在の位置を使用。
        button (str): The mouse button to press down ('left', 'middle', 'right'). Defaults to 'left'. 押し下げるマウスボタン ('left', 'middle', 'right')。デフォルトは 'left'。

    Returns:
        str: A confirmation message. 確認メッセージ。
    """
    try:
        pyautogui.mouseDown(x=x, y=y, button=button)
        location = f"at ({x}, {y})" if x is not None and y is not None else "at current position"
        return f"{button.capitalize()} mouse button pressed down {location}."
    except Exception as e:
        return f"Error pressing mouse button down: {e}"

# English: Define a tool to release a mouse button.
# Japanese: マウスボタンを離すツールを定義します。
@mcp.tool()
def mouse_up(x: int | None = None, y: int | None = None, button: str = 'left') -> str:
    """Releases the specified mouse button.
    指定されたマウスボタンを離します。

    Args:
        x (int | None): The x-coordinate to release at. If None, uses current position. 離すX座標。Noneの場合は現在の位置を使用。
        y (int | None): The y-coordinate to release at. If None, uses current position. 離すY座標。Noneの場合は現在の位置を使用。
        button (str): The mouse button to release ('left', 'middle', 'right'). Defaults to 'left'. 離すマウスボタン ('left', 'middle', 'right')。デフォルトは 'left'。

    Returns:
        str: A confirmation message. 確認メッセージ。
    """
    try:
        pyautogui.mouseUp(x=x, y=y, button=button)
        location = f"at ({x}, {y})" if x is not None and y is not None else "at current position"
        return f"{button.capitalize()} mouse button released {location}."
    except Exception as e:
        return f"Error releasing mouse button: {e}"

# English: Define a tool to get the current mouse position.
# Japanese: 現在のマウスカーソル位置を取得するツールを定義します。
@mcp.tool()
def get_position() -> dict | str:
    """Gets the current X and Y coordinates of the mouse cursor.
    現在のマウスカーソルのX座標とY座標を取得します。

    Returns:
        dict | str: A dictionary {'x': x_pos, 'y': y_pos} with the coordinates, or an error message string. 座標を含む辞書 {'x': x_pos, 'y': y_pos}、またはエラーメッセージ文字列。
    """
    try:
        x, y = pyautogui.position()
        return {"x": x, "y": y}
    except Exception as e:
        return f"Error getting mouse position: {e}"


# --- Additional Keyboard Tools ---
# --- 追加のキーボードツール ---

# English: Define a tool to press and hold a key down.
# Japanese: キーを押し下げたままにするツールを定義します。
@mcp.tool()
def key_down(key: str) -> str:
    """Presses and holds down the specified keyboard key.
    指定されたキーボードのキーを押し下げたままにします。

    Args:
        key (str): The key to hold down (e.g., 'ctrl', 'shift', 'a'). 押し下げるキー（例: 'ctrl', 'shift', 'a'）。

    Returns:
        str: A confirmation message. 確認メッセージ。
    """
    try:
        pyautogui.keyDown(key)
        return f"Key '{key}' pressed down."
    except Exception as e:
        return f"Error pressing key down: {e}"

# English: Define a tool to release a key.
# Japanese: キーを離すツールを定義します。
@mcp.tool()
def key_up(key: str) -> str:
    """Releases the specified keyboard key.
    指定されたキーボードのキーを離します。

    Args:
        key (str): The key to release (e.g., 'ctrl', 'shift', 'a'). 離すキー（例: 'ctrl', 'shift', 'a'）。

    Returns:
        str: A confirmation message. 確認メッセージ。
    """
    try:
        pyautogui.keyUp(key)
        return f"Key '{key}' released."
    except Exception as e:
        return f"Error releasing key: {e}"

# English: Define a tool to perform a hotkey combination.
# Japanese: ホットキー（ショートカットキー）を実行するツールを定義します。
@mcp.tool()
def hotkey(*keys: str) -> str:
    """Performs a hotkey combination by pressing keys down in order and releasing them in reverse order.
    キーを順番に押し下げ、逆順に離すことでホットキー（ショートカットキー）を実行します。

    Args:
        *keys (str): The keys to press in the hotkey combination (e.g., 'ctrl', 'c'). ホットキーで押すキー（例: 'ctrl', 'c'）。

    Returns:
        str: A confirmation message. 確認メッセージ。
    """
    try:
        pyautogui.hotkey(*keys)
        return f"Hotkey '{'+'.join(keys)}' executed."
    except Exception as e:
        return f"Error executing hotkey: {e}"


# --- Screenshot Tools ---
# --- スクリーンショットツール ---

# English: Define a tool to take a screenshot.
# Japanese: スクリーンショットを撮るツールを定義します。
@mcp.tool()
def screenshot(filename: str | None = None, region: tuple[int, int, int, int] | None = None) -> str:
    """Takes a screenshot of the entire screen or a specific region and optionally saves it to a file.
    画面全体または特定の領域のスクリーンショットを撮り、オプションでファイルに保存します。

    Args:
        filename (str | None): The path to save the screenshot file. If None, the image is not saved. デフォルトは None。 スクリーンショットファイルを保存するパス。None の場合、画像は保存されません。 Defaults to None.
        region (tuple[int, int, int, int] | None): A tuple of (left, top, width, height) specifying the region to capture. If None, captures the entire screen. デフォルトは None。 キャプチャする領域を指定するタプル (left, top, width, height)。None の場合、画面全体をキャプチャします。 Defaults to None.

    Returns:
        str: A confirmation message, including the save path if provided. 確認メッセージ。ファイル名が指定された場合は保存パスを含みます。
        Note: Returning the image data directly via MCP might be inefficient for large images.
        注意: 大きな画像の場合、MCP経由で画像データを直接返すのは非効率的な場合があります。
    """
    try:
        img = pyautogui.screenshot(region=region)
        if filename:
            img.save(filename)
            return f"Screenshot taken and saved to '{filename}'." + (f" Region: {region}" if region else "")
        else:
            # Returning Base64 encoded image could be an option, but might exceed message limits.
            # Base64エンコードされた画像を返すことも可能ですが、メッセージサイズ制限を超える可能性があります。
            return "Screenshot taken (not saved)." + (f" Region: {region}" if region else "")
    except Exception as e:
        return f"Error taking screenshot: {e}"

# English: Define a tool to locate an image on the screen.
# Japanese: 画面上で画像の位置を特定するツールを定義します。
@mcp.tool()
def locate_on_screen(image_path: str, confidence: float = 0.9, grayscale: bool = False, region: tuple[int, int, int, int] | None = None) -> dict | str | None:
    """Locates the first occurrence of an image on the screen.
    画面上で指定された画像が最初に出現する位置を特定します。

    Args:
        image_path (str): The path to the image file to locate. 検索する画像ファイルのパス。
        confidence (float): The confidence level for matching (0.0 to 1.0). Requires OpenCV. デフォルトは 0.9。 マッチングの信頼度レベル（0.0から1.0）。OpenCVが必要です。 Defaults to 0.9.
        grayscale (bool): Convert the screen to grayscale for faster matching. Defaults to False. マッチングを高速化するために画面をグレースケールに変換します。デフォルトは False。 Defaults to False.
        region (tuple[int, int, int, int] | None): A tuple of (left, top, width, height) specifying the search region. If None, searches the entire screen. デフォルトは None。 検索領域を指定するタプル (left, top, width, height)。None の場合、画面全体を検索します。 Defaults to None.

    Returns:
        dict | str | None: A dictionary {'left': l, 'top': t, 'width': w, 'height': h} with the location, None if not found, or an error message string. 位置を含む辞書 {'left': l, 'top': t, 'width': w, 'height': h}、見つからない場合は None、またはエラーメッセージ文字列。
    """
    try:
        location = pyautogui.locateOnScreen(image_path, confidence=confidence, grayscale=grayscale, region=region)
        if location:
            # Convert Box object to dictionary for JSON serialization
            return {'left': location.left, 'top': location.top, 'width': location.width, 'height': location.height}
        else:
            return None # Indicate image not found
    except pyautogui.ImageNotFoundException:
        return None # Explicitly return None on not found exception
    except ImportError:
        return "Error: locateOnScreen requires OpenCV. Please install it (`uv add opencv-python`)."
    except Exception as e:
        return f"Error locating image '{image_path}' on screen: {e}"

# English: Define a tool to locate the center of an image on the screen.
# Japanese: 画面上で画像の中心位置を特定するツールを定義します。
@mcp.tool()
def locate_center_on_screen(image_path: str, confidence: float = 0.9, grayscale: bool = False, region: tuple[int, int, int, int] | None = None) -> dict | str | None:
    """Locates the center coordinates of the first occurrence of an image on the screen.
    画面上で指定された画像が最初に出現する中心座標を特定します。

    Args:
        image_path (str): The path to the image file to locate. 検索する画像ファイルのパス。
        confidence (float): The confidence level for matching (0.0 to 1.0). Requires OpenCV. デフォルトは 0.9。 マッチングの信頼度レベル（0.0から1.0）。OpenCVが必要です。 Defaults to 0.9.
        grayscale (bool): Convert the screen to grayscale for faster matching. Defaults to False. マッチングを高速化するために画面をグレースケールに変換します。デフォルトは False。 Defaults to False.
        region (tuple[int, int, int, int] | None): A tuple of (left, top, width, height) specifying the search region. If None, searches the entire screen. デフォルトは None。 検索領域を指定するタプル (left, top, width, height)。None の場合、画面全体を検索します。 Defaults to None.

    Returns:
        dict | str | None: A dictionary {'x': x_pos, 'y': y_pos} with the center coordinates, None if not found, or an error message string. 中心の座標を含む辞書 {'x': x_pos, 'y': y_pos}、見つからない場合は None、またはエラーメッセージ文字列。
    """
    try:
        center = pyautogui.locateCenterOnScreen(image_path, confidence=confidence, grayscale=grayscale, region=region)
        if center:
            # Convert Point object to dictionary for JSON serialization
            return {'x': center.x, 'y': center.y}
        else:
            return None # Indicate image not found
    except pyautogui.ImageNotFoundException:
        return None # Explicitly return None on not found exception
    except ImportError:
        return "Error: locateCenterOnScreen requires OpenCV. Please install it (`uv add opencv-python`)."
    except Exception as e:
        return f"Error locating center of image '{image_path}' on screen: {e}"


# --- Message Box Tools ---
# --- メッセージボックスツール ---

# English: Define a tool to display an alert box.
# Japanese: アラートボックスを表示するツールを定義します。
@mcp.tool()
def alert(text: str = '', title: str = '', button: str = 'OK') -> str:
    """Displays a simple alert box with text and a single button.
    テキストと単一のボタンを持つシンプルなアラートボックスを表示します。

    Args:
        text (str): The text to display in the alert box. Defaults to ''. アラートボックスに表示するテキスト。デフォルトは ''。
        title (str): The title of the alert box window. Defaults to ''. アラートボックスウィンドウのタイトル。デフォルトは ''。
        button (str): The text of the button. Defaults to 'OK'. ボタンのテキスト。デフォルトは 'OK'。

    Returns:
        str: The text of the button that was clicked (always the button text provided). クリックされたボタンのテキスト（常に提供されたボタンテキスト）。
    """
    try:
        # Note: pyautogui.alert returns the button text.
        result = pyautogui.alert(text=text, title=title, button=button)
        return str(result) # Ensure result is string
    except Exception as e:
        return f"Error displaying alert: {e}"

# English: Define a tool to display a confirmation box.
# Japanese: 確認ボックスを表示するツールを定義します。
@mcp.tool()
def confirm(text: str = '', title: str = '', buttons: list[str] = ['OK', 'Cancel']) -> str | None:
    """Displays a confirmation box with multiple buttons.
    複数のボタンを持つ確認ボックスを表示します。

    Args:
        text (str): The text to display in the confirmation box. Defaults to ''. 確認ボックスに表示するテキスト。デフォルトは ''。
        title (str): The title of the confirmation box window. Defaults to ''. 確認ボックスウィンドウのタイトル。デフォルトは ''。
        buttons (list[str]): A list of strings for the button texts. Defaults to ['OK', 'Cancel']. ボタンテキストの文字列リスト。デフォルトは ['OK', 'Cancel']。

    Returns:
        str | None: The text of the button that was clicked, or None if the dialog was closed. クリックされたボタンのテキスト、またはダイアログが閉じられた場合は None。
    """
    try:
        result = pyautogui.confirm(text=text, title=title, buttons=buttons)
        return result # Can be None if closed
    except Exception as e:
        return f"Error displaying confirm box: {e}"

# English: Define a tool to display a prompt box for text input.
# Japanese: テキスト入力用のプロンプトボックスを表示するツールを定義します。
@mcp.tool()
def prompt(text: str = '', title: str = '', default: str = '') -> str | None:
    """Displays a prompt box with a text field for user input.
    ユーザー入力用のテキストフィールドを持つプロンプトボックスを表示します。

    Args:
        text (str): The text to display in the prompt box. Defaults to ''. プロンプトボックスに表示するテキスト。デフォルトは ''。
        title (str): The title of the prompt box window. Defaults to ''. プロンプトボックスウィンドウのタイトル。デフォルトは ''。
        default (str): The default text to display in the input field. Defaults to ''. 入力フィールドに表示するデフォルトテキスト。デフォルトは ''。

    Returns:
        str | None: The text entered by the user, or None if Cancel was clicked or the dialog was closed. ユーザーが入力したテキスト、またはキャンセルがクリックされたかダイアログが閉じられた場合は None。
    """
    try:
        result = pyautogui.prompt(text=text, title=title, default=default)
        return result # Can be None
    except Exception as e:
        return f"Error displaying prompt box: {e}"

# English: Define a tool to display a password input box.
# Japanese: パスワード入力ボックスを表示するツールを定義します。
@mcp.tool()
def password(text: str = '', title: str = '', default: str = '', mask: str = '*') -> str | None:
    """Displays a prompt box for password input (typed characters are masked).
    パスワード入力用のプロンプトボックスを表示します（入力文字はマスクされます）。

    Args:
        text (str): The text to display in the password box. Defaults to ''. パスワードボックスに表示するテキスト。デフォルトは ''。
        title (str): The title of the password box window. Defaults to ''. パスワードボックスウィンドウのタイトル。デフォルトは ''。
        default (str): The default text to display in the input field. Defaults to ''. 入力フィールドに表示するデフォルトテキスト。デフォルトは ''。
        mask (str): The character used to mask the input. Defaults to '*'. 入力をマスクするために使用される文字。デフォルトは '*'。

    Returns:
        str | None: The text entered by the user, or None if Cancel was clicked or the dialog was closed. ユーザーが入力したテキスト、またはキャンセルがクリックされたかダイアログが閉じられた場合は None。
    """
    try:
        result = pyautogui.password(text=text, title=title, default=default, mask=mask)
        return result # Can be None
    except Exception as e:
        return f"Error displaying password box: {e}"


# --- Configuration Tools ---
# --- 設定ツール ---

# English: Define a tool to set the pause duration between pyautogui calls.
# Japanese: pyautogui 関数の呼び出し間の待機時間を設定するツールを定義します。
@mcp.tool()
def set_pause(duration: float) -> str:
    """Sets the pause duration (in seconds) between each pyautogui function call.
    各 pyautogui 関数呼び出し間の待機時間（秒）を設定します。

    Args:
        duration (float): The time in seconds to pause after each call. 各呼び出し後に一時停止する時間（秒）。

    Returns:
        str: A confirmation message. 確認メッセージ。
    """
    try:
        if duration < 0:
            return "Error: Pause duration cannot be negative."
        pyautogui.PAUSE = duration
        return f"Global pause set to {duration} seconds."
    except Exception as e:
        return f"Error setting pause: {e}"

# English: Define a tool to enable or disable the failsafe mechanism.
# Japanese: フェイルセーフ機構を有効または無効にするツールを定義します。
@mcp.tool()
def set_failsafe(enable: bool) -> str:
    """Enables or disables the failsafe feature (moving mouse to top-left corner to stop).
    フェイルセーフ機能（マウスを左上隅に移動して停止）を有効または無効にします。

    Args:
        enable (bool): True to enable failsafe, False to disable. True でフェイルセーフを有効化、False で無効化。

    Returns:
        str: A confirmation message. 確認メッセージ。
    """
    try:
        pyautogui.FAILSAFE = bool(enable)
        status = "enabled" if enable else "disabled"
        return f"Failsafe mechanism {status}."
    except Exception as e:
        return f"Error setting failsafe: {e}"

# --- Window Management Tools (pygetwindow) ---
# --- ウィンドウ管理ツール (pygetwindow) ---

# Helper function to convert window object to dictionary
# ウィンドウオブジェクトを辞書に変換するヘルパー関数
def _window_to_dict(window: gw.Window) -> dict:
    if not window:
        return None
    return {
        'title': window.title,
        'left': window.left,
        'top': window.top,
        'width': window.width,
        'height': window.height,
        'isMinimized': window.isMinimized,
        'isMaximized': window.isMaximized,
        'isActive': window.isActive,
        # Add other relevant attributes if needed
        # 必要に応じて他の関連属性を追加
    }

# English: Define a tool to get the titles of all open windows.
# Japanese: 開いているすべてのウィンドウのタイトルを取得するツールを定義します。
@mcp.tool()
def get_all_titles() -> list[str] | str:
    """Gets a list of titles of all currently open windows.
    現在開いているすべてのウィンドウのタイトルのリストを取得します。

    Returns:
        list[str] | str: A list of window titles, or an error message string. ウィンドウタイトルのリスト、またはエラーメッセージ文字列。
    """
    try:
        titles = gw.getAllTitles()
        # Filter out empty titles which can sometimes occur
        # 時々発生する空のタイトルを除外する
        return [title for title in titles if title]
    except Exception as e:
        return f"Error getting all window titles: {e}"

# English: Define a tool to get information about windows with a specific title.
# Japanese: 特定のタイトルを持つウィンドウの情報を取得するツールを定義します。
@mcp.tool()
def get_windows_with_title(title: str) -> list[dict] | str:
    """Gets information about all windows matching the given title.
    指定されたタイトルに一致するすべてのウィンドウの情報を取得します。

    Args:
        title (str): The title of the window(s) to find. 検索するウィンドウのタイトル。

    Returns:
        list[dict] | str: A list of dictionaries containing window information, or an error message string. ウィンドウ情報を含む辞書のリスト、またはエラーメッセージ文字列。
    """
    try:
        windows = gw.getWindowsWithTitle(title)
        return [_window_to_dict(win) for win in windows if win]
    except Exception as e:
        return f"Error getting windows with title '{title}': {e}"

# English: Define a tool to get information about the currently active window.
# Japanese: 現在アクティブなウィンドウの情報を取得するツールを定義します。
@mcp.tool()
def get_active_window() -> dict | str:
    """Gets information about the currently active window.
    現在アクティブなウィンドウの情報を取得します。

    Returns:
        dict | str: A dictionary containing the active window's information, or an error message string. アクティブウィンドウの情報を含む辞書、またはエラーメッセージ文字列。
    """
    try:
        active_window = gw.getActiveWindow()
        return _window_to_dict(active_window)
    except Exception as e:
        return f"Error getting active window: {e}"

# English: Define a tool to get the geometry (position and size) of a window.
# Japanese: ウィンドウのジオメトリ（位置とサイズ）を取得するツールを定義します。
@mcp.tool()
def get_window_geometry(title: str) -> dict | str | None:
    """Gets the position (top-left corner) and size of the first window matching the title.
    タイトルに一致する最初のウィンドウの位置（左上隅）とサイズを取得します。

    Args:
        title (str): The title of the window. ウィンドウのタイトル。

    Returns:
        dict | str | None: A dictionary {'left': l, 'top': t, 'width': w, 'height': h}, None if not found, or an error message string. 辞書 {'left': l, 'top': t, 'width': w, 'height': h}、見つからない場合は None、またはエラーメッセージ文字列。
    """
    try:
        windows = gw.getWindowsWithTitle(title)
        if not windows:
            return None # Window not found
        win = windows[0]
        return {'left': win.left, 'top': win.top, 'width': win.width, 'height': win.height}
    except Exception as e:
        return f"Error getting geometry for window '{title}': {e}"

# English: Define a tool to activate (bring to front) a window.
# Japanese: ウィンドウをアクティブにする（前面に表示する）ツールを定義します。
@mcp.tool()
def activate_window(title: str) -> str:
    """Activates (brings to the front) the first window matching the title.
    タイトルに一致する最初のウィンドウをアクティブにします（前面に表示します）。

    Args:
        title (str): The title of the window to activate. アクティブにするウィンドウのタイトル。

    Returns:
        str: A confirmation or error message. 確認またはエラーメッセージ。
    """
    try:
        windows = gw.getWindowsWithTitle(title)
        if not windows:
            return f"Error: Window with title '{title}' not found."
        win = windows[0]
        # Check if already active?
        # すでにアクティブか確認？
        # Sometimes activate() might not work if the window is minimized
        # ウィンドウが最小化されている場合、activate()が機能しないことがある
        if win.isMinimized:
            win.restore()
        win.activate()
        # Add a small delay to allow the window to come to the front
        # ウィンドウが前面に出るのを許可するために少し遅延を追加する
        pyautogui.sleep(0.2)
        # Verify activation (optional, might be tricky)
        # アクティベーションを確認（オプション、難しい場合がある）
        # active_win_check = gw.getActiveWindow()
        # if active_win_check and active_win_check.title == title:
        #     return f"Window '{title}' activated."
        # else:
        #     return f"Attempted to activate window '{title}', but verification failed."
        return f"Window '{title}' activated."

    except Exception as e:
        return f"Error activating window '{title}': {e}"

# English: Define a tool to minimize a window.
# Japanese: ウィンドウを最小化するツールを定義します。
@mcp.tool()
def minimize_window(title: str) -> str:
    """Minimizes the first window matching the title.
    タイトルに一致する最初のウィンドウを最小化します。

    Args:
        title (str): The title of the window to minimize. 最小化するウィンドウのタイトル。

    Returns:
        str: A confirmation or error message. 確認またはエラーメッセージ。
    """
    try:
        windows = gw.getWindowsWithTitle(title)
        if not windows:
            return f"Error: Window with title '{title}' not found."
        win = windows[0]
        if win.isMinimized:
             return f"Window '{title}' is already minimized."
        win.minimize()
        # Add a small delay to allow the action
        pyautogui.sleep(0.2)
        # Verification (check isMinimized) could be added here
        return f"Window '{title}' minimized."
    except Exception as e:
        return f"Error minimizing window '{title}': {e}"

# English: Define a tool to maximize a window.
# Japanese: ウィンドウを最大化するツールを定義します。
@mcp.tool()
def maximize_window(title: str) -> str:
    """Maximizes the first window matching the title.
    タイトルに一致する最初のウィンドウを最大化します。

    Args:
        title (str): The title of the window to maximize. 最大化するウィンドウのタイトル。

    Returns:
        str: A confirmation or error message. 確認またはエラーメッセージ。
    """
    try:
        windows = gw.getWindowsWithTitle(title)
        if not windows:
            return f"Error: Window with title '{title}' not found."
        win = windows[0]
        if win.isMaximized:
             return f"Window '{title}' is already maximized."
        win.maximize()
        pyautogui.sleep(0.2)
        return f"Window '{title}' maximized."
    except Exception as e:
        return f"Error maximizing window '{title}': {e}"

# English: Define a tool to restore a window (from minimized or maximized state).
# Japanese: ウィンドウを元のサイズに戻す（最小化または最大化状態から）ツールを定義します。
@mcp.tool()
def restore_window(title: str) -> str:
    """Restores the first window matching the title (if minimized or maximized).
    タイトルに一致する最初のウィンドウを元のサイズに戻します（最小化または最大化されている場合）。

    Args:
        title (str): The title of the window to restore. 元のサイズに戻すウィンドウのタイトル。

    Returns:
        str: A confirmation or error message. 確認またはエラーメッセージ。
    """
    try:
        windows = gw.getWindowsWithTitle(title)
        if not windows:
            return f"Error: Window with title '{title}' not found."
        win = windows[0]
        if not win.isMinimized and not win.isMaximized:
            return f"Window '{title}' is already restored (neither minimized nor maximized)."
        win.restore()
        pyautogui.sleep(0.2)
        return f"Window '{title}' restored."
    except Exception as e:
        return f"Error restoring window '{title}': {e}"

# English: Define a tool to move a window to a specific position.
# Japanese: ウィンドウを指定された位置に移動するツールを定義します。
@mcp.tool()
def move_window(title: str, x: int, y: int) -> str:
    """Moves the top-left corner of the first window matching the title to the specified coordinates.
    タイトルに一致する最初のウィンドウの左上隅を指定された座標に移動します。

    Args:
        title (str): The title of the window to move. 移動するウィンドウのタイトル。
        x (int): The target x-coordinate for the top-left corner. 左上隅のターゲットX座標。
        y (int): The target y-coordinate for the top-left corner. 左上隅のターゲットY座標。

    Returns:
        str: A confirmation or error message. 確認またはエラーメッセージ。
    """
    try:
        windows = gw.getWindowsWithTitle(title)
        if not windows:
            return f"Error: Window with title '{title}' not found."
        win = windows[0]
        win.moveTo(x, y)
        pyautogui.sleep(0.2)
        # Verification could be added here by checking win.topleft
        return f"Window '{title}' moved to ({x}, {y})."
    except Exception as e:
        return f"Error moving window '{title}': {e}"

# English: Define a tool to resize a window.
# Japanese: ウィンドウのサイズを変更するツールを定義します。
@mcp.tool()
def resize_window(title: str, width: int, height: int) -> str:
    """Resizes the first window matching the title to the specified width and height.
    タイトルに一致する最初のウィンドウを指定された幅と高さにリサイズします。

    Args:
        title (str): The title of the window to resize. リサイズするウィンドウのタイトル。
        width (int): The target width. ターゲット幅。
        height (int): The target height. ターゲット高さ。

    Returns:
        str: A confirmation or error message. 確認またはエラーメッセージ。
    """
    try:
        windows = gw.getWindowsWithTitle(title)
        if not windows:
            return f"Error: Window with title '{title}' not found."
        win = windows[0]
        if width <= 0 or height <= 0:
            return "Error: Width and height must be positive."
        win.resizeTo(width, height)
        pyautogui.sleep(0.2)
        # Verification could be added here by checking win.size
        return f"Window '{title}' resized to {width}x{height}."
    except Exception as e:
        return f"Error resizing window '{title}': {e}"

# English: Define a tool to close a window.
# Japanese: ウィンドウを閉じるツールを定義します。
@mcp.tool()
def close_window(title: str) -> str:
    """Closes the first window matching the title.
    タイトルに一致する最初のウィンドウを閉じます。

    Args:
        title (str): The title of the window to close. 閉じるウィンドウのタイトル。

    Returns:
        str: A confirmation or error message. 確認またはエラーメッセージ。
    """
    try:
        windows = gw.getWindowsWithTitle(title)
        if not windows:
            return f"Error: Window with title '{title}' not found."
        win = windows[0]
        win.close()
        pyautogui.sleep(0.2) # Allow time for close operation
        # Verification (checking if window still exists) could be added
        return f"Window '{title}' closed."
    except Exception as e:
        # Note: Closing might sometimes raise errors depending on the application
        # 注意: アプリケーションによっては、閉じる際にエラーが発生する場合があります
        return f"Error closing window '{title}': {e}"

# English: Entry point to run the MCP server if the script is executed directly.
# Japanese: スクリプトが直接実行された場合にMCPサーバーを実行するエントリーポイント。
if __name__ == "__main__":
    # English: Run the MCP server. It will listen for requests according to the MCP specification.
    # Japanese: MCPサーバーを実行します。MCP仕様に従ってリクエストを待ち受けます。
    mcp.run() 