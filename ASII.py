lista = input("Dose string: ")
lista2= [ord(c) for c in lista]
def convert(lista2): 
    global res
    res =int("".join(map(str, lista2))) 
      
    return res 
convert(lista2)
for i in range(2,res):
  
  if(res % i) == 0:
    print ("O arithmos: ",res,"Den einai protos")
    break
else:
    print("O arithmos: ",res,"einai protos")
  

