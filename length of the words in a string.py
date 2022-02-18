#To print even length words in a string
def s(words):
    words=words.split(' ')
    for word in words:
        if len(word)%2==0:
            print(word)

s('hi hello python')