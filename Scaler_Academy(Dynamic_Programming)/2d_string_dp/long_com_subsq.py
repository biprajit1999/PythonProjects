str1=input("Enter 1st string: ")
str2=input("Enter 2nd string: ")

def com_substring(str1,str2):
    list1=[]
    list2=[]

    for i in range(1,len(str1)+1):
        list1.append(str1[:i])

    for i in range(1,len(str2)+1):
        list2.append(str2[:i])

    list3=[]
    for i in list1:
        for j in list2:
            if(i==j):
                list3.append(i)

    return max(list3)


    print(list1)
    print(list2)
    print(list3)

print(com_substring(str1,str2))