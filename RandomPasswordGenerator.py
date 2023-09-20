import random
passlen = int(input("Enter the length of Password:"))
s = "abcdefghijklmnopqstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s, passlen))
print(p)