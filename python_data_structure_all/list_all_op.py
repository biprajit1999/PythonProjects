import itertools
req_list = []

def list_insert():
    n = int(input("Enter elements: "))
    req_list.append(n)
    print("Element inserted ",n)

def list_insert_at_beginning():
    n=int(input("Enter the element to be inserted "))
    req_list.insert(0,n)
    print ("value inserted ",n)

def list_insert_at_end():
    n=int(input("Enter the element to be inserted "))
    req_list.insert(len(req_list),n)
    print ("value inserted ",n)

def list_insert_at_specific_loc():
    n=int(input("Enter the element to be inserted "))
    m=int(input("Enter the index "))
    req_list.insert(m,n)

def list_delete_by_element():
    n=int(input("Enter the element to be deleted: "))
    req_list.remove(n)
    print ("Item deleted",n)

def list_delete_by_index():
    n=int(input("Enter the index"))
    req_list.pop(n)
    print ("Item deleted at index ",n)

def list_delete_from_beggining():
    req_list.pop(0)
    print('Item Deleted')

def list_delete_from_end():
    req_list.pop(-1)
    print ("Item Deleted")


def list_traverse():
    print (req_list)

def list_reverse_traverse():
    req_list2 = []
    req_list2 = list(filter(lambda x:x,req_list))
    req_list2.reverse()
    print (req_list2)

def list_isEmpty():
    if(len(req_list)==0):
        print ("List is empty")
    else:
        print ("list is not empty")

def list_isunique():
    for i in req_list:
        if (list.count(req_list,i)>1):
            return False
        else:
            return True

def list_max():
    print (max(req_list))

def list_min():
    print (min(req_list))

def list_sort_ascending():
    req_list3 = []
    req_list3 = list(filter(lambda x:x,req_list))
    req_list3.sort()
    print (req_list3)

def list_sort_descending():
    req_list4 = []
    req_list4 = list(filter(lambda x:x,req_list))
    req_list4.sort(reverse = True)
    print(req_list4)

def list_sum():
    sum = 0
    for i in req_list:
        sum=sum+i
    print(sum)

def list_multiply():
    mult=1
    for i in req_list:
        mult = mult*i
    print (mult)

def list_remove_duplicates():
    req_list5 = []
    req_list5 = list(filter(lambda x:x,req_list))
    duplicate_list = set()
    req_list6 = []
    for i in req_list5:
        if i not in req_list6:
            req_list6.append(i)
            duplicate_list.add(i)

    print (duplicate_list)

def list_sort_condn():
    n=int(input("Enter the number to which the elements are to be sorted: "))
    req_list11 = []
    req_list12=[]
    req_list11 = list(filter(lambda x:x,req_list))

    for i in req_list11:
        if (i<n):
            req_list12.append(i)
        else:
            continue
    print (req_list12)


def list_sort_even():
    req_list2=[]
    req_list2 = list(filter(lambda x:x,req_list))

    print (list(filter(lambda x:x%2==0,req_list2)))

def list_sort_odd():
    req_list2 = []
    req_list2 = list(filter(lambda x:x,req_list))

    print(list(filter(lambda x:x%2!=0, req_list2)))

def list_contains():
    n = int(input("Enter the element to be checked "))

    if(req_list.__contains__(n)==True):
        print ("Element Found")
    else:
        print("Element Not Found")

def list_swap():
    n=int(input("Enter the first loc"))
    m=int(input("Enter the second loc"))
    req_list3=[]
    req_list3 = list(filter(lambda x:x,req_list))

    req_list3[n],req_list3[m]=req_list3[m],req_list3[n]
    print (req_list3)

def list_permutation():
    list2=[]
    req_list3 =[]
    list2=list(filter(lambda x:x,req_list))
    req_list3 = list(itertools.permutations(list2))
    print (req_list3)

while(True):

    ch = int(input("Enter choice: "))

    if(ch==1):
        list_insert()

    elif(ch==2):
        list_insert_at_beginning()

    elif(ch==3):
        list_insert_at_end()

    elif(ch==4):
        list_insert_at_specific_loc()

    elif(ch==5):
        list_isEmpty()

    elif (ch == 6):
        list_contains()

    elif(ch==7):
        list_delete_by_index()

    elif(ch==8):
        list_delete_by_element()

    elif(ch==9):
        list_delete_from_beggining()

    elif(ch==10):
        list_delete_from_end()

    elif(ch==11):
        list_remove_duplicates()

    elif(ch==12):
        list_traverse()

    elif(ch==13):
        list_reverse_traverse()

    elif(ch==14):
        list_max()

    elif(ch==15):
        list_min()

    elif(ch==16):
        list_sum()

    elif(ch==17):
        list_multiply()

    elif(ch==18):
        list_sort_ascending()

    elif(ch==19):
        list_sort_descending()

    elif(ch==20):
        list_sort_condn()

    elif(ch==21):
        list_sort_even()

    elif(ch==22):
        list_sort_odd()

    elif(ch==23):
        list_swap()

    elif(ch==24):
        list_permutation()

    elif(ch==25):
        print (list_isunique())

    elif(ch==26):
        exit(0)

    else:
        print ("Wrong choice")




