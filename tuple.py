def mytuple():
    Tuple1 = ()
    print(f"Initial empty Tuple:{Tuple1} ")
    
    # Creating a Tuple
    # with the use of string
    Tuple1 = ('Geeks', 'For')
    print("\nTuple with the use of String: ")
    print(Tuple1)
    
    # Creating a Tuple with
    # the use of list
    list1 = [1, 2, 4, 5, 6]
    print("\nTuple using List: ")
    print(tuple(list1))
    
    # Creating a Tuple
    # with the use of built-in function
    Tuple1 = tuple('Geeks')
    print("\nTuple with the use of function: ")
    print(Tuple1)
    
    Tuple1 = (0, 1, 2, 3, 4)
    del Tuple1
    print(Tuple1)
    


'''
Tuples are immutable, and usually, they contain a sequence of heterogeneous elements that are accessed 
via unpacking or indexing (or even by attribute in the case of named tuples)
'''

'''
Accessing Tuple

Time complexity: O(1)
Space complexity: O(1)

Concat
Time Complexity: O(1)
Auxiliary Space: O(1)

Complexities for traversal/searching elements in tuples:
Time complexity: O(1)
Space complexity: O(1)


'''