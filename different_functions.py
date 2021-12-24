def incFun(elementNumber):
  arrayInc = []
  print('The new array of',elementNumber,'numbers consist of')
  for i in range(elementNumber):
    arrayInc.insert(i,i+1)
    print(arrayInc[i])
  return arrayInc
def SumFun(sumArray):
  sumvar = 0
  for i in range(len(sumArray)):
    sumvar += sumArray[i]
  return sumvar
def MaxFunc(maxArray):
  maxNumber = maxArray[0]
  for i in range(len(maxArray)):
    if maxNumber < maxArray[i]:
      maxNumber = maxArray[i]
  return maxNumber
def MinFunc(minArray):
  minNumber = minArray[0]
  for i in range(len(minArray)):
    if minNumber > minArray[i]:
      minNumber = minArray[i]
  return minNumber
def IntegerFunc(MessArray):
  IntegerArray = []
  for i in range(len(MessArray)):
    if MessArray[i] % 2 == 0:
      IntegerArray.append(MessArray[i])
  return IntegerArray
repetitions = int(input('how much? '))
NewArray = incFun(repetitions)
print('The sum of',NewArray,'is',SumFun(NewArray))
print('The maximum number is',MaxFunc(NewArray))
print('The minimum number is',MinFunc(NewArray))
print('This array',NewArray,'used to be a mess, but now it has only integer numbers:',IntegerFunc(NewArray))
