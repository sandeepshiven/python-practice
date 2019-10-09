def find_replace2(filename, word, replacement):
    with open('test.txt','r+') as file:
        words = file.read()
        text = words.replace(word,replacement)
        file.seek(0)
        file.write(text)
        file.truncate()
    with open('alice.txt','w+') as file2:
        file2.write(text)

find_replace2('test.txt', 'Alice','Colt')
