

def word_reverse(input_string):
    
    return_string = ""
    list_of_split_strings = input_string.split(" ")

    for word in list_of_split_strings:
        if len(word) <= 5:
            return_string += word
        else:
            return_string += word[::-1]
        return_string += " "

    return return_string.strip()

