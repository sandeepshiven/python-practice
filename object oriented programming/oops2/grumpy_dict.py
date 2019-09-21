class GrumpyDict(dict):

    def __repr__(self):
        print("None of your business")
        return super().__repr__()

    def __missing__(self,key):
        print(f"You want {key}? Well it ain't here!")
    
    def __setitem__(self,key,value):
        print("You want to change the dictionary?")
        print("OK fine...")
        super().__setitem__(key,value)


data = GrumpyDict({'first':'Tom','animal':'cat'})
print(data)
data['city']
data['city'] = 'Indore'
print(data)





