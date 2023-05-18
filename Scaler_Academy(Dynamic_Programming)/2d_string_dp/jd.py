from itertools import permutations
from random import choice


ls = []  # To create an empty list


def isEmpty():
    return len(ls) == 0


def length():
    print(len(ls))


def find_duplicate():
    print(set([i for i in ls if ls.count(i) > 1]))


def insert_from_end(n):
    ls.append(n)


def insert_from_begin(m):
    ls.insert(0, m)


def update_value(val, val2):
    if (isEmpty()):
        print("List is Empty")
    else:
        if (val not in ls):
            print("Not Found")
        else:
            m = ls.index(val)
            ls[m] = val2


def delete_from_begin():
    if (isEmpty()):
        print("List is Empty")
    else:
        ls.pop(0)


def delete_from_end():
    if (isEmpty()):
        print("List is Empty")
    else:
        ls.pop()


def del_by_value(n):
    if (isEmpty() or n not in ls):
        print("Not Found")
    else:
        ls.remove(n)


def del_by_index(n):
    if (isEmpty() or n > len(ls)):
        print("List is Empty")
    else:
        ls.pop(n)


def search(n):
    if (isEmpty()):
        print("List is Empty")
    else:
        print(n in ls)


def get_index(n):
    if (isEmpty()):
        print("List is Empty")
    else:
        if (n in ls):
            print(ls.index(n))
        else:
            print("Not in List")


def sort_asc():
    ll = []
    ll = ls.copy()
    print(sorted(ll))


def sort_desc():
    ll = []
    ll = ls.copy()
    print(sorted(ll, reverse=True))


def traverse_reverse():
    print(ls[::-1])


def sum_of_el():
    print(sum(ls))


def traverse():
    print(ls)

def add_list():
    return sum(ls)


def ls_count(n):
    print(ls.count(n))


def ls_max():
    print(max(ls))


def ls_min():
    print(min(ls))

def ls_lexicographical_val():
    print(ord(sum(ls)))


def ls_isunique():
    if(sorted(ls)==list(set(ls))):
        print("list is unique", ls)
    else:
        print("list is not unique: ", ls)


def ls_multiply():
    mul = 1
    for i in ls:
        mul = mul*i
    print(mul)

def ls_pallindrome():
    if(ls==ls[::-1]):
        print("list is pallindrome: ", ls)
    else:
        print("list is not pallindrome: ", ls)


def ls_remove_duplicates():
    l = ls.copy()
    if(sorted(l)==list(set(l))):
        return l
    else:
        return list(set(l))

def ls_permute():
    print(list(permutations(ls)))

def ls_freq_of_elm():
    l = set(ls)
    for i in l:
        print("Frequency of ", i, "is: ", ls.count(i), " times")


def ls_random_selection():
    print(choice(ls))


def ls_odd():
    lp = [i for i in ls if i%2!=0]
    print(lp)


def ls_even():
    lp = [i for i in ls if i % 2 == 0]
    print(lp)


while True:

    ch = int(input("Enter Your Choice: "))
    if (ch == 1):
        m = int(input("Enter a number: "))
        insert_from_begin(m)

    elif (ch == 2):
        n = int(input("Enter a number: "))
        insert_from_end(n)

    elif(ch == 3):
        add_list()

    elif (ch == 4):
        traverse()

    elif (ch == 5):
        delete_from_begin()

    elif (ch == 6):
        delete_from_end()

    elif (ch == 7):
        p = int(input("Enter value to be deleted: "))
        del_by_value(p)

    elif (ch == 8):
        inx = int(input("Enter index to be deleted: "))
        del_by_index(inx)

    elif (ch == 9):
        traverse_reverse()

    elif (ch == 10):
        length()

    elif (ch == 11):
        nm = int(input("Enter number to be searched: "))
        search(nm)

    elif (ch == 12):
        nm2 = int(input("Enter number to get index: "))
        get_index(nm2)

    elif (ch == 13):
        mn3 = int(input("Enter value: "))
        mn4 = int(input("Enter val update: "))
        update_value(mn3, mn4)

    elif (ch == 14):
        find_duplicate()

    elif (ch == 15):
        sort_asc()

    elif (ch == 16):
        sort_desc()

    elif (ch == 17):
        sum_of_el()

    elif(ch == 18):
        k1 = int(input("Enter Number to be counted: "))
        ls_count(k1)

    elif(ch == 19):
        ls_max()

    elif(ch==20):
        ls_min()

    elif(ch==21):
        isEmpty()

    elif(ch==22):
        ls_lexicographical_val()

    elif(ch == 23):
        ls_isunique()

    elif(ch==24):
        ls_multiply()

    elif(ch==25):
        ls_pallindrome()

    elif(ch==26):
        ls_remove_duplicates()

    elif(ch==27):
        ls_permute()

    elif(ch==28):
        ls_freq_of_elm()

    elif(ch==29):
        ls_random_selection()

    elif(ch==30):
        ls_even()

    elif(ch==31):
        ls_odd()

    elif (ch == 32):
        exit(0)

    elif (ch == 33):
        break