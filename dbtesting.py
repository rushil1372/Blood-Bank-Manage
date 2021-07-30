import pymysql
import sys
# Creation of PyMySQL Connection Object
conn = pymysql.connect(host="localhost",port=3306,db="test",user="root",password="")
print("Connection established sucessfully")

# Creation of a Cursor object
cursor = conn.cursor()
conn.begin() # initiate the transaction
# Storing SQL Statements in a variable sql
sql = "INSERT INTO pre_exam(hemogloblin_gdl,temp_f,blood_pressure,pulse_rate_BPM) VALUES (17.0,35.5,140/60,40)"
# Calling execute method
cursor.execute(sql)
# Update/Delete/Insert commands via execute won't be finalized until changes are committed
conn.commit() # finalize the changes
# Close the connection
cursor.close()
conn.close()
