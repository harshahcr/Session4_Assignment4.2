#Character in vowel..
def vowl(eng_string):
    vowels = ('a','e','i','o','u','A','E','I','O','U')
    if eng_string not in vowels:
        return False
    return True

if __name__=="__main__":
    print(vowl('a'))
    print(vowl('A'))
    print(vowl('f'))
    print(vowl('X'))
    print(vowl('I'))
