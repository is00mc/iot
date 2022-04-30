import ctypes
from itertools import count
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


    def printNotice(self, level, text, color=True):
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
                if color == True:
                        symbol = colored(f"{l['symbol']}", l['color'])
                else:
                    symbol = l['symbol']
                print(f"{symbol} error in module TermAttributes \n{symbol} notice level \'{level}\' not found in function TermAttributes.termAttr.printText for text \'{text}\'")


    def printTitle(self, text, border='-', color='none'):

        if color != 'none':
            cBorder = colored(border, color)
            cText = colored(text, color)
        else:
            cBorder = border
            cText = text

        def getSpacer(bLen, text, spacer=' '):
            tLen = len(text)
            spacerLen = int((bLen - tLen) / 2)
            return spacer * spacerLen
        
        def getBorderLen(text):
            return len(text) * 2

        borderLen= getBorderLen(text)
        spacer = getSpacer(borderLen, text)

        count = 1
        while count <= borderLen:
            print(cBorder, end='')
            count += 1
        print(cBorder)
        print(spacer + cText)
        count = 1
        while count <= borderLen:
            print(cBorder, end='')
            count += 1
        print(cBorder)

            

termAttr = TermAttributes()
