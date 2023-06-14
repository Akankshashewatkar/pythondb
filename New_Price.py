import mysql.connector as my

con = my.connect(host='bplx7zjluj8ztqdment0-mysql.services.clever-cloud.com', user='utdc4xugroxopi4q', password='l3A4aV1qVd3bMPBHITBG', database='bplx7zjluj8ztqdment0')
curs=con.cursor()

try:
    id = int(input('Enter Book id : '))
    pr = float(input('Enter the new price of Book : '))
    curs.execute("Select Price from Books where Book_Id = %d" %id)
    data = curs.fetchall()

    if data:
        curs.execute("update Books set Price = %.1f where Book_Id = %d" %(pr, id))
        con.commit()

        print()
        print('Price of Book is changed')

    else:
        print()
        print('Book does not exist')

except:
    print()
    print('Invalid input')

con.close()