import pyodbc
import datetime

class Loans:

    """
     Name: Mir Shukhman
     Date: 25.08.23
     Class of library's Loans
     Has funcs for: Loaning book, Returning book, Showing all loans, Showing late loans.
     """

    def __init__(self):
        # Establishing the connection to the SQL server and the cursor as class objects
        self.conn = pyodbc.connect(
            'Driver={ODBC Driver 17 for SQL Server};Server=localhost\\SQLEXPRESS;Database=BookLibraryManagment;Trusted_Connection=yes;'
        )
        self.cursor = self.conn.cursor()


    def loan_book(self,custID,bookID):

        """
        Name: Mir Shukhman
        Date: 27.08.23
        The func allows to add a new loan to the table "Loans" of the SQL Database.
        The input requires the loaning customer's ID and loaned book ID
        If the action successful, will print out approval message
        THE FUNC IS TO BE USED ONLY AFTER IMPLEMENTATION OF "find_customer_BY_ID" from Customers class
            and "find_book_BY_ID" from Books class, witch will prevent errors when creating the new loan.
        """

        try:
            self.conn  # Establishing connection to SQL server
            today= datetime.datetime.today()

            q = 'insert into Loans (custID, bookID, loan_Date) values (?,?,?)'
            self.cursor.execute(q, (custID,bookID, today))
            self.conn.commit()  # Adding the new loan to the database
            print("Book loaned successfully") # Prints approval

            self.conn.close()  # Closing the connection with the server

        except Exception:
            print('An ERROR has occurred:', Exception)


    def return_book(self,bookID):

        """
        Name: Mir Shukhman
        Date: 27.08.23
        The func allows to add return date to existing loan in the table "Loans" of the SQL Database.
        The input requires the loaned book ID
        The func will search for loan in the database with given bookID & no return date
        If not found, will print "not found" message
        If found, will proceed with adding return date and will print out approval message
        THE FUNC IS TO BE USED ONLY AFTER IMPLEMENTATION OF "find_book_BY_ID" from Books class
        """

        try:
            self.conn # Establishing connection to SQL server
            today = datetime.datetime.today()

            # Finding loan in the database with given bookID & no return date
            q = 'select * from Loans where bookID=? and return_Date is null'
            self.cursor.execute(q, (bookID,))
            found = self.cursor.fetchall()

            # If not found - print "not found" message
            if not found:
                print("No open loans with given Book ID")

            # If found - input today as return date for the loan
            else:
                q = "Update Loans set return_date = ? where bookID= ? and return_Date is null"
                self.cursor.execute(q, (today,bookID))
                self.conn.commit()
                print('Return Successful') # Print approval message

            self.conn.close() # Closing the connection with the server

        except Exception:
            print('An ERROR has occurred:', Exception)

    def show_all_loans(self):

        """
        Name: Mir Shukhman
        Date: 27.08.23
        The func shows all the loans from the table "Loans" of the SQL Database.
        No input required, returns ALL the loans (open and closed)
        """

        try:
            self.conn  # Establishing connection to SQL server
            q = "Select * from Loans"
            self.cursor.execute(q)
            loans = self.cursor.fetchall()  # Getting loans data

            if not loans:
                # If no loans in the database
                print("No loans in the database.")

            else:
                # Returns the details of all loans
                print("List of all the Loans:")
                for i in loans:
                    print(f'Loaning Customer ID: {i[0]}, Book ID: {i[1]}, Loan Date: {i[2]}, Return Date {i[3]}')

            self.conn.close()  # Closing the connection with the server

        except Exception:
            print('An ERROR has occurred:', Exception)

    def LATE(self):
        try:
            self.conn  # Establishing connection to SQL server

            # Finding all loans in the database with no return date
            q = "Select * from Loans where return_Date is null"
            self.cursor.execute(q)
            open_loans = self.cursor.fetchall()  # Getting loans data
            bookID=[i[1] for i in open_loans]
            loan_Date=[i[2] for i in open_loans]
            q= "Select "





            self.conn.close()  # Closing the connection with the server

        except Exception:
            print('An ERROR has occurred:', Exception)