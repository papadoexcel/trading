from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
import sys

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Crypto Bot Dashboard')
        layout = QVBoxLayout()
        label = QLabel('Bem-vindo ao robô de trading')
        layout.addWidget(label)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec_())
