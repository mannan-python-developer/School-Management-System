from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QDialog
import sys, sqlite3, icons_rc

class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi('login.ui', self)
        self.login_button.clicked.connect(self.loginfunction)
        self.signup_button.clicked.connect(self.signupfunction)
        
    def signupfunction(self):
        submit = Submit()
        widget.addWidget(submit)
        widget.setFixedWidth(630)
        widget.setFixedHeight(395)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def loginfunction(self):
        email = self.email.text()
        password = self.password.text()
        if len(email)==0 or len(password)==0:
            self.error.setText('Please Input the Field')
        else:
            conn = sqlite3.connect('sqlite.db')
            c = conn.cursor()
            try:
                query = 'SELECT password FROM users WHERE email =\''+email+"\'"
                c.execute(query)
                result_pass = c.fetchone()[0]
                if result_pass == password:
                    self.error.setText('')
                    student_input = Check()
                    widget.addWidget(student_input)
                    widget.setFixedWidth(565)
                    widget.setFixedHeight(275)
                    widget.setCurrentIndex(widget.currentIndex()+1)
                else:
                    self.error.setText('Invalid Password')
            except:
                self.error.setText('Invalid Username or Password') 
        
                
class Submit(QDialog):
    def __init__(self):
        super(Submit, self).__init__()
        loadUi('signup.ui', self)
        self.submit_button.clicked.connect(self.submitfunction)
        self.back_button.clicked.connect(self.login2function)
        
    def login2function(self):
        submit = Login()
        widget.addWidget(submit)
        widget.setFixedWidth(540)
        widget.setFixedHeight(385)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def submitfunction(self):
        firstname= self.first_name.text()
        lastname= self.last_name.text()
        email= self.signup_email.text()
        id = self.signup_id.text()
        password= self.signup_password.text()
        confirmpassword= self.confirm_password.text()
        if len(firstname)==0 or len(email)==0 or len(password)==0 or len(confirmpassword)==0 or len(id)==0:
            self.error_2.setText("Please Input all Fields")
        elif password!=confirmpassword:
            self.error_2.setText("Conform Password don't be match.")
        elif len(id)<6 or len(id)>6:
            self.error_2.setText("Your ID is not match, (HINT): Please used only 6 Digits")
        else:
            conn = sqlite3.connect("sqlite.db")
            c = conn.cursor()
            user_info = [firstname +" "+ lastname, email, id, password]
            c.execute('INSERT INTO users (name, email, ID, password) VALUES (?, ?, ?, ?)', user_info)
            
            conn.commit()
            conn.close()
            print("Submit Successfully")
            self.error_2.setText("")
            self.error_3.setText("                       SignUp Seccesfully:\nNow go back and enter your email and password.")


class Check(QDialog):
    def __init__(self):
        super(Check, self).__init__()
        loadUi('student_input.ui', self)
        self.st_check_button.clicked.connect(self.checkfunction)
        self.st_add_button.clicked.connect(self.addfunction)
        
    def checkfunction(self):
        st_id = self.st_id.text()
        if len(st_id)==0:
            self.error_4.setText("Please Enter the ID*")
        else:
            conn = sqlite3.connect('sqlite.db')
            c = conn.cursor()
            query = 'SELECT id FROM student WHERE id = ?'
            c.execute(query, (st_id,))

            result = c.fetchone()
            if result is not None:
                self.error_4.setText('')
                Check = Manage()
                Check.result_button.setProperty('st_id', st_id)
                Check.st_info_button.setProperty('st_id', st_id)
                Check.fee_button.setProperty('st_id', st_id)
                widget.addWidget(Check)
                widget.setFixedWidth(640)
                widget.setFixedHeight(400)
                widget.setCurrentIndex(widget.currentIndex()+1)
            else:
                self.error_4.setText('This ID* not Available')
            
    def addfunction(self):
        add = Add()
        widget.addWidget(add)
        widget.setFixedWidth(580)
        widget.setFixedHeight(540)
        widget.setCurrentIndex(widget.currentIndex()+1)
            
            
class Add(QDialog):
    def __init__(self):
        super(Add, self).__init__()
        loadUi('add_student.ui', self)
        self.add_submit_button.clicked.connect(self.addstfunction)
        self.back_button.clicked.connect(self.checkfunction)
        
    def checkfunction(self):
        student_input = Check()
        widget.addWidget(student_input)
        widget.setFixedWidth(565)
        widget.setFixedHeight(275)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def addstfunction(self):
        firstname = self.add_first_name.text()
        lastname = self.add_last_name.text()
        grdname = self.add_grd_name.text()
        addclass = self.add_class.text()
        phone = self.add_phone.text()
        grdphone = self.add_grd_phone.text()
        dob = self.add_dob.text()
        gender = "" 
        if self.add_male.isChecked():
            gender = "Male"
        elif self.add_female.isChecked():
            gender = "Female"
        
            
        if len(firstname)==0 or len(grdname)==0 or len(grdphone)==0 or len(phone)==0 or len(dob)==0 or len(gender)==0:
            self.error.setText("Please Input all Fields.")
        else:
            conn = sqlite3.connect("sqlite.db")
            c = conn.cursor()
            user_info1 = [firstname +" "+ lastname, dob, gender, phone, addclass, grdname, grdphone ]
            user_info2 = [firstname +" "+ lastname, addclass]
            user_info3 = [firstname +" "+ lastname, addclass]
            c.execute("INSERT INTO student (name, dob, gender, phone, class, guardianname, guardianphone) VALUES (?, ?, ?, ?, ?, ?, ?)", user_info1)
            c.execute("INSERT INTO results (name, class) VALUES (?, ?)", user_info2)
            c.execute("INSERT INTO fee (name, class) VALUES (?, ?)", user_info3)
                
            conn.commit()
            conn.close()
    
            add_scf = Add_scf(firstname, lastname, grdname, grdphone, addclass, dob, phone, gender)
            widget.addWidget(add_scf)
            widget.setFixedWidth(850)
            widget.setFixedHeight(470)
            widget.setCurrentIndex(widget.currentIndex()+1)
        
        
class Add_scf(QDialog):
    def __init__(self, firstname, lastname, grdname, grdphone, addclass, dob, phone, gender):
        super(Add_scf, self).__init__()
        loadUi('add_scf.ui', self)
        self.back_button.clicked.connect(self.checkfunction)
        
        self.firstname = firstname
        self.lastname = lastname
        self.grdname = grdname
        self.grdphone = grdphone
        self.phone = phone
        self.adddclass = addclass
        self.dob = dob
        self.gender = gender
        
        conn = sqlite3.connect("sqlite.db")
        c = conn.cursor()
        c.execute('SELECT id FROM student WHERE phone=?', (phone,))
        id = c.fetchone()
        conn.commit()
        conn.close()
        
        self.scf_id.setText(str(id[0]))
        self.scf_id.setFont(QtGui.QFont("Arial", 11))
        self.scf_name.setText(firstname +" "+ lastname)
        self.scf_name.setFont(QtGui.QFont("Arial", 11))
        self.scf_class.setText(addclass)
        self.scf_class.setFont(QtGui.QFont("Arial", 11))
        self.scf_phone.setText(phone)
        self.scf_phone.setFont(QtGui.QFont("Arial", 11))
        self.scf_grd_name.setText(grdname)
        self.scf_grd_name.setFont(QtGui.QFont("Arial", 11))
        self.scf_grd_phone.setText(grdphone)
        self.scf_grd_phone.setFont(QtGui.QFont("Arial", 11))
        self.scf_gender.setText(gender)
        self.scf_gender.setFont(QtGui.QFont("Arial", 11))
        self.scf_dob.setText(dob)
        self.scf_dob.setFont(QtGui.QFont("Arial", 11))
        
    def checkfunction(self):
        student_input = Check()
        widget.addWidget(student_input)
        widget.setFixedWidth(565)
        widget.setFixedHeight(275)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
class Manage(QDialog):
    def __init__(self):
        super(Manage, self).__init__()
        loadUi('interface.ui', self)
        self.result_button.clicked.connect(self.resultfunction)
        self.fee_button.clicked.connect(self.feefunction)
        self.st_info_button.clicked.connect(self.st_infofunction)
        self.back_button.clicked.connect(self.checkfunction)
    
    def checkfunction(self):
        student_input = Check()
        widget.addWidget(student_input)
        widget.setFixedWidth(565)
        widget.setFixedHeight(275)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def resultfunction(self):
        st_id = self.sender().property('st_id') 
           
        conn = sqlite3.connect("sqlite.db")
        c = conn.cursor()
        c.execute('SELECT * FROM results WHERE id=?', (st_id,))
        row = c.fetchone()
        conn.commit()
        conn.close()
        
        result = Result(row, st_id)
        widget.addWidget(result)
        widget.setFixedWidth(850)
        widget.setFixedHeight(400)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def st_infofunction(self):
        st_id = self.sender().property('st_id')
        
        
        conn = sqlite3.connect("sqlite.db")
        c = conn.cursor()
        c.execute('SELECT * FROM student WHERE id=?', (st_id,))
        row = c.fetchone()
        
        st_info = St_info(row, st_id)
        st_info.del_button.setProperty('st_id', st_id)
        widget.addWidget(st_info)
        widget.setFixedWidth(850)
        widget.setFixedHeight(490)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def feefunction(self):
        st_id = self.sender().property('st_id')
        
        conn = sqlite3.connect("sqlite.db")
        c = conn.cursor()
        c.execute('SELECT * FROM fee WHERE id=?', (st_id,))
        row = c.fetchone()
        
        fee = Fee(row, st_id)
        widget.addWidget(fee)
        widget.setFixedWidth(850)
        widget.setFixedHeight(400)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
class Result(QDialog):
    def __init__(self, row, st_id):
        super(Result, self).__init__()
        loadUi('result_table.ui', self)
        self.back_button.clicked.connect(self.checkfunction)
        self.save_button.clicked.connect(self.savefunction)
        self.back_button.setFont(QtGui.QFont("Arial", 8))

        self.result_name.setText(str(row[1]))
        self.result_name.setFont(QtGui.QFont("Arial", 12))
        self.result_id.setText(str(row[0]))
        self.result_id.setFont(QtGui.QFont("Arial", 12))
        self.result_class.setText(str(row[2]))
        self.result_class.setFont(QtGui.QFont("Arial", 12))
        self.exam_type.setText(str(row[3]))
        self.exam_type.setFont(QtGui.QFont("Arial", 12))
        self.exam_date.setText(str(row[4]))
        self.exam_date.setFont(QtGui.QFont("Arial", 12))
        self.marks_obtain.setText(str(row[5]))
        self.marks_obtain.setFont(QtGui.QFont("Arial", 12))
        
        self.back_button.setProperty('st_id', st_id)
        
    def savefunction(self):
        st_id = self.back_button.property('st_id')
        
        examtype = self.exam_type.text()
        examdate = self.exam_date.text()
        marksobtain = self.marks_obtain.text()
        
        if len(examtype)==0 or len(examdate)==0 or len(marksobtain)==0:
            self.error.setStyleSheet('background-color: white')
            self.error_2.setText("")
            self.error_3.setText("Please Input all Field.")
            self.error_3.setFont(QtGui.QFont("Arial", 8))
        else:
            conn = sqlite3.connect('sqlite.db')
            c = conn.cursor()
            c.execute('''UPDATE results SET examtype=?, examdate=?, marksobtain=? WHERE id=?''', (examtype, examdate, marksobtain, st_id))
            conn.commit()
            conn.close()
            self.error.setStyleSheet('background-color: white')
            self.error_3.setText("")
            self.error_2.setText("Your data submit Successfully.")
            self.error_2.setFont(QtGui.QFont("Arial", 8))
    
    def checkfunction(self):
        st_id = self.sender().property('st_id')
        Check = Manage()
        Check.result_button.setProperty('st_id', st_id)
        Check.st_info_button.setProperty('st_id', st_id)
        Check.fee_button.setProperty('st_id', st_id)
        widget.addWidget(Check)
        widget.setFixedWidth(640)
        widget.setFixedHeight(400)
        widget.setCurrentIndex(widget.currentIndex()+1)
        

class St_info(QDialog):
    def __init__(self, row, st_id):
        super(St_info, self).__init__()
        loadUi('student_info.ui', self)
        self.back_button.clicked.connect(self.check3function)
        self.save_button.clicked.connect(self.savefunction)
        self.del_button.clicked.connect(self.delfunction)
        
        self.st_info_name.setText(str(row[1]))
        self.st_info_name.setFont(QtGui.QFont("Arial", 11))
        self.st_info_id.setText(str(row[0]))
        self.st_info_id.setFont(QtGui.QFont("Arial", 11))
        self.st_info_class.setText(str(row[5]))
        self.st_info_class.setFont(QtGui.QFont("Arial", 11))
        self.st_info_grd_name.setText(str(row[6]))
        self.st_info_grd_name.setFont(QtGui.QFont("Arial", 11))
        self.st_info_phone.setText(str(row[4]))
        self.st_info_phone.setFont(QtGui.QFont("Arial", 11))
        self.st_info_grd_phone.setText(str(row[7]))
        self.st_info_grd_phone.setFont(QtGui.QFont("Arial", 11))
        self.st_info_gender.setText(str(row[3]))
        self.st_info_gender.setFont(QtGui.QFont("Arial", 11))
        self.st_info_dob.setText(str(row[2]))
        self.st_info_dob.setFont(QtGui.QFont("Arial", 11))
        
            
        self.back_button.setProperty('st_id', st_id)
        
    def savefunction(self):
        st_id = self.back_button.property('st_id')
        
        name = self.st_info_name.text()
        id = self.st_info_id.text()
        grdname = self.st_info_grd_name.text()
        grdphone = self.st_info_grd_phone.text()
        addclass = self.st_info_class.text()
        dob = self.st_info_dob.text()
        phone = self.st_info_phone.text()
        gender = self.st_info_gender.text()
        
        if len(name)==0 or len(addclass)==0 or len(grdname)==0 or len(phone)==0 or len(grdphone)==0 or len(gender)==0 or len(dob)==0:
            self.error.setStyleSheet('background-color: white')
            self.error_2.setText("")
            self.error_3.setText("Please Input all Field.")
            self.error_3.setFont(QtGui.QFont("Arial", 8))
        else:
            conn = sqlite3.connect('sqlite.db')
            c = conn.cursor()
            c.execute('''UPDATE student SET id=?, name=?, dob=?, gender=?, phone=?, class=?, guardianname=?, guardianphone=? WHERE id=?''', (id, name, dob, gender, phone, addclass, grdname, grdphone, st_id))
            c.execute('''UPDATE results SET id=?, name=?, class=? WHERE id=?''', (id, name, addclass, st_id))
            c.execute('''UPDATE fee SET id=?, name=?, class=? WHERE id=?''', (id, name, addclass, st_id))
            conn.commit()
            conn.close()
            
            self.error.setStyleSheet('background-color: white')
            self.error_3.setText("")
            self.error_2.setText("Your data submit Successfully.")
            self.error_2.setFont(QtGui.QFont("Arial", 8))
        
    def delfunction(self, st_id):
        st_id = self.sender().property('st_id')
        conn = sqlite3.connect('sqlite.db')
        c = conn.cursor()

        c.execute("DELETE FROM student WHERE id=?", (st_id,))
        c.execute("DELETE FROM results WHERE id=?", (st_id,))
        c.execute("DELETE FROM fee WHERE id=?", (st_id,))
        conn.commit()

        conn.close()
        
        student_input = Check()
        widget.addWidget(student_input)
        widget.setFixedWidth(565)
        widget.setFixedHeight(275)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def check3function(self):
        st_id = self.sender().property('st_id')
        Check = Manage()
        Check.result_button.setProperty('st_id', st_id)
        Check.st_info_button.setProperty('st_id', st_id)
        Check.fee_button.setProperty('st_id', st_id)
        widget.addWidget(Check)
        widget.setFixedWidth(640)
        widget.setFixedHeight(400)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
class Fee(QDialog):
    def __init__(self, row, st_id):
        super(Fee, self).__init__()
        loadUi('fee_table.ui', self)
        self.back_button.clicked.connect(self.check4function)
        self.save_button.clicked.connect(self.savefunction)
        self.back_button.setFont(QtGui.QFont("Arial", 8))
        
        self.fee_name.setText(str(row[1]))
        self.fee_name.setFont(QtGui.QFont("Arial", 12))
        self.fee_id.setText(str(row[0]))
        self.fee_id.setFont(QtGui.QFont("Arial", 12))
        self.fee_class.setText(str(row[2]))
        self.fee_class.setFont(QtGui.QFont("Arial", 12))
        self.fee_type.setText(str(row[3]))
        self.fee_type.setFont(QtGui.QFont("Arial", 12))
        self.fee_date.setText(str(row[4]))
        self.fee_date.setFont(QtGui.QFont("Arial", 12))
        self.fee_paid.setText(str(row[5]))
        self.fee_paid.setFont(QtGui.QFont("Arial", 12))
        
        self.back_button.setProperty('st_id', st_id)
        
        
        
    def savefunction(self):
        st_id = self.back_button.property('st_id')
        
        feetype = self.fee_type.text()
        paymentdate = self.fee_date.text()
        amountpaid = self.fee_paid.text()
        
        if len(feetype)==0 or len(paymentdate)==0 or len(amountpaid)==0:
            self.error.setStyleSheet('background-color: white')
            self.error_2.setText("")
            self.error_3.setText("Please Input all Field.")
            self.error_3.setFont(QtGui.QFont("Arial", 8))
        else:
            conn = sqlite3.connect('sqlite.db')
            c = conn.cursor()
            c.execute('''UPDATE fee SET feetype=?, paymentdate=?, amountpaid=? WHERE id=?''', (feetype, paymentdate, amountpaid, st_id))
            conn.commit()
            conn.close()
            self.error.setStyleSheet('background-color: white')
            self.error_3.setText("")
            self.error_2.setText("Your data submit Successfully.")
            self.error_2.setFont(QtGui.QFont("Arial", 8))
        
        
    def check4function(self):
        st_id = self.sender().property('st_id')
        Check = Manage()
        Check.result_button.setProperty('st_id', st_id)
        Check.st_info_button.setProperty('st_id', st_id)
        Check.fee_button.setProperty('st_id', st_id)
        widget.addWidget(Check)
        widget.setFixedWidth(640)
        widget.setFixedHeight(400)
        widget.setCurrentIndex(widget.currentIndex()+1)
        

app = QApplication(sys.argv)
mainwindow= Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(540)
widget.setFixedHeight(385)
widget.show()
app.exec_()
