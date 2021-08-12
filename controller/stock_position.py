from model import stock_model
from view import stock_list
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QWidget
import sys


class StockPosition:
    def __init__(self):
        self.stockModel = stock_model.PositionModel()
        self.app = QApplication(sys.argv)
        self.timer = QTimer(self.app)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.onTick)
        self.timer.start()

        self.positionView = stock_list.StockList()
        self.positionView.setWindowTitle("my positions")
        self.positionView.show()

        self.stockModel.startUpdating()

    def onTick(self):
        self.positionView.updateView(self.stockModel.GetData())

