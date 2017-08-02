import random
import string

regex_dict = {'digit': '\d', 'single_char': '[a-zA-Z]', 'space': '\s'}

def regex_step_function(func_key):
    if func_key == "single_char":
        return random.choice(string.ascii_letters)
    elif func_key == "digit":
        return str(random.randrange(0,10,1))
    elif func_key == 'space':
        return ' '

def compress_indicies(regex_list):
    regex_string = ""
    regex_list_compressed = []
    how_many_indicies = 1
    compress_to_do = False
    print(str(regex_list))
    for i in range(0, len(regex_list)):
        if i == len(regex_list) - 1:
            if compress_to_do:
                compressed_string = regex_list[i] + "{" + str(how_many_indicies)  + "}"
                regex_list_compressed.append(compressed_string)
            else:
                regex_list_compressed.append(regex_list[i])
        elif regex_list[i] != regex_list[i+1]:
            if compress_to_do:
                compressed_string = regex_list[i] + "{" + str(how_many_indicies) + "}"
                regex_list_compressed.append(compressed_string)
                how_many_indicies = 1
                compress_to_do = False
            else:
                regex_list_compressed.append(regex_list[i])
        else:
            how_many_indicies += 1
            compress_to_do = True
    return regex_list_compressed

def regex_gen():
    match_num = random.randrange(1, 5, 1)
    selectme_string_list = []
    for i in range(0, match_num):
        selectme_string_list.append("")
    regex_list = []
    for i in range(0, 4):
        regex_step = random.choice(list(regex_dict))
        regex_list.append(regex_dict[regex_step])
        for i in range(0, match_num):
            selectme_string_list[i] += regex_step_function(regex_step)
    return compress_indicies(regex_list), selectme_string_list

def regex_nonselect_gen(selectme_string_list):
    nonselect_string_list = []
    for i in range(0, len(selectme_string_list) + 1):
        nonselect_string_list.append("")
        for j in range(0, random.randrange(2,10,1)):
            nonselect_string_list[i] += regex_step_function(random.choice(list(regex_dict)))
    print(str(nonselect_string_list))
    return nonselect_string_list

def regex_question():
    regex_list, selectme_string_list = regex_gen()
    nonselect_string_list = regex_nonselect_gen(selectme_string_list)
    full_string = ""
    for i in range(0, len(selectme_string_list)):
        full_string += nonselect_string_list[i]
        full_string += selectme_string_list[i]
    full_string += nonselect_string_list[-1]
    print(full_string)
    print("Find these ones: \n" + str(selectme_string_list))
    print("Answer: " + str(regex_list))
        

"""
Before it asks the question, it should try to use the regex on the full string, just to verify
I need to make a regex shortener, which means that it should be kept as a list, not a string

"""
