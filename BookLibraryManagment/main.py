from Customers import Customers
from Books import Books
from Loans import Loans

if __name__=='__main__':

    def main():

        customers = Customers()
        books = Books()
        loans = Loans()

        while True:

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
                  '12. Remover customer\n'
                  '13. Exit')

            choice=input('Enter Number of the desired function: ')

            if choice=='1':
                print("Please enter the new customer's details:")
                name=input('Name: ')
                city=input('City: ')
                age=input('Age: ')
                customers.add_customer(name,city,age)
                print (f'Customer {name} added successfully.')
                #add show newcust ID to the print

            elif choice=='2':
                print("Please enter the new Book's details:")
                title = input('Title: ')
                author = input('Author: ')
                # add error handling for if year!=int
                year = int(input('Publication Year: '))
                # add error handling for if loan_type!=int
                loan_type= input('Type (1-up to 10 day loan,2-up to 5 days,3-up to 2 days): ')
                books.add_book(title,author,year,loan_type)
                print(f'The Book "{title}" by {author} added successfully.')
                # add show newbook ID to the print

            elif choice == '3':
                custID=("Enter ID of the loaning Customer: ")
                bookID = ("Enter ID of the Book being loaned: ")
                loans.loan_book(custID,bookID)
                print ("")#booktitle loaned to custname sucseffuly. expected return date:

            elif choice == '4':
                bookID = ("Enter ID of the Book being returned: ")
                loans.return_book(bookID)
                print("")#book title returned sucsefully.

            elif choice == '5':
                books.show_all_books()

            elif choice == '6':
                customers.show_all_customers()

            elif choice == '7':
                loans.show_all_loans()

            elif choice == '8':
                loans.LATE()

            elif choice == '9':
                title=input("Enter Book Title: ")
                books.find_book(title)

            elif choice == '10':
                name=input('Enter Customer Name: ')
                customers.find_customer(name)

            elif choice == '11':
                ID=input("Enter Book ID for removal: ")
                books.remove_book(ID)

            elif choice == '12':
                ID=input("Enter Customer ID for removal: ")
                customers.remove_customer(ID)

            elif choice == '13':
                print ('Exiting, Goodbye.')
                break
            else:
                print('Invalid Choice. Please select again:')

    main()

