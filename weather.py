#mini = 1000000
#maxi = 0
total = 0
tempe = []
for i in range (0,7):
  temp = int(input('What is the air temperature today?: \n'))
  total = total + temp
  tempe.append(temp)
  #if temp < mini:
   # mini = temp
 # elif temp > maxi:
   # maxi = temp
print (tempe)
mini = min(tempe)
maxi = max(tempe)
mean = total//7
print ('This is the minimum temperature: %s degrees Celsius' % mini)
print ('This is the maximum temperature: %s degrees Celsius' % maxi)
print ('This is the average temperature: %s degrees Celsius' % mean)