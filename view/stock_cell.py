from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QFrame, QListView, QListWidgetItem
from PyQt6.QtGui import QPalette
from PyQt6.QtCore import Qt


class StockCell(QWidget):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller
        self.fontSize = 5
        self.initUI()

    def updateView(self, stockCode, floatPcnt):
        self.nameLabel.setText(f'<font color="white" size={self.fontSize}>{stockCode}</font>')
        percent = "{:+.02f} %".format(floatPcnt)
        if floatPcnt >= 0:
            self.floatLabel.setText(f'<font color="red" size={self.fontSize}>{percent}</font>')
        else:
            self.floatLabel.setText(f'<font color="red" size={self.fontSize}>{percent}</font>')

    def initUI(self):
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Base, Qt.GlobalColor.black)
        self.setAutoFillBackground(True)
        self.setPalette(palette)
        layout = QHBoxLayout()
        self.nameLabel = QLabel(f'<font color="red" size=5>123</font>')
        self.floatLabel = QLabel(f'<font color="green" size=5>456</font>')
        layout.addWidget(self.nameLabel)
        layout.addStretch(1)
        layout.addWidget(self.floatLabel)
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 50)