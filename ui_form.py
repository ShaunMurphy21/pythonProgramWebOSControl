

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(552, 488)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.volume_control_group = QGroupBox(self.centralwidget)
        self.volume_control_group.setObjectName(u"volume_control_group")
        self.volume_control_group.setGeometry(QRect(10, 10, 111, 61))
        self.volume_up = QPushButton(self.volume_control_group)
        self.volume_up.setObjectName(u"volume_up")
        self.volume_up.setGeometry(QRect(20, 20, 31, 31))
        self.volume_down = QPushButton(self.volume_control_group)
        self.volume_down.setObjectName(u"volume_down")
        self.volume_down.setGeometry(QRect(60, 20, 31, 31))
        self.power_control_group = QGroupBox(self.centralwidget)
        self.power_control_group.setObjectName(u"power_control_group")
        self.power_control_group.setGeometry(QRect(10, 70, 111, 141))
        self.power_on = QPushButton(self.power_control_group)
        self.power_on.setObjectName(u"power_on")
        self.power_on.setGeometry(QRect(20, 40, 71, 31))
        self.power_off = QPushButton(self.power_control_group)
        self.power_off.setObjectName(u"power_off")
        self.power_off.setGeometry(QRect(20, 80, 71, 31))
        self.notification_group = QGroupBox(self.centralwidget)
        self.notification_group.setObjectName(u"notification_group")
        self.notification_group.setGeometry(QRect(10, 210, 321, 71))
        self.label = QLabel(self.notification_group)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 91, 21))
        self.notification_text = QLineEdit(self.notification_group)
        self.notification_text.setObjectName(u"notification_text")
        self.notification_text.setGeometry(QRect(10, 40, 191, 21))
        self.send_notification = QPushButton(self.notification_group)
        self.send_notification.setObjectName(u"send_notification")
        self.send_notification.setGeometry(QRect(210, 40, 71, 21))
        self.dpad_group = QGroupBox(self.centralwidget)
        self.dpad_group.setObjectName(u"dpad_group")
        self.dpad_group.setGeometry(QRect(340, 10, 201, 161))
        self.dpad_up = QPushButton(self.dpad_group)
        self.dpad_up.setObjectName(u"dpad_up")
        self.dpad_up.setGeometry(QRect(80, 40, 31, 41))
        self.dpad_down = QPushButton(self.dpad_group)
        self.dpad_down.setObjectName(u"dpad_down")
        self.dpad_down.setGeometry(QRect(80, 110, 31, 41))
        self.dpad_left = QPushButton(self.dpad_group)
        self.dpad_left.setObjectName(u"dpad_left")
        self.dpad_left.setGeometry(QRect(40, 80, 41, 31))
        self.dpad_right = QPushButton(self.dpad_group)
        self.dpad_right.setObjectName(u"dpad_right")
        self.dpad_right.setGeometry(QRect(110, 80, 41, 31))
        self.dpad_enter = QPushButton(self.dpad_group)
        self.dpad_enter.setObjectName(u"dpad_enter")
        self.dpad_enter.setGeometry(QRect(80, 80, 31, 31))
        self.use_arrow_keys = QRadioButton(self.dpad_group)
        self.use_arrow_keys.setObjectName(u"use_arrow_keys")
        self.use_arrow_keys.setGeometry(QRect(20, 20, 171, 20))
        self.text_input_group = QGroupBox(self.centralwidget)
        self.text_input_group.setObjectName(u"text_input_group")
        self.text_input_group.setGeometry(QRect(130, 10, 201, 101))
        self.label_2 = QLabel(self.text_input_group)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 49, 16))
        self.key_strokes_input = QLineEdit(self.text_input_group)
        self.key_strokes_input.setObjectName(u"key_strokes_input")
        self.key_strokes_input.setGeometry(QRect(10, 40, 171, 22))
        self.send_keystrokes = QPushButton(self.text_input_group)
        self.send_keystrokes.setObjectName(u"send_keystrokes")
        self.send_keystrokes.setGeometry(QRect(10, 70, 71, 21))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 280, 321, 181))
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 20, 71, 151))
        self.volume_slider = QSlider(self.groupBox_2)
        self.volume_slider.setObjectName(u"volume_slider")
        self.volume_slider.setGeometry(QRect(10, 20, 21, 121))
        self.volume_slider.setOrientation(Qt.Vertical)
        self.volume_label = QLabel(self.groupBox_2)
        self.volume_label.setObjectName(u"volume_label")
        self.volume_label.setEnabled(True)
        self.volume_label.setGeometry(QRect(40, 50, 21, 16))
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(90, 19, 221, 151))
        self.play_button = QPushButton(self.groupBox_3)
        self.play_button.setObjectName(u"play_button")
        self.play_button.setGeometry(QRect(10, 30, 61, 24))
        self.pause_button = QPushButton(self.groupBox_3)
        self.pause_button.setObjectName(u"pause_button")
        self.pause_button.setGeometry(QRect(80, 30, 61, 24))
        self.stop_button = QPushButton(self.groupBox_3)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setGeometry(QRect(150, 30, 61, 24))
        self.rewind_button = QPushButton(self.groupBox_3)
        self.rewind_button.setObjectName(u"rewind_button")
        self.rewind_button.setGeometry(QRect(50, 70, 51, 61))
        self.fast_forward_button = QPushButton(self.groupBox_3)
        self.fast_forward_button.setObjectName(u"fast_forward_button")
        self.fast_forward_button.setGeometry(QRect(110, 70, 51, 61))
        self.WOL_group = QGroupBox(self.centralwidget)
        self.WOL_group.setObjectName(u"WOL_group")
        self.WOL_group.setGeometry(QRect(130, 110, 201, 101))
        self.label_3 = QLabel(self.WOL_group)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 20, 111, 16))
        self.mac_address = QLineEdit(self.WOL_group)
        self.mac_address.setObjectName(u"mac_address")
        self.mac_address.setGeometry(QRect(10, 40, 181, 22))
        self.default_mac = QPushButton(self.WOL_group)
        self.default_mac.setObjectName(u"default_mac")
        self.default_mac.setGeometry(QRect(100, 70, 91, 21))
        self.wake_button = QPushButton(self.WOL_group)
        self.wake_button.setObjectName(u"wake_button")
        self.wake_button.setGeometry(QRect(10, 70, 81, 21))
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(340, 180, 201, 281))
        self.home_button = QPushButton(self.groupBox_4)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setGeometry(QRect(50, 110, 91, 61))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.volume_control_group.setTitle(QCoreApplication.translate("MainWindow", u"Volume Controls", None))
        self.volume_up.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.volume_down.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.power_control_group.setTitle(QCoreApplication.translate("MainWindow", u"Power Controls", None))
        self.power_on.setText(QCoreApplication.translate("MainWindow", u"Power On", None))
        self.power_off.setText(QCoreApplication.translate("MainWindow", u"Power Off", None))
        self.notification_group.setTitle(QCoreApplication.translate("MainWindow", u"Send Notification", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Notification Text:", None))
        self.notification_text.setInputMask("")
        self.notification_text.setText("")
        self.send_notification.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.dpad_group.setTitle(QCoreApplication.translate("MainWindow", u"D-PAD Control", None))
        self.dpad_up.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.dpad_down.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.dpad_left.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.dpad_right.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.dpad_enter.setText(QCoreApplication.translate("MainWindow", u"\u25cf", None))
        self.use_arrow_keys.setText(QCoreApplication.translate("MainWindow", u"Use arrow keys to navigate?", None))
        self.text_input_group.setTitle(QCoreApplication.translate("MainWindow", u"Keyboard Inputs", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Input:", None))
        self.send_keystrokes.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Media Controls", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.volume_label.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Media", None))
        self.play_button.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.pause_button.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.rewind_button.setText(QCoreApplication.translate("MainWindow", u"<<", None))
        self.fast_forward_button.setText(QCoreApplication.translate("MainWindow", u">>", None))
        self.WOL_group.setTitle(QCoreApplication.translate("MainWindow", u"Wake-on-LAN", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Enter MAC Address:", None))
        self.mac_address.setInputMask("")
        self.mac_address.setText("")
        self.default_mac.setText(QCoreApplication.translate("MainWindow", u"Load Defaults?", None))
        self.wake_button.setText(QCoreApplication.translate("MainWindow", u"Send MAGIC!", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Random Buttons", None))
        self.home_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))


