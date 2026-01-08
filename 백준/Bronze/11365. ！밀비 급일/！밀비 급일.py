while True:
    sentence = input()
    
    if sentence == 'END':
        break
    else:
        sentence = sentence[::-1]
        print(sentence)

