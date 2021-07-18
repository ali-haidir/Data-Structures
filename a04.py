class Node:
    def __init__(self , data = None):
        self.val = data
        self.next = None

class Ring:
    def __init__(self):
        self.head = None

def __str__(self):
    ret_str = '['
    temp = self.head
    while temp is not None:
        ret_str+=str(temp.val)+ ', '
        temp = temp.next

        if temp == self.head:
            break

    ret_str = ret_str.rstrip(', ')
    ret_str += ']'
    return ret_str


Ring.__str__ = __str__



def get_last(self):

    if self.head is None:
        return None

    temp = self.head.next
    while temp.next != self.head:
        temp = temp.next

    return temp
Ring.get_last = get_last


def insert(self , index , val):
    new_node = Node(val)
    last = self.get_last()

    if index == 0:
        new_node.next = self.head
        self.head = new_node


        if last is None:
            self.head.next = self.head
        else:
            last.next = new_node
        return

    if self.head is None:
        raise Exception("cannot insert")


    temp = self.head

    counter = 0
    while temp is not None and counter<index:
        prev = temp
        temp = temp.next
        counter+=1

    prev.next = new_node
    new_node.next = temp

Ring.insert = insert


def len(self):

    if self.head is None:
        #raise Exception("the list is Empty")
        return 0

    last = self.get_last()
    temp = self.head.next
    counter = 1
    while last.next != temp:
        temp = temp.next
        counter = counter + 1

    return counter

Ring.len = len


def push(self,val):
    last_index = self.len()
    self.insert(last_index , val)
Ring.push = push

def pop(self):
    la=self.get_last()
    return self.remove(la.val)

Ring.pop=pop


def get(self, index):
    if self.head is None:
        raise IndexError("the list is empty")

    temp = self.head

    counter = -1
    while index != counter:
        counter = counter + 1
        if index == counter:
            val = temp.val
            break
        temp = temp.next

    return val

Ring.get = get

def remove(self,val):
        if self.head is None:
            return

        temp = self.head
        last = self.get_last()

        if temp.val == val:
            if last == self.head:
                self.head = None

            else:
                self.head = temp.next
                last.next = self.head
            return
        prev = temp
        temp = temp.next

        while temp != self.head:
            if temp.val == val:
                break

            prev = temp
            temp = temp.next

        if temp == self.head:
            return
        prev.next = temp.next

Ring.remove=remove

def remove_at(self, index):
        count=1

        if self.head is None:
            return

        temp= self.head.next
        prev= self.head

        if index == 0:
            temp = self.head
            prev.next = temp.next
            val = temp.val
            self.head = None
            return val

        while count != index:
            prev =temp
            temp=temp.next
            count +=1


        prev.next = temp.next
        val = temp.val
        temp=None

        return val
Ring.remove_at=remove_at





if __name__ == '__main__':
    r = Ring()
    r.insert(1, 1)
    r.insert(0, 1)
    r.insert(0, 2)
    r.insert(1, 3)
    r.insert(7, 5)  # different behavrior since it's a ring!
    print(r)
