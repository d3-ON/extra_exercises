def run():
    stop = False
    list_words = []
    
    while stop == False:
        word = input('Enter a word: ')

        if word == '***':
            stop = True
        else:
            if word not in list_words:
                list_words.append(word)

    print(list_words)

if __name__ == '__main__':
    run()