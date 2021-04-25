from main import *


class UIFunctions(QMainWindow):
    def pushButton_toggle(self, enable):
        if enable:

            width = self.ui.frame_left_menu.width()
            maxExtend = self.ui.frame_left_menu.maximumWidth()
            standard = 40

            if width == 40:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            ### toggle animation
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(150)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.start()

            ### changing menu texts
            if self.ui.frame_left_menu.width() > standard:
                self.ui.frame_19.hide()
                self.ui.frame_22.hide()
                self.ui.frame_24.hide()
                self.ui.label_home.setText("")
                self.ui.label_dash.setText("")
                self.ui.label_settings.setText("")
            else:
                self.ui.frame_19.show()
                self.ui.frame_22.show()
                self.ui.frame_24.show()
                self.ui.label_home.setText("Home")
                self.ui.label_dash.setText("Dashboard")
                self.ui.label_settings.setText("Settings")
            ###############

    def pushButton_home(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def pushButton_dash(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def pushButton_settings(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def settings_pushButton_save(self):
        print("save button pressed")