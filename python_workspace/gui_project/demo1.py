import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chart = QChart()
    chart.setTitle("简单折线图")
    chart.setAnimationOptions(QChart.SeriesAnimations)
    chart.legend().hide()

    line_series = QLineSeries()  # Using line charts for this example
    x_values = [1, 2, 3, 4,5,6,7]
    y_values = [1.6, 1.7, 2.1, 3.6,2,2.5,1.6]
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
    W = QWidget()
    W.setLayout(v_box)
    W.show()
    sys.exit(app.exec_())
