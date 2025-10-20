import random

def addBuffer():
    bufferSpace = '\n' + '\n' + '\n'
    print(bufferSpace)

def capitalize():
    print('Type a word:')
    inputReceived = input('Type your word here > ').upper()

    addBuffer()
    print(inputReceived)
    addBuffer()

def bathroomBreak():
    breakOptions = ['Peed', 'Pooped']
    chosenOption = random.choice(breakOptions)

    addBuffer()
    print(AHHHHHHHHHHHHHHHHHH! I  {chosenOption.lower(} in my pants!!!!!.')

    addBuffer()

if __name__ == '__main__':
    bathroomBreak()