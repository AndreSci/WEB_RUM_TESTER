from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import json
import os

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
        # step 1
        self.ui.bt_RequestCompanyTransaction.clicked.connect(self.request_company_transaction)
        self.ui.bt_AddAccount.clicked.connect(self.add_account)
        self.ui.bt_RemoveAccount.clicked.connect(self.remove_account)
        self.ui.bt_RequestEmployees.clicked.connect(self.request_employees)
        self.ui.bt_GetEmployeeInfo.clicked.connect(self.get_employee_info)

        # step 2
        self.ui.bt_DoRequestCreatCardHolder.clicked.connect(self.do_request_create_car_holder)
        self.ui.bt_GetRequestCreateCardHolder.clicked.connect(self.get_request_create_card_holder)
        self.ui.bt_openFile_jpg.clicked.connect(self.open_file_in_folder)
        self.ui.bt_DoRequestReplaceCard.clicked.connect(self.do_request_replace_card)
        self.ui.bt_DoRequestBlockCardHolder.clicked.connect(self.do_request_block_card_holder)

        self.ui.bt_GetPhoto.clicked.connect(self.get_photo)

        # step 3
        self.ui.bt_DoRequestGuest.clicked.connect(self.do_request_guest)  # теперь это DoCreateGuest
        self.ui.bt_DoBlockGuest.clicked.connect(self.do_block_guest)
        self.ui.bt_GetGuestsStatus.clicked.connect(self.get_guest_status)
        self.ui.bt_GetGuestsList.clicked.connect(self.get_guests_list)
        self.ui.bt_DoChangeStatus.clicked.connect(self.do_change_status)

        self.ui.bt_DoTestCarNumber.clicked.connect(self.do_test_car_number)

        self.set_ini = settings_ini

        self.request_api = TestRequestRum(self.set_ini['host'], self.set_ini['port'])

        self.load_readme()

    def load_readme(self):

        # STEP 1
        url_file = "./readme/step 1/AddAccount.txt"
        if os.path.exists(url_file):
            with open(url_file, 'r', encoding='utf-8') as file:
                self.ui.readme_AddAccount.setText(file.read())

        url_file = "./readme/step 1/RemoveAccount.txt"
        if os.path.exists(url_file):
            with open(url_file, 'r', encoding='utf-8') as file:
                self.ui.readme_RemoveAccount.setText(file.read())

        url_file = "./readme/step 1/RequestEmployees.txt"
        if os.path.exists(url_file):
            with open(url_file, 'r', encoding='utf-8') as file:
                self.ui.readme_RequestEmployees.setText(file.read())

        url_file = "./readme/step 1/GetEmployeeInfo.txt"
        if os.path.exists(url_file):
            with open(url_file, 'r', encoding='utf-8') as file:
                self.ui.readme_GetEmployeeInfo.setText(file.read())

        url_file = "./readme/step 1/RequestCompanyTransaction.txt"
        if os.path.exists(url_file):
            with open(url_file, 'r', encoding='utf-8') as file:
                self.ui.readme_RequestCompanyTransaction.setText(file.read())

        # STEP 2
        url_file = "./readme/step 2/DoRequestBlockCardHolder.txt"
        if os.path.exists(url_file):
            with open(url_file, 'r', encoding='utf-8') as file:
                self.ui.readme_DoRequestBlockCardHolder.setText(file.read())
        url_file = "./readme/step 2/DoRequestCreateCardHolder.txt"
        if os.path.exists(url_file):
            with open(url_file, 'r', encoding='utf-8') as file:
                self.ui.readme_DoRequestCreatCardHolder.setText(file.read())
        url_file = "./readme/step 2/DoRequestReplaceCard.txt"
        if os.path.exists(url_file):
            with open(url_file, 'r', encoding='utf-8') as file:
                self.ui.readme_DoRequestReplaceCard.setText(file.read())
        url_file = "./readme/step 2/GetPhoto.txt"
        if os.path.exists(url_file):
            with open(url_file, 'r', encoding='utf-8') as file:
                self.ui.readme_GetPhoto.setText(file.read())
        url_file = "./readme/step 2/GetRequestCreateCardHolder.txt"
        if os.path.exists(url_file):
            with open(url_file, 'r', encoding='utf-8') as file:
                self.ui.readme_GetRequestCreateCardHolder.setText(file.read())

        # STEP 3
        if os.path.exists("./readme/step 3/DoBlockGuest.txt"):
            with open("./readme/step 3/DoBlockGuest.txt", 'r', encoding='utf-8') as file:
                self.ui.readme_DoBlockGuest.setText(file.read())
        if os.path.exists("./readme/step 3/DoCreateGuest.txt"):
            with open("./readme/step 3/DoCreateGuest.txt", 'r', encoding='utf-8') as file:
                self.ui.readme_DoRequestGuest.setText(file.read())
        if os.path.exists("./readme/step 3/GetGuestsList.txt"):
            with open("./readme/step 3/GetGuestsList.txt", 'r', encoding='utf-8') as file:
                self.ui.readme_GetGuestsList.setText(file.read())
        if os.path.exists("./readme/step 3/GetGuestStatus.txt"):
            with open("./readme/step 3/GetGuestStatus.txt", 'r', encoding='utf-8') as file:
                self.ui.readme_GetGuestsStatus.setText(file.read())
        if os.path.exists("./readme/step 3/service/DoChangeStatus.txt"):
            with open("./readme/step 3/service/DoChangeStatus.txt", 'r', encoding='utf-8') as file:
                self.ui.readme_DoChangeStatus.setText(file.read())
        if os.path.exists("./readme/step 3/service/DoTestCarNumber.txt"):
            with open("./readme/step 3/service/DoTestCarNumber.txt", 'r', encoding='utf-8') as file:
                self.ui.readme_DoTestCarNumber.setText(file.read())

    # STEP 1
    def add_account(self):
        """ Функция пополнения счета сотрудника за счет компании """
        guid = self.ui.text_AddAccount_guid.text()
        units = self.ui.text_AddAccount_units.text()

        result = self.request_api.add_account(guid, units)

        print(result)
        self.ui.browser_AddAccount.setText(str(json.dumps(result, sort_keys=True,
                                                                        indent=4, ensure_ascii=False)))

    def remove_account(self):
        """ Функция списания со счета сотрудника в счет компании """
        guid = self.ui.text_RemoveAccount_guid.text()
        units = self.ui.text_RemoveAccount_units.text()

        result = self.request_api.remove_account(guid, units)

        print(result)
        self.ui.browser_RemoveAccount.setText(str(json.dumps(result, sort_keys=True,
                                                                        indent=4, ensure_ascii=False)))

    def request_employees(self):
        """ Функция запрашивает список сотрудников на компанию """
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
        """ Функция заполнения таблицы списком сотрудников """
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

    def __request_company_transaction(self, list_transaction: list):
        """ Функция заполнения таблицы списком сотрудников """
        ret_value = {'RESULT': True, 'DESC': ''}

        self.ui.tab_list_RequestCompanyTransaction.setRowCount(0)

        if list_transaction:
            self.ui.tab_list_RequestCompanyTransaction.setRowCount(len(list_transaction))

            index = 0

            try:
                for it in list_transaction:

                    self.ui.tab_list_RequestCompanyTransaction.\
                        setItem(index, 0, QtWidgets.QTableWidgetItem(str(it['FGUIDFrom'])))
                    self.ui.tab_list_RequestCompanyTransaction.\
                        setItem(index, 1, QtWidgets.QTableWidgetItem(str(it['FGUIDTo'])))
                    self.ui.tab_list_RequestCompanyTransaction.\
                        setItem(index, 2, QtWidgets.QTableWidgetItem(str(it['FTime'])))
                    self.ui.tab_list_RequestCompanyTransaction.\
                        setItem(index, 3, QtWidgets.QTableWidgetItem(str(it['FTransactionTypeName'])))
                    self.ui.tab_list_RequestCompanyTransaction.\
                        setItem(index, 4, QtWidgets.QTableWidgetItem(str(it['FValue'])))

                    index += 1
            except Exception as ex:
                msg = f"Исключение вызвало: {ex}"
                print(msg)
                ret_value['DESC'] = msg
                ret_value['RESULT'] = False

            self.ui.tab_list_RequestCompanyTransaction.resizeColumnsToContents()

        return ret_value

    def request_company_transaction(self):
        """ Функция запрашивает список сотрудников на компанию """
        guid = self.ui.guid_RequestCompanyTransaction.text()
        data_from = self.ui.data_from_RequestCompanyTransaction.text()
        data_to = self.ui.data_to_RequestCompanyTransaction.text()

        result = self.request_api.request_company_transaction(guid, data_from, data_to)

        tab_res = self.__request_company_transaction(result.get('DATA'))

        if tab_res['RESULT']:
            self.ui.browser_RequestCompanyTransaction.setText(str(json.dumps(result, sort_keys=True,
                                                                             indent=4, ensure_ascii=False)))
        else:
            self.ui.browser_RequestCompanyTransaction.setText(str(json.dumps(tab_res, sort_keys=True,
                                                                             indent=4, ensure_ascii=False)))

    def __get_employee_info(self, list_data: list):
        """ Функция заполнения таблицы списком сотрудников """
        ret_value = {'RESULT': True, 'DESC': ''}

        self.ui.tab_list_GetEmployeeInfo.setRowCount(0)

        if list_data:
            self.ui.tab_list_GetEmployeeInfo.setRowCount(len(list_data))

            index = 0

            try:
                for it in list_data:

                    self.ui.tab_list_GetEmployeeInfo.\
                        setItem(index, 0, QtWidgets.QTableWidgetItem(str(it['UID'])))
                    self.ui.tab_list_GetEmployeeInfo.\
                        setItem(index, 1, QtWidgets.QTableWidgetItem(str(it['FLastName'])))
                    self.ui.tab_list_GetEmployeeInfo.\
                        setItem(index, 2, QtWidgets.QTableWidgetItem(str(it['FFirstName'])))
                    self.ui.tab_list_GetEmployeeInfo.\
                        setItem(index, 3, QtWidgets.QTableWidgetItem(str(it['FMiddleName'])))
                    self.ui.tab_list_GetEmployeeInfo.\
                        setItem(index, 4, QtWidgets.QTableWidgetItem(str(it['FPhone'])))
                    self.ui.tab_list_GetEmployeeInfo.\
                        setItem(index, 5, QtWidgets.QTableWidgetItem(str(it['FGUID'])))
                    self.ui.tab_list_GetEmployeeInfo.\
                        setItem(index, 6, QtWidgets.QTableWidgetItem(str(it['FEmail'])))
                    self.ui.tab_list_GetEmployeeInfo.\
                        setItem(index, 7, QtWidgets.QTableWidgetItem(str(it['FCreateDate'])))
                    self.ui.tab_list_GetEmployeeInfo.\
                        setItem(index, 8, QtWidgets.QTableWidgetItem(str(it['FPersonalAccount'])))
                    self.ui.tab_list_GetEmployeeInfo.\
                        setItem(index, 9, QtWidgets.QTableWidgetItem(str(it['FCompanyAccount'])))
                    self.ui.tab_list_GetEmployeeInfo.\
                        setItem(index, 10, QtWidgets.QTableWidgetItem(str(it['FLastModifyDate'])))
                    self.ui.tab_list_GetEmployeeInfo.\
                        setItem(index, 11, QtWidgets.QTableWidgetItem(str(it['FLastDecreaseDate'])))
                    self.ui.tab_list_GetEmployeeInfo.\
                        setItem(index, 12, QtWidgets.QTableWidgetItem(str(it['FFavorite'])))
                    self.ui.tab_list_GetEmployeeInfo.\
                        setItem(index, 13, QtWidgets.QTableWidgetItem(str(it['FBlocked'])))
                    self.ui.tab_list_GetEmployeeInfo.\
                        setItem(index, 14, QtWidgets.QTableWidgetItem(str(it['FActivity'])))

                    index += 1
            except Exception as ex:
                msg = f"Исключение вызвало: {ex}"
                print(msg)
                ret_value['DESC'] = msg
                ret_value['RESULT'] = False

            self.ui.tab_list_GetEmployeeInfo.resizeColumnsToContents()

        return ret_value

    def get_employee_info(self):
        """ Функция запрашивает информацию о сотруднике """
        guid = self.ui.guid_GetEmployeeInfo.text()
        uid = self.ui.uid_GetEmployeeInfo.text()

        result = self.request_api.get_employee_info(guid, uid)

        tab_res = self.__get_employee_info(result.get('DATA'))

        if tab_res['RESULT']:
            self.ui.browser_GetEmployeeInfo.setText(str(json.dumps(result, sort_keys=True,
                                                                             indent=4, ensure_ascii=False)))
        else:
            self.ui.browser_GetEmployeeInfo.setText(str(json.dumps(tab_res, sort_keys=True,
                                                                             indent=4, ensure_ascii=False)))

    # STEP 2
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

    def __get_request_create_card_holder(self, list_card_holders: list):
        """ Функция заполнения таблицы списком ожидающих выпуск карты """
        ret_value = {'RESULT': True, 'DESC': ''}

        self.ui.tab_GetRequestCreateCardHolder.setRowCount(0)

        if list_card_holders:
            self.ui.tab_GetRequestCreateCardHolder.setRowCount(len(list_card_holders))

            index = 0

            try:
                for it in list_card_holders:

                    self.ui.tab_GetRequestCreateCardHolder.setItem(index, 0,
                                                                   QtWidgets.QTableWidgetItem(str(it['FID'])))
                    self.ui.tab_GetRequestCreateCardHolder.setItem(index, 1,
                                                                   QtWidgets.QTableWidgetItem(str(it['FlastName'])))
                    self.ui.tab_GetRequestCreateCardHolder.setItem(index, 2,
                                                                   QtWidgets.QTableWidgetItem(str(it['FFirstName'])))
                    self.ui.tab_GetRequestCreateCardHolder.setItem(index, 3,
                                                                   QtWidgets.QTableWidgetItem(str(it['FMiddleName'])))
                    self.ui.tab_GetRequestCreateCardHolder.setItem(index, 4,
                                                                   QtWidgets.QTableWidgetItem(str(it['FTime'])))
                    self.ui.tab_GetRequestCreateCardHolder.setItem(index, 5,
                                                                   QtWidgets.QTableWidgetItem(str(it['Status'])))
                    self.ui.tab_GetRequestCreateCardHolder.setItem(index, 6,
                                                                   QtWidgets.QTableWidgetItem(str(it['FActivity'])))

                    index += 1
            except Exception as ex:
                msg = f"Исключение вызвало: {ex}"
                print(msg)
                ret_value['DESC'] = msg
                ret_value['RESULT'] = False

            self.ui.tab_GetRequestCreateCardHolder.resizeColumnsToContents()

        return ret_value

    def get_request_create_card_holder(self):
        """ Получить список ожидающих выпуск карты на компанию """
        json_data = {
            "inn": self.ui.text_GerRequestCreateCardHolder_inn.text(),
            "user_id": self.ui.text_GetRequestCreateCardHolder_user_id.text()
        }
        result = self.request_api.get_request_create_card_holder(json_data)

        tab_res = self.__get_request_create_card_holder(result.get('DATA'))
        tab_res['HEADER'] = result['HEADER']

        if tab_res['RESULT']:
            self.ui.browser_GetRequestCreateCardHolder.setText(str(json.dumps(result, sort_keys=True,
                                                                                indent=4, ensure_ascii=False)))
        else:
            self.ui.browser_GetRequestCreateCardHolder.setText(str(json.dumps(tab_res, sort_keys=True,
                                                                                indent=4, ensure_ascii=False)))

    def do_request_block_card_holder(self):
        """ Заблокировать сотрудника """
        json_data = {
            "inn": self.ui.text_inn_DoRequestBlockCardHolder.text(),
            "user_id": self.ui.text_user_id_DoRequestBlockCardHolder.text(),
            "FApacsID": self.ui.text_FApacsID_DoRequestBlockCardHolder.text(),
            "desc": self.ui.text_desc_DoRequestBlockCardHolder.toPlainText()
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
        """ Получить фото по имени файла из интерфейса """
        img_name = self.ui.text_GetPhoto.text()

        if len(img_name) < 256:
            result = self.request_api.get_photo(img_name)
            header = result.get('HEADER')

            if result['RESULT'] == 'SUCCESS':
                result = self.__get_photo(result)

            result['HEADER'] = header

            self.ui.browser_GetPhoto.clear()
        else:
            result = {"RESULT": "ERROR", "DESC": 'Слишком длинное имя: max=256', "DATA": ''}

        self.ui.browser_GetPhoto.setText(str(json.dumps(result, sort_keys=True,
                                                                        indent=4, ensure_ascii=False)))

    def __get_photo(self, json_data: dict):
        """ Функция обработки фото и добавление её в графический интерфейс """
        ret_value = {"RESULT": "ERROR", "DESC": '', "DATA": ''}

        pixmap = QtGui.QPixmap()

        try:
            import base64
            decoded_data = base64.b64decode(json_data['DATA']['img64'])

            # Метод преобразования строки в байт код
            # data = ast.literal_eval(json_data['DATA']['img64'])
            # ba = QtCore.QByteArray.fromBase64(data)

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

    # STEP 3

    def do_request_guest(self):
        """ Создать гостя на компанию """

        json_data = {
            "inn": self.ui.text_inn_DoRequestGuest.text(),
            "user_id": self.ui.text_user_id_DoRequestGuest.text(),
            "id": self.ui.text_id_remote_DoRequestGuest.text(),

            "FFirstName": self.ui.text_FFirstName_DoRequestGuest.text(),
            "FLastName": self.ui.text_FLastName_DoRequestGuest.text(),
            "FMiddleName": self.ui.text_FMiddleName_DoRequestGuest.text(),

            "FCarNumber": self.ui.text_FCarNumber_DoRequestGuest.text(),
            "FEmail": self.ui.text_FEmail.text(),

            "FDateFrom": self.ui.text_FDateFrom_DoRequestGuest.text(),
            "FDateTo": self.ui.text_FDateTo_DoRequestGuest.text()
        }

        result = self.request_api.do_request_guest(json_data)

        self.ui.browser_DoRequestGuest.clear()
        self.ui.browser_DoRequestGuest.setText(str(json.dumps(result, sort_keys=True,
                                                                        indent=4, ensure_ascii=False)))

    def do_block_guest(self):
        """ Заблокировать гостя """

        json_data = {
            "inn": self.ui.text_inn_DoBlockGuest.text(),
            "user_id": self.ui.text_user_id_DoBlockGuest.text(),
            "id": self.ui.text_id_remote_DoBlockGuest.text()
        }

        result = self.request_api.do_block_guest(json_data)

        self.ui.browser_DoBlockGuest.clear()
        self.ui.browser_DoBlockGuest.setText(str(json.dumps(result, sort_keys=True,
                                                                        indent=4, ensure_ascii=False)))

    def __get_guests_list_table(self, list_guests: list):
        """ (Приватная функция) Заполняет таблицу в интерфейсе """
        ret_value = {'RESULT': True, 'DESC': ''}

        self.ui.tab_GetGuestsList.setRowCount(0)

        if list_guests:
            self.ui.tab_GetGuestsList.setRowCount(len(list_guests))

            index = 0

            try:
                # Заполняет таблицу данными
                for it in list_guests:
                    self.ui.tab_GetGuestsList.setItem(index, 0, QtWidgets.QTableWidgetItem(str(it['ID_Request'])))
                    self.ui.tab_GetGuestsList.setItem(index, 1, QtWidgets.QTableWidgetItem(str(it['Name_LastName'])))
                    self.ui.tab_GetGuestsList.setItem(index, 2, QtWidgets.QTableWidgetItem(str(it['Name_FirstName'])))
                    self.ui.tab_GetGuestsList.setItem(index, 3,
                                                        QtWidgets.QTableWidgetItem(str(it['Name_MIddleName'])))
                    self.ui.tab_GetGuestsList.setItem(index, 4, QtWidgets.QTableWidgetItem(str(it['Number_Car'])))
                    self.ui.tab_GetGuestsList.setItem(index, 5, QtWidgets.QTableWidgetItem(str(it['Date_Request'])))
                    self.ui.tab_GetGuestsList.setItem(index, 6,
                                                        QtWidgets.QTableWidgetItem(str(it['DateFrom_Request'])))
                    self.ui.tab_GetGuestsList.setItem(index, 7, QtWidgets.QTableWidgetItem(str(it['DateTo_Request'])))

                    index += 1
            except Exception as ex:
                msg = f"Исключение вызвало: {ex}"
                print(msg)
                ret_value['DESC'] = msg
                ret_value['RESULT'] = False

            # Подгоняет таблицу по тексту
            self.ui.tab_list_employees.resizeColumnsToContents()

        return ret_value

    def get_guest_status(self):
        """ Получить статус конкретного гостя """
        json_data = {
            "inn": self.ui.text_inn_GetGuestsStatus.text(),
            "user_id": self.ui.text_user_id_GetGuestsStatus.text(),
            "id_request": self.ui.text_id_reques_GetGuestsStatus.text()
        }

        result = self.request_api.get_guests_status(json_data)

        self.ui.browser_GetGuestsStatus.clear()
        self.ui.browser_GetGuestsStatus.setText(str(json.dumps(result, sort_keys=True,
                                                                        indent=4, ensure_ascii=False)))

    def get_guests_list(self):
        """ Получить список всех гостей на компанию """
        json_data = {
            "inn": self.ui.text_inn_GetGuestsList.text(),
            "user_id": self.ui.text_user_id_GetGuestsList.text()
        }

        result = self.request_api.get_guests_list(json_data)

        self.__get_guests_list_table(result['DATA'])

        self.ui.browser_GetGuestsList.clear()
        self.ui.browser_GetGuestsList.setText(str(json.dumps(result, sort_keys=True,
                                                                        indent=4, ensure_ascii=False)))

    def do_change_status(self):
        """ Изменить статус гостя """
        json_data = {
            "inn": self.ui.text_inn_DoChangeStatus.text(),
            "user_id": self.ui.text_user_id_DoChangeStatus.text(),
            "id_request": self.ui.text_id_request_DoChangeStatus.text(),
            "id_status": self.ui.text_id_status_DoChangeStatus.text()
        }

        result = self.request_api.do_change_status(json_data)

        self.ui.browser_DoChangeStatus.clear()
        self.ui.browser_DoChangeStatus.setText(str(json.dumps(result, sort_keys=True,
                                                                        indent=4, ensure_ascii=False)))

    def do_test_car_number(self):
        """ Сервисная функция проверки работы алгоритма коррекции номера для БД """

        json_data = {
            "car_number": self.ui.text_car_number_DoTestCarNumber.text()
        }

        result = self.request_api.do_test_car_number(json_data)

        self.ui.browser_DoTestCarNumber.clear()
        self.ui.browser_DoTestCarNumber.setText(str(json.dumps(result, sort_keys=True,
                                                                        indent=4, ensure_ascii=False)))

    @staticmethod
    def exit_def():
        """ Выход из программы """
        sys.exit()


# pyuic5 -x gui_sms_sender_ru.ui -o gui_sms_sender_ru.py
# auto-py-to-exe
