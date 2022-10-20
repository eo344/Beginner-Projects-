import random 

score = 0
question = 0
name = input('What is your name?:\n')
while question !=3:
  num = random.randint(1,100)
  num2 = random.randint(1,101)
  op = random.randint(1,4)
  if op == 1:
    question = question+1
    result = num + num2
    print ('Here is your question:\n', num, '+', num2)
    answer =  int(input('Enter your answer:\n'))
    if result == answer:
      print ('Correct!, Well done')
      score= score+1
    else:
      print ('Incorrect')
      print (result)
  elif op == 2:
    question = question+1
    result = num - num2
    print ('Here is your question:\n', num, '-', num2)
    answer =  int(input('Enter your answer:\n'))
    if result == answer:
      print ('Correct!, Well done')
      score= score+1
    else:
      print ('Incorrect')
      print (result)
  elif op == 3:
    question = question+1
    result = num // num2
    print ('Here is your question:\n', num, '/', num2)
    answer =  int(input('Enter your answer:\n'))
    if result == answer:
      print ('Correct!, Well done')
      score= score+1
    else:
      print ('Incorrect')
      print (result)
  elif op == 4:
    question = question+1
    result = num * num2
    print ('Here is your question:\n', num, 'x', num2)
    answer =  int(input('Enter your answer:\n'))
    if result == answer:
      print ('Correct!, Well done')
      score= score+1
    else:
      print ('Incorrect')
      print (result)

print ('Your final score = ', score, 'out of 3')