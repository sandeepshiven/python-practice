def count_lines():
    with open('test.txt','r') as file:
        lines = len(file.readlines())
    return lines

def count_words():
    with open('test.txt','r') as file:
        words = file.read()
    
    words = words.split('\n')
    length =0
    for i in words:
        length += len(i.split())
    return length
  
def count_characters():
    with open('test.txt','r') as file:
        char = file.read()
    char = list(char)
    return len(char)

def statistics():
    lines = count_lines()
    words = count_words()
    characters = count_characters()
    return {'lines':lines,"words":words,"characters":characters }


result = statistics()
print(result)

def statistics2():
    with open('test.txt','r') as file:
        lines = file.readlines()

    return {"lines":len(lines),
            "words": sum(len(line.split()) for line in lines),     
            "characters": sum(len(line) for line in lines)
}

result2 = statistics()
print(result2)


