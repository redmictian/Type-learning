from random import randrange
letters = ['a','s','d','f','l','k','j']
difficulty = 2
def letterSequenceFun(quantity,letter1,letter2):
  letterSequence = ''
  for i in range(quantity):
      if randrange((2)) == 1:
        letterSequence += letter1
      else:
        letterSequence += letter2
  return letterSequence
def gameCode():
  global difficulty
  print('Type those:',rightSequence)
  while True:
    typeOut = input()
    if rightSequence == typeOut:
      print('Congratulations! Welcome to the next level')
      difficulty += 2
      break
    else:
      print('Try again.')
print('put your left hands pinky finger on letter A, ring finger to S, middle to D, pointing on F. Pinky finger of your right hand on ;, ring finger on L, middle one on K, pointing on J. Remember position of your fingers. Repeat after me')
while True: 
  rightSequence = letterSequenceFun(difficulty,letters[randrange((7))],letters[randrange((7))])
  gameCode()