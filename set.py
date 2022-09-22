'''
In Python, a Set is an unordered collection of data types that is iterable, mutable and has no duplicate elements. 
The order of elements in a set is undefined though it may consist of various elements. 
The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for 
checking whether a specific element is contained in the set.


Frozen sets in Python are immutable objects that only support methods and operators that produce a result without affecting the frozen set or sets to which they are applied. 
'''

def mysaet():
    set1 = set()
    print("Initial blank Set: ")
    print(set1)
    
    # Creating a Set with
    # the use of a String
    set1 = set("GeeksForGeeks")
    print("\nSet with the use of String: ")
    print(set1)
    
    # Creating a Set with
    # the use of Constructor
    # (Using object to Store String)
    String = 'GeeksForGeeks'
    set1 = set(String)
    print("\nSet with the use of an Object: " )
    print(set1)
    
    # Creating a Set with
    # the use of a List
    set1 = set(["Geeks", "For", "Geeks"])
    print("\nSet with the use of List: ")
    print(set1)
    
    set1.add(8)
    set1.add(9)
    set1.add((6, 7))
    
    set1 = set([4, 5, (6, 7)])
    set1.update([10, 11])
    
    set1 = set([1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12])
    print("Initial Set: ")
    print(set1)
    
    # Removing elements from Set
    # using Remove() method
    set1.remove(5)
    set1.remove(6)
    print("\nSet after Removal of two elements: ")
    print(set1)
    
    # Removing elements from Set
    # using Discard() method
    set1.discard(8)
    set1.discard(9)
    print("\nSet after Discarding two elements: ")
    print(set1)
    set1.pop()
    # Removing all the elements from
    # Set using clear() method
    set1.clear()
    
    String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r')
    Fset1 = frozenset(String)
    print("The FrozenSet is: ")
    print(Fset1)