import json
import os
libraray_file='library_data.json'
def load_libraray():
    if not os.path.exists(libraray_file):
     return{}
    try:
        with open(libraray_file,'r') as file  :
            return json .load(file) 
    except Exception as e:
        print(f"Error loading library data:{e}")
        return{}

def save_library(library):
    try: 
        with open(libraray_file,'w') as file  :
            json.dump(library,file)
    except Exception as e:
        print(f"Eroor saving library data:",{e})

def add_book(library, title, author,quantity):
    if title in library:
        print("Book already exists. Updating the quantity.")
        library[title][quantity]+=quantity
    else:
        library[title]={'author':author, 'quantity':quantity, 'borrowedby':None}
    save_library(library)
    print(f"Book '{title}' added successfully!")

def view_books (libraray):
        if not (libraray):
          print("The library is empty")   
          return
        for title, details in libraray.items():
            status=f"Available ({details['quantity']})" if not details['borrowed_by'] else f"borrowed by {details['borrowed by']}"
            print(f"Title:{title}, Author:{details['author']}, status:{status}")


def borrow_book(library, title, borrower_name):
    if title not in library:
        print("Book not found in the library.") 
        return
    if library[title]['quantity']==0:
        print(f"All copies of '{title}' are currently borrowed") 
        return
    if library[title]['borrowed_by']:
        print(f"the book '{title}' is currently borrowed by {library[title]['borrowed_by']}, ")
        return
    library[title]['quantity']=-1
    library[title]['borrowed_by']=borrower_name
    save_library(library)
    print(f"'{title}' has been borrowed by {borrower_name},")
           
# function to return a borrowed book to the laibrary_____
def return_book(laibrary, title):
    if title not in laibrary:
        print("Book not found in the laibrary.")
        return
    if not laibrary[title]['borrowed_by']:
        print(f" The book '{title}' was not borrowed.")
        return
    laibrary[title]['quantity'] += 1
    borrower_name = laibrary[title]['borrowed_by']
    laibrary[title]['borrowed_by'] = None
    save_library(laibrary)
    print(f"'{title}' has been returned by {borrower_name}.")

# main function to run the laibrary management system_____
def main():
    laibrary = load_libraray()
    while True:
        print("\nlaibrary Management System")
        print("1. Add book")
        print("2. View books")
        print("3. Borrow book")
        print("4. Return book")
        print("5. Exit")
        choice = input("Enter your choice:")
        if choice == '1':
            title = input("Enter the book title:")
            author = input("Enter the book author:")
            try:
                quantity = int(input("enter the quantity of the book:"))
                add_book(laibrary, title, author, quantity)
            except ValueError:
                print("Invaild input for quantity. please enter an integer.")
        elif choice == '2':
            view_books(laibrary)
        elif choice == '3':
            title = input("enter the book title:")
            borrower_name = input("enter the your name:")
            borrower_name(laibrary, title, borrower_name)
        elif choice == '4':
            title = input ("enter the book title:")
            return_book(laibrary, title)
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()







   
