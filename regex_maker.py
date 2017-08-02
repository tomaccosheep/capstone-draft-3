import random
import string

regex_dict = {'digit': '\d', 'single_char': '[a-zA-Z]'}

def regex_step_function(func_key):
    if func_key == "single_char":
        return random.choice(string.ascii_letters)
    if func_key == "digit":
        return str(random.randrange(0,10,1))

def regex_gen():
    match_num = random.randrange(1, 5, 1)
    selectme_string_list = []
    for i in range(0, match_num):
        selectme_string_list.append("")
    regex_string = ""
    for i in range(0, 4):
        regex_step = random.choice(list(regex_dict))
        regex_string += regex_dict[regex_step]
        for i in range(0, match_num):
            selectme_string_list[i] += regex_step_function(regex_step)
    return regex_string, selectme_string_list

def regex_nonselect_gen(selectme_string_list):
    nonselect_string_list = []
    for i in range(0, len(selectme_string_list) + 1):
        nonselect_string_list.append("")
        for j in range(0, random.randrange(2,10,1)):
            nonselect_string_list[i] += regex_step_function(random.choice(list(regex_dict)))
    print(str(nonselect_string_list))
    return nonselect_string_list

def regex_question():
    regex_string, selectme_string_list = regex_gen()
    nonselect_string_list = regex_nonselect_gen(selectme_string_list)
    full_string = ""
    for i in range(0, len(selectme_string_list)):
        full_string += nonselect_string_list[i]
        full_string += selectme_string_list[i]
    full_string += nonselect_string_list[-1]
    print(full_string)
    print("Find these ones: \n" + str(selectme_string_list))
    print("Answer: " + regex_string)
        

"""
Before it asks the question, it should try to use the regex on the full string, just to verify


"""
