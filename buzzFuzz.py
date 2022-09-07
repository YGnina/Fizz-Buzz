import sys

try:
  a,b,c = map(int,input().split())
  for i in range (1,c+1,1):
    if(i%a==0) and (i%b==0):
      print('FB', end = " ")
    elif(i%a==0):
      print('F', end = " ")
    elif(i%b==0):
      print('B', end = " ")
    else:
      print(1,end = " ")
  i+=1

except:
  pass