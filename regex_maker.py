import random
import string

regex_dict = {'digit': '\d', 'single_char': '[abc]'}


def regex_gen_digit(selectme_string):
    return str(random.randrange(0,10,1))

def regex_gen_single_char(selectme_string, regex_string):
    return random.choice(string.ascii_letters)

def regex_gen():
    match_num = random.randrange(1, 5, 1)
    selectme_string_list = []
    for i in range(0, match_num):
        selectme_string_list[i] = ""
    regex_string = ""
    for i in range(0, 10):
        regex_step = random.choice(list(regex_dict))
        if regex_step == "single_char":
            for i in range(0, match_num):
                regex_string += '[abc]'
                selectme_string_list[i] += regex_gen_single_char(selectme_string)
        elif regex_step == "digit":
            regex_string += '\d'
            selectme_string, regex_string = regex_gen_digit(selectme_string, regex_string)
    print(selectme_string + '\n' + regex_string)
