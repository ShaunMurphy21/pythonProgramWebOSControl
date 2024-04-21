# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from remote_setup import *
from wakeonlan import send_magic_packet
import keyboard

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        send_magic_packet('AC.5A.F0.A6.17.42')
        self.client = initiate_remote()
        self.media = MediaControl(self.client)
        self.system = SystemControl(self.client)
        self.app = ApplicationControl(self.client)
        self.inp = InputControl(self.client)
        self.source_control = SourceControl(self.client)
        self.apps = self.app.list_apps()


        self.ui.power_on.clicked.connect(lambda: self.on_button_command())
        self.ui.power_off.clicked.connect(lambda: self.off_button_command())
        self.ui.volume_up.clicked.connect(lambda: self.volume_up_button_command())
        self.ui.volume_down.clicked.connect(lambda: self.volume_down_button_command())
        self.ui.send_notification.clicked.connect(lambda: self.notification_send_button_command(self.ui.notification_text.text()))

        self.ui.send_keystrokes.clicked.connect(lambda: self.get_keystrokes(self.ui.key_strokes_input.text()))
        self.ui.dpad_up.clicked.connect(lambda: self.dpad_up())
        self.ui.dpad_down.clicked.connect(lambda: self.dpad_down())
        self.ui.dpad_left.clicked.connect(lambda: self.dpad_left())
        self.ui.dpad_right.clicked.connect(lambda: self.dpad_right())
        self.ui.dpad_enter.clicked.connect(lambda: self.dpad_enter())

        self.ui.volume_slider.valueChanged.connect(lambda: self.update_volume())
        self.ui.play_button.clicked.connect(lambda: self.play_button())
        self.ui.pause_button.clicked.connect(lambda: self.pause_button())
        self.ui.stop_button.clicked.connect(lambda: self.stop_button())
        self.ui.rewind_button.clicked.connect(lambda: self.rewind_button())
        self.ui.fast_forward_button.clicked.connect(lambda: self.fast_forward_button())

        self.ui.default_mac.clicked.connect(lambda: self.default_mac())
        self.ui.wake_button.clicked.connect(lambda: self.wake_button())

        self.ui.home_button.clicked.connect(lambda: self.home_button())

        self.ui.use_arrow_keys.toggled.connect(lambda: self.use_arrow_keys())


    def home_button(self):
        self.connectinput()
        self.inp.home()
        self.disconnectinput()
    def wake_button(self):
        send_magic_packet(self.ui.mac_address.text())

    def default_mac(self):
        mac = 'AC.5A.F0.A6.17.42'
        print(mac)
        self.ui.mac_address.setText(mac)

    def use_arrow_keys(self):
        print('huh')
        if self.ui.use_arrow_keys.isChecked() == True:
            keyboard.add_hotkey('up', lambda: self.dpad_up())
            keyboard.add_hotkey('down', lambda: self.dpad_down())
            keyboard.add_hotkey('left', lambda: self.dpad_left())
            keyboard.add_hotkey('right', lambda: self.dpad_right())
            keyboard.add_hotkey('return', lambda: self.dpad_enter())
        else:
            keyboard.unhook_all_hotkeys()

    def play_button(self):
        self.media.play()
    def pause_button(self):
        self.media.pause()
    def pause_button(self):
        self.media.pause()
    def rewind_button(self):
        self.media.rewind()
    def fast_foward_button(self):
        self.media.fast_foward()




    def connectinput(self):
        self.inp.connect_input()

    def disconnectinput(self):
        self.inp.disconnect_input()

    def off_button_command(self):
        self.system.screen_off()

    def dpad_up(self):
        self.connectinput()
        self.inp.up()
        self.disconnectinput()
    def dpad_down(self):
        self.connectinput()
        self.inp.down()
        self.disconnectinput()
    def dpad_left(self):
        self.connectinput()
        self.inp.left()
        self.disconnectinput()
    def dpad_right(self):
        self.connectinput()
        self.inp.right()
        self.disconnectinput()
    def dpad_enter(self):
        self.connectinput()
        self.inp.ok()
        self.disconnectinput()

    def update_volume(self):
        self.ui.volume_label.text = self.ui.volume_slider.value()
        self.media.set_volume(int(self.ui.volume_slider.value()))

    def get_keystrokes(self, text):
        self.inp.type(text)


    def on_button_command(self):
        self.system.screen_on()

    def volume_up_button_command(self):
        self.media.volume_up()

    def volume_down_button_command(self):
        self.media.volume_down()

    def notification_send_button_command(self, text):
        self.system.notify(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
