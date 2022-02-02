import random 

lower = "abcdefghijklmnopqrstuvwxy"
Upper = "ABCDEFGHIJKLMNOPQRSTUVWYZ"
numbers = "0123456789"
symbols = "@!#%"

all = lower + Upper + numbers + symbols

length = 16
password = "" .join(random.sample(all,length))
print(password)