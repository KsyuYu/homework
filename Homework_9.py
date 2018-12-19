﻿#Task_1----------------------------------------------------#

"""
    Условие
    Дан список чисел. Определите, сколько в нем встречается различных чисел.
    Примечание. Эту задачу на Питоне можно решить в одну строчку.
"""

print(len(set(input().split())))

#----------------------------------------------------------#

#Task_2----------------------------------------------------#

"""
    Условие
    Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
    Примечание. Эту задачу на Питоне можно решить в одну строчку.
"""

print(len(set(input().split()).intersection(set(input().split())))) 

#----------------------------------------------------------#

#Task_3----------------------------------------------------#

"""
    Условие
    Даны два списка чисел. Найдите все числа, которые входят как в первый, так и во второй список и выведите их в порядке возрастания.
    Примечание. И даже эту задачу на Питоне можно решить в одну строчку.
"""

print(' '.join(sorted(list(set(input().split()).intersection(set(input().split())))))) 

#----------------------------------------------------------#

#Task_4----------------------------------------------------#

"""
    Условие
    Во входной строке записана последовательность чисел через пробел.
    Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.
"""

List_A = input().split()

Set_A = set([])

for element in List_A:

    if element not in Set_A:

        print("NO")

        Set_A.add(element) 
    else:

        print("YES")



#----------------------------------------------------------#

#Task_5----------------------------------------------------#


"""
    Условие
    Аня и Боря любят играть в разноцветные кубики, причем у каждого из них свой набор и в каждом наборе все кубики различны по цвету.
    Однажды дети заинтересовались, сколько существуют цветов таких, что кубики каждого цвета присутствуют в обоих наборах.
    Для этого они занумеровали все цвета случайными числами от 0 до 108. На этом их энтузиазм иссяк, поэтому вам предлагается помочь им в оставшейся части.
    В первой строке входных данных записаны числа N и M — число кубиков у Ани и Бори.
    В следующих N строках заданы номера цветов кубиков Ани.
    В последних M строках номера цветов Бори.
    Найдите три множества: номера цветов кубиков, которые есть в обоих наборах; номера цветов кубиков, которые есть только у Ани и номера цветов кубиков, которые есть только у Бори. Для каждого из множеств выведите сначала количество элементов в нем, а затем сами элементы, отсортированные по возрастанию.
"""


String_len = input().split()

N_colors = int(String_len[0])

M_colors = int(String_len[1])


Colors_List_N = [input() for i in range(N_colors)]

Colors_List_M = [input() for j in range(M_colors)]


print(len(set(Colors_List_N).intersection(set(Colors_List_M)))) 
print(' '.join(sorted(list(set(Colors_List_N).intersection(set(Colors_List_M))))))


print(len(set(Colors_List_N).difference(set(Colors_List_M))))

print(' '.join(sorted(list(set(Colors_List_N).difference(set(Colors_List_M))))))


print(len(set(Colors_List_M).difference(set(Colors_List_N))))

print(' '.join(sorted(list(set(Colors_List_M).difference(set(Colors_List_N))))))



#----------------------------------------------------------#

#Task_6----------------------------------------------------#


"""
    Условие
    Дан текст: в первой строке записано число строк, далее идут сами строки. Определите, сколько различных слов содержится в этом тексте.
    Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.
"""



Count_of_strings = int(input())

List_A = []

for i in range(Count_of_strings):

    for element in input().split():

        List_A.append(element)

        

print(len(set(List_A)))



#----------------------------------------------------------#

#Task_7----------------------------------------------------#


"""
    Условие
    Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n. Беатриса пытается угадать это число, для этого она называет некоторые множества натуральных чисел. Август отвечает Беатрисе YES, если среди названных ей чисел есть задуманное или NO в противном случае. После нескольких заданныъх вопросов Беатриса запуталась в том, какие вопросы она задавала и какие ответы получила и просит вас помочь ей определить, какие числа мог задумать Август.
    В первой строке задано n - максимальное число, которое мог загадать Август. Далее каждая строка содержит вопрос Беатрисы (множество чисел, разделенных пробелом) и ответ Августа на этот вопрос.
    Вы должны вывести через пробел, в порядке возрастания, все числа, которые мог задумать Август.
"""


Max_num = int(input())

answer = ""

Set_A = set([])

ask = [""]


while True:

    ask = input().split()

    if ask[0] == "HELP":

        break

    answer = str(input())

    if answer == "YES":

        Set_A.update(set(ask))

    else:

        Set_A.difference_update(set(ask))

        
print(' '.join(sorted(list(Set_A))))



#----------------------------------------------------------#