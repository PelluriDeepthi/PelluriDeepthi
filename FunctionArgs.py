#Required Arguments
def display(a, b):
    print(a, b)
display(20, 10)

#Keyword Arguments
def display(a, b):
    print(a, b)
display(b = 20, a = 10)

#Default Arguments
def display(name, course = 'Btech'):
    print(name)
    print(course)
display('Deepthi')
display('Vaishnavi', 'BTech')

#Variable Length Arguments
def display(*courses):
    for i in courses:
        print(i)
display('btech', 'inter', '10th')