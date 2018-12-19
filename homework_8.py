"""Користувач вводить координати клітин. Програма рахує, чи може

походити слон"""
"""
black - x парні, у парні
        
х непарні, у непарні

white - х парні, у непарні
        
х непарні, у парні
"""

print("Please, enter four coordinates from 1 to 8 in format X")

x1=int(input("X1 is: "))

y1=int(input("Y1 is: "))

x2=int(input("X2 is: "))

y2=int(input("Y2 is: "))

if (x1%2==1 and y1%2==1) or (x1%2==0 and y1%2==0): #for first - black 
    
	if (x2%2==1 and y2%2==1) or (x2%2==0 and y2%2==0): #for second - black 
        
		print("TRUE") 
    
	else: #for second - white 
        
		print("FALSE") 

else: #for first - white 
    
	if (x2%2==1 and y2%2==0) or (x2%2==0 and y2%2==1): #for second - white 
        
		print("TRUE") 
    
	else: #for second - black 
        
		print("FALSE")

if (x2-x1==y1-y2) or (x2-x1==y2-y1):
    
	print("YES")

elif (x1-x2==y1-y2) or (x1-x2==y2-y1):
    
	print("YES")

else:
    
	print("NO")

#----------------------------------------------------------------------------
pin_throw = input()

N = int(pin_throw.split()[0])

K = int(pin_throw.split()[1])

list_to_compare = []

list_a = []

for j in range(1, N + 1):
    list_to_compare.append(j)

for i in range(K):

    row = input()

    left = int(row.split()[0])

    right = int(row.split()[1])

    for i in range(left, right + 1):
        list_a.append(i)

for element in list_to_compare:

    if element in list_a:

        print('.', end="")

    else:

        print('I', end="")
#---------------------------------------------------------------------------------------------------------------
num_list = []
num_count = int (input ("Enter count"))
while len(num_list) < num_count:
    num_list.append(int(input('Введіть число')))
print (num_list)
sum = 0
for i in range (0,len(num_list)):
    sum += num_list[i]
print (sum)
#------------------------------------------------------------------------------------------------------------------
num_list = []
num_count = int (input ("Enter count"))
while len(num_list) < num_count:
    num_list.append(int(input('Введіть число')))
print (num_list)
i = 0
sum = 0
while i != len(num_list):
    sum += num_list[i]
    i += 1
print (sum)