def rotate_loop():
    arr = [1,2,3,4,5,6,7]
    n =2
    for i in range(n):
        last = arr[i]
        arr[i]=arr[i+1]
        arr[len(arr)]=last
        i+=1
    print(arr)
    
def rotate_temp():
    my_list=[1,2,3,4,5,6,7]
    n =2
    temp = my_list[n::]
    temp.extend(my_list[0:n]) 
    my_list = temp
    del temp 
    print(my_list)


def reverse_list():
    my_list = [1,2,3,4,5,6,7]
    my_list.reverse()
    print(my_list)
    chunk1 = my_list[-2:]
    chunk2 = my_list[:-2]
    chunk1.reverse()
    chunk2.reverse()
    print(chunk2+chunk1)

     
if __name__=="__main__":
    reverse_list()