import mysql.connector as my

con = my.connect(host='bplx7zjluj8ztqdment0-mysql.services.clever-cloud.com', user='utdc4xugroxopi4q', password='l3A4aV1qVd3bMPBHITBG', database='bplx7zjluj8ztqdment0')
curs=con.cursor()

try:
    id = int(input('Enter Book id : '))
    re = input('Enter Review for the Book : ')
    curs.execute("Select * from Books where Book_Id = %d" %id)
    data = curs.fetchall()
    if data:
        curs.execute("update Books set Review = '%s' where Book_Id = %d" %(re, id))
        con.commit()

        print()
        print('Book review is added')

    else:
        print()
        print('Book does not exist')

except:
    print()
    print('Invalid input')

con.close()