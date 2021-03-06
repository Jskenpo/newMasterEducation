import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from Datos import Archivos
from Opciones_GUI import Opc
from OpcProfe_GUI import Oprofe
import pandas as pd


class Inicio(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("Sesion.ui",self)
        self.butInicio.clicked.connect(self.Iniciar)
        self.butSalir.clicked.connect(self.close)



    def Iniciar(self):
        global RegistrosPo, RegistrosP
        correo = str(self.textCorreo.text())
        contra = str(self.textContra.text())
        tipo = self.comboBox.currentText()

        arch = Archivos()
        profe = False
        try:
            RegistrosPo = pd.read_csv('CSV_PROYECTO.csv', encoding= 'windows-1252')
            RegistrosP = RegistrosPo.set_index("Correo")


        except Exception as e:
            print("error en archivos:  ", e)

        if tipo == 'Estudiante':
            try:
                if not arch.ingreso(RegistrosPo, RegistrosP, correo, contra,tipo):
                    self.veri.setText("El correo y/o la contra son incorrectos")
                else :
                    self.opc = Opc()
                    self.opc.show()
            except Exception as e:
                print("error en estudiante: ", e)

        elif tipo == 'Profesor':
            try:
                profe = arch.ingreso(RegistrosPo, RegistrosP, correo, contra, tipo)
            except Exception as e:
                print("error en profesor: ", e)

            try:
                if not profe:
                    self.veri.setText("El correo y/o la contra son incorrectos")
                else :
                    self.opc = Oprofe()
                    self.opc.show()
            except Exception as e :
                print("error en el if ", e)

        self.close()







if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = Inicio()
    GUI.show()
    sys.exit(app.exec_())