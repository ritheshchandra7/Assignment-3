def rev_string(string):
    rev_str=" "
    
    rev_str+= string[-1::-1]
    return rev_str
print(rev_string("1234abcd"))