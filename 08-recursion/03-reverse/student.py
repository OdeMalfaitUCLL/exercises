def reverse_from_left(text):
    if len(text) == 0:
        return text
    else:
        result = text[0]
        return reverse_from_left(text[1:]) + result

def reverse_from_right(text):
    if len(text) == 0:
        return text
    else:
        result = text[-1]
        return result + reverse_from_right(text[:-1])
    
print(reverse_from_right("abcd"))
print(reverse_from_left("abcd"))