my_str = """dttfghn dtt oujkk drtgn drtee hyui ftyy in pikkn"""
def count_words(string):
    for word in string.split():
        if word.endswith("n") == True:
            print(word,":",string.count(word))
count_words(my_str)
