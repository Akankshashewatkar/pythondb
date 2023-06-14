import mysql.connector as my

con = my.connect(host='bplx7zjluj8ztqdment0-mysql.services.clever-cloud.com', user='utdc4xugroxopi4q', password='l3A4aV1qVd3bMPBHITBG', database='bplx7zjluj8ztqdment0')
curs=con.cursor()

ct = input('Enter category of book you want to search : ')

curs.execute("Select Book_Name from Books where Category = '%s'" %ct)
data = curs.fetchall()

if data:
    print()
    no = 0
    for rec in data:
        no += 1
        print('%d) %s' %(no, rec[0]))

else:
    print()
    print('No Book have these category')

print()
con.close()