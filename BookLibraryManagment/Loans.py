import pyodbc
import datetime
from datetime import timedelta, datetime

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


    def __del__(self):
        # Closing the connection when the instance is destroyed
        self.conn.close()


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
            today = datetime.now().date()

            q = 'insert into Loans (custID, bookID, loan_Date) values (?,?,?)'
            self.cursor.execute(q, (custID,bookID, today))
            self.conn.commit()  # Adding the new loan to the database
            print("Book loaned successfully") # Prints approval

        except Exception as e:
            print('An ERROR has occurred:', str(e))


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
            today = datetime.now().date()

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


        except Exception as e:
            print('An ERROR has occurred:', str(e))


    def show_all_loans(self):

        """
        Name: Mir Shukhman
        Date: 27.08.23
        The func shows all the loans from the table "Loans" of the SQL Database.
        No input required, returns ALL the loans (open and closed)
        """

        try:
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


        except Exception as e:
            print('An ERROR has occurred:', str(e))


    def LATE(self):

        """
        Name: Mir Shukhman
        Date: 27.08.23
        The func shows all the late loans from the table "Loans" of the SQL Database.
        The func finds all open (return date = null) loans
        For all open loans finds loan type for the book using book ID
        Using loan type, calculates expected return date for the book
        If expected return date has passed, appends loan to list of late loans
        Prints list of late loans (if none found, will return "non found" message)
        No input required
        """

        try:
            # Finding all loans in the database with no return date
            q = "Select * from Loans where return_Date is null"
            self.cursor.execute(q)
            open_loans = self.cursor.fetchall()  # Getting loans data
            late_loans= []  # Creating empty list of late loans
            today = datetime.now().date()

            for i in open_loans:
                cust_id = i[0]
                book_id = i[1]
                loan_date = i[2]

                # Getting loan type by book ID from Books table of the database
                q = "Select loan_type from Books where ID = ?"
                self.cursor.execute(q, (book_id,))
                loan_type_row = self.cursor.fetchone()
                loan_type = loan_type_row[0]

                # Calculating the maximum loan time based on book type
                if loan_type == 1:
                    max_loan_time = timedelta(days=10)
                elif loan_type == 2:
                    max_loan_time = timedelta(days=5)
                elif loan_type == 3:
                    max_loan_time = timedelta(days=2)
                else:
                    print ("Invalid loan type")
                    return

                # Calculating the expected return date
                expected_return_date = loan_date + max_loan_time

                # If expected return date has passed, append the loan to list of late loans (as tupple)
                if today > expected_return_date:
                    late_loans.append((cust_id, book_id, loan_date, expected_return_date))

            # If no late loans - return "no late loans" message
            if not late_loans:
                print("No Late Loans!")
                return

            # If late loans found- print those
            else:
                print("Late Loans:")
                for i in late_loans:
                    print(f'Loaning Customer ID: {i[0]}, Book ID: {i[1]}, Loan Date: {i[2]}, Expected Return Date (Passed): {i[3]}')

        except Exception as e:
            print('An ERROR has occurred:', str(e))