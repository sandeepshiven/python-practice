def be_polite(fn):
    def wrapper():
        print("Hi! there")
        fn()
        print("Goodbye!\n")
    
    return wrapper


@be_polite
def name():
    print("Sandeep Shiven")
@be_polite
def not_polite():
    print("Idiot")


name()

not_polite()


# if we didn't use decorator the we had to do this

def name1():
    print("Sandeep Shiven")

def not_polite1():
    print("Idiot")

# we use decorators for avoiding this
sandy = be_polite(name1)
sandy()

idi = be_polite(not_polite1)
idi()
