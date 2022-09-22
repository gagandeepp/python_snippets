from cgi import test
import keyword

def main():
    name  = input("Enter your name: ")
    print(f"Hello World {name}!")
   
    # Dictionary
    mydict = {0:'India',1:'Pak',2:'Eng'}
    print(mydict)
    
    
    a=10;b=20;c='my var'
    print(a,b,c)
    
    # *args for variable number of arguments
    
    def myFun(*argv):
        for arg in argv:
            print(arg)

    myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
    
    
    # *kwargs for variable number of keyword arguments
    def myFun(**kwargs):
        for key, value in kwargs.items():
            print("%s == %s" % (key, value))
            
    # Driver code
    myFun(first='Geeks', mid='for', last='Geeks')
    
    #python keywords
    print(keyword.kwlist)
    lst1 = keyword.kwlist
    kw = input("Enter keyword:")
    
    #Ternary operator
    print("yes") if kw in lst1 else print("no")
    
    x, y, z = input("Enter three values: ").split()
    print("Total number of students: ", x)
    print("Number of boys is : ", y)
    print("Number of girls is : ", z)
    print() 
    
    # reverse string
    mystr = 'mary had a little lamb'
    print(*mystr)
    print(mystr[::-1])
    
    #slice string
    print(mystr[3:6])   
    
    # Printing characters between 3rd and 2nd last character
    print("\nSlicing characters between " +"3rd and 2nd last character: ")
    print(mystr[3:-2])
    
    x = input("Enter anything:")
    print("number") if (type(x) is int) else print ("not a number")
    
    
    cube_v2 = lambda x : x*x*x

    print(cube_v2(7))

    
    '''
    Iterable is an object, that one can iterate over. 
    It generates an Iterator when passed to iter() method. 
    An iterator is an object, which is used to iterate over an iterable object using the __next__() method. 
    Iterators have the __next__() method, which returns the next item of the object.
    '''
    testStr = 'helloWorld'
    
    #testStr is iterable
    #myitr is iterator
    
    myitr = iter(testStr)
    print(next(myitr))

if __name__ == "__main__":
    main()
    