import pyodbc

class Customers:

    """
    Name: Mir Shukhman
    Date: 23.08.23
    Class of library's Customers
    Has funcs for: Adding customer, Removing customer,
        Searching for customer by Name, and Showing all the customers.
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


    def add_customer(self,name,city,age):

        """
        Name: Mir Shukhman
        Date: 23.08.23
        The func allows to add a new customer to the table "Customers" of the SQL Database.
        The input requires the new customer's detains: name, city and age.
        If the action successful, will print out approval and new customer's ID number
        """

        try:
            q = 'INSERT into Customers (name,city,age) VALUES (?,?,?)'
            self.cursor.execute(q, (name, city, age))
            self.conn.commit()   # Adding the new customer to the database

            # Getting&Returning new customer's ID num to be printed to the user
            q = 'select ID from Customers where name=? and city=? and age=?'
            self.cursor.execute(q, (name, city, age))
            new_cus_id = self.cursor.fetchone()[0]
            print(name, "has been added successfully to the customer database, ID num:", new_cus_id)

        except Exception as e:
            print('An ERROR has occurred:', str(e))


    def remove_customer(self,ID):

        """
        Name: Mir Shukhman
        Date: 23.08.23
        The func allows to remove a customer from the table "Customers" of the SQL Database.
        The input requires the customers ID num.
        The func will first display the customer's details to the user, then ask if the user wants to proceed.
        If the user cancels, exits func.
        If user proceeds, deletes the chosen customer from the SQL Database & prints approval message.
        """

        try:
            q = 'select * from Customers where ID=?'
            self.cursor.execute(q, (ID,))
            found=self.cursor.fetchall()  # Looking & Getting the customer's details with matching ID num

            # If customer with given ID not found, returns error message
            if not found:
                print("No customer found with the ID:", ID)

            else:
                # Returns the found customer's details to the user:
                # Making sure the one user wanted to delete was picked
                while True:
                    print ("Is this the customer you would like to remove?")
                    for i in found:
                        print(f'Customer ID: {i[0]}, Name: {i[1]}, City: {i[2]}, Age: {i[3]}')
                    # The user will choose if to proceed with delete
                    choice=int(input('1-Yes (Remove the customer permanently) \n2-No (Cancel the action)\nChoice: '))

                    # User approved the customer's details and the func deletes the customer from the database
                    if choice== 1:
                        delete='Delete from Customers where ID=?'
                        self.cursor.execute(delete,(ID,))
                        self.conn.commit()
                        print('Customer deleted from database successfully')
                        break

                    # User chose to cancel the action, exits func
                    elif choice==2:
                        print('Action Canceled')
                        break

                    # Invalid input was given by user, will show the options again
                    else:
                        print('Invalid option. Try again:')

        except Exception as e:
            print('An ERROR has occurred:', str(e))


    def find_customer_BY_ID(self,ID):

        """
        Name: Mir Shukhman
        Date: 27.08.23
        The func allows to find a customer from the table "Customers" of the SQL Database, by the customer's ID.
        The input requires the customer's ID.
        If customer by the given ID found, will show the customer details and return them
        If not, will show "not found" message and return None
        """

        try:
            q = 'select * from Customers where ID=?'
            self.cursor.execute(q, (ID,))
            found = self.cursor.fetchall()  # Looking & Getting the customer's details with matching ID num

            # If customer with given ID not found, returns "not found" message
            if not found:
                print("No customer found with the ID:", ID)

                return None  # Returns None for cust not found

            # Returns the found customer's details to the user:
            else:
                print ("Customer Found:")
                for i in found:
                    print(f'Customer ID: {i[0]}, Name: {i[1]}, City: {i[2]}, Age: {i[3]}')

                return found  # Returns the cust found

        except Exception as e:
            print('An ERROR has occurred:', str(e))


    def find_customer(self,name):

        """
        Name: Mir Shukhman
        Date: 23.08.23
        The func allows to find a customer from the table "Customers" of the SQL Database, by the customer's name.
        The input requires the customer's name.
        If customer(s) by the given name found, will show the customer(s) details.
        If not, will show "not found" message.
        """

        try:
            q = ('select * from Customers where name=?')
            self.cursor.execute(q,(name,))
            found = self.cursor.fetchall() # Looking & Getting the customer's details with the given name

            # No customer by given name found, returns "not found" message
            if not found:
                print("No customer found by the name:", name)

            # Returns the details of customer(s) found with given name
            else:
                for i in found:
                    print("Customer found:")
                    print(f'Customer ID: {i[0]}, Name: {i[1]}, City: {i[2]}, Age: {i[3]}')

        except Exception as e:
            print('An ERROR has occurred:', str(e))


    def show_all_customers(self):

        """
        Name: Mir Shukhman
        Date: 23.08.23
        The func shows all the customers from the table "Customers" of the SQL Database.
        No input required, returns all customers.
        """

        try:
            q="Select * from Customers"
            self.cursor.execute(q)
            customers= self.cursor.fetchall() # Getting customer data

            if not customers:
                # If no customers in the database
                print("No customers in the database.")

            else:
                # Returns the details of all customers
                print("List of all the Customers:")
                for i in customers:
                    print(f'Customer ID: {i[0]}, Name: {i[1]}, City: {i[2]}, Age: {i[3]}')

        except Exception as e:
            print('An ERROR has occurred:', str(e))
