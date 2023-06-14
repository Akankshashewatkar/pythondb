import mysql.connector as my

con = my.connect(host='bplx7zjluj8ztqdment0-mysql.services.clever-cloud.com', user='utdc4xugroxopi4q', password='l3A4aV1qVd3bMPBHITBG', database='bplx7zjluj8ztqdment0')
curs=con.cursor()

curs.execute("Select Book_Name from Books")
data = curs.fetchall()

no = 0
for rec in data:
    no += 1
    print('%d) %s' %(no, rec[0]))

con.close()