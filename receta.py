import sys, os
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QMainWindow
from principal import Ui_Buscardor
from resultado import Ui_Resultado

class Resultado(QMainWindow):
    def __init__(self):
        super(Resultado, self).__init__()
        self.ui = Ui_Resultado()
        self.ui.setupUi(self)

    @Slot()
    def cerrar(self):
        self.close()

class Principal(QMainWindow):
    def __init__(self):
        super(Principal, self).__init__()
        self.ui = Ui_Buscardor()
        self.ui.setupUi(self)
        self.opened_file = None

    @Slot()
    def buscar(self):
        print("Buscar funciona")
        self.nombre = self.ui.lblNombre.text()
        self.user = os.popen("whoami").read()
        self.user = self.user.rsplit()
        self.ruta = "/home/"+self.user[0]
        print(self.ruta)
        self.resultado = os.listdir("find -not -path '*/\.*' | grep '" + self.nombre + "'").read()
        print(self.resultado)
        self.ventanita = Resultado()
        self.ventanita.ui.txtResultado.setText(self.resultado)
        self.ventanita.show()


    @Slot()
    def borrar(self):
        print("Borrar funciona")
        self.ui.lblNombre.setText("")


    @Slot()
    def func(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Principal()
    window.show()
    sys.exit(app.exec_())

"""if os.name == 'nt':
    import win32api, win32con

def folder_is_hidden(p):
    if os.name== 'nt':
        attribute = win32api.GetFileAttributes(p)
        return attribute & (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM)
    else:
        return p.startswith('.') #linux-osx"""
#Lo de arriba es para una futura correccion.