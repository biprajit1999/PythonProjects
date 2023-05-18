class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

class Singly_linked_list:
    def __init__(self):
        self.head = None

    def insert_at_begining(self):
        data = int(input("Enter data: "))
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insert_at_end(self):
        data = int(input("Enter data: "))
        newNode = Node(data)
        if(self.head==Node):
            self.head=newNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next=newNode


    def traverse_list(self):
        trv = self.head
        while trv is not None:
            print(trv.data,end=" ")
            trv = trv.next
        print()

    def reverse_list(self):
        if self.head is None:
            return
        temp = self.head
        prev = None
        while temp is not None:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt


    def insert_in_between(self):
        middle_node = list.head.next
        if middle_node is None:
            print("The mentioned node is absent")
            return
        newdata = int(input("Enter Data: "))
        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode


    def delete_by_value(self):
        Removekey = int(input("Enter element to be deleted: "))
        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next
        HeadVal = None


    def delete_at_begin(self):
        if(self.head==None):
            print("Empty")
        else:
            Headvl = self.head
            self.head = Headvl.next
            Headvl=None

    def delete_at_end(self):
        if(self.head==None):
            print("Empty")
        else:
            headval = self.head
            while (headval.next.next):
                headval=headval.next
            headval.next=None

list = Singly_linked_list()

while(True):

    ch = int(input("Enter choice: "))

    if(ch==1):
        list.insert_at_begining()
    elif(ch==2):
        list.insert_at_end()
    elif(ch==3):
        list.traverse_list()
    elif(ch==4):
        list.insert_in_between()
    elif(ch==5):
        list.delete_by_value()
    elif(ch==6):
        list.delete_at_begin()
    elif(ch==7):
        list.delete_at_end()
    elif(ch==8):
        list.reverse_list()
    elif(ch==10):
        exit(0)
    else:
        print("Wrong Choice")


