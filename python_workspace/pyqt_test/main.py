from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QAction, QTextEdit, QStatusBar, QPushButton, QMdiSubWindow, QMdiArea, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
import sys

# 增加了多个子窗口


class MainWindow(QMainWindow):
    count = 0
    def __init__(self):
        super(MainWindow, self).__init__()
        self.title = "GNSS Test"
        self.setWindowTitle(self.title)
        self.init_ui()
        self.center()

    def init_ui(self):
        self.resize(800, 500)
        # 状态栏
        # self.status = self.statusBar()
        # self.status.showMessage("只存在五秒的消息", 5000)
        self.mdiarea = QMdiArea()
        self.setCentralWidget(self.mdiarea)
        self.createMenu()
        self.createToolBar()
        # self.setCentralWidget(QTextEdit())
        self.editer = QTextEdit("我是默认的文本", self)
        self.editer.setHtml("good")

        self.editer.setGeometry(100,100, 250, 200)
        self.getbtn = QPushButton("点我获取文本信息", self)
        self.getbtn.setGeometry(100, 350, 100, 30)
        self.getbtn.clicked.connect(self.btn_click)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        self.comNum = QLabel("串口号：")
        self.bauNum = QLabel("波特率：")
        self.status.addPermanentWidget(self.comNum, stretch=0)
        self.status.addPermanentWidget(self.bauNum, stretch=0)


    def btn_click(self):
        input_str = self.editer.toPlainText()
        input_html = self.editer.toPlainText()
        self.editer.clear()
        print(input_str)
        print(input_html)



    def center(self):
        screen = QDesktopWidget().screenGeometry()
        window_size = self.geometry()
        top_left_x_point = (screen.width() - window_size.width()) / 2
        top_left_y_point = (screen.height() - window_size.height()) / 2
        self.move(top_left_x_point, top_left_y_point)

    def createMenu(self):
        self.mainMenuBar = self.menuBar()
        self.fileMenu = self.mainMenuBar.addMenu("File")

        save = QAction("Save", self)
        save.setShortcut("Ctrl + S")
        self.fileMenu.addAction(save)
        save.triggered.connect(self.handle_save)

        quit_app = QAction("Quit", self)
        self.fileMenu.addAction(quit_app)
        quit_app.triggered.connect(self.handle_quit)

        self.view = self.mainMenuBar.addMenu("视图方式")

        new_view = QAction("new_view", self)
        self.view.addAction(new_view)

        x_dic = QAction("水平方向", self)
        self.view.addAction(x_dic)

        y_dic = QAction("垂直方向", self)
        self.view.addAction(y_dic)
        self.view.triggered.connect(self.addSubWindow)



    def addSubWindow(self, q):
        if q.text() == "new_view":
            MainWindow.count += 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit(f"子窗口{MainWindow.count}"))
            sub.setWindowTitle(f"我是子窗口{MainWindow.count}")
            self.mdiarea.addSubWindow(sub)
            sub.show()
        elif q.text() == "水平方向":
            self.mdiarea.cascadeSubWindows()
        elif q.text() == "垂直方向":
            self.mdiarea.tileSubWindows()

    def createToolBar(self):
        tb1 = self.addToolBar("文件")
        
        new = QAction(QIcon("/images/new.png"), "新建文件", self)
        tb1.addAction(new)
        open_action = QAction(QIcon("/images/open.png"), "打开", self)
        tb1.addAction(open_action)

        tb1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        tb1.actionTriggered.connect(self.pushButton)


        tb2 = self.addToolBar("文件")
        new2 = QAction(QIcon("/images/new.png"), "新建文件2", self)
        tb2.addAction(new2)


    def pushButton(self, a):
        print("按下的按钮是", a.text())
        self.comNum.setText("串口号：COM19")
        self.bauNum.setText("波特率:30db")

    def handle_save(self):
        print(self.sender().text())
        self.status.showMessage(f"{self.sender().text()}被点击了", 5000)
        self.comNum.setText("串口号：COM19")
        self.bauNum.setText("波特率:20db")

    def handle_quit(self):
        print(self.sender().text())
        app = QApplication.instance()
        app.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
