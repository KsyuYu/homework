#task1----------------------------------------------
"""По данному целому числу 
N распечатайте все квадраты натуральных чисел, 
не превосходящие N, в порядке возрастания. """

#default
i = 1


#input
user_number = int ( input ( "Enter integer number" ) )


#validation
if type(user_number)!=int:

    print("Incorrect type")

#main and output
while ( i*i ) <= user_number:

    print( i*i )
    
    i += 1
#---------------------------------------------------


#task2----------------------------------------------
"""Дано целое число, не меньшее 2. Выведите его 
наименьший натуральный делитель, отличный от 1. """

#defaults and input
Nunber = int ( input ( "Enter a number greater than 2" ))

i = Number

min_divider = Number

#validation
if type(Number)!=int and Number<2:
    print( "Input error" )

#main
while i > 1:

    if Number % i == 0:

        min_divider = i

    i -= 1


#output
print( min_divider )
#---------------------------------------------------


#task3----------------------------------------------
"""По данному натуральному числу N найдите наибольшую целую степень двойки, 
не превосходящую N. Выведите показатель степени и саму степень.
Операцией возведения в степень пользоваться нельзя! """

#defaults
i = 1

power = 0

#input
Number = int ( input ("Enter an integer maximum number greater than zero") )


#validation
if type(Number)!=int and Number<0:
    print( "Incorrect input" ) 

#main
while i <= Number :

    i = i*2

    power += 1


#output
print( power-1, i-i//2 )
#---------------------------------------------------


#task4----------------------------------------------
"""В первый день спортсмен пробежал x километров, а 
затем он каждый день увеличивал пробег на 10% от 
предыдущего значения. По данному числу y определите 
номер дня, на который пробег спортсмена составит 
не менее y километров.
Программа получает на вход действительные числа 
x и y и должна вывести одно натуральное число. """

#default
days = 1

#input
km_first_day = float ( input ( "How many kilometers you ran?" ) )

user_km= float ( input ( "How many kilometers you can run?" ))


#main
while km_first_day < user_km:

    km_first_day = km_first_day (1+0.1)

    days += 1


#output
print ( "You will have ",user_km," earlier then ",days," days" )
#---------------------------------------------------


#task5----------------------------------------------
"""Вклад в банке составляет x рублей. Ежегодно он 
увеличивается на p процентов, после чего дробная часть 
копеек отбрасывается. Определите, через сколько лет 
вклад составит не менее y рублей.
Выражение «дробная часть копеек отбрасывается» означает, 
что если у вас оказалось 123.4567 рублей, т. е. 123 
рубля и 45.67 копеек, то после округления у вас 
получится 123 рубля и 45 копеек, т.е. 123.45 рублей.
Программа получает на вход три натуральных числа: 
x, p, y и должна вывести одно целое число. """

#defaults
years = 0


#input
contrib = float ( input ("Enter please your contribution" ) )

perc = float ( input ( "Enter your percents from 1 to 100" ) )

user_value = float ( input( "What is the maximum value?" ) )

#main
while contrib < user_value :

    contrib = contrib * ( 1 + perc/100 )

    contrib = ( contrib*100 ) // 1 / 100

    years += 1


#output
print(years," years later")
#---------------------------------------------------


#task6----------------------------------------------
"""Программа получает на вход последовательность целых неотрицательных чисел, 
каждое число записано в отдельной строке. Последовательность завершается числом 0, 
при считывании которого программа должна закончить свою работу и вывести 
количество членов последовательности (не считая завершающего числа 0). 
Числа, следующие за числом 0, считывать не нужно."""

#defaults
length = 0

user_number = 1


#input,validation and main
while user_number != 0 :

    user_number = int ( input ( "Please, enter non-negative integer" ) )

    if user_number < 0 or type ( user_number ) != int :

        length = length
        print ( "Input error")
    else:

        length += 1


#output
print ( "Length of sequence is ", length-1 )
#---------------------------------------------------


#task7----------------------------------------------
"""Определите сумму всех элементов последовательности, 
завершающейся числом 0. В этой и во всех следующих 
задачах числа, следующие за первым нулем, учитывать не нужно. """

#defaults
sum = 0

number = 1


#input and main
while number != 0:

    number = int ( input ("Enter a number") )

    sum += number


#output
print("Sum of elements in sequence is ", sum-number)
#---------------------------------------------------


#task8--------------------------------------------— 
"""Определите среднее значение всех элементов последовательности, завершающейся числом 0.""" 

#defaults
average = 0

element = 1

counter = 0

sum = 0

#input and main


while element != 0:

    element = int ( input () ) 

    counter += 1

    sum += element

    average = sum/counter

counter -= 1


#output
print("Average value is ", sum/counter )
#---------------------------------------------------


#task9--------------------------------------------— 
"""Последовательность состоит из натуральных чисел 
и завершается числом 0. Определите значение
 наибольшего элемента последовательности. """

#defaults
element = 1

max = 0 


#input and main
while element != 0:

    element = int ( input ( "Enter an integer greater than zero number" ) )

    if element > max:

        max = element

    else:

        max = max


#output
print("Maximum in sequence is ",max)
#---------------------------------------------------


#task10--------------------------------------------— 
"""Последовательность состоит из натуральных чисел и 
завершается числом 0. Определите индекс наибольшего 
элемента последовательности. 
Если наибольших элементов несколько, выведите индекс 
первого из них. Нумерация элементов начинается с нуля. """

#defaults
number = 1

max = 0

index = -1

index_max = 0


#input an main
while number != 0:

    number = int ( input ("Enter an integer greater than 0 element") )

    index += 1

    if number > max:

        max, index_max = number, index

    else:

        max = max


#output
print( index_max, " is an index of maximum in sequence")
#---------------------------------------------------


#task11--------------------------------------------— 
"""Определите количество четных элементов в 
последовательности, завершающейся числом 0. """

#defaults
number = 1

counter = 0


#input and main
while number != 0:

    number = int ( input () ) 

    if number % 2 == 0:

        counter += 1


#output
print( counter-1 ," numbers are even")
#---------------------------------------------------


#task12--------------------------------------------— 
"""Последовательность состоит из натуральных чисел 
и завершается числом 0. Определите, сколько 
элементов этой последовательности больше предыдущего элемента. """

#default
number = 1

counter = 0


#input and main
prev_to_number = int ( input ("Enter an element") )

while number != 0:

    number = int ( input ("Enter the next element") )

    if number > prev_to_number:

        counter += 1

    prev_to_number = n
umber

#output
print( counter ," elements greater than their previous")
#---------------------------------------------------


#task13--------------------------------------------—
"""Последовательность состоит из различных натуральных 
чисел и завершается числом 0. Определите значение 
второго по величине элемента в этой последовательности.
Гарантируется, что в последовательности есть хотя бы два элемента. """

#input
first_max = int(input("Enter please an integer greater than zero number"))

second_max = int(input("... once more"))


#main
if first_max < second_max:

    first_max, second_max = second_max, first_max

element = int(input("Enter an integer greater than zero number"))

while element != 0:

    if element > first_max:

        second_max, first_max = first_max, element

    elif element > second_max:

        second_max = element

    element = int(input("Enter an integer greater than zero number"))


#output
print(second_max, " is a second largest value")
#---------------------------------------------------


#task14----------------------------------------------
"""Последовательность состоит из натуральных чисел и завершается 
числом 0. Определите, сколько элементов этой последовательности 
равны ее наибольшему элементу. """

#defaults
maximum = 0

num_max = 0

element = -1


#input and main
while element != 0:

    element = int(input("Enter please a number"))

    if element > maximum:

        maximum, num_max = element, 1

    elif element == maximum:

        num_max += 1


#output
print("We have ", num_max," elements like maximum in sequence")
#---------------------------------------------------


#task15----------------------------------------------
"""Последовательность Фибоначчи определяется так:
φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
По данному числу n определите n-е число Фибоначчи φn.
Эту задачу можно решать и циклом for. """

#defaults
fib=1

position = 1

fib_next = 1

fib_prev = 0


#input
n=int(input("Enter a number of element in fibonacci sequence"))


#validation and main; output
if n==0:

    print(0)

else:

    while position < n:

        fib = fib_prev+fib_next

        fib_prev=fib_next

        fib_next=fib

        position+=1

    print("This number has element ",fib_next)
#---------------------------------------------------


#task16----------------------------------------------
"""Дано натуральное число A. Определите, 
каким по счету числом Фибоначчи оно является, то 
есть выведите такое число n, что φn = A. Если А не 
является числом Фибоначчи, выведите число -1. """
#defaults
fibonacci_current_number=1
fibonacci_next_number=1
position=2;
fibonacci_numbers="1"+" "+"1"
 
#input
A=int(input("Enter an integer a"))
 
#main
while fibonacci_next_number<=A:
    if fibonacci_next_number==A:
        break
 
    fibonacci_sum=fibonacci_current_number+fibonacci_next_number
    fibonacci_current_number=fibonacci_next_number
    fibonacci_next_number=fibonacci_sum
 
    position+=1
 
    fibonacci_numbers+=" "+str(fibonacci_next_number)
else:
    position=-1
 
#ouput
print(position)
#---------------------------------------------------


#task17----------------------------------------------
"""Дана последовательность натуральных чисел, завершающаяся 
числом 0. Определите, какое наибольшее число подряд идущих 
элементов этой последовательности равны друг другу. """

#defaults
count = 0
max_count = 0

#input
num=int(input("Enter please a number"))    
prev = num

#main and input
while num != 0:
    if num == prev:
        count+=1
    else:
        count = 1 
        prev = num  
    if count > max_count:
        max_count = count  
    num=int(input("Enter please a number"))

#output
print("Maximum ", max_count, " elements are equal")  
#---------------------------------------------------


#task18----------------------------------------------
"""Дана последовательность натуральных чисел x1x1, x2x2, ..., xnxn. Стандартным отклонением называется величина
σ=(x1−s)2+(x2−s)2+…+(xn−s)2n−1−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−√
σ=(x1−s)2+(x2−s)2+…+(xn−s)2n−1
где s=x1+x2+…+xnns=x1+x2+…+xnn — среднее арифметическое последовательности.

Определите стандартное отклонение для данной последовательности натуральных чисел, завершающейся числом 0. """

#defaults
from math import sqrt
sum_x=0

sum_sqr=0

counter=0


#input and main
x=int(input())
while x !=0:

    sum_x+=x

    sum_sqr+=x**2

    counter+=1

    x=int(input())

av=sum_x/counter

ci=sqrt((sum_sqr-2*av*sum_x+counter*av*av)/(counter-1))


#output
print(ci)
#---------------------------------------------------