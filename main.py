import sys

from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)
        self.circles = []

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        circle_x, circle_y = randint(0, 650), randint(0, 650)
        circle_coord = randint(10, 500)
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.circles.append([circle_x, circle_y, circle_coord, color])
        self.repaint()

    def draw_circle(self, qp):
        for circle in self.circles:
            qp.setBrush(circle[3])
            qp.drawEllipse(circle[0], circle[1], circle[2], circle[2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
