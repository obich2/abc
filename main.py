import random
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.x = self.width()
        self.y = self.height()
        self.flag = False
        self.pushButton.clicked.connect(self.draw)

    def paintEvent(self, event):
        if self.flag:
            x0, y0 = random.randint(0, self.x), random.randint(0, self.y)
            r = random.randint(0, max(self.x, self.y))
            painter = QPainter(self)
            painter.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            painter.drawEllipse(x0, y0, r, r)
            self.flag = False

    def draw(self):
        self.flag = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
