class Node:
    def __init__(self, data):
        self.val=data
        self.next=None
        self.pre=None
class LinkedList:
    def __init__(self):
        self.head=None




def push(self, val):
    new_node=Node(val)

    if self.head is None:
        self.head=new_node
        return

    last=self.head
    while last.next is not None:
        last= last.next
    last.next=new_node
    new_node.pre=last




LinkedList.push =push


def insert(self , index , val ):
    new_node=Node(val)
    if index==0:
        new_node.next=self.head
        self.head.pre=new_node
        self.head=new_node
        return

    temp=self.head
    counter =0
    while temp  is not None and counter < index:
        pre =temp
        temp=temp.next
        count +=1

    pre.next=new_node
    new_node.pre=pre

    new_node.next=temp
    temp.pre=new_node

LinkedList.insert=insert


def __str__(self):
    list="["
    temp= self.head
    while temp:
        list += str(temp.val) + " ,"
        temp=temp.next

    list=list.rstrip( " ,")
    list +=" ]"
    return list

LinkedList.__str__= __str__




def pop(self):
    if self.head is None:
        raise Exception(" no value to pop .")

    if self.head.next is None:
        val= self.head.val
        self.head = None
        return val

    temp= self.head
    while temp.next is not None:
        pre=temp
        temp=temp.next

    val=temp.val
    pre.next=None
    return val


LinkedList.pop= pop



def len(self):
    temp=self.head
    count=0

    while temp:
        count +=1
        temp=temp.next

    return count

LinkedList.len= len



def get(self, Index):
    count=0
    temp=self.head

    if temp.next is None:
        val=temp.val

        return val

    if count == Index:
            val = temp.val

            return val


    while count != Index:
        count +=1
        pre =temp
        temp= temp.next

        val=temp.val



        if Index > count :
            raise IndexError("list index out of range")


LinkedList.get=get



if __name__ == "__main__":
    l = LinkedList()
    l.push(5)
    l.push(6)

    print(l)

    print(l.len())

    l.pop()
    print(l.len())

    print(l.get(0))
    l.get(2) # Should say "IndexError: Index out of bound"
