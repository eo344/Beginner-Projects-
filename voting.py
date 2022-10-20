age = int(input('How old are you: \n'))
if age < 18:
  if age >= 16:
    print ('You can vote in Scotland')
  else: 
    print ('You cannot vote in Scotland ')
else: 
  print ('You can vote in England and Scotland')