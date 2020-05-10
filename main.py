from random import randint

# tries = gettries()
tries = 5
choosediff = input('Select a difficulty:  ')
possdiff = ('e', 'm', 'h')



# def gettries(diff):

diff = []
R = []
def getdiff():
    choosediff
    if diff == 'e':
        R = (0, 10)
        print('range is 0 to 1000')
    elif diff == 'm':
        R = (0, 100)
        print('range is 0 to 1000')
    elif diff == 'h':
        R = (0, 1000)
        print('range is 0 to 1000')
 

diff = getdiff()
rannum = randint(0, 10)
guesses = 0
while guesses != tries:
    playerguess = int(input('enter a number:  '))
    if playerguess > rannum:
        print('Lower...')
        guesses += 1
    elif playerguess < rannum:
        print('Higher...')
        guesses += 1
    elif playerguess == rannum:
        print('you won!')
        break

if guesses == tries:
    print('you lost')
    print('my number was', rannum)
