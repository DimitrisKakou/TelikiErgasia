number=int(input("Dose enan arithmo:"))

while number>9:
  number*=3
  print ("O arithmos epi 3", int(number))
  number+=1
  print ("O arithmos sin 1", int(number))
  sum = 0
  while (number > 0):
     d = number%10
     number = number//10
     sum += d
  print("Athroisma: ",sum)
  number=sum
else: 
 print ("Telos")  
 
  
