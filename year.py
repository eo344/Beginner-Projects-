year = str(input('Enter a year:\n'))
while len(year) !=4:
  year = str(input('Enter a year:\n'))
one = year[0:1]
n1 = int(one)
two = year [1:2]
n2 = int(two)
three = year[2:3]
n3 = int(three)
four = year [3:4]
n4 = int(four)

result = n1 + n2 + n3 +n4
print (result)