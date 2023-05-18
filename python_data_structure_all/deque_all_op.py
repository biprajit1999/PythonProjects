from collections import deque

queue = deque();

def queue_append_right():
    n=int(input("Enter integer elements: "))
    queue.append(n)
    print ("Element appended at right ")

def queue_append_left():
    n=int(input("Enter the element to append: "))
    queue.appendleft(n)
    print ("Element appended at the left ")

def queue_set_at_index():
    m=int(input('Enter index'))
    n=int(input("Enter element"))
    queue.__setitem__(m,n)
    print ("Element replaced by new element")

def queue_delete():
    if(queue_isEmpty()==False):
        queue.pop()
        print("Element deleted")
    else:
        print ("Queue is Empty")

def queue_delete_by_val():
    n=int(input("Enter the value to be deleted: "))
    if(n in queue):
        queue.remove(n)
        print ("Element deleted")
    else:
        print ("Element not found")

def queue_traverse():
    print (queue)

def queue_reverse():
    queue_rev1= deque();
    queue_rev1=queue
    queue_rev = queue_rev1.reverse();
    print (queue_rev1)

def queue_count_el():
    print ("Number of element in the queue: ",len(queue))

def queue_rotate_positive():
    n=int(input("Enter the number of rotations in positive: "))
    if(n<=len(queue)):
        queue.rotate(n)
        print (queue)
    else:
        print ("Not possible")

def queue_rotate_negative():
    n=int(input("Enter the number of rotations in negative: "))
    if(abs(n)<=len(queue)):
        queue.rotate(n)
        print (queue)
    else:

        print ("Not posiible")

def queue_get_item():
    n=int(input("Enter the index of element to obtain: "))
    if(n<=len(queue)):
        print ("The element at index ",n,"is ",queue.__getitem__(n))
    else:
        print ("Invalid index")

def queue_clear_all():
    if(queue_isEmpty()==False):
        queue.clear()
        print ("Queue is emptied")
    else:
        print ("Queue is empty")

def queue_count_occr_el():
    n=int(input("Enter the element whose occurence to be counted: "))
    if(n in queue):
        print ("Number of times ",n,"occured is ",queue.count(n))
    else:
        print ("Element not found")

def queue_isEmpty():
    if(len(queue)==0):
        return True
    else:
        return False

def queue_contains_el():
    n=int(input("Enter the element to be searched: "))
    if(n in queue):
         print ("Element Found ")
    else:
         print ("Element Not Found ")



while(True):

    ch=int(input("Enter your choice: "))

    if(ch==1):
        queue_append_right()
    elif(ch==2):
        queue_append_left()
    elif(ch==3):
        queue_set_at_index()
    elif(ch==4):
        queue_delete()
    elif(ch==5):
        queue_delete_by_val()
    elif(ch==6):
        queue_traverse()
    elif(ch==7):
        queue_reverse()
    elif(ch==8):
        queue_count_el()
    elif(ch==9):
        queue_rotate_positive()
    elif(ch==10):
        queue_rotate_negative()
    elif(ch==11):
        queue_count_occr_el()
    elif(ch==12):
        queue_get_item()
    elif(ch==13):
        queue_clear_all()
    elif(ch==14):
        queue_contains_el()
    elif(ch==20):
        exit(0)
    else:
        print ("Wrong Choice")

