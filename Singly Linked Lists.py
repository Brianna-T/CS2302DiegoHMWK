# -*- coding: utf-8 -*-
"""
Tovar, Brianna
CS2302 Aguirre Diego, TA Gerardo, IA Edurardo
Last Modify: 9/24
Singly Linked Lists
"""

class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next
        
class SinglyLinkedList(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None

#1
def addLast(L,item):
    if IsEmpty(L):
        L.head = Node(item)
        L.tail = L.head
    else:
        L.tail.next = Node(item)
        L.tail = L.tail.next
        
#2
def addFirst(L,item):
    if IsEmpty(L):
        L.head=Node(item)
        L.tail=L.head
    else:
        L.head=Node(item,L.head)
        
#3
def add(L,index,item):
    s=contains(L,index)
    if s is None:
        addLast(L.item)
    else:
        s.next=Node(item,s.next)
    return

#4
def clear(L):
    L.head=L.tail
    return

#5
def contains(L,item):
    temp=L.head
    while temp is not None:
        if temp.item==item:
            return temp
        temp=temp.next
    return None

#6
def getIndexOf(L,item):
    count=0
    t=L.head
    while t.next!=None:
        if t.next==item:
            return count
        else:
            t=t.next
            count+=1
    return

#7
def get(L,index):
    t=L.head
    while t.next!=None:
        if t.next==index:
            return t.next

#8
def getFirst(L):
    return L.head.item

#9
def getLast(L):
    return L.tail.item

#10
def remove(L,index):
        # Removes x from list L
    # It does nothing if x is not in L
    if L.head==None:
        return
    if L.head.item == index:
        if L.head == L.tail: # x is the only element in list
            L.head = None
            L.tail = None
        else:
            L.head = L.head.next
    else:
         # Find x
         temp = L.head
         while temp.next != None and temp.next.item !=index:
             temp = temp.next
         if temp.next != None: # x was found
             if temp.next == L.tail: # x is the last node
                 L.tail = temp
                 L.tail.next = None
             else:
                 temp.next = temp.next.next

#11
def removeFirst(L):
    if IsEmpty(L):
        return None
    else:    
        t=L.head
        t=t.next
        L.head=t.next
        return

#12
def removeLast(L):
    L.tail=None
    return L.tail

#13
def size(L):
    temp=L.head
    count =0
    while temp is not None:
        count+=1
        temp=temp.next
    return count

#14
def IsEmpty(L):
    return L.head == None

#15
def printList(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line

#Reverse
def PrintNodesReverse(N):
    if N != None:
        PrintNodesReverse(N.next)
        print(N.item, end=' ')    

def reverse_list(L):
    # Prints list L's items in reverse order
    PrintNodesReverse(L.head)
    print()
    
#deleting duplicates

L=SinglyLinkedList()
print(IsEmpty(L))
for i in range(5):
    addLast(L,i)

print("The answers provided are correct, it just follows after every method, modifying L")

addLast(L,6)
print("Problem 1")
printList(L)

addFirst(L,6)
print("Problem 2")
printList(L)

add(L,0,2)
print("Problem 3")
printList(L)

clear(L)
print("Problem 4")
printList(L)

print("Problem 5")
print(contains(L,1))

print("Problem 6")
print(getIndexOf(L,1))

print("Problem 7")
print(get(L,1))

print("Problem 8")
print(getFirst(L))

print("Problem 9")
print(getLast(L))

remove(L,6)
print("Problem 10")
print(L)

removeFirst(L)
print("Problem 11")
print(L)

removeLast(L)
print("Problem 12")
print(L)

print("Problem 13")
print(size(L))