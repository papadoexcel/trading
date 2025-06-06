from core import trading_bot
from gui.dashboard import Dashboard
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    trading_bot.run_bot()
    sys.exit(app.exec_())
