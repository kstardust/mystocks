from PyQt6.QtWidgets import QListWidgetItem, QWidget, QVBoxLayout, QListWidget
from view.stock_cell import StockCell
from model import stock_model


class StockList(QWidget):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller
        self.stockCode2Widget = {}
        self.initUI()

    def updateView(self, listStocks):
        for stock in listStocks:
            item = QListWidgetItem()
            widget = StockCell()
            self.listView.addItem(item)
            self.listView.setItemWidget(item, widget)
            item.setSizeHint(widget.sizeHint())
            self.stockCode2Widget[stock.code] = widget
            widget.updateView(stock.code, stock.floatPcnt)

    def initUI(self):
        layout = QVBoxLayout()
        self.listView = QListWidget(self)
        self.listView.setStyleSheet(
            "QListView::item {border-bottom: 1px solid black;}"
            "QListView {outline: none;}"
            "QScrollBar {width: 0px;}"
        )
        layout.addWidget(self.listView)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet("{border: 0px;}")
        self.setLayout(layout)
