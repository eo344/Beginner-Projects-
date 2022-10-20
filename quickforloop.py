num = int(input('Enter a number:\n'))
seven = 0
for i in range (0,num):
  sev = i%7
  if sev == 0:
    seven = seven + 1
print ('%s of the numbers inbetween 0 and %d are divisible by 7' % (seven, num))