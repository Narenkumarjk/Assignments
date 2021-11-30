import json
import random

with open('Sample.json','r') as infile:
    dict1 = json.load(infile)

    number_of_question = 0
    Correct_Answers = 0
    new_list =list()
    Dict2 = {}

    def get_usr_data():
        try:
            var1 = int(input("How many Questions you want to answer ? "))
            print("====================================================")
        except ValueError:
            print("your input is not correct please retry.")
            var1 = get_usr_data()
        return var1

    def generate_list_of_questions():
        list1 =list()
        for a, b in dict1.items():
            for lines in b:
                for key, value in lines.items():
                    if key[0:8] == 'question':
                        list1.append(key)

        li1=random.sample(list(list1), number_of_question)
        return li1

    def get_user_answers(NO_OF_Options):
        try:
            ans = int(input("Enter you Answer for above Question: "))
            print("====================================================")
            print("====================================================")
            if ans not in range(1,NO_OF_Options+1):
                print("please enter a value between 1 and ", NO_OF_Options)
                ans = get_user_answers(NO_OF_Options)
                print("====================================================")
                print("====================================================")
        except ValueError:
            print("Enter value between 1 & ", NO_OF_Options)
            ans = get_user_answers(NO_OF_Options)
            print("====================================================")
            print("====================================================")
        return ans

    def read_dict():
        for key, value in dict1.items():
            for lines in value:
                y = list((lines.keys()))[0]
                if y in list1:
                    Dict2 = {}
                    Dict2.update(lines)
                    for i, j in lines.items():
                        if i[0:8] == 'question':
                            print(j)
                            keys = ("your answer")
                        elif i == 'options :':
                            NO_OF_Options = len(j)
                            for z in j:
                                print(z)
                            print("====================================================")
                        else:
                            user_answer = get_user_answers(NO_OF_Options)
                            Dict2[keys] = user_answer
                            new_list.append(Dict2)


    def revisit():
        for j in new_list:
            for key, value in j.items():
                if key[:8] == 'question':
                    print(value)
                    print("====================================================")
                elif key == 'options :':
                    NO_OF_Options = len(j)
                    for z in value:
                        print(z)
                    print("====================================================")
                else:
                    if key[:4] == 'your':
                        print(key, value)
                        print("====================================================")
                        if (input("do you want to change your answer : Y/N ?")).upper() == 'Y':
                            print("====================================================")
                            j[key] = get_user_answers(NO_OF_Options)



    number_of_question = get_usr_data()
    list1 = generate_list_of_questions()
    read_dict()
    re_visit = input("Do you want to revisit the questions ?  y/n: ").upper()
    print("====================================================")
    if re_visit == 'Y':
        revisit()

    for all_items in new_list:
        for key, value in all_items.items():
            if all_items["your answer"] == all_items["answer"]:
                Correct_Answers = Correct_Answers + 1
                break

    print("You Scored: ",  round((Correct_Answers/number_of_question)*100,2) , '%')
    print("====================================================")

















