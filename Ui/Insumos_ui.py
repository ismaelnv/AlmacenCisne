# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\manue\Documents\GitHub\AlmacenCisne\Ui\Insumos.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 703)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 20, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(31)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 110, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 170, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 220, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 270, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(390, 260, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(390, 120, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.cboEstado = QtWidgets.QComboBox(self.groupBox)
        self.cboEstado.setGeometry(QtCore.QRect(20, 30, 161, 22))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cboEstado.setFont(font)
        self.cboEstado.setObjectName("cboEstado")
        self.cboEstado.addItem("")
        self.cboEstado.addItem("")
        self.cboEstado.addItem("")
        self.btnRegistrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegistrar.setGeometry(QtCore.QRect(44, 380, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegistrar.setFont(font)
        self.btnRegistrar.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(251, 235, 220);\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgb(235, 208, 180);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.btnRegistrar.setObjectName("btnRegistrar")
        self.btnModificar = QtWidgets.QPushButton(self.centralwidget)
        self.btnModificar.setGeometry(QtCore.QRect(180, 380, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnModificar.setFont(font)
        self.btnModificar.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(251, 235, 220);\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgb(235, 208, 180);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.btnModificar.setObjectName("btnModificar")
        self.btnBorrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBorrar.setGeometry(QtCore.QRect(440, 380, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnBorrar.setFont(font)
        self.btnBorrar.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(251, 235, 220);\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgb(235, 208, 180);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.btnBorrar.setObjectName("btnBorrar")
        self.txtId = QtWidgets.QLineEdit(self.centralwidget)
        self.txtId.setGeometry(QtCore.QRect(210, 120, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.txtId.setFont(font)
        self.txtId.setObjectName("txtId")
        self.txtNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(210, 170, 113, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.txtNombre.setFont(font)
        self.txtNombre.setObjectName("txtNombre")
        self.txtPrecio = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPrecio.setGeometry(QtCore.QRect(210, 220, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.txtPrecio.setFont(font)
        self.txtPrecio.setObjectName("txtPrecio")
        self.txtStock = QtWidgets.QLineEdit(self.centralwidget)
        self.txtStock.setGeometry(QtCore.QRect(210, 270, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.txtStock.setFont(font)
        self.txtStock.setObjectName("txtStock")
        self.txtIdcategoria = QtWidgets.QLineEdit(self.centralwidget)
        self.txtIdcategoria.setGeometry(QtCore.QRect(510, 270, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.txtIdcategoria.setFont(font)
        self.txtIdcategoria.setObjectName("txtIdcategoria")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, -30, 721, 711))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("c:\\Users\\manue\\Documents\\GitHub\\AlmacenCisne\\Ui\\../Img/Imagen2.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.tbDatos = QtWidgets.QTableWidget(self.centralwidget)
        self.tbDatos.setGeometry(QtCore.QRect(10, 430, 701, 192))
        self.tbDatos.setObjectName("tbDatos")
        self.tbDatos.setColumnCount(7)
        self.tbDatos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbDatos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbDatos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbDatos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbDatos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbDatos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbDatos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbDatos.setHorizontalHeaderItem(6, item)
        self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalir.setGeometry(QtCore.QRect(620, 380, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnSalir.setFont(font)
        self.btnSalir.setStyleSheet("QPushButton {    \n"
"\n"
"    background-color: rgb(251, 235, 220);\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgb(235, 208, 180);\n"
"    color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"")
        self.btnSalir.setObjectName("btnSalir")
        self.btnConsultar = QtWidgets.QPushButton(self.centralwidget)
        self.btnConsultar.setGeometry(QtCore.QRect(310, 380, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnConsultar.setFont(font)
        self.btnConsultar.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(251, 235, 220);\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgb(235, 208, 180);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.btnConsultar.setObjectName("btnConsultar")
        self.label_8.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.groupBox.raise_()
        self.btnRegistrar.raise_()
        self.btnModificar.raise_()
        self.btnBorrar.raise_()
        self.txtId.raise_()
        self.txtNombre.raise_()
        self.txtPrecio.raise_()
        self.txtStock.raise_()
        self.txtIdcategoria.raise_()
        self.tbDatos.raise_()
        self.btnSalir.raise_()
        self.btnConsultar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Insumos"))
        self.label_2.setText(_translate("MainWindow", "Id Insumo"))
        self.label_3.setText(_translate("MainWindow", "Nombre"))
        self.label_4.setText(_translate("MainWindow", "Precio"))
        self.label_5.setText(_translate("MainWindow", "Stock"))
        self.label_7.setText(_translate("MainWindow", "Id Catergoria"))
        self.groupBox.setTitle(_translate("MainWindow", "Estado"))
        self.cboEstado.setItemText(0, _translate("MainWindow", "Seleccione estado"))
        self.cboEstado.setItemText(1, _translate("MainWindow", "Activo"))
        self.cboEstado.setItemText(2, _translate("MainWindow", "Desactivo"))
        self.btnRegistrar.setText(_translate("MainWindow", "Registrar"))
        self.btnModificar.setText(_translate("MainWindow", "Modificar"))
        self.btnBorrar.setText(_translate("MainWindow", "Borrar"))
        item = self.tbDatos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tbDatos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Id Insumo"))
        item = self.tbDatos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tbDatos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Precio"))
        item = self.tbDatos.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Stock"))
        item = self.tbDatos.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Existencia"))
        item = self.tbDatos.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Id Categoria"))
        self.btnSalir.setText(_translate("MainWindow", "Salir"))
        self.btnConsultar.setText(_translate("MainWindow", "Consultar"))
