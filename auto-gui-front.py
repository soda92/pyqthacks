from pywinauto.findwindows    import find_window
import pywinauto
import win32gui

def show_window(title):
    try:
        window = find_window(title_re=title)
        win32gui.ShowWindow(window, True)
        win32gui.SetForegroundWindow(window)
    except Exception as e:
        print("Error: ", e)

show_window('微信')

# from pywinauto import Desktop

# windows = Desktop(backend="uia").windows()
# arr = [w.window_text() for w in windows]

# for i in arr:
#     if 'dialog' in i:
#         print(i)

# ShowWindow(find_window(title_re='.*video_dialog.*'), False)
