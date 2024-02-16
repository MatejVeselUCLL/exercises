def word_count(string):
    if string in ["", " "]:
        return 0
    return len(string.split(" "))

# print(word_count(" "))