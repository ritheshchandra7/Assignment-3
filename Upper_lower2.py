def count_letters(string):
    upper=0
    lower=0
    for t in string:
        for i in t:
            if i.isupper():
                upper+=1
            elif i.islower():
                lower+=1
    print("No. of Upper case characters",upper)
    print("No. of Lower case characters",lower)
count_letters('The quick Brow Fox')