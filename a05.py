class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

def push(self, val):
    new_node= Node(val)

    if self.head is None:
        self.head= new_node
        return

    else:
        last=self.head

    while last.next is not None:
        last= last.next

    last.next= new_node

LinkedList.push=push

def pop(self):
    if self.head is None:
        raise Exception(" nothing to pop .")
        print("case 1")

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

def __str__(self):
    ret_str = '['
    temp = self.head
    while temp is not None:
        ret_str += str(temp.val) + ', '
        temp = temp.next

    ret_str = ret_str.rstrip(', ')
    ret_str += ']'
    return ret_str
LinkedList.__str__ = __str__

def insert( self, index , val ):
    new_node = node(val)

    if index == 0:
        new_node.next = self.head
        if self.head is not None:
            self.head.prev=new_node
        self.head =new_node
        return

    temp= self.head
    counter =0

    while temp is not None and counter< index:
        pre = temp
        temp = temp.next
        counter +=1


    pre.next = new_node
    new_node.prev=prev

    new_node.next=temp
    if temp is not None:
        temp.prev=new_node


LinkedList.insert = insert

def remove(self,val):
    temp=self.head
    if temp is not None:
        if temp.val==val:
            self.head=temp.next
            temp=None
            return
    while temp is not None:
        if temp.val==val:
            break

        prev=temp
        temp=temp.next

    if temp is None:
        return
    prev.next=temp.next
LinkedList.remove=remove

def remove_at(self, index):
    if self.head is None:
        return None
    temp=self.head
    pre=self.head
    count=0

    if count == index:
        self.head=temp.next
        temp=None
        return

    while count != index:
        pre=temp
        temp=temp.next
        count +=1

    pre.next=temp.next
    temp=None
LinkedList.remove_at=remove_at


def length(self):
    temp= self.head

    count =0

    while temp.next is not None :
        count +=1
        temp= temp.next

    return count

LinkedList.length = length

def reverse_list(self):
    temp2=None
    temp=self.head

    if self.head is None:
        return None

    if temp is None:
        return None

    while temp is not None:
        current=temp.next
        temp.next=temp2
        temp2 =temp
        temp=current
        self.head=temp2
LinkedList.reverse_list=reverse_list




if __name__ == '__main__':
    l = LinkedList()
    l.push(1)
    l.push(2)
    l.push(3)

    print(l)

    l.reverse_list()
    print(l)
