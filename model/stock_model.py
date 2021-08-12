import threading

class StockModel:
    def __init__(self, code, name=None):
        self.code = name
        self.name = name
        self.floatPcnt = 0


class PositionModel:
    def __init__(self):
        self.lock = threading.Lock()
        self.updatingThread = threading.Thread(target=self.updateData, daemon=True)

    def GetData(self):
        with self.lock:
            stocks = []
            for i in range(10):
                stock = StockModel(f"stock_{i}")
                stock.floatPcnt = i
                stocks.append(stock)
            return stocks

    def updateData(self):
        import time
        while True:
            print("updateData")
            time.sleep(1)

    def startUpdating(self):
        if not self.updatingThread.is_alive():
            self.updatingThread.start()
