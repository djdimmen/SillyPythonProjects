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
    breakOptions = ['Pee', 'Poop']
    chosenOption = random.choice(breakOptions)

    addBuffer()
    print(f'Excuse me, I think you need to take a bathroom break to go {chosenOption.lower()}.')
    addBuffer()

if __name__ == '__main__':
    capitalize()