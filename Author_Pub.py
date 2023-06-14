import mysql.connector as my

con = my.connect(host='bplx7zjluj8ztqdment0-mysql.services.clever-cloud.com', user='utdc4xugroxopi4q', password='l3A4aV1qVd3bMPBHITBG', database='bplx7zjluj8ztqdment0')
curs=con.cursor()

au = input('Enter the Name of Author : ')
pu = input('Enter the Name of Publication : ')

curs.execute("select Book_Name from Books where Author = '%s' AND Publication = '%s'" %(au, pu))
data = curs.fetchall()

if data:
    print()
    no = 0
    for rec in data:
        no += 1
        print('%d) %s' %(no, rec[0]))

else:
    print()
    print('No Book have these Author and Publication combination')

con.close()