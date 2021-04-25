from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from app_ui import Ui_MainWindow
from ui_functions import *
import sys, time, os, datetime
from api import Weather_API_Engine


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(os.path.abspath("."), relative)


class WeatherApiThread(QThread):
    def __init__(self, window, parent=None):
        QThread.__init__(self, parent)
        self.window = window
        engine = Weather_API_Engine()
        self.data = engine.get_weather_data()

    def run(self):
        while True:
            self.update_weather()
            time.sleep(20)

    def update_weather(self):
        print("I'm here")
        #self.window.ui.label_home_top_right_time.setText(self.data["current"]["time"])
        self.window.ui.label_home_top_right_time.setText(datetime.datetime.now().strftime('%H:%M'))
        self.window.ui.label_home_temperature.setText(self.data["current"]["temp"])
        pixmap = QPixmap(resource_path(f'images/{self.data["current"]["icon"]}.png')).scaled(128, 164, Qt.KeepAspectRatio,
                                                                              Qt.SmoothTransformation)
        self.window.ui.label_weather_image.setPixmap(pixmap)

        self.window.ui.label_home_desc.setText(self.data["current"]["desc"])
        self.window.ui.label_home_content_wind.setText(self.data["current"]["wind"])
        pixmap = QPixmap(resource_path('images/wind.png')).scaled(30, 30, Qt.KeepAspectRatio,
                                                                              Qt.SmoothTransformation)
        self.window.ui.label_wind.setPixmap(pixmap)
        self.window.ui.label_home_content_humidity.setText(self.data["current"]["humidity"])
        pixmap = QPixmap(resource_path('images/humidity.png')).scaled(20, 20, Qt.KeepAspectRatio,
                                                                              Qt.SmoothTransformation)
        self.window.ui.label_humidity.setPixmap(pixmap)
        self.window.ui.label_home_content_pressure.setText(self.data["current"]["pressure"])
        pixmap = QPixmap(resource_path('images/pressure.png')).scaled(20, 20, Qt.KeepAspectRatio,
                                                                              Qt.SmoothTransformation)
        self.window.ui.label_pressure.setPixmap(pixmap)
        ###

        
        self.window.ui.label_p3.setText(self.data["hourly"][0]["time"])
        pixmap = QPixmap(resource_path(f'images/{self.data["hourly"][0]["icon"]}.png')).scaled(64, 72, Qt.KeepAspectRatio,
                                                                              Qt.SmoothTransformation)
        self.window.ui.label_image_p3.setPixmap(pixmap)
        self.window.ui.label_p3t.setText(self.data["hourly"][0]["temp"])
        ###
        self.window.ui.label_p6.setText(self.data["hourly"][1]["time"])
        pixmap = QPixmap(resource_path(f'images/{self.data["hourly"][1]["icon"]}.png')).scaled(64, 72, Qt.KeepAspectRatio,
                                                                              Qt.SmoothTransformation)
        self.window.ui.label_image_p6.setPixmap(pixmap)
        self.window.ui.label_p6t.setText(self.data["hourly"][1]["temp"])
        ###
        self.window.ui.label_p9.setText(self.data["hourly"][2]["time"])
        pixmap = QPixmap(resource_path(f'images/{self.data["hourly"][2]["icon"]}.png')).scaled(64, 72, Qt.KeepAspectRatio,
                                                                                Qt.SmoothTransformation)
        self.window.ui.label_image_p9.setPixmap(pixmap)
        self.window.ui.label_p9t.setText(self.data["hourly"][2]["temp"])
        ###
        self.window.ui.label_p12.setText(self.data["hourly"][3]["time"])
        pixmap = QPixmap(resource_path(f'images/{self.data["hourly"][3]["icon"]}.png')).scaled(64, 72, Qt.KeepAspectRatio,
                                                                                Qt.SmoothTransformation)
        self.window.ui.label_image_p12.setPixmap(pixmap)
        self.window.ui.label_p12t.setText(self.data["hourly"][3]["temp"])
        ###


        self.window.ui.dash_label_now.setText(self.data["daily"][0]["day"])
        pixmap = QPixmap(resource_path(f'images/{self.data["daily"][0]["icon"]}.png')).scaled(60, 64, Qt.KeepAspectRatio,
                                                                              Qt.SmoothTransformation)
        self.window.ui.label_icon_now.setPixmap(pixmap)
        self.window.ui.dash_label_now_t.setText(self.data["daily"][0]["temp"])
        ###
        self.window.ui.dash_label_tomorrow.setText(self.data["daily"][1]["day"])
        pixmap = QPixmap(resource_path(f'images/{self.data["daily"][1]["icon"]}.png')).scaled(60, 64, Qt.KeepAspectRatio,
                                                                               Qt.SmoothTransformation)
        self.window.ui.label_icon_tomorrow.setPixmap(pixmap)
        self.window.ui.dash_label_tomorrow_t.setText(self.data["daily"][1]["temp"])
        ###
        self.window.ui.dash_label_day3.setText(self.data["daily"][2]["day"])
        pixmap = QPixmap(resource_path(f'images/{self.data["daily"][2]["icon"]}.png')).scaled(60, 64, Qt.KeepAspectRatio,
                                                                              Qt.SmoothTransformation)
        self.window.ui.label_icon_day3.setPixmap(pixmap)
        self.window.ui.dash_label_day3_t.setText(self.data["daily"][2]["temp"])
        ###
        self.window.ui.dash_label_day4.setText(self.data["daily"][3]["day"])
        pixmap = QPixmap(resource_path(f'images/{self.data["daily"][3]["icon"]}.png')).scaled(60, 64, Qt.KeepAspectRatio,
                                                                               Qt.SmoothTransformation)
        self.window.ui.label_icon_day4.setPixmap(pixmap)
        self.window.ui.dash_label_day4_t.setText(self.data["daily"][3]["temp"])
        ###
        self.window.ui.dash_label_day5.setText(self.data["daily"][4]["day"])
        pixmap = QPixmap(resource_path(f'images/{self.data["daily"][4]["icon"]}.png')).scaled(60, 64, Qt.KeepAspectRatio,
                                                                               Qt.SmoothTransformation)
        self.window.ui.label_icon_day5.setPixmap(pixmap)
        self.window.ui.dash_label_day5_t.setText(self.data["daily"][4]["temp"])
        ###
        self.window.ui.dash_label_day6.setText(self.data["daily"][5]["day"])
        pixmap = QPixmap(resource_path(f'images/{self.data["daily"][5]["icon"]}.png')).scaled(60, 64, Qt.KeepAspectRatio,
                                                                               Qt.SmoothTransformation)
        self.window.ui.label_icon_day6.setPixmap(pixmap)
        self.window.ui.dash_label_day6_t.setText(self.data["daily"][5]["temp"])
        ###
        self.window.ui.dash_label_day7.setText(self.data["daily"][6]["day"])
        pixmap = QPixmap(resource_path(f'images/{self.data["daily"][6]["icon"]}.png')).scaled(60, 64, Qt.KeepAspectRatio,
                                                                               Qt.SmoothTransformation)
        self.window.ui.label_icon_day7.setPixmap(pixmap)
        self.window.ui.dash_label_day7_t.setText(self.data["daily"][6]["temp"])
        ###
        self.window.ui.dash_label_day8.setText(self.data["daily"][7]["day"])
        pixmap = QPixmap(resource_path(f'images/{self.data["daily"][7]["icon"]}.png')).scaled(60, 64, Qt.KeepAspectRatio,
                                                                               Qt.SmoothTransformation)
        self.window.ui.label_icon_day8.setPixmap(pixmap)
        self.window.ui.dash_label_day8_t.setText(self.data["daily"][7]["temp"])


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.frame_19.hide()
        self.ui.frame_22.hide()
        self.ui.frame_24.hide()
        self.setWindowIcon(QIcon(resource_path('images/icon.png')))
        self.ui.pushButton_toggle.setIcon(QIcon(resource_path('images/menu.png')))
        self.ui.pushButton_home.setIcon(QIcon(resource_path('images/home.png')))
        self.ui.pushButton_dash.setIcon(QIcon(resource_path('images/dash.png')))
        self.ui.pushButton_settings.setIcon(QIcon(resource_path('images/settings.png')))
        dataThread = WeatherApiThread(self)
        dataThread.start()
        ###########################################################

        #toggle menu button (burger)
        self.ui.pushButton_toggle.clicked.connect(lambda: UIFunctions.pushButton_toggle(self, True))

        #turn page to home
        self.ui.pushButton_home.clicked.connect(lambda: UIFunctions.pushButton_home(self))

        # turn page to dashboard
        self.ui.pushButton_dash.clicked.connect(lambda: UIFunctions.pushButton_dash(self))

        #turn page to settings
        self.ui.pushButton_settings.clicked.connect(lambda: UIFunctions.pushButton_settings(self))

        #save button (settings page)
        self.ui.settings_pushButton_save.clicked.connect(lambda: UIFunctions.settings_pushButton_save(self))

        ###########################################################
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())