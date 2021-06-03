class Node: 
     def __init__(self, data): 
          self.data = data
          self.next = None

class LinkedList: 
     def __init__(self): 
          self.head = None
          
     def push(self, new_data): 
          new_node = Node(new_data) 
          new_node.next = self.head 
          self.head = new_node
     
     def insertAfter(self, prev_node, new_data):  
          if prev_node is None:  
               print("The given previous node must inLinkedList.")
               return
          new_node = Node(new_data)  
          new_node.next = prev_node.next
          prev_node.next = new_node


     def append(self, new_data): 
          new_node = Node(new_data) 
          if self.head is None: 
               self.head = new_node 
               return
          last = self.head 
          while (last.next): 
               last = last.next
          last.next =  new_node

     def display(self):
          temp = self.head
          temp_list = []
          while(temp.next):
               temp_list.append(temp.data)
               temp = temp.next
          print(temp_list)


     def insertion_sort(self):  #INSERTION SORT ALGORITHM FOR LINKEDLIST
          arr = []
          while(self.head.next):
               arr.append(self.head.data)
               self.head = self.head.next
          arr.append(self.head.data)
          for i in range(1, len(arr)): 
               key = arr[i]
               j = i-1
               while j >=0 and key < arr[j] : 
                    arr[j+1] = arr[j] 
                    j -= 1
               arr[j+1] = key

          print(arr)
          for value in arr:
               self.push(value)

if __name__=='__main__':

     llist = LinkedList()
     data_list = [5, 10, 4, 54, 81]

     #Filling our linked list using pre-defined array
     for value in data_list:
          llist.push(value)

     #Unsorted Linked List
     llist.display()
     llist.insertion_sort() #Sorting linked list
     #Sorted Linked List
     llist.display() 

     
          
	
