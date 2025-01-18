import pyautogui

def close_current_window():
    pyautogui.hotkey('alt', 'f4')
    return "Window closed successfully!"