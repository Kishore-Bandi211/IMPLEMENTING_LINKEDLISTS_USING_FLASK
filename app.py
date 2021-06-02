import os
from flask import Flask, request, redirect, render_template, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

@app.route("/")
def index():
    
    
    
    print(l1)
    return render_template("index.html")

@app.route("/vpythons")
def vpythons():
    return render_template("single.html")

@app.route("/vpythond")
def vpythond():
    return render_template("double.html")
 
@app.route("/input")
def input():
    return render_template('input_form.html')

@app.route("/delete")
def delete():
    return render_template('delete.html')

@app.route("/printing")
def printing():

    # print(l1)
    
    return render_template('print.html',l2=l2)

@app.route("/insert_val", methods=["GET","POST"])
def insert_val():
    option = request.form['exampleRadios']
    if(option == "option1"):
        l1.insert_first(request.form["node"])
    else:
        l1.insert_last(request.form["node"])

    print(l1)
    return render_template('print.html',l2=l2)


@app.route("/insert_at", methods=["GET","POST"])
def insert_at():
    if(int(request.form["pos"])>(l1.length()-1) or int(request.form["pos"])<0):

        return render_template('invalid.html')
    l1.insert_at(int(request.form["pos"]), request.form["val"])
    print(l1)
    return render_template('print.html',l2=l2)



@app.route("/delete_val", methods=["GET","POST"])
def delete_val():
    option = request.form['exampleRadios']
    if(option == "option1"):
        l1.remove_first()
    else:
        l1.remove_last()

    print(l1)
    return render_template('print.html',l2=l2)


@app.route("/delete_at", methods=["GET","POST"])
def delete_at():
    if(int(request.form["pos"])>(l1.length()-1) or int(request.form["pos"])<0):

        return render_template('invalid.html')

    l1.remove_at(int(request.form["pos"]))
    print(l1)
    return render_template('print.html',l2=l2)

@app.route("/reverse")
def reverse():
    l1.reverse()
    print(l1)
    return render_template('print.html',l2=l2)
   





class Node:
    def __init__(self, data, prev=None, next=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next
        

    def __str__(self) -> str:
        return str({'data': self.data, 'prev': self.prev, 'next': self.next})

    def __repr__(self) -> str:
        return str({'data': self.data, 'prev': self.prev, 'next': self.next})


class LinkedList:
    def __init__(self) -> None:

        self.head: Node = None
        self.tail: Node = None

    def __str__(self) -> str:
        linkedlist = ''
        global l2
        l2=[]
        print(self.head.data)
        current = self.head

        while current:
            l2.append(current.data)
            linkedlist += str(current.data)
            linkedlist += ' -><- '
            current = current.next

        linkedlist += 'None'

        return linkedlist

    def __repr__(self) -> str:
        return str(self.head)

    def insert_first(self, data) -> None:
        if self.head is None and self.tail is None:
            node = Node(data)
            self.head = node
            self.tail = node
            return

        node = Node(data, next=self.head)
        self.head = node
        self.head.next.prev = self.head

    def insert_last(self, data) -> None:
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
        self.tail = new_node
        


    def insert_at(self, index: int, data) -> None:
        if index<0 or index>self.length():
            print("Invalid Index")
            return
        if self.head is None and self.tail is None:
            node = Node(data)
            self.head = node
            self.tail = node
            return

        counter = 1
        current = self.head

        while current and counter != index:
            if counter == index:
                break
            counter+=1

            current = current.next

        node = Node(data, prev=current, next=current.next)
        current.next = node

    def remove_first(self) -> None:
        if self.head is None:
            return

        self.head = self.head.next
        self.head.prev = None

    def remove_last(self) -> None:
        if self.head is None and self.tail is None:
            return

        previous = self.tail.prev
        self.tail = previous
        self.tail.next = None

    def remove_at(self, index: int) -> None:

        if index<0 or index>self.length():

            print("Invalid Index")
            return

        if self.head is None and self.tail is None:

            return
        current = self.head
        counter = 0 
        while current.next and counter!=index:

            if counter == index:

                break
            counter+=1

        current = current.next
        current.next.prev = current.prev
        current.prev.next = current.next
            

    def reverse(self) -> None:
        if self.head is None and self.tail is None:
            return
        prev = None
        current = self.head
        while(current is not None):
            
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def get_first(self) -> Node:
        if self.head is None:
            return

        return self.head

    def get_at(self, index: int) -> Node:
        if self.head is None and self.tail is None:
            return

        current = self.head

        while current and index > 0:
            current = current.next
            index -= 1

        return current

    def __getitem__(self, index: int) -> Node:
        return self.get_at(index)

    def get_last(self) -> Node:
        if self.head is None and self.tail is None:
            return

        return self.tail

    def length(self) -> int:
        if self.head is None and self.tail is None:
            return 0

        counter = 0
        current = self.head

        while current:
            current = current.next
            counter += 1

        return counter

    def __len__(self) -> int:
        return self.length()

    def clear(self) -> None:
        if self.head is None and self.tail is None:
            return

        self.head = None
        self.tail = None



    def find_index(self, data) -> int:
        if self.head is None and self.tail is None:
            return -1

        index = 0
        current = self.head

        while current:
            if current.data == data:
                return index

            current = current.next
            index += 0

        return -1

    def find(self, data) -> Node or None:
        if self.head is None and self.tail is None:
            return

        current = self.head

        while current:
            if current.data == data:
                return data

            current = current.next

        return None
    
    def insert_values(self, data_list) -> None:
        for data in data_list:
            
            self.insert_last(data)
        return
    def contains(self, data) -> bool:
        if self.head is None and self.tail is None:
            return False

        current = self.head

        while current:
            if current.data == data:
                return True

            current = current.next

        return False




if __name__ == "__main__":
    global l1
    l1 = LinkedList()
    l1.insert_values([1,2,3])
    
    # t= int(input("ENTER NUMBER OF TEST CASES"))

    # global l1
    # ll = LinkedList()
    # commands=[]
 
    # while(x>0):
    
    #     stream = input().split(" ")
    #     commands.append(stream)
    #     print(stream)
    #     x-=1
    
    # i=0  
    # while(t>0):
    #     stream=commands[i]
    #     i+=1
    #     if(stream[0] == "AB"):
    #         ll.insert_first(int(stream[1]))
    #         print(ll)
    #     elif(stream[0] == "AE"):
    #         ll.insert_last(int(stream[1]))
    #         print(ll)
    #     elif(stream[0] == "DB"):
    #         ll.remove_first()
    #         print(ll)
    #     elif(stream[0] == "DE"):
    #         ll.remove_last()
    #         print(ll)
    #     elif(stream[0] == "P"):
    #         print(ll)
    #     elif(stream[0] == "L"):
    #         print(ll.length())
    #     elif(stream[0] == "IL"): 
    #         list1 = stream[1:]
    #         ll.insert_values(list1)
    #         print(ll)
    #     elif(stream[0] == "IA"): 
    #         ll.insert_at(int(stream[1]),int(stream[2]))
    #         print(ll)
    #     elif(stream[0] == "RA"):
    #         ll.remove_at(int(stream[1]))
    #         print(ll)
    
    #     else:
    #         print("enter valid command")
                         
    #     t-=1


    app.run(port=5000)











