from PyQt5 import QtWidgets, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import numpy as np

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        #Load the UI Page
        uic.loadUi('window.ui', self)
        self.graphWidget.setBackground('w')
        self.graphWidget.setMenuEnabled(False)
        self.graphWidgetVel.setBackground('w')
        self.graphWidgetVel.setMenuEnabled(False)
        self.btn_graficar.clicked.connect(self.calcular)


    def calcular(self):

        qmax = float(self.spbox_pos.text())
        tf = float(self.spbox_tiempo.text())
        if (tf==0):
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Parece que hubo un error, vuelve a intentar con otros valores.")
            x = msg.exec_()
        else:
            x = np.linspace(0, tf, num=50)
            pos = qmax * ((10 * ((x / tf)) ** 3) - (15 * ((x / tf)) ** 4) + (6 * ((x / tf) ** 5)))
            vel = qmax * ((30 * ((x ** 2) / (tf ** 3))) - 60 * ((x ** 3) / (tf ** 4)) + 30 * ((x ** 4) / (tf ** 5)))
            acel = qmax * ((60 * (x / (tf ** 3))) - (180 * ((x ** 2) / (tf ** 4))) + (120 * ((x ** 3) / (tf ** 5))))
            self.graphWidget.clear()
            self.graphWidgetVel.clear()
            self.plot(x, pos, vel)



    def plot(self, x, pos, vel):
        styles = {'color': '000000', 'font-size': '14px'}
        pen = pg.mkPen(color=(255, 0, 0),width=3)
        self.graphWidget.setTitle("Posición vs. Tiempo",color="000000")
        self.graphWidget.setLabel('left', 'Posición', **styles)
        self.graphWidget.setLabel('bottom', 'Tiempo', **styles)
        self.graphWidget.setBackground('w')
        self.graphWidget.setMouseEnabled(x=False,y=False)
        self.graphWidget.setXRange(0, x[-1])
        self.graphWidget.setYRange(0, pos[-1])
        self.graphWidget.setMenuEnabled(False)
        self.graphWidget.plot(x, pos,pen=pen)

        pen = pg.mkPen(color=(0, 255, 0),width=3)
        self.graphWidgetVel.setTitle("Velocidad vs. Tiempo",color="000000")
        self.graphWidgetVel.setLabel('left', 'Velocidad', **styles)
        self.graphWidgetVel.setLabel('bottom', 'Tiempo', **styles)
        self.graphWidgetVel.setBackground('w')
        self.graphWidgetVel.setMouseEnabled(x=False, y=False)
        self.graphWidgetVel.setXRange(0, x[-1])
        self.graphWidgetVel.setYRange(0, vel[25])
        self.graphWidgetVel.setMenuEnabled(False)
        self.graphWidgetVel.plot(x,vel,pen=pen)

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()