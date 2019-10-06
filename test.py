import re
def count_substring(string, sub_string):
    print(re.findall(sub_string,string,overlap = True))

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)