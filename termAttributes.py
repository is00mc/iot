from termcolor import colored


class TermAttributes:

    # this would be simpler as a function

    info = {'symbol': '[*]', 'color': 'blue'}
    success = {'symbol': '[+]', 'color': 'green'}
    warning = {'symbol': '[!]', 'color': 'yellow'}
    error = {'symbol': '[x]', 'color': 'red'}

    def __init__(self):
        pass

    @classmethod
    def printText(self, level, text, color=True):
        for k, v in level.items():
            if color == True:
                symbol = colored(f"{level['symbol']}", level['color'])
            else:
                symbol = level['symbol']
        print(f"{symbol} {text}")
