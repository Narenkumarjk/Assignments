=============================================================================
#Get two integers from user
#print multiples of 17 between two numbers

def func_get_data():
    Var1 = int(input("Enter Start Value:"))
    Var2 = int(input("Enter End Value:"))
    return Var1,Var2

def func_find_multiples(Var1,Var2):
    inc=1
    if Var1 > Var2:
        inc = -1

    for i in range(Var1, Var2 + inc, inc):
        if i % 17 == 0 and i!=0:
            print(i)

Var1, Var2=func_get_data()
func_find_multiples(Var1,Var2)

=============================================================================
#Remove duplicates from list without using set function

lst1=[]
lst=[]

def func_get_data():
    cntr = int(input("Enter no of records to be added:"))
    for i in range(cntr):
        lst.append(int(input("Enter the Value:")))
    return lst

def func_del_dup(lst):
    for i in lst:
        if i not in lst1:
            lst1.append(i)
    return lst1


print(func_del_dup(func_get_data()))

=============================================================================

#Get list of values from user through while loop

cntr = int(input("Enter the number of entries to be added: "))
i=0
lst=[]
while i < cntr:
    lst.append(input("Enter Value:"))
    i = i+1

print(lst)

=============================================================================


# Multiples of a number  Get one number from user
# 3 ==> [1,3]
# 5 ==> [1,5]
# 9 ==> [1,3,9]
# 20 ===> [1,2,4,5,10,20]

_flag = 'Y'
multiple_lst=[]

def func_find_multiple(cntr):
    inc =1
    if cntr < 0:
        inc = -1
    for i in range(inc, cntr + inc,inc):
        if cntr % i == 0:
            multiple_lst.append(i)

    print(multiple_lst)
    _flag =  str(input("Do you Wish to Continue: ")).upper()
    return _flag


while _flag !='N':
    cntr = int(input("Enter a Value:"))
    multiple_lst.clear()
    _flag = func_find_multiple(cntr)


=============================================================================

#Collect two strings from user
#Check whether both are anagrams or not

def get_data():
    lst = []
    global tup
    for i in range(2):
        lst.append(input("Enter String: "))
    tup = tuple(lst)

get_data()
if sorted(tup[0].upper()) == sorted(tup[1].upper()):
    print("String 1 & String 2 are anagrams")
else:
    print("String 1 & String 2 are NOT anagrams")

=============================================================================
 










