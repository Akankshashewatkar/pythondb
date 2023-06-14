import mysql.connector as my

con = my.connect(host='bplx7zjluj8ztqdment0-mysql.services.clever-cloud.com', user='utdc4xugroxopi4q', password='l3A4aV1qVd3bMPBHITBG', database='bplx7zjluj8ztqdment0')
curs=con.cursor()

try:
    id = int(input('Enter the book id : '))
    nm = input('Enter Book name : ')
    ct = input('Enter the category of Book : ')
    au = input('Enter the Author name of Book : ')
    pu = input('Enter publication of Book : ')
    ed = input('Enter the edition of Book : ')
    pr = float(input('Enter the price of Book > 0 : '))
    re = input('Enter review for book : ')

    curs.execute("insert into Books values(%d, '%s', '%s', '%s', '%s', '%s', %.1f, '%s')" %(id, nm, ct, au, pu, ed, pr, re))
    con.commit()

    print()
    print('Your Book is added into the database')

except:
    print()
    print('Invalid input')
    print("We can't add new book into database")
    print()

con.close()