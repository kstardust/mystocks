import sys
from controller.stock_position import StockPosition


def main():
    PositionApp = StockPosition()
    sys.exit(PositionApp.app.exec())


if __name__ == '__main__':
    main()
