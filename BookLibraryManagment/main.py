# Importing the required classes
from Customers import Customers
from Books import Books
from Loans import Loans

if __name__=='__main__':

    def main():

        """
        Name: Mir Shukhman
        Date: 24.08.23
        The func creates the main menu for the Book Library Manager.
        Displays the menu to the user & Allows the user to pick the desired function.
        Will loop back to showing main menu and asking for input upon completing the chosen func,
            until user chooses to use the "exit" func.
        If invalid func num was chosen, will show "try again" message and show the menu again.
        """

        # Creating class instances for required classes
        customers = Customers()
        books = Books()
        loans = Loans()

        # Strats the loop of show menu -> ask for input -> preform the func -> again
        while True:

            # Shows the main menu
            print ('\n'
                   'Please choose the desired function: \n'
                  '1. Add a new customer\n'
                  '2. Add a new book\n'
                  '3. Loan a book\n'
                  '4. Return a book\n'
                  '5. Display all books\n'
                  '6. Display all customers\n'
                  '7. Display all loans\n'
                  '8. Display late loans\n'
                  '9. Find book by title\n'
                  '10. Find customer by name\n'
                  '11. Remove book\n'
                  '12. Remove customer\n'
                  '13. Exit\n')

            # User chooses func
            choice=input('Enter Number of the desired function: ')


            # Func to add new customer
            # Asks from user to input the new customer's details one by one
            # Makes sure "age" input is integer
            # Calls for "add_customer" func from Customers class and gives it the details inputted by the user
            if choice=='1':
                print("Please enter the new customer's details:")
                name=input('Name: ')
                city=input('City: ')

                # Error handling for if age is not int
                while True:
                    try:
                        # Age input is int, exit loop
                        age=int(input('Age: '))
                        break

                    # Age input not int, shows "try again" message and loops back to input
                    except ValueError:
                        print('Age must be a number, please try again:')

                # Call func from the class, give func the inputs as parameters
                customers.add_customer(name,city,age)


            # Func to add new book
            # Asks from user to input the new book's details one by one
            # Makes sure "pub year" input is integer
            # Makes sure "loan type" input is integer, and either 1,2 or 3.
            # Calls for "add_book" func from Books class and gives it the details inputted by the user
            elif choice=='2':
                print("Please enter the new Book's details:")
                title = input('Title: ')
                author = input('Author: ')

                # Error handling for if year is not int
                while True:
                    try:
                        # Year input is int, exit loop
                        year = int(input('Publication Year: '))
                        break

                    # Year input not int, shows "try again" message and loops back to input
                    except ValueError:
                        print('Publication Year must be a number, please try again:')

                # Error handling for if loan_type is not int (or not 1,2,3)
                while True:
                    try:
                        # Loan_type input is int, check if 1,2,3
                        loan_type= int(input('Loan Type (1-up to 10 day loan,2-up to 5 days,3-up to 2 days): '))

                        # Loan_type input is  1 or 2 or 3, exit loop
                        if loan_type in (1,2,3):
                            break

                        # Loan_type input is not 1 or 2 or 3, shows "try again" message and loops back to input
                        else:
                            print('Invalid loan type. Please enter 1, 2, or 3.')

                    # Loan_type input not int, shows "try again" message and loops back to input
                    except ValueError:
                        print('Invalid loan type. Please enter 1, 2, or 3.')

                # Call func from the class, give func the inputs as parameters
                books.add_book(title,author,year,loan_type)

            # Func to create new loan
            # Asks from user to input loaning customer's ID and loaned book ID
            # Makes sure the input is integer
            # Calls for "find_customer_BY_ID" func from customers class
            # If such customer not found, aborts func
            # If found, asks for user's approval that indeed correct customer was selected- if not, aborts func
            # Same steps for book's ID and using "find_book_BY_ID" func from books class
            # If both ID's valid and approved by user, calls for "loan_book" func from loans class
                # and gives it both ID's as parameters
            elif choice == '3':
                try:
                    # Receives custID as input and calls for find cust by ID func
                    custID = int(input("Enter loaning customer ID: "))
                    found_cust = customers.find_customer_BY_ID(custID)
                    if not found_cust:  # If not found - aborts func
                        return

                    else: # If found asks for user's approval of correct cust
                        approval = input("Correct customer (yes/no)? ")
                        if approval.lower() != "yes": # If not approved - aborts func
                            print("Customer not approved")
                            return

                    # Recives bookID as input and calls for find book by ID func
                    bookID= int(input("Enter loaned book ID: "))
                    found_book = books.find_book_BY_ID(bookID)
                    if not found_book: # If not found - aborts func
                        return

                    else: # If found asks for user's approval of correct book
                        approval = input("Correct book (yes/no)? ")
                        if approval.lower() != "yes": # If not approved - aborts func
                            print("Book not approved")
                            return

                    loans.loan_book(custID,bookID)  # Calls for "loan_book" func and gives it both ID's as parameters

                # Error handling for input is not int
                except ValueError:
                    print("Invalid input: ID's must be integers only.")


            # Func to add return date to existing loan
            # Asks from user to input loaned book ID
            # Makes sure the input is integer
            # Calls for "find_book_BY_ID" func from books class
            # If such book not found, aborts func
            # If found, asks for user's approval that indeed correct book was selected- if not, aborts func
            # If ID valid and book approved by user, calls for "return_book" func from loans class
                # and gives it book's ID as parameter
            elif choice == '4':
                try:
                    # Receives bookID as input and calls for find book by ID func
                    bookID = int(input("Enter loaned book ID: "))
                    found_book = books.find_book_BY_ID(bookID)
                    if not found_book:  # If not found - aborts func
                        return

                    else:  # If found asks for user's approval of correct book
                        approval = input("Correct book (yes/no)? ")
                        if approval.lower() != "yes":  # If not approved - aborts func
                            print("Book not approved")
                            return

                    # Calls for "return_book" func and gives it book's ID as parameter
                    loans.return_book(bookID)

                # Error handling for input is not int
                except ValueError:
                    print("Invalid input: ID's must be integers only.")


            # Func to show all of library's Books
            # Calls for "show_all_books" func from Books class
            elif choice == '5':
                books.show_all_books()


            # Func to show all of library's customers
            # Calls for "show_all_customers" func from Customers class
            elif choice == '6':
               customers.show_all_customers()


            # Func to show all of library's loans
            # Calls for "show_all_loans" func from Loans class
            elif choice == '7':
                loans.show_all_loans()


            elif choice == '8':
                loans.LATE()


            # Func to search for a book(s) by the title
            # Asks from user to input the book's title
            # Calls for "find_book" func from Books class and gives it the title inputted by the user
            elif choice == '9':
                title=input("Enter Book Title: ")
                # Call func from the class, give func the input as parameter
                books.find_book(title)


            # Func to search for a customer(s) by mane
            # Asks from user to input the customer's name
            # Calls for "find_customer" func from Customers class and gives it the name inputted by the user
            elif choice == '10':
                name=input('Enter Customer Name: ')
                # Call func from the class, give func the input as parameter
                customers.find_customer(name)


            # Func to delete a book using book's ID
            # Asks from user to input the book's ID
            # Makes sure input is integer
            # Calls for "remove_book" func from Books class and gives it the ID num inputted by the user
            elif choice == '11':
                try:
                    ID=int(input("Enter Book ID for removal: "))
                    # Call func from the class, give func the input as parameter
                    books.remove_book(ID)

                # Error handling for input is not int
                except ValueError:
                    print("Invalid input: ID's must be integers only.")


            # Func to delete a customer using customer's ID
            # Asks from user to input the customer's ID
            # Makes sure input is integer
            # Calls for "remove_customer" func from Customers class and gives it the ID num inputted by the user
            elif choice == '12':
                try:
                    ID=input("Enter Customer ID for removal: ")
                    # Call func from the class, give func the input as parameter
                    customers.remove_customer(ID)

                # Error handling for input is not int
                except ValueError:
                    print("Invalid input: ID's must be integers only.")

            # Func to exit the program
            # Breaks the loop
            elif choice == '13':
                print ('Exiting, Goodbye.')
                break


            # Func to prevent the program crashing if user gives invalid input
            # Will show "try again" message and loop back to showing the main menu and asking for input
            else:
                print('Invalid Choice. Please select again:')


    # Run the "main" func
    main()

