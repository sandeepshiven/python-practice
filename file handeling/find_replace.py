def find_replace(filename, word, replacement):
    with open('test.txt','r') as file:
        words = file.read()
        for i in range(len(words)):
            flag = 0
            temp = ''
            try:
                if words[i] == word[0]:
                    for j in range(len(word)):
                        if words[i+j] == word[j]:
                            temp += word[j]
                        else:
                            break
                    if temp == word:
                        flag = 1
            except:
                break
            if flag:
                words = words[:i] + replacement +words[i+len(word):]
    with open('test.txt','w') as file:
        file.write(words)

find_replace('test.txt',"Sandeep", "Alice")
