from PyQt5 import QtCore, QtGui, QtWidgets

import requests
import sys
import json
import ast

from misc.logger import Logger
from misc.utility import SettingsIni
from gui_files.main_window import Ui_MainWindow
from requests_api.requests_api import TestRequestRum
from misc.img64 import PhotoReader


NAME_VER = "TEST WEB RUM"


class MainWindow(QtWidgets.QMainWindow):

    signal_for_log = QtCore.pyqtSignal(str)  # переменная для отправки сигналов на добавление логов
    signal_for_status = QtCore.pyqtSignal()  # переменная для отправки сигналов на изменение статуса сервера
    signal_for_sim = QtCore.pyqtSignal()  # переменная для отправки сигналов на изменение статуса SIM карт

    def __init__(self, settings_ini: dict):
        super().__init__()

        # обьявляем интерфейс
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(NAME_VER)

        self.photo_folder = ''

        # кнопки
        self.ui.bt_DoRequestCreatCardHolder.clicked.connect(self.do_request_create_car_holder)
        self.ui.bt_RequestEmployees.clicked.connect(self.request_employees)
        self.ui.bt_AddAccount.clicked.connect(self.add_account)
        self.ui.bt_RemoveAccount.clicked.connect(self.remove_account)
        self.ui.bt_GetRequestCreateCardHolder.clicked.connect(self.get_request_create_card_holder)
        self.ui.bt_openFile_jpg.clicked.connect(self.open_file_in_folder)
        self.ui.bt_DoRequestReplaceCard.clicked.connect(self.do_request_replace_card)
        self.ui.bt_DoRequestBlockCardHolder.clicked.connect(self.do_request_block_card_holder)

        self.ui.bt_GetPhoto.clicked.connect(self.get_photo)

        self.set_ini = settings_ini

        self.request_api = TestRequestRum(self.set_ini['host'], self.set_ini['port'])

    def do_request_create_car_holder(self):

        json_data = {
            "inn": self.ui.text_inn.text(),
            "user_id": self.ui.text_user_id.text(),

            "FFirstName": self.ui.text_FFirstName.text(),
            "FLastName": self.ui.text_FLastName.text(),
            "FMiddleName": self.ui.text_FMiddleName.text(),

            "FCarNumber": self.ui.text_FCarNumber.text(),
            "FPhone": self.ui.text_FPhone.text(),
            "FEmail": self.ui.text_FEmail.text(),

            "img64": PhotoReader.take_photo(self.ui.text_img64.text())
        }

        result = self.request_api.do_request_create_card_holder(json_data)

        self.ui.browser_DoRequestCreatCardHolder.clear()
        self.ui.browser_DoRequestCreatCardHolder.setText(str(json.dumps(result, sort_keys=True,
                                                                        indent=4, ensure_ascii=False)))

    def request_employees(self):

        guid = self.ui.text_guid_request_employees.text()

        result = self.request_api.request_employees(guid)

        tab_res = self.__request_employees(result.get('DATA'))

        if tab_res['RESULT']:
            self.ui.browser_RequestEmployees.setText(str(json.dumps(result, sort_keys=True,
                                                                        indent=4, ensure_ascii=False)))
        else:
            self.ui.browser_RequestEmployees.setText(str(json.dumps(tab_res, sort_keys=True,
                                                                    indent=4, ensure_ascii=False)))

    def __request_employees(self, list_employees: list):

        ret_value = {'RESULT': True, 'DESC': ''}

        self.ui.tab_list_employees.setRowCount(0)

        if list_employees:
            self.ui.tab_list_employees.setRowCount(len(list_employees))

            index = 0

            try:
                for it in list_employees:

                    self.ui.tab_list_employees.setItem(index, 0, QtWidgets.QTableWidgetItem(str(it['UID'])))
                    self.ui.tab_list_employees.setItem(index, 1, QtWidgets.QTableWidgetItem(str(it['FID'])))
                    self.ui.tab_list_employees.setItem(index, 2, QtWidgets.QTableWidgetItem(str(it['FGUID'])))
                    self.ui.tab_list_employees.setItem(index, 3, QtWidgets.QTableWidgetItem(str(it['FApacsID'])))
                    self.ui.tab_list_employees.setItem(index, 4, QtWidgets.QTableWidgetItem(str(it['FCompanyID'])))
                    self.ui.tab_list_employees.setItem(index, 5, QtWidgets.QTableWidgetItem(str(it['FLastName'])))
                    self.ui.tab_list_employees.setItem(index, 6, QtWidgets.QTableWidgetItem(str(it['FFirstName'])))
                    self.ui.tab_list_employees.setItem(index, 7, QtWidgets.QTableWidgetItem(str(it['FMiddleName'])))
                    self.ui.tab_list_employees.setItem(index, 8, QtWidgets.QTableWidgetItem(str(it['FPhone'])))
                    self.ui.tab_list_employees.setItem(index, 9, QtWidgets.QTableWidgetItem(str(it['FEmail'])))
                    self.ui.tab_list_employees.setItem(index, 10, QtWidgets.
                                                       QTableWidgetItem(str(it['FLastModifyDate'])))
                    self.ui.tab_list_employees.setItem(index, 11, QtWidgets.QTableWidgetItem(str(it['FBlocked'])))
                    self.ui.tab_list_employees.setItem(index, 12, QtWidgets.QTableWidgetItem(str(it['FActivity'])))
                    self.ui.tab_list_employees.setItem(index, 13, QtWidgets.QTableWidgetItem(str(it['FActiveFrom'])))
                    self.ui.tab_list_employees.setItem(index, 14, QtWidgets.QTableWidgetItem(str(it['FActiveTo'])))

                    self.ui.tab_list_employees.setItem(index, 15, QtWidgets.QTableWidgetItem(str(it['FCreateDate'])))
                    self.ui.tab_list_employees.setItem(index, 16, QtWidgets.
                                                       QTableWidgetItem(str(it['FLastDecreaseDate'])))
                    self.ui.tab_list_employees.setItem(index, 17, QtWidgets.QTableWidgetItem(str(it['FFavorite'])))

                    self.ui.tab_list_employees.setItem(index, 18, QtWidgets.QTableWidgetItem(str(it['FGALState'])))

                    self.ui.tab_list_employees.setItem(index, 19, QtWidgets.QTableWidgetItem(str(it['FAutobalance'])))
                    self.ui.tab_list_employees.setItem(index, 20, QtWidgets.
                                                       QTableWidgetItem(str(it['FCompanyAccount'])))
                    self.ui.tab_list_employees.setItem(index, 21, QtWidgets.
                                                       QTableWidgetItem(str(it['FPersonalAccount'])))
                    self.ui.tab_list_employees.setItem(index, 22, QtWidgets.
                                                       QTableWidgetItem(str(it['FPresentAccount'])))
                    self.ui.tab_list_employees.setItem(index, 23, QtWidgets.QTableWidgetItem(str(it['FVIPState'])))

                    index += 1
            except Exception as ex:
                msg = f"Исключение вызвало: {ex}"
                print(msg)
                ret_value['DESC'] = msg
                ret_value['RESULT'] = False

            self.ui.tab_list_employees.resizeColumnsToContents()

        return ret_value

    def add_account(self):

        guid = self.ui.text_AddAccount_guid.text()
        units = self.ui.text_AddAccount_units.text()

        result = self.request_api.add_account(guid, units)

        print(result)
        self.ui.browser_AddAccount.setText(str(json.dumps(result, sort_keys=True,
                                                                        indent=4, ensure_ascii=False)))

    def remove_account(self):
        guid = self.ui.text_RemoveAccount_guid.text()
        units = self.ui.text_RemoveAccount_units.text()

        result = self.request_api.remove_account(guid, units)

        print(result)
        self.ui.browser_RemoveAccount.setText(str(json.dumps(result, sort_keys=True,
                                                                        indent=4, ensure_ascii=False)))

    def get_request_create_card_holder(self):
        json_data = {
            "inn": self.ui.text_GerRequestCreateCardHolder_inn.text(),
            "user_id": self.ui.text_GetRequestCreateCardHolder_user_id.text()
        }
        result = self.request_api.get_request_create_card_holder(json_data)

        print(result)
        self.ui.browser_GetRequestCreateCardHolder.setText(str(json.dumps(result, sort_keys=True,
                                                                            indent=4, ensure_ascii=False)))

    def do_request_block_card_holder(self):
        json_data = {
            "inn": self.ui.text_inn_DoRequestBlockCardHolder.text(),
            "user_id": self.ui.text_user_id_DoRequestBlockCardHolder.text(),
            "FApacsID": self.ui.text_FApacsID_DoRequestBlockCardHolder.text()
        }
        result = self.request_api.do_request_block_card_holder(json_data)

        self.ui.browser_DoRequestBlockCardHolder.setText(str(json.dumps(result, sort_keys=True,
                                                                            indent=4, ensure_ascii=False)))

    def open_file_in_folder(self):
        res = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', './', 'JPG File(*.jpg)')

        if len(res[0]) > 1:
            self.photo_folder = res[0]
            self.ui.text_img64.setText(self.photo_folder)
            # """<img height="200" width="200" src="data:image/png;base64,{}"/>"""

            bro_size = self.ui.browser_DoRequestCreatCardHolder.size()

            self.ui.browser_DoRequestCreatCardHolder.clear()

            self.ui.browser_DoRequestCreatCardHolder.insertHtml(
                """<img height={} src="data:image/png;base64,{}"/>"""
                .format(bro_size.height(), PhotoReader.take_photo(self.photo_folder))
            )

    def do_request_replace_card(self):

        json_data = {
            "inn": self.ui.text_inn_DoRequestReplaceCard.text(),
            "user_id": self.ui.text_user_id_DoRequestReplaceCard.text(),

            "FFirstName": self.ui.text_FFirstName_DoRequestReplaceCard.text(),
            "FLastName": self.ui.text_FLastName_DoRequestReplaceCard.text(),
            "FMiddleName": self.ui.text_FMiddleName_DoRequestReplaceCard.text(),

            "FApacsID": self.ui.text_FApacsID_DoRequestReplaceCard.text()
        }

        result = self.request_api.get_request_replace_card_holder(json_data)

        self.ui.browser_DoRequestReplaceCard.clear()
        self.ui.browser_DoRequestReplaceCard.setText(str(json.dumps(result, sort_keys=True,
                                                                        indent=4, ensure_ascii=False)))

    def get_photo(self):

        img_name = self.ui.text_GetPhoto.text()

        result = self.request_api.get_photo(img_name)

        if result['RESULT'] == 'SUCCESS':
            result = self.__get_photo(result)

        self.ui.browser_GetPhoto.clear()

        self.ui.browser_GetPhoto.setText(str(json.dumps(result, sort_keys=True,
                                                                        indent=4, ensure_ascii=False)))

    def __get_photo(self, json_data: dict):

        ret_value = {"RESULT": "ERROR", "DESC": '', "DATA": ''}

        try:
            import base64
            decoded_data = base64.b64decode(json_data['DATA']['img64'])

            # Метод преобразования строки в байт код
            # data = ast.literal_eval(json_data['DATA']['img64'])
            # ba = QtCore.QByteArray.fromBase64(data)

            pixmap = QtGui.QPixmap()
            if pixmap.loadFromData(decoded_data, "JPG"):
                pixmap_resized = pixmap.scaled(345, 500, QtCore.Qt.KeepAspectRatio)
                self.ui.label_GetPhoto_pixmap.setPixmap(pixmap_resized)
                ret_value['RESULT'] = "SUCCESS"
            else:
                ret_value['DESC'] = "Не удалось выгрузить img64: pixmap.loadFromData()"

        except SyntaxError as sx:
            ret_value['DESC'] = f'SyntaxError: вызвала функция __get_photo.' \
                                f' Не удалось перестроить из запроса img64: {sx}'
            print(f"Ошибка: {sx}")
        except Exception as ex:
            ret_value['DESC'] = f'SyntaxError: вызвала функция __get_photo.' \
                                f' Не удалось перестроить из запроса img64: {ex}'
            print(f"Ошибка: {ex}")

        return ret_value

    def exit_def(self):
        sys.exit()


# pyuic5 -x gui_sms_sender_ru.ui -o gui_sms_sender_ru.py
# auto-py-to-exe
