import random 
import string 

print ("Password generation")

n = int(input("Enter the lenght of password: "))
c = string.ascii_letters + string.digits + string.punctuation
p = "".join(random.choice(c) for i in range(n))

print("Your password is: ", p)

