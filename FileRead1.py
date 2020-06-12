print ("Hello World")
file = open ("abc.txt",'r')
f = file.readlines()
for i in f:
    if '#' in i:
            print(i)
