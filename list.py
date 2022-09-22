def list_ops():
    lst = ['a','b',123,45.0,'hellow','a','b','hellow']
    print(*lst)
    
    print("List Iteration")
    l = ["geeks", "for", "geeks"]
    for i in l:
        print(i)
    
    
    list2 = ["geeks", "for", "geeks"]
    for index in range(len(list2)):
        print(list2[index])

    fruits = ["apple", "orange", "kiwi"]
 
    # Creating an iterator object
    # from that iterable i.e fruits
    iter_obj = iter(fruits)
    
    # Infinite while loop
    while True:
        try:
            # getting the next item
            fruit = next(iter_obj)
            print(fruit)
        except StopIteration:
        
            # if StopIteration is raised,
            # break from loop
            break
    
    
    cars = ["Aston", "Audi", "McLaren "]
    for i, x in enumerate(cars):
        print(str(i)+ ": " +x)
        
     # Two separate lists
    cars = ["Aston", "Audi", "McLaren"]
    accessories = ["GPS", "Car Repair Kit",
               "Dolby sound kit"]
 
    # Combining lists and printing
    for c, a in zip(cars, accessories):
        print(f"Car: {c}, Accessory required: {a}")
    
'''
Create List 
Time Complexity: O(1)
Space Complexity: O(n)

Accessing list
Time Complexity: O(1)
Space Complexity: O(1)

Append List List.append(3) - value
Time Complexity: O(1)
Space Complexity: O(1)

Insert List  List.insert(3, 12) - position and value
Time Complexity: O(n)
Space Complexity: O(1)


Deleting remove method
Time Complexity: O(n)
Space Complexity: O(1)


Time Complexity: O(1)/O(n) (O(1) for removing the last element using pop, 
O(n) for removing the first and middle elements)

Space Complexity: O(1)



'''