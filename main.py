import sys
from PyQt5 import QtWidgets
from Modelo.Login import FormularioLogin

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=FormularioLogin()
    app.exec()