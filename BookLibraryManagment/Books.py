import pyodbc

class Books:

    """
    Name: Mir Shukhman
    Date: 24.08.23
    Class of library's Books
    Has funcs for: Adding book, Removing book,
        Searching for book by Title, and Showing all the books.
    """


    def __init__(self):
        # Establishing the connection to the SQL server and the cursor as class objects
        self.conn = pyodbc.connect(
            'Driver={ODBC Driver 17 for SQL Server};Server=localhost\\SQLEXPRESS;Database=BookLibraryManagment;Trusted_Connection=yes;'
        )
        self.cursor = self.conn.cursor()


    def add_book(self,title,author,pub_year,loan_type):

        """
        Name: Mir Shukhman
        Date: 25.08.23
        The func allows to add a new book to the table "Books" of the SQL Database.
        The input requires the new book's detains: title, author, publication year, and type of loan for the book.
        If the action successful, will print out approval and new book's ID number
        """

        try:
            self.conn # Establishing connection to SQL server
            q = 'insert into Books (title,autor,pub_year,loan_type) values (?,?,?,?)'
            self.cursor.execute(q, (title,author,pub_year,loan_type))
            self.conn.commit()  # Adding the new book to the database

            # Getting&Returning new book's ID num to be printed to the user
            self.cursor.execute('select SCOPE_IDENTITY()')
            new_book_ID = self.cursor.fetchone()[0]
            print(title,"by", author, "has been added successfully to the books database, ID num:", new_book_ID)

            self.conn.close()  # Closing the connection with the server

        except Exception:
            print('An ERROR has occurred:', Exception)


    def remove_book(self,ID):

        """
        Name: Mir Shukhman
        Date: 25.08.23
        The func allows to remove a book from the table "Books" of the SQL Database.
        The input requires the book's ID num.
        The func will first display the book's details to the user, then ask if the user wants to proceed.
        If the user cancels, exits func.
        If user proceeds, deletes the chosen book from the SQL Database & prints approval message.
        """

        try:
            self.conn  # Establishing connection to SQL server
            q = 'select * from Books where ID=?'
            self.cursor.execute(q, (ID,))
            found = self.cursor.fetchall()  # Looking & Getting the book's details with matching ID num

            # If a book with given ID not found, returns error message
            if not found:
                print("No book found with the ID:", ID)

            else:
                # Returns the found book's details to the user, making sure the one user wanted to delete was picked
                while True:
                    print("Is this the book you would like to remove?")
                    for i in found:
                        print(f'Book ID: {i[0]}, Title: {i[1]}, Author: {i[2]}, Publication Year: {i[3]}')
                    # The user will choose if to proceed with delete
                    choice = int(input('1-Yes (Remove the book permanently) \n2-No (Cancel the action)\nChoice: '))

                    # User approved the book's details and the func deletes the book from the database
                    if choice == 1:
                        delete = 'Delete from Books where ID=?'
                        self.cursor.execute(delete, (ID,))
                        self.conn.commit()
                        print('The Book deleted from database successfully')
                        break

                    # User chose to cancel the action, exits func
                    elif choice == 2:
                        print('Action Canceled')
                        break

                    # Invalid input was given by user, will show the options again
                    else:
                        print('Invalid option. Try again:')

            self.conn.close()  # Closing the connection with the server

        except Exception:
            print('An ERROR has occurred:', Exception)


    def find_book(self,title):

        """
        Name: Mir Shukhman
        Date: 25.08.23
        The func allows to find book(s) from the table "Books" of the SQL Database, by the book's title.
        The input requires the book's title.
        If book(s) by the given title found, will show the book(s) details.
        If not, will show "not found" message.
        """

        try:
            self.conn  # Establishing connection to SQL server
            q = ('select * from Books where title=?')
            self.cursor.execute(q, (title,))
            found = self.cursor.fetchall()  # Looking & Getting the book's details with the given title

            # No book by given title found, returns "not found" message
            if not found:
                print("No books found by the title:", title)

            # Returns the details of book(s) found with given title
            else:
                for i in found:
                    print("Book found:")
                    print(f'Book ID: {i[0]}, Title: {i[1]}, Author: {i[2]}, Publication Year: {i[3]}, Loan Type: {i[4]}')

            self.conn.close()  # Closing the connection with the server

        except Exception:
            print('An ERROR has occurred:', Exception)


    def find_book_BY_ID(self,ID):

        """
        Name: Mir Shukhman
        Date: 27.08.23
        The func allows to find a book from the table "Books" of the SQL Database, by the book's ID.
        The input requires the book's ID.
        If book by the given ID found, will show the book's details and return them
        If not, will show "not found" message and return None
        """

        try:
            self.conn # Establishing connection to SQL server
            q = 'select * from Books where ID=?'
            self.cursor.execute(q, (ID,))
            found=self.cursor.fetchall()  # Looking & Getting the book's details with matching ID num

            # If book with given ID not found, returns "not found" message
            if not found:
                print("No book found with the ID:", ID)

                return None  # Returns None for book not found

            # Returns the found book's details to the user:
            else:
                print ("Book Found:")
                for i in found:
                    print(f'Book ID: {i[0]}, Title: {i[1]}, Author: {i[2]}, Publication Year: {i[3]}, Loan Type: {i[4]}')

                return found  # Returns the book found

            self.conn.close()  # Closing the connection with the server

        except Exception:
            print ('An ERROR has occurred:',Exception)


    def show_all_books(self):

        """
        Name: Mir Shukhman
        Date: 23.08.23
        The func shows all the books from the table "Books" of the SQL Database.
        No input required, returns all the books.
        """

        try:
            self.conn  # Establishing connection to SQL server
            q = "Select * from Books"
            self.cursor.execute(q)
            books = self.cursor.fetchall() # Getting books data

            if not books:
                # If no books in the database
                print("No books in the database.")

            else:
                # Returns the details of all books
                print("List of all the Books:")
                for i in books:
                    print(f'Book ID: {i[0]}, Title: {i[1]}, Author: {i[2]}, Publication Year: {i[3]}, Loan Type: {i[4]}')

            self.conn.close()  # Closing the connection with the server

        except Exception:
            print('An ERROR has occurred:', Exception)