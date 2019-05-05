#open the file for writing
f = open('myfile.txt','w')  #w=write/r=read/a=append
print('Enter text (Type # when done)')

s=''
while s != '#':
    s = input()
    f.write(s+'\n')

f.close()