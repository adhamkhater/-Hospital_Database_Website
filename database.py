import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="mysql"
)


mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE Operation_rooms_database")
mycursor.execute("CREATE DATABASE Operation_rooms_database")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="mysql",
  database="Operation_rooms_database"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE ROOM (Room_no int NOT NULL AUTO_INCREMENT, Room_name VARCHAR(50), P_ssn INT, PRIMARY KEY (Room_no))")
mycursor.execute("CREATE TABLE PATIENT (Pssn int NOT NULL AUTO_INCREMENT, age INT DEFAULT NULL, fname VARCHAR(100), lname VARCHAR(100), gender VARCHAR(10), illness VARCHAR(100), insurance_company VARCHAR(50), e_mail VARCHAR(50), PRIMARY KEY (Pssn))")
mycursor.execute("CREATE TABLE DOCTOR (Dssn int NOT NULL AUTO_INCREMENT, fname VARCHAR(100), lname VARCHAR(100), gender VARCHAR(10), phone_number VARCHAR(12), salary INT, age INT DEFAULT NULL, e_mail VARCHAR(30), speciality VARCHAR(50), room INT, PRIMARY KEY (Dssn), FOREIGN KEY (room) REFERENCES ROOM (Room_no))")
mycursor.execute("CREATE TABLE NURSE (Nssn int NOT NULL AUTO_INCREMENT, age INT DEFAULT NULL, fname VARCHAR(100), lname VARCHAR(100), e_mail VARCHAR(50), gender VARCHAR(10), salary INT, PRIMARY KEY (Nssn), room INT, FOREIGN KEY (room) REFERENCES ROOM (Room_no))")
mycursor.execute("CREATE TABLE TECHNICIAN (Tssn int NOT NULL AUTO_INCREMENT, age INT DEFAULT NULL, fname VARCHAR(100), lname VARCHAR(100), working_hours INT, e_mail VARCHAR(50), gender VARCHAR(10), salary INT, major VARCHAR(50), PRIMARY KEY (Tssn))")
mycursor.execute("CREATE TABLE EMPLOYEE (Essn int NOT NULL AUTO_INCREMENT, age INT DEFAULT NULL, fname VARCHAR(100), lname VARCHAR(100), working_hours INT, e_mail VARCHAR(50), gender VARCHAR(10), salary INT, major VARchar(50), PRIMARY KEY (Essn))")
mycursor.execute("CREATE TABLE MACHINE (serial_number int NOT NULL AUTO_INCREMENT, name VARCHAR(100), out_of_order VARCHAR(1) , room INT, PRIMARY KEY (serial_number), FOREIGN KEY (room) REFERENCES ROOM (Room_no))") # el out of order ya ema y= yes ya ema n= no
mycursor.execute("CREATE TABLE TECH_MAC (T_ssn int NOT NULL AUTO_INCREMENT, SN INT, FOREIGN KEY (T_ssn) REFERENCES TECHNICIAN (Tssn),FOREIGN KEY (SN) REFERENCES MACHINE (serial_number))")
#mycursor.execute("CREATE TABLE USER (e_mail VARCHAR(50), Password int")
#mycursor.execute("CREATE TABLE BLOODSAMPLES (ID int NOT NULL AUTO_INCREMENT, BLOODTYPE VARCHAR(10), HEMO  VARCHAR(10), oxygen  VARCHAR(10), whiteblood  VARCHAR(10), redblood  VARCHAR(10),  P_ssn INT, PRIMARY KEY (ID), FOREIGN KEY (P_ssn) REFERENCES PATIENT (Pssn))")
#mycursor.execute("CREATE TABLE MEDICATION (MED_code int NOT NULL AUTO_INCREMENT ,MED_name VARCHAR(100), P_ssn INT, dose VARCHAR(20), no_perday INT, PRIMARY KEY (MED_code), FOREIGN KEY (P_ssn) REFERENCES PATIENT (Pssn))")

#******************************* ADD TO PATIENT ********************************************
sql="INSERT INTO PATIENT (age,fname,lname,gender,illness,insurance_company, e_mail) VALUES (%s,%s,%s,%s,%s,%s,%s)"
value= [
  ('40','ahmed','mahmoud','male','kidney_failure','royal','habd@habd.com'),
  ('22','ahmed','mohamed','male','brain_tumor','alianz','habd2@habd2.com'),
  ('18','khalid','ahmed','male','liver_tumor','royal','khalid@habad.com'),
  ('25','menna','youssef','female','heart_attack','medcom','menna@gmail.com'),
  ('22','youssef','khalid','male','autism','alianz','A.khalid@hotmail.com'),
  ('27','omar','hussein','male','brain_tumor','alianz','habd2@habd2.com'),
  ('30','souhaila','mohamed','female','short_sight','medcom','sue@yahoo.com'),
  ('28','mahmoud','ahmed','male','autism','royal','7oda@gmail.com'),
  ('50','layla','mohamed','female','heart_attack','metlife','layla@hotmail.com'),
  ('19','hisham','khaled','male','bone_fracture','alianz','hisham@habd2.com'),
]

mycursor.executemany(sql,value)
mydb.commit()
#*********************************** ADD TO DOCTOR *******************************************
sql="INSERT INTO DOCTOR (fname,lname,gender, phone_number,salary,age,e_mail,speciality) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
value = [
  ('aly','mahmoud','Male','01100888555', '30000','50','aly_aly@aly.com','bone surgery'),
  ('khalid','ahmed','Male','01104088555','25000','35','khalid@gmail.com','bone surgery'),
  ('ahmed','mostafa','Male','01177888525','30000','65','ahmed@yahoo.com','cardiologist'),
  ('omar','mahmoud','Male','01558488188','17000','30','omar@gmail.com','Anesthetization'),
  ('hanan','aly','Male','01578128845','17000','50','h_aly@gmail.com','Anesthetization'),
  ('menna','assem','Female','01234888645','27000','40','Menna84@hotmail.com','Ocular surgery'),
  ('osama','ahmed','Male','01007516444','17000','55','osos@yahoo.com','Anesthetization'),
  ('essam','naguib','Male','01100778545','27000','45','Essam_87@gmail.com','cardiologist'),
  ('youssef','mohamed','Male','01202888335','33000','60','youssef@gmail.com','neurologist'),
]
mycursor.executemany(sql,value)
mydb.commit()
#*********************************** ADD TO NURSE ****************************************************
sql="INSERT INTO NURSE (age,fname,lname,e_mail,gender,salary) VALUES (%s,%s,%s,%s,%s,%s)"
value = [
  ('34','noha','mohamed','noha@gmail.com','female','3000'),
  ('32','mai','ahmed','mai@gmail.com','female','3500'),
  ('30','menna','omar','menna@hotmail.com','female','4000'),
  ('29','layla','khalid','layla@yahoo.com','female','3000'),
  ('27','omar','hisham','omar@gmail.com','male','2000'),
  ('29','hoda','hisham','hoda@gmail.com','female','3000'),
  ('34','doaa','youssef','dodo@hotmail.com','female','4000'),
  ('33','noha','mohamed','noha@gmail.com','female','3000'),
  ('32','mai','mohamed','mai@hotmail.com','female','2000'),
  ('29','noha','mahmoud','noha_mahmoud@gmail.com','female','2500'),
]
mycursor.executemany(sql,value)
mydb.commit()
#********************************** ADD TO TECHNICIAN *******************************
sql="INSERT INTO TECHNICIAN (age,fname,lname,working_hours,e_mail,gender,salary,major) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
value = [
  ('30','mahmoud','omar','6','7odda@7oda.com','male','2000','diploma'),
  ('29','mohamed','ahmed','6','mohamed@ahmed.com','male','3000','diploma'),
  ('32','youssef','khalid','5','joe@gmail.com','male','2500','commerce'),
  ('35','omar','hassan','8','abo_omar@hotmail.com','male','4000','institute'),
  ('40','mahmoud','omar','6','7odda@7oda.com','male','2000','diploma')
]
mycursor.executemany(sql,value)
mydb.commit()
#*********************************** ADD TO EMPLOYEE **********************************
sql="INSERT INTO EMPLOYEE (age,fname,lname,working_hours,e_mail,gender,salary,major) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
value = [
  ('30','moaaz','zaki','6','xkazblanca@habd.com','male','800','diploma'),
  ('29','deeb','ahmed','6','mohamed@ahmed.com','male','3000','diploma'),
  ('32','habd','khalid','5','joe@gmail.com','male','2500','commerce'),
  ('35','tmam','hassan','8','abo_omar@hotmail.com','male','4000','institute'),
  ('40','andrew','omar','6','7odda@7oda.com','male','2000','diploma')
]
mycursor.executemany(sql,value)
mydb.commit()
#********************************** ADD TO MACHNIE **************************************
sql= "INSERT INTO MACHINE (name,out_of_order) VALUES (%s,%s)"
value= [
  ('Anethesia','y'),
  ('surgical_table','n'),
  ('sterilization','y'),
  ('monitor','y'),
  ('surgical_microscope','n')
]
mycursor.executemany(sql,value)
mydb.commit()
#******************************** ADD TO Mediction ****************************************
#sql = "INSERT INTO MEDICATION (MED_code ,MED_name, dose, no_perday) VALUES (%s,%s,%s,%s)"
#value= [
  #('0001','profin','3 cm cube', '2'),
  #('0002','morfin','5 cm cube','0'),
  #('0003','augmenten','1 pill', '2'),
  #('0004','panadol','2 pills', '2'),
#]
#mycursor.executemany(sql,value)
#mydb.commit()
#******************************** ADD TO ROOM ****************************************
sql = "INSERT INTO ROOM (Room_name, P_ssn) VALUES (%s, %s)"
value= [
  ('Heart surgery', 'NULL'),
  ('Neuro surgery', 'NULL'),
  ('Heart surgery', 'NULL'),
  ('ocular surgery', 'NULL'),
  ('ocular surgery', 'NULL'),
  ('Orthopedic', 'NULL'),
  ('Orthopedic', 'NULL')
]
mycursor.executemany(sql, value)
mydb.commit()