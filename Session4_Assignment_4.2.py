def len_of_words(speakup):
    length=[]
    for i in speakup:
        length.append(len(i))
        return length

def len_of_each_words(speakup):
    return [len(i) for i in speakup]
    
if __name__ == "__main__":
    speakup = ['I','Hello','King','Maker','Always','Bengalurur','Place']
    print(len_of_each_words(speakup))
