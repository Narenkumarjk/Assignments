
#Get list of strings from user
#separate it two list (with same first letter and last letter and othr)

lst= ["garg", "kohli", "rohitr", "ishan", "dhoni","dad"]
first_lst =[]
second_lst = []

for i in lst:
    if i[0] == i [-1]:
        first_lst.append(i)
    else:
        second_lst.append(i)

print(first_lst)
print(second_lst)


#################################################################

#Get list of strings from user
#separate it in to two lists with vowles and non vowels

_flag = 'y'
lst = []
vowel_list =[]

while _flag != 'N':
    lst.insert( 0,input("Enter Value:"))
    _flag = input("do you want to add more: ")
    
for x in lst:
    for i in range(len(x)):
        if(x[i]) in ('a','e','i','o','u'):
            vowel_list.insert(0, x)
            break

new_set = set(vowel_list)
set1 = set(lst)
set1.symmetric_difference_update(new_set)
lst = list(set1)

print("Non Vowels", lst)
print("Vowels", vowel_list)

#################################################################
#################################################################
