charsList = [
    'ico',
    'bob',
    'bob2',
    'bob3',
    'bob4',
    'bob5',
    'bob6',
    'bob7',
    'bob8',
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'r',
    's',
    't',
    'u',
    'w',
    'x',
    'y',
    'z',
    'v',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'R',
    'S',
    'T',
    'U',
    'W',
    'X',
    'Y',
    'Z',
    'V',
    '_',
    '+',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '0',
    ',',
    '.',
    '<',
    '>',
    '-',
    '!',
    '?',
    ' ',
    '%',
    'ą',
    'ę',
    'ć',
    'ó',
    'ż',
    'ź',
    'ś',
    'ł',
    'ń',
    'Ą',
    'Ę',
    'Ć',
    'Ó',
    'Ż',
    'Ź',
    'Ś',
    'Ł',
    'Ń'
]

def encode(text):
  encodedText = ""
  for x in text:
    if x in charsList:
      encodedText = encodedText + str(charsList.index(x)+1)
    else:
        raise Exception(x + " character isn't supported")
  return encodedText

def decode(text):
  decodedText = ""
  double = ""
  for x in text:
    double = double + x
    if len(double) > 1:

      if int(double)-1 < len(charsList):
        decodedText = decodedText + charsList[int(double)-1]

      double = ""
  return decodedText