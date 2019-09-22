from random import choice

def greet(person):
    def get_mood():
        msg = choice(('Hello',"Go away","Yo bro"))
        return msg

    result = get_mood() + person
    return result

print(greet(' Sandeep'))