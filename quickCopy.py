import win32clipboard

def copyString(item):
    """
    Copies a single string.
    """
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(item)
    win32clipboard.CloseClipboard()


def copyList(lst):
    """
    Copies a list of items.
    """
    toCopy = ""
    for i in range(len(lst)):
        toCopy += f"{lst[i]} \n"
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(toCopy)
    win32clipboard.CloseClipboard()

