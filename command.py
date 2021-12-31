import socket


class Command:

    commands = []
    lineDelim = '----------------------------------------'
    
    def __init__(self, name, command, data, ack, description, parameterType, port):

        self.name = name
        self.command = command
        self.data = data
        self.ack = ack
        self.description = description
        self.parameterType = parameterType
        self.port = port
        self.attr = {'name': self.name, 'command': self.command, 'data': self.data, 'ack': self.ack, 'description': self.description, 'parameterType': self.parameterType, 'port': self.port}
        self.commands.append(self.attr)


    def send(self, server, command, port, buffer=1024):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            s.connect((server, port))
            s.sendall(command.encode())
            response = s.recv(buffer)

        return response


    def getDescription(self):
        return self.description


    def listParameters(self):

        parameters = []
        if self.parameterType == 'dict':
            for k, v in self.data.items():
                parameters.append(k)
        elif self.parameterType == 'range':
            parameters.append(self.data[0])
            parameters.append(self.data[1])
        return parameters
    
    @classmethod
    def printAttr(self): # wht???

        for cmd in self.commands:
            for k, v in cmd.items():
                if type(v) == dict:
                    newLine = "\n    "
                else:
                    newLine = " "
                print(f"{k}:",end=newLine)
                if type(v) == dict:
                    for key, val in v.items():
                        print(key, val, end=newLine)
                else:
                    print(v)
            print(self.lineDelim)
