from main_window.window import *
from misc.utility import SettingsIni


def main():
    # подгружаем данные из файла settings
    set_ini = SettingsIni()
    set_ini.create_settings()

    app_gui = QtWidgets.QApplication(sys.argv)
    app_gui.setWindowIcon(QtGui.QIcon('icon.png'))
    gui_app = MainWindow(set_ini.settings_ini)

    gui_app.show()

    sys.exit(app_gui.exec())


if __name__ == "__main__":
    main()
