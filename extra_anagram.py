def run():
    word_1 = input('Enter the firts word: ')
    word_2 = input('Enter the second word: ')
    count = 0
    
    for i in word_1:
        if i in word_2:
            count += 1

    if count == len(word_1):
        print('The words are anagrams')
    else:
        print('The words not are anagrams')

if __name__ == '__main__':
    run()