"""
动态显示当前时间
QTimer      定时器，周期性任务
QThread     完成单个任务

多线程：用于同时完成多个任务
"""

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QListWidget, QGridLayout, QLabel
from PyQt5.QtCore import QTimer, QDateTime
import sys


class showTime(QWidget):
    def __init__(self, parent=None):
        super(showTime, self).__init__(parent)
        self.setWindowTitle("动态显示当前时间")     # 设置窗口标题

        self.label = QLabel("显示当前时间")       # 创建显示当前时间标签对象
        self.startBtn = QPushButton("开始")       # 创建开始按钮对象
        self.endBtn = QPushButton("结束")         # 创建结束按钮对象

        layout = QGridLayout()      # 创建网格布局对象
        # 把"显示当前时间"标签放到网格布局中的（第0行，第0列，占1行，占2列）
        layout.addWidget(self.label, 0, 0, 1, 2)
        layout.addWidget(self.startBtn, 1, 0)
        layout.addWidget(self.endBtn, 1, 1)

        self.timer = QTimer()  # 创建QTimer（计时器）对象
        self.timer.timeout.connect(self.updateTime)  # 把timer对象的timeout信号连接到updateTime槽函数

        self.startBtn.clicked.connect(self.startTimer)      # 把"开始按钮"的"点击信号"连接到"startTimer"槽函数
        self.endBtn.clicked.connect(self.endTimer)       # 把"结束按钮"的"点击信号"连接到"endTime"槽函数

        self.setLayout(layout)      # 设定布局

    def updateTime(self):
        time = QDateTime.currentDateTime()      # 获取当前日期时间

        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")  # 格式化输出字符串年月日星期
        self.label.setText(timeDisplay)     # 把时间更新到标签

    def startTimer(self, **kwargs):
        self.timer.start(1000)  # 设置更新时间间隔
        self.startBtn.setEnabled(False)  # 设置开始按钮为禁用
        self.endBtn.setEnabled(True)     # 设置结束按钮为启用

    def endTimer(self):
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = showTime()
    form.show()
    sys.exit(app.exec_())
