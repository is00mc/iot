import ctypes
from termcolor import colored


class TermAttributes:

    # this would be simpler as a function

    levels = [
        {'name': 'info', 'symbol': '[*]', 'color': 'blue'},
        {'name': 'success', 'symbol': '[+]', 'color': 'green'},
        {'name': 'warning', 'symbol': '[!]', 'color': 'yellow'},
        {'name': 'error', 'symbol': '[x]', 'color': 'red'}
    ]

    def __init__(self):
        # enable VT100 support in Windows 10 for colored text in terminal
        kernel32 = ctypes.WinDLL('kernel32')
        hStdOut = kernel32.GetStdHandle(-11)
        mode = ctypes.c_ulong()
        kernel32.GetConsoleMode(hStdOut, ctypes.byref(mode))
        mode.value |= 4
        kernel32.SetConsoleMode(hStdOut, mode)

    def printText(self, level, text, color=True):
        for l in TermAttributes.levels:
            if level == l['name']:
                for k, v in l.items():
                    if color == True:
                        symbol = colored(f"{l['symbol']}", l['color'])
                    else:
                        symbol = l['symbol']
                print(f"{symbol} {text}")
                return
        for l in TermAttributes.levels:
            if l['name'] == 'error':
                symbol = colored(f"{l['symbol']}", l['color'])
                print(f"{symbol} notice level \'{level}\' not found in function for text \'{text}\'")


termAttr = TermAttributes()
