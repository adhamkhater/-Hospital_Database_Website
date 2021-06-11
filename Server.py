import mysql.connector
from flask import Flask, redirect, url_for, request,render_template
import numpy as np

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="mysql",
  database="Operation_rooms_database"
)
mycursor = mydb.cursor()
app = Flask(__name__)

@app.route('/' , methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      password = request.form['password']
      email = request.form['email']
      data = []

      if email == 'admin@admin.com' and password == 'adminadmin':
         return render_template('home.html')
      
      else:
         ####################################################
         sql = "SELECT * FROM PATIENT WHERE e_mail = %s"
         mycursor.execute(sql, (email,))
         data.append(mycursor.fetchall())
         
         if(len(data[0]) > 0):
            return render_template('home.html')
         ####################################################
         sql = "SELECT * FROM doctor WHERE e_mail = %s"
         mycursor.execute(sql, (email,))
         data.append(mycursor.fetchall())

         if(len(data[0]) > 0):
            return render_template('home.html')
         ####################################################
         sql = "SELECT * FROM nurse WHERE e_mail = %s"
         mycursor.execute(sql, (email,))
         data.append(mycursor.fetchall())

         if(len(data[0]) > 0):
            return render_template('home.html')
         ####################################################
         sql = "SELECT * FROM technician WHERE e_mail = %s"
         mycursor.execute(sql, (email,))
         data.append(mycursor.fetchall())

         if(len(data[0]) > 0):
            return render_template('home.html')   
         ####################################################
         sql = "SELECT * FROM employee WHERE e_mail = %s"
         mycursor.execute(sql, (email,))
         data.append(mycursor.fetchall())

         if(len(data[0]) > 0):
            return render_template('home.html')            
         ####################################################
      return render_template('error_login.html', data = 'Wrong Username or Password')
   else:
      return render_template('login.html')

@app.route('/home')
def Home():
   return render_template('Home.html')

@app.route('/room' , methods = ['POST', 'GET'])
def room():
   if request.method == 'POST':
      room = request.form['room']
      sql = "SELECT * FROM ROOM WHERE Room_no = %s;"
      val = tuple(room)
      mycursor.execute(sql, val)
      R_data = mycursor.fetchall()

      sql = "SELECT * FROM PATIENT WHERE EXISTS (SELECT * FROM ROOM WHERE P_ssn = Pssn AND Room_no = %s);"
      mycursor.execute(sql, val)
      patient = mycursor.fetchall()

      sql = "SELECT * FROM Doctor WHERE room = %s AND speciality = 'Anesthetization';"
      mycursor.execute(sql, val)
      A_doctor = mycursor.fetchall()

      sql = "SELECT * FROM Doctor WHERE room = %s AND NOT speciality = 'Anesthetization';"
      mycursor.execute(sql, val)
      doctor = mycursor.fetchall()

      sql = "SELECT * FROM NURSE WHERE room = %s;"
      mycursor.execute(sql, val)
      nurse = mycursor.fetchall()

      return render_template('view/room.html', data = R_data, data2 = patient, data3 = A_doctor, data4 = doctor, data5 = nurse)
   else:
      mycursor.execute("SELECT * FROM ROOM")
      rooms = mycursor.fetchall()
      return render_template('view/room_choose.html', data = rooms)

@app.route('/Doctor')
def Doctor():
   mycursor.execute("SELECT * FROM DOCTOR")
   myresult=mycursor.fetchall()
   return render_template('view/Doctor.html',data=myresult)


@app.route('/Patient')
def Patient():
   mycursor.execute("SELECT * FROM PATIENT")
   myresult=mycursor.fetchall()
   return render_template('view/Patient.html',data=myresult)

@app.route('/Nurse')
def Nurse():
   mycursor.execute("SELECT * FROM Nurse")
   myresult=mycursor.fetchall()
   return render_template('view/Nurse.html',data=myresult)

@app.route('/Machine')
def Machine():
   mycursor.execute("SELECT * FROM Machine")
   myresult=mycursor.fetchall()
   return render_template('view/Machine.html',data=myresult)

@app.route('/Technician')
def Technician():
   mycursor.execute("SELECT * FROM Technician")
   myresult=mycursor.fetchall()
   return render_template('view/Technician.html',data=myresult)

@app.route('/Employee')
def Employee():
   mycursor.execute("SELECT * FROM Employee")
   myresult=mycursor.fetchall()
   return render_template('view/Employee.html',data=myresult)

@app.route('/adddoctor' , methods = ['POST', 'GET'])
def adddoctor():
   if request.method == 'POST':
      fname = request.form['fname']
      lname = request.form['lname']
      gender = request.form['gender']
      phone_number = request.form['phone_number']
      salary = request.form['salary']
      age = request.form['age']
      e_mail = request.form['e_mail']
      speciality = request.form['speciality']
     
      sql = "INSERT INTO DOCTOR (fname, lname, gender, phone_number, salary, age, e_mail, speciality) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
      val = (fname, lname, gender, phone_number, salary, age, e_mail, speciality)
      mycursor.execute(sql, val)
      mydb.commit()
      return render_template('Home.html')
   else:
      return render_template('add/adddoctor.html')

@app.route('/addpatient' , methods = ['POST', 'GET'])
def addpatient():
   if request.method == 'POST':
      fname = request.form['fname']
      lname = request.form['lname']
      gender = request.form['gender']
      age = request.form['age']
      e_mail = request.form['e_mail']
      illness = request.form['illness']
      insurance_company = request.form['insurance_company']
     
      sql = "INSERT INTO PATIENT (fname, lname, gender, age, e_mail, illness, insurance_company) VALUES (%s,%s,%s,%s,%s,%s,%s)"
      val = (fname, lname, gender, age, e_mail, illness, insurance_company)
      mycursor.execute(sql, val)
      mydb.commit()
      return render_template('Home.html')
   else:
      return render_template('add/addpatient.html')

@app.route('/addmachine' , methods = ['POST', 'GET'])
def addmachine():
   if request.method == 'POST':
      name = request.form['name']
      out_of_order = request.form['out_of_order']
     
      sql = "INSERT INTO MACHINE (name, out_of_order) VALUES (%s,%s)"
      val = (name, out_of_order)
      mycursor.execute(sql, val)
      mydb.commit()
      return render_template('Home.html')
   else:
      return render_template('add/addmachine.html')

@app.route('/addtech', methods = ['POST', 'GET'])
def addtech():
   if request.method == 'POST':
      fname = request.form['fname']
      lname = request.form['lname']
      working_hours = request.form['working_hours']
      salary = request.form['salary']
      gender = request.form['gender']
      age = request.form['age']
      e_mail = request.form['e_mail']
      major = request.form['major']
     
      sql = "INSERT INTO TECHNICIAN (fname, lname, gender, working_hours, salary, age, e_mail, major) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
      val = (fname, lname, gender, working_hours, salary, age, e_mail, major)
      mycursor.execute(sql, val)
      mydb.commit()
      return render_template('Home.html')
   else:
      return render_template('add/addtech.html')

@app.route('/addnurse', methods = ['POST', 'GET'])
def addnurse():
   if request.method == 'POST':
      fname = request.form['fname']
      lname = request.form['lname']
      gender = request.form['gender']
      salary = request.form['salary']
      age = request.form['age']
      e_mail = request.form['e_mail']
     
      sql = "INSERT INTO Nurse (fname, lname, gender, salary, age, e_mail) VALUES (%s,%s,%s,%s,%s,%s)"
      val = (fname, lname, gender, salary, age, e_mail)
      mycursor.execute(sql, val)
      mydb.commit()
      return render_template('Home.html')
   else:
      return render_template('add/addnurse.html')

@app.route('/addemployee', methods = ['POST', 'GET'])
def addemployee():
   if request.method == 'POST':
      fname = request.form['fname']
      lname = request.form['lname']
      working_hours = request.form['working_hours']
      salary = request.form['salary']
      gender = request.form['gender']
      age = request.form['age']
      e_mail = request.form['e_mail']
      major = request.form['major']
     
      sql = "INSERT INTO EMPLOYEE (fname, lname, gender, working_hours, salary, age, e_mail, major) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
      val = (fname, lname, gender, working_hours, salary, age, e_mail, major)
      mycursor.execute(sql, val)
      mydb.commit()
      return render_template('Home.html')
   else:
      return render_template('add/addemployee.html') 



@app.route('/f_operation', methods = ['POST', 'GET'])
def f_operation():
   if request.method == 'POST':
      try:
         room = request.form['room']

         sql = "UPDATE ROOM SET P_ssn = NULL WHERE Room_no = %s;"
         val = tuple(room)
         mycursor.execute(sql, val)
         mydb.commit()

         sql = "UPDATE Nurse SET room = NULL WHERE room = %s;"
         mycursor.execute(sql, val)
         mydb.commit()

         sql = "UPDATE Doctor SET room = NULL WHERE room = %s;"
         mycursor.execute(sql, val)
         mydb.commit()

         return render_template('Home.html')
      except:
         return render_template('error.html', data = "No room is currently in surgery to empty.")   
   else:
      mycursor.execute("SELECT * FROM ROOM WHERE EXISTS (SELECT Pssn FROM PATIENT WHERE Pssn = P_ssn);")
      rooms = mycursor.fetchall()

      return render_template('room_assign/f_operation.html', data = rooms)


@app.route('/b_operation', methods = ['POST', 'GET'])
def b_operation():
   if request.method == 'POST':
      try:
         ssn = request.form['patient']
         room = request.form['room']
         nurse = request.form['nurse']
         a_doctor = request.form['a_doctor']
         doctor = request.form['doctor']

         sql = "UPDATE ROOM SET p_ssn = %s WHERE Room_no = %s;"
         val = (ssn, room)
         mycursor.execute(sql, val)
         mydb.commit()

         sql = "UPDATE Nurse SET room = %s WHERE Nssn = %s;"
         val = (room, nurse)
         mycursor.execute(sql, val)
         mydb.commit()

         sql = "UPDATE Doctor SET room = %s WHERE Dssn = %s;"
         val = (room, a_doctor)
         mycursor.execute(sql, val)
         mydb.commit()

         sql = "UPDATE Doctor SET room = %s WHERE Dssn = %s;"
         val = (room, doctor)
         mycursor.execute(sql, val)
         mydb.commit()
         return render_template('Home.html')
      except:
         return render_template('error.html', data = "ERROR: all rooms are used or the staff number is not enough to begin Surgery.")
   else:
      mycursor.execute("SELECT * FROM PATIENT WHERE NOT EXISTS (SELECT P_ssn FROM ROOM WHERE Pssn = P_ssn);")
      patients = mycursor.fetchall()

      mycursor.execute("SELECT * FROM NURSE WHERE NOT EXISTS (SELECT Room_no FROM ROOM WHERE Room_no = room);")
      Nurses = mycursor.fetchall()

      mycursor.execute("SELECT * FROM DOCTOR WHERE speciality = 'Anesthetization' AND NOT EXISTS (SELECT Room_no FROM ROOM WHERE Room_no = room);")
      A_Doctors = mycursor.fetchall()

      mycursor.execute("SELECT * FROM DOCTOR WHERE NOT speciality = 'Anesthetization' AND NOT EXISTS (SELECT Room_no FROM ROOM WHERE Room_no = room);")
      Doctors = mycursor.fetchall()

      mycursor.execute("SELECT * FROM ROOM WHERE NOT EXISTS (SELECT Pssn FROM PATIENT WHERE Pssn = P_ssn);")
      rooms = mycursor.fetchall()

      return render_template('room_assign/b_operation.html', data = patients, data2 = rooms, data3 = Nurses, data4 = A_Doctors, data5 = Doctors)


'''
@app.route('/M_room', methods = ['POST', 'GET'])
def M_room():
   if request.method == 'POST':
      fname = request.form['fname']
     
      sql = "INSERT INTO EMPLOYEE (fname, lname, Essn, gender, working_hours, salary, age, e_mail, major) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
      val = (fname, lname, Essn, gender, working_hours, salary, age, e_mail, major)
      mycursor.execute(sql, val)
      mydb.commit()
      return render_template('Home.html')
   else:
      return render_template('room_assign/M_room.html')       
'''

if __name__ == '__main__':
   app.run(host="0.0.0.0")
