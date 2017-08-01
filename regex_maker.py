import random
import string

regex_dict = {'digit': '\d', 'single_char': '[abc]'}


def regex_gen_digit(unfiltered, regex_string):
    regex_string += '\d'
    unfiltered += str(random.randrange(0,10,1))
    return unfiltered, regex_string

def regex_gen_single_char(unfiltered, regex_string):
    regex_string += '[abc]'
    unfiltered += random.choice(string.ascii_letters)
    return unfiltered, regex_string
    

def regex_gen():
    unfiltered = ""
    regex_string = ""
    for i in range(0, 10):
        regex_step = random.choice(list(regex_dict))
        if regex_step == "single_char":
            unfiltered, regex_string = regex_gen_single_char(unfiltered, regex_string)
        elif regex_step == "digit":
            unfiltered, regex_string = regex_gen_digit(unfiltered, regex_string)
    print(unfiltered + '\n' + regex_string)
