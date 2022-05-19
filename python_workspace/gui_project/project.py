import sys

from PyQt5.QtChart import QChart, QLineSeries, QValueAxis, QChartView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPainter
from PyQt5.QtWidgets import QWidget, QApplication, QMenu, QAction, QMainWindow, QHBoxLayout, QFrame, QSplitter, \
    QVBoxLayout, QLabel, QLineEdit, QGridLayout


class GnssTest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.init_menu()
        self.base = QWidget(self)
        self.base.resize(500,500)
        self.base.move(20, 20)
        self.init_box()
        self.setGeometry(50, 50, 1000, 650)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def init_menu(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('打开')

        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)
        newAct = QAction('New', self)
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

    def init_box(self):
        hbox = QHBoxLayout(self.base)
        self.topleft = QFrame(self.base)
        self.topleft.resize(250, 250)
        self.topleft.setLayout(self.init_chart())
        self.topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self.base)
        grid = QGridLayout(topright)
        topright.setLayout(grid)
        self.lbl = QLabel(topright)
        qle = QLineEdit(self)

        grid.addWidget(self.lbl, 20, 10)
        topright.resize(250, 250)
        topright.setFrameShape(QFrame.StyledPanel)
        self.bottom = QFrame(self.base)
        self.bottom.resize(500, 250)
        self.bottom.setLayout(self.init_chart())
        self.bottom.setFrameShape(QFrame.StyledPanel)
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(self.topleft)
        splitter1.addWidget(topright)
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(self.bottom)
        hbox.addWidget(splitter2)

    def init_chart(self):
        chart = QChart()
        chart.setTitle("简单折线图")
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.legend().hide()

        line_series = QLineSeries()  # Using line charts for this example
        x_values = [1, 2, 3, 4, 5, 6, 7]
        y_values = [1.6, 1.7, 2.1, 3.6, 2, 2.5, 1.6]
        for value in range(0, len(x_values)):
            line_series.append(x_values[value], y_values[value])
        chart.addSeries(line_series)  # Add line series to chart instance

        axis_x = QValueAxis()
        axis_x.setLabelFormat("%d")
        chart.addAxis(axis_x, Qt.AlignBottom)
        line_series.attachAxis(axis_x)

        axis_y = QValueAxis()
        axis_y.setLabelFormat("%d")
        chart.addAxis(axis_y, Qt.AlignLeft)
        line_series.attachAxis(axis_y)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        v_box = QVBoxLayout()
        v_box.addWidget(chart_view)
        return v_box

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gnss_test = GnssTest()
    sys.exit(app.exec_())
