# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'msgConcealer.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import cv2
import string



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(730, 650)
        MainWindow.setStyleSheet("background-color:rgb(76, 139, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.heading = QtWidgets.QLabel(self.centralwidget)
        self.heading.setGeometry(QtCore.QRect(0, 10, 611, 61))
        self.heading.setStyleSheet("font:26pt \"Palatino Linotype\";")
        self.heading.setObjectName("heading")
        self.encText = QtWidgets.QTextEdit(self.centralwidget)
        self.encText.setGeometry(QtCore.QRect(30, 230, 691, 41))
        self.encText.setObjectName("encText")
        self.decText = QtWidgets.QTextEdit(self.centralwidget)
        self.decText.setGeometry(QtCore.QRect(30, 330, 691, 41))
        self.decText.setObjectName("decText")
        self.enterMessage = QtWidgets.QLabel(self.centralwidget)
        self.enterMessage.setGeometry(QtCore.QRect(20, 80, 251, 41))
        self.enterMessage.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.enterMessage.setObjectName("enterMessage")
        self.msgText = QtWidgets.QTextEdit(self.centralwidget)
        self.msgText.setGeometry(QtCore.QRect(30, 120, 691, 51))
        self.msgText.setObjectName("msgText")
        self.encryptBtn = QtWidgets.QPushButton(self.centralwidget)
        self.encryptBtn.setGeometry(QtCore.QRect(30, 180, 171, 41))
        self.encryptBtn.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.encryptBtn.setObjectName("encryptBtn")
        self.decryptBtn = QtWidgets.QPushButton(self.centralwidget)
        self.decryptBtn.setGeometry(QtCore.QRect(30, 280, 171, 41))
        self.decryptBtn.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.decryptBtn.setObjectName("decryptBtn")
        self.hideBtn = QtWidgets.QPushButton(self.centralwidget)
        self.hideBtn.setGeometry(QtCore.QRect(30, 380, 321, 41))
        self.hideBtn.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.hideBtn.setObjectName("hideBtn")
        self.hideText = QtWidgets.QTextEdit(self.centralwidget)
        self.hideText.setGeometry(QtCore.QRect(30, 430, 691, 31))
        self.hideText.setObjectName("hideText")
        self.hideText.setPlaceholderText("Enter the full image location")
        self.hideBtn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.hideBtn_2.setGeometry(QtCore.QRect(30, 470, 321, 41))
        self.hideBtn_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.hideBtn_2.setObjectName("hideBtn_2")
        self.hideText_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.hideText_2.setGeometry(QtCore.QRect(30, 520, 691, 31))
        self.hideText_2.setObjectName("hideText_2")
        self.hideText_2.setPlaceholderText("Enter the image location")
        self.hideText_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.hideText_3.setGeometry(QtCore.QRect(30, 560, 691, 31))
        self.hideText_3.setObjectName("hideText_3")
        self.hideText_3.setPlaceholderText("Hidden Message in Image")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 730, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def encryption(self):
        userMsg = self.msgText.toPlainText()
        
        encryptedResult = ''
        for i in userMsg:
            encryptedResult += chr(ord(i)+6)
        
        self.encText.setPlainText(encryptedResult)
        return encryptedResult

    
    def decryption(self):
        userMsg = self.msgText.toPlainText()
        
        decryptedResult = ''
        for i in userMsg:
            decryptedResult += chr(ord(i)-6)
        self.decText.setPlainText(decryptedResult)
        return decryptedResult  
    result = ''
    def hideInImage(self):
        path = self.hideText.toPlainText()
        if path == '':
            pass
        else:
            c = {}
            d = {}

            for i in range(255):
                d[chr(i)]=i
                c[i]=chr(i)

            x = cv2.imread(path)

            i = x.shape[0]
            j = x.shape[1]
            print(i,j)

            key = '1234'
            text = self.msgText.toPlainText()

            kl = 0
            tln = len(text)
            z = 0 #decides plane
            n = 0 #number of row
            m = 0 #number of column

            l = len(text)

            for i in range(l):
                x[n,m,z] = d[text[i]]^d[key[kl]]
                n += 1
                m += 1
                m = (m+1)%3 #this is for every value of z , remainder will be between 0,1,2 . i.e G,R,B plane will be set automatically.
                            #whatever be the value of z , z=(z+1)%3 will always between 0,1,2 . The same concept is used for random number in dice and card games.
                kl = (kl+1)%len(key)
                
            cv2.imwrite("encrypted_img.jpg", x) 
            os.startfile("encrypted_img.jpg")
            self.hideText.setPlainText("Image saved as encrypted_img.jpg")
            #x=cv2.imread(“encrypted_img.jpg")

            if self.hideBtn_2.clicked:
                imgPath = self.hideText_2.toPlainText()
                kl = 0
                # tln = len(text)
                z = 0 #decides plane
                n = 0 #number of row
                m = 0 #number of columns

                key = '1234'
                decryptedMsg=""
                for i in range(l):
                    decryptedMsg += c[x[n,m,z]^d[key[kl]]]
                    n = n+1
                    m = m+1
                    m = (m+1)%3
                    kl = (kl+1)%len(key)
                self.hideText_3.setPlainText('')
    def getFromImage(self):

        imgPath = self.hideText_2.toPlainText()
        c = {}
        d = {}
        x = cv2.imread(imgPath)
        for i in range(255):
            d[chr(i)]=i
            c[i]=chr(i)
        kl = 0
        # tln = len(text)
        z = 0 #decides plane
        n = 0 #number of row
        m = 0 #number of columns

        key = '1234'
        decryptedMsg=""
        for i in range(100):
            decryptedMsg += c[x[n,m,z]^d[key[kl]]]
            n = n+1
            m = m+1
            m = (m+1)%3
            kl = (kl+1)%len(key)
        self.hideText_3.setPlainText(decryptedMsg)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.heading.setText(_translate("MainWindow", "            Message Concealer"))
        self.enterMessage.setText(_translate("MainWindow", "    Enter Message"))
        self.encryptBtn.setText(_translate("MainWindow", "Encrypt "))
        self.decryptBtn.setText(_translate("MainWindow", "Decrypt"))
        self.hideBtn.setText(_translate("MainWindow", "Hide Message in Image"))
        self.hideBtn_2.setText(_translate("MainWindow", "Get Message from Image "))
        
        self.encryptBtn.clicked.connect(self.encryption)
        self.decryptBtn.clicked.connect(self.decryption)
        self.hideBtn.clicked.connect(self.hideInImage)
        self.hideBtn_2.clicked.connect(self.getFromImage)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
