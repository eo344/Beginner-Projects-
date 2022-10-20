score = int(input('Enter score:\n'))
#if score >= 50 and score < 60:
 # print ('You Passed')
if score > 80:
  print ('You got an A')
#elif score >= 60 and score < 70:
 # print ('You got a C')
elif score > 70:
  print ('You got a B')
#elif score >= 70 and score < 80:
 # print ('You got a B')
elif score > 60:
  print ('You got a C')
#elif score >= 80:
 # print ('You got an A')
elif score > 50:
  print ('You Passed')
else:
  print ('You Failed')