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
        try:
            self.conn  # Establishing connection to SQL server
            today= datetime.datetime.today()
            q = 'insert into Loans (custID, bookID, loan_Date) values (?,?,?)'
            self.cursor.execute(q, (custID,bookID, today))
            self.conn.commit()  # Adding the new loan to the database

            self.conn.close()  # Closing the connection with the server

        except Exception:
            print('An ERROR has occurred:', Exception)

    def return_book(self,bookID):
        pass

    def show_all_loans(self):
        try:
            self.conn  # Establishing connection to SQL server
            q = "Select * from Loans"
            self.cursor.execute(q)
            loans = self.cursor.fetchall()  # Getting loans data

            if not loans:
                # If no loans in the database
                print("No customers in the database.")

            else:
                # Returns the details of all customers
                print("List of all the Customers:")
                for i in customers:
                    print(f'Customer ID: {i[0]}, Name: {i[1]}, City: {i[2]}, Age: {i[3]}')

            self.conn.close()  # Closing the connection with the server

        except Exception:
            print('An ERROR has occurred:', Exception)

    def LATE(self):
        #return_Date==Null
        pass