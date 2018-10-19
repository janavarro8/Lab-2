"""
Course: CS2302 Data Structures
Author: Javier Navarro
Assignment: Option B
Instructor: Diego Aguirre
TA: Manoj Saha
Last modified: 9/17/18
Purpose: Find 20 most common passwords in a given file
"""

def main():
    dict = {}               #Dictionary. Holds 
    validInput = False      #used to exit loops if it's a valid input
    head = None             #used to hold head of list
    sortedHead = None       #used to hold head of sorted list
    
    while(validInput == False):
        print("Would you like to create a linked list using solution A or B?")
        userInput = input("Enter 'A' for without a dictionary or 'B' for with a dictionary: ")
        userInput = userInput.lower()
        
        if(userInput != 'a' and userInput != 'b'):
            validInput = False
            print("Error. The only options are 'a' and 'b'. Try again.")
        else:
            validInput = True

    validInput = False
    while(validInput == False):
        fileName = input("Enter the name of your file: ")
        try:
            if(userInput == 'a'):
                head = createListSolA(fileName)
            else:
                head = createListSolB(fileName, dict)
            validInput = True
        except FileNotFoundError:
            print("File not found. Try again.")
    
    validInput = False
    while(validInput == False):
        print("Would you like to sort the list using solution A or B?")
        userInput = input("Enter 'A' for Bubble Sort or 'B' for Merge Sort: ")
        userInput = userInput.lower()
        
        if(userInput != 'a' and userInput != 'b'):
            validInput = False
            print("Error. The only options are 'a' and 'b'. Try again.")
        else:
            validInput = True
    if(userInput == 'a'):
        sortedHead = bubbleSort(head)
    #else:
        #sortedHead = mergeSort(head) #Incomplete
    printTop20(sortedHead)

def createListSolA(fileName):
    head = None         #used to hold the head of the list
    temp = None         #used to traverse list
    found = False       #used if password is found in list
    with open(fileName, "r") as file:   #opens file with given fileName
        for i in file:                  #i holds each line in the file 
            found = False
            line = i.split()            #splits i into an array
            try:
                while(temp != None and found != True):
                    if(temp.password == line[1]):       #if password already in list
                        temp.count += 1
                        found = True        
                    temp = temp.next
                if(found == False):
                    head = Node(line[1], 1, head)
                temp = head
            except IndexError:
                pass
            
    return head

def createListSolB(fileName, dict):
    head = None     #used to create list
    with open(fileName, "r") as file:   #opens file with given fileName
        for item in file:               #item holds each line in the file
            line = item.split()         #splits item into an array
            try:
                if(line[1] in dict):    #if password is already in dictionary
                    dict[line[1]].count += 1    #increment value for password in dictionary
                else:
                    head = Node(line[1], 1, head)
                    dict[line[1]] = head        #dictionary stores new node
            except IndexError:
                pass
            
    return head

def bubbleSort(head):
    swap = True             #holds whether there was a swap or not
    current = head          #used to traverse list
    while(swap == True):    #loops until there's no swaps left
        swap = False
        while(current != None and current.next != None):
            if(current.count < current.next.count):
                temp = current.count                    #next 3 statements swap the values
                current.count = current.next.count
                current.next.count = temp
                swap = True
            current = current.next
        current = head      #set to head to traverse again
        
    return current
    
def printTop20(head):
    temp = head         #used to traverse list
    counter = 0         #used to keep track of top 20
    while(temp != None and counter < 20):
        counter += 1
        print("Password ", counter, ": ", temp.password)
        print("Number of times repeated: ", temp.count)
        print("-------------------------------")
        temp = temp.next
        
#Class given through the pdf 
class Node(object):
    password = ""
    count = -1
    next = None
    
    def __init__(self, password, count, next):
        self.password = password
        self.count = count
        self.next = next


main()