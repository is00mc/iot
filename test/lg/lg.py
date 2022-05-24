from command import Command # in parent directory may need to update import statement


class LG(Command):

    def __init__(self, name, command, data, ack, description, parameterType, port=9761):
        super().__init__(name, command, data, ack, description, parameterType, port)

#    def formatData(self):
#        if self.parameterType == dict:
#            return
#        elif self.parameterType == range:
#            return
#        else:
#            return


    def formatCommand(self, parameter, id='01', delimeter=' ', terminator='\\r'):

        parts = [self.command, id, self.data[parameter], terminator]
        formattedCommand = delimeter.join(parts)

        return formattedCommand


    def parseResponse(self, data, response, id='01', delimeter=' '):

        posParts = [self.ack, id, f'OK{data}x']
        negParts = [self.ack, id, f'NG{data}x']
        expectedPosResponse = delimeter.join(posParts)
        expectedNegResponse = delimeter.join(negParts)

        if response == expectedPosResponse:
            return (0, response)
        if response == expectedNegResponse:
            return (1, response)
        else:
            return (255, response)


power = LG(
    'power',
    'ka',
    {
        'OFF': '00',
        'ON': '01',
        'RESTART': '02'
    },
    'a',
    'Controls the power on/off status of the monitor.',
    'dict'
)

select_input = LG(
    'input',
    'xb',
    {
        'AV': '20',
        'COMPONENT': '40',
        'RGB': '60',
        'DVI-D(PC)': '70',
        'DVI-D(DTV)': '80',
        'HDMI1(DTV)': '90',
        'HDMI1(PC)': 'A0',
        'HDMI2(DTV)': '91',
        'HDMI2(PC)': 'A1',
        'OPS/HDMI3/DVI-D(DTV)': '92',
        'OPS/HDMI3/DVI-D(PC)': 'A2',
        'OPS/DVI-D(DTV)': '95',
        'OPS/DVI-D(PC)': 'A5',
        'HDMI3/DVI-D(DTV)': '96',
        'HDMI3/DVI-D(PC)': 'A6',
        'HDMI3/HDMI2/DVI-D(DTV)': '97',
        'HDMI3/HDMI2/DVI-D(PC)': 'A7',
        'OPS(DTV)': '98',
        'OPS(PC)': 'A8',
        'HDMI2/OPS(DTV)': '99',
        'HDMI2/OPS(PC)': 'A9',
        'DISPLAYPORT(DTV)': 'C0',
        'DISPLAYPORT(PC)': 'D1',
        'HDMI3(DTV)': 'C2',
        'HDMI3(PC)': 'D2',
        'HDBASET(DTV)': 'C3',
        'HDBASET (PC)': 'D3',
        'SUEPERSIGN_WEBOS_PLAYER': 'E0',
        'OTHERS': 'E1',
        'MULTISCREEN': 'E2',
        'PLAY_VIA_URL': 'E3'
    },
    'b',
    'Selects an input signal.',
    'dict',
    )

aspect_ratio = LG(
    'aspect ratio',
    'kc',
    {
        'FULL_SCREEN': '02',
        'ORIGINAL': '06'
    },
    'c',
    'Adjusts the aspect ratio of your monitor.',
    'dict'
)

brightness = LG(
    'brightness',
    'jq',
    {
        'OFF': '00',
        'MINIMUM': '01',
        'MEDIUM': '02',
        'MAXIMUM': '03',
        'AUTO': '04',
    },
    'h',
    'Adjusts the screen brightness.',
    'dict'
)

picture_mode = LG(
    'picture mode',
    'dx',
    {
        'MALL/QSR': '00',
        'GENERAL': '01',
        'GOV/CORP': '02',
        'TRANSPORTATION': '03',
        'EDUCATION': '04',
        'EXPERT1': '05',
        'APS': '08',
        'CALIBRATION': '11',
        'HOSPITAL': '12'
    },
    'x',
    'Selects a picture mode.',
    'dict'
)

contrast = LG(
    'contrast',
    'kk',
    (0,100),
    'g',
    'Adjusts the screen contrast.',
    'range'
)

brightness = LG(
    'brightness',
    'kh',
    (0,100),
    'h',
    'Adjusts the screen brightness.',
    'range'
)

sharpness = LG(
    'sharpness',
    'kk',
    (0,50),
    'k',
    'Adjusts the screen sharpness.',
    'range'
)

color = LG(
    'color',
    'ki',
    (0,100),
    'i',
    'Adjusts the screen colors.',
    'range'
)

tint = LG(
    'tint',
    'ki',
    (0,100),
    'j',
    'tint',
    'range'
)

color_temp = LG(
    'color temperature',
    'xu',
    (112,210),
    'u',
    'color temp',
    'range'
)

balance = LG(
    'balance',
    'kt',
    (0,100),
    't',
    'balance',
    'range'
)

sound_mode = LG(
    'sound mode',
    'dy',
    {
        'STANDARD': '01',
        'MUSIC': '02',
        'CINEMA': '03',
        'SPORTS': '04',
        'GAME': '05',
        'NEWS': '07'
    },
    'y',
    'sound mode',
    'dict'
)

mute = LG(
    'mute',
    'ke',
    {
        'ON': '00',
        'OFF': '01'
    },
    'e',
    'mute',
    'dict'
)

volume = LG(
    'volume',
    'kf',
    (0,100),
    'f',
    'volume',
    'range'
)
