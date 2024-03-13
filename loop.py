#3 3 3
#3 3 3
#3 3 3
# n=int(input('Enter a row :'))
# for i in range(n):
#     print((str(n-i)+' ')*n)
#..........................

#ASCI value
# n=3
# C C C -->67=64+n-i
# B B B -->66=64+n-i
# A A A -->65=64+n-i

# n=int(input('Enter a numb :'))
# for i in range(n):
#       print((chr(64+n-i)+' ')*n)

#........................................

#n=3
#3 2 1
#3 2 1
#3 2 1

# n=int(input('Enter number of rows: '))
# for i in range(n): #0,1,2
#     for j in range(n):#0,1,2
#         print(n-j,end=' ')
#     print()

#......................................

n=int(input('Enter number of rows: '))
for i in range(n): #0,1,2
     for j in range(n):#0,1,2
         print(chr(64+n-j),end=' ')
     print()

