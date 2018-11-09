my_str = """most of latest projects in this monotonomous world  are most  mesmerising"""
def count_words(string):
    for word in string.split():
        if word.startswith("m") == True:
            print(word,":",string.count(word))
count_words(my_str)
