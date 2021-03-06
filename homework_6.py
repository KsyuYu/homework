#task1------------------------------------------------------------
"""
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
"""
#default

list_B=[]

n=1

k=0

print("Program prints all element with even indexes")


#input

n=(input("Enter a row"))



#main and output

list_B=n.split( )


for element in list_B:

    if k%2==0:

        print(element)

    k+=1
#-----------------------------------------------------------------



#task2------------------------------------------------------------
"""
Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы!
"""
#default

list_A=[]

print("Program shows even elements")



#input

list_A=input("Enter a row of numbers").split()



#main and output

for element in list_A:

    element=int(element)

    if element%2==0:

        print(element)
#-----------------------------------------------------------------



#task3------------------------------------------------------------
"""
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
"""
#default

x=0

print("Program shows numbers, greater then previous")



#input

n=input("Enter a row of numbers")



#main

list_int = n.split()

prev=int(list_int[0])


for element in list_int[1:]:

    element=int(element)

    x=element

    if x>prev:

        print(x,end=" ")

    prev=element
#-----------------------------------------------------------------



#task4------------------------------------------------------------
"""
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа.
 Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько
 — выведите первую пару.
"""
#default

print("Program prints neighbours with the same sign")



#input

n=input("Enter a row of numbers")



#main and output

list_A=n.split()

prev=int(list_A[0])


for element in list_A[1:]:

    x=int(element)

    if (x>0 and prev>0) or (x<0 and prev<0):

        print(prev,element)

        break

    else:

        print(end="")

    prev=x
#-----------------------------------------------------------------



#task5------------------------------------------------------------
"""
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей,
и выведите количество таких элементов.
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
"""
#default

counter = 0


print("Program prints numbers which greater than neighbours")

#input

n = input ( "Enter a row of numbers" )



#main

list_int = n.split ( )

for i in range ( 1 , len ( list_int ) - 1 ) :

    if list_int [ i ] > list_int [ i - 1 ] and list_int [ i ] > list_int[ i + 1 ] :

        counter += 1



#output

print(counter)
#-----------------------------------------------------------------



#task6------------------------------------------------------------
"""
Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента
в списке.
Если наибольших элементов несколько, выведите индекс первого из них.
"""
#default

i = 0

print("Program shows maximum element")



#main

list_A = [int(element) for element in input("Enter a row of numbers").split()]

maximum = int(max(list_A))


for element in list_A:

    if int(element) != maximum:

        i+=1

    if int(element) == maximum:

        break



#output

print (maximum,i,end=" ")

#-----------------------------------------------------------------



#task7------------------------------------------------------------
"""
Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю.
Помогите ему это сделать.
Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост 
каждого человека в строю. После этого вводится число X – рост Пети. 
Все числа во входных данных натуральные и не превышают 200.

Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым 
ростом, таким же, как у Пети, то он должен встать после них.
"""
#default

counter = 0



#input

row = input ("Enter a row of heights")



#main

list_height = row.split ()

Petja_height = int(input("Enter Petjas height"))



for element in list_height:

    if int(element)<Petja_height:

        list_height.insert(counter,Petja_height)

        break

    counter+=1



#output

print(counter+1)
#-----------------------------------------------------------------



#task8------------------------------------------------------------
"""
Дан список, упорядоченный по неубыванию элементов в нем.
 Определите, сколько в нем различных элементов.
"""
#defaults

temp = 0

counter = 0

print("Program prints, how many elements are different")



#input

row = input ("Enter a sorted by descending row of numbers")



#main

list_A = row.split ()


for element in list_A:

    if element != temp:

        temp = element

        counter +=1



#output

print(counter)
#-----------------------------------------------------------------



#task9------------------------------------------------------------
"""
Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.).
Если элементов нечетное число,
то последний элемент остается на своем месте.
"""
#input

row = input ()

print("Program replaces neighbours")



#main

list_A = row.split ()



for i in range (1,len(list_A),2):

    Temp = list_A [i-1]

    list_A [i-1] = list_A[i]

    list_A[i] = Temp



#output

print(" ".join(list_A))

#-----------------------------------------------------------------



#task10------------------------------------------------------------
"""
В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
"""
#default

print("Program replaces minimum and maximum")



#input

n=input("Enter a row of numbers")



#main

list_numbers=n.split()


      #defaults--------------------

max_num = int ( list_numbers [ 0 ] )

min_num = int ( list_numbers [ 0 ] )

max_pos , min_pos = 0, 0

counter = 0

      #----------------------------



for i in range(len(list_numbers)):

    if int(list_numbers[i])>max_num:

        max_num = int( list_numbers[i] )

        max_pos = i

    if int(list_numbers[i])<min_num:

        min_num = int( list_numbers[i] )

        min_pos = i



temp = list_numbers[max_pos]

list_numbers[max_pos] = list_numbers[min_pos]

list_numbers[min_pos] = temp



#output

print(" ".join(list_numbers))
#-----------------------------------------------------------------



#task11------------------------------------------------------------
"""
Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k, 
сдвинув влево все элементы, стоящие правее элемента с индексом k.
Программа получает на вход список, затем число k. Программа сдвигает все элементы, а после 
этого удаляет последний элемент списка при помощи метода pop() без параметров.

Программа должна осуществлять сдвиг непосредственно в списке, а не делать это 
при выводе элементов. Также нельзя использовать дополнительный список.
Также не следует использовать метод pop(k) с параметром.
"""
#default

print("Program delets element with changed index")



#input

row = input ("Enter a row of numbers")

k = int( input ("Enter index of number to delete") )



#main

list = row.split()

for i in range (k+1,len(list)):

    list[i-1]=list[i]

list.pop()



#output

print(" ".join(list))
#-----------------------------------------------------------------



#task12------------------------------------------------------------
"""
Дан список целых чисел, число k и значение C. Необходимо вставить в список на позицию с 
индексом k элемент, равный C, сдвинув все элементы, имевшие индекс не менее k, вправо.
Посколько при этом количество элементов в списке увеличивается, после считывания списка 
в его конец нужно будет добавить новый элемент, используя метод append.

Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не 
создавая дополнительного списка.
"""
#default

print("Program insert value given by user to list on position, which given by user")



#input

row = input ("Enter a row of numbers")

list_A = row.split ()


index_number = input ("Enter index to remove and element to change")



#main

list_B = index_number.split ()


k = int ( list_B [ 0 ] )

c = int ( list_B [ 1 ] )




list_A.append( '' )



for i in range ( len ( list_A ) -  1 , k , -1 ):

    list_A [ i ] = list_A [ i - 1 ]



list_A[k] = str(c)



#output

print( " ".join ( list_A ) )
#-----------------------------------------------------------------



#task13------------------------------------------------------------
"""
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
Считается, что любые два 
элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
"""
#default
counter = 0
print("Program prints amount of pairs")




#input

row = input("Enter a row of numbers")



#main

list_a = row.split()


for i in list_a:

    for j in list_a:

        if i == j:

           counter+=1

    counter-=1



#output

print (counter // 2)
#-----------------------------------------------------------------



#task14------------------------------------------------------------
"""
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. 
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""
#default

temp = 0

print("Program prints non-repeat elements")



#input

row = input ("Please enter elements of list")



#main

list_A = row.split ()

list_new = []


for element in list_A:

    if element != temp:

        temp = element

        if list_A.count(temp) ==1:

            list_new.append(temp)



#output

print(" ".join(list_new))
#-----------------------------------------------------------------



#task15------------------------------------------------------------
"""
N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N. 
Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с номерами от 
li до ri включительно. Определите, какие кегли остались стоять на месте.
Программа получает на вход количество кеглей N и количество бросков K. Далее идет K 
пар чисел li, ri, при этом 1≤ li≤ ri≤ N.

Программа должна вывести последовательность из N символов, где j-й символ есть “I”, если 
j-я кегля осталась стоять, или “.”, если j-я кегля была сбита.
"""
#default

list_to_compare = [  ]

list_a = [  ]



#input

pin_throw = input ("Enter amount of pins and throws")



#main

N = int ( pin_throw.split() [ 0 ] )

K = int ( pin_throw.split() [ 1 ] )



for j in range (1,N+1):

    list_to_compare.append(j)

    
for i in range ( K ) :

    row = input ("Input broken interval")

    left = int ( row.split ()[0] )

    right = int ( row.split()[1] )

    for i in range (left,right+1):

        list_a.append(i)



#output

for element in list_to_compare:

    if element in list_a:

        print('.',end="")

    else:

        print('I',end="")
#-----------------------------------------------------------------



#task16------------------------------------------------------------
"""
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей. 
Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
"""
#default

list_x , list_y = [ ] , [ ]

correct = True



#input

for i in range( 8 ):

    x, y = [ int ( num ) for num in input ("Enter pair of numbers from [1..8] in format X X").split ( ) ]

    list_x.append(x)

    list_y.append(y)



#main

for i in range(8):

    for j in range(i + 1, 8):

        if list_x[i] == list_x[j] or list_y[i] == list_y[j] or abs(list_x[i] - list_x[j]) == abs(list_y[i] - list_y[j]):

            correct = False



#output

if correct:

    print('NO')

else:

    print('YES')
#-----------------------------------------------------------------