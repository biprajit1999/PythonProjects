import itertools

a=[]

def insert_el_at_end():
    n=int(input("Enter elements: "))
    a.append(n)
    print("Inserted",n)

def list_insert_at_beginning():
    n=int(input("Enter the element to be inserted "))
    a.insert(0,n)
    print ("value inserted ",n)

def list_delete_from_beggining():
    a.pop(0)
    print('Item Deleted')

def list_delete_from_end():
    a.pop(-1)
    print ("Item Deleted")

def list_traverse():
    print (a)

def bubble_sort():
    m = list(filter(lambda x: x, a))
    l=[]
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if m[j] < m[i]:
                temp = m[j]
                m[j] = m[i]
                m[i] = temp
    print("... Printing Sorted Element List Bubble Sort ...")
    for i in m:
        l.append(i)
    print(l)

def insertion_sort():
    ar = list(filter(lambda x: x, a))
    l=[]
    for k in range(0, len(ar)):
        temp = ar[k]
        j = k - 1
        while j >= 0 and temp <= ar[j]:
            ar[j + 1] = ar[j]
            j = j - 1
        ar[j + 1] = temp
    print("... Printing sorted elements Insertion Sort ...")
    for i in ar:
        l.append(i)
    return l

'''
def bucket_sort():
    arr = []
    slot_num = len(a)  # 10 means 10 slots, each
    # slot's size is 0.1
    for i in range(slot_num):
        arr.append([])

    # Put array elements in different buckets
    for j in a:
        index_b = int(slot_num * j)
        arr[index_b].append(j)

    # Sort individual buckets
    for i in range(slot_num):
        arr[i] = insertion_sort(arr[i])

    # concatenate the result
    k = 0
    l=[]
    for i in range(slot_num):
        for j in range(len(arr[i])):
            l[k] = arr[i][j]
            k += 1
    print (l)
'''


def getNextGap(gap):
    # Shrink gap by Shrink factor
    gap = (gap * 10) / 13
    if gap < 1:
        return 1
    return gap


def comb_sort():
    l = list(filter(lambda x: x, a))
    n = len(l)
    gap = n

    swapped = True

    while gap != 1 or swapped == 1:

        # Find next gap
        gap = getNextGap(gap)

        # Initialize swapped as false so that we can
        # check if swap happened or not
        swapped = False

        # Compare all elements with current gap
        for i in range(0, n - gap):
            if l[i] > l[i + gap]:
                l[i], l[i + gap] = l[i + gap], l[i]
                swapped = True

    print (l)


while(True):

    ch = int(input("Enter choice: "))

    if(ch==1):
        list_insert_at_beginning()
    elif(ch==2):
        list_delete_from_end()
    elif(ch==3):
        list_delete_from_beggining()
    elif(ch==4):
        list_delete_from_end()
    elif(ch==5):
        list_traverse()
    elif(ch==6):
        bubble_sort()
    elif(ch==7):
        print (insertion_sort())
    elif(ch==8):
        comb_sort()
    elif(ch==15):
        exit(0)
    else:
        print ("Wrong")





