
#Test input
#3 5 10
#Expected output
#1 2 F 4 B F 7 8 F B

#Test input
#2 7 15
#Expected output
#1 F 3 F B F 9 F 11 F 13 FB 15





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
