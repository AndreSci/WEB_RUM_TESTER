import requests
import json


def convert_header(header) -> str:
    type(header)

    result = json.dumps(header, sort_keys=True, indent=4, ensure_ascii=False)
    return result


class TestRequestRum:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    # ФАЗА 1
    # done
    def request_employees(self, guid):
        """ Получаем список сотрудников по GUID компании """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/RequestEmployees?GUIDCompany={guid}"

        try:
            result = requests.get(url, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    # done
    def add_account(self, guid, units):
        """ Переместить п.е. от компании к сотруднику """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/AddAccount?guid={guid}&units={units}"

        try:
            result = requests.get(url, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    # done
    def remove_account(self, guid, units):
        """ Переместить п.е. от сотрудника к компании """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/RemoveAccount?guid={guid}&units={units}"

        try:
            result = requests.get(url, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    #
    def set_contacts(self, guid, phone, email):
        """ Переместить п.е. от сотрудника к компании """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/SetContacts?guid={guid}&phone={phone}&email={email}"

        try:
            result = requests.get(url, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    def set_car_employee(self, guid, car_number):
        """ Добавить номер автомобиля сотруднику, Номер может быть записан только на одного сотрудника """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/SetCarEmployee?guid={guid}&car_number={car_number}"

        try:
            result = requests.get(url, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    def set_favorite(self, guid, is_favorite):
        """ Меняет флаг Favorite в БД """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/SetFavorite?guid={guid}&is_favorite={is_favorite}"

        try:
            result = requests.get(url, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    def request_company(self, inn, id_company):
        """ Получает данные компании из БД """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/RequestCompany?InnCompany={inn}&IDCompany={id_company}"

        try:
            result = requests.get(url, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    # done
    def remove_car_employee(self, guid, id_number):
        """ Отвязать номер от сотрудника """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/RemoveCarEmployee?guid={guid}&fplateid={id_number}"

        try:
            result = requests.get(url, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    # done
    def request_company_transaction(self, guid, data_from, data_to) -> dict:
        """ Переместить п.е. от компании к сотруднику """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/RequestCompanyTransaction?" \
              f"guid={guid}&data_from={data_from}&data_to={data_to}"

        try:
            result = requests.get(url, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    # done
    def get_employee_info(self, guid, uid) -> dict:
        """ Получить информацию о сотруднике """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/GetEmployeeInfo?guid={guid}&uid={uid}"

        try:
            result = requests.get(url, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    # done
    def request_cars_employee(self, guid) -> dict:
        """ Получить информацию о сотруднике """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/RequestCarsEmployee?guid={guid}"

        try:
            result = requests.get(url, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    # done
    def set_auto_balance(self, guid, units) -> dict:
        """ Получить информацию о сотруднике """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/SetAutoBalance?guid={guid}&units={units}"

        try:
            result = requests.get(url, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    # done
    def request_transaction(self, guid, data_from, data_to) -> dict:
        """ Получить историю транзакция за период """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/RequestTransaction?" \
              f"guid={guid}&data_from={data_from}&data_to={data_to}"

        try:
            result = requests.get(url, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    # done
    def request_decrease(self, guid, data_from, data_to) -> dict:
        """ Получить историю транзакция за период """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/RequestDecrease?" \
              f"guid={guid}&data_from={data_from}&data_to={data_to}"

        try:
            result = requests.get(url, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    # ФАЗА 2

    # done
    def do_request_create_card_holder(self, json_data: dict):
        """ Создает сотрудника """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/DoRequestCreateCardHolder"

        try:
            result = requests.get(url, json=json_data, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    # done
    def get_request_create_card_holder(self, json_data: dict):
        """ Получить список заявок """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/GetRequestCreateCardHolder"

        try:
            result = requests.get(url, json=json_data, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    # done
    def get_request_replace_card_holder(self, json_data: dict):
        """ Запрос на перевыпуск """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/DoRequestReplaceCard"

        try:
            result = requests.get(url, json=json_data, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    # done
    def do_request_block_card_holder(self, json_data: dict):
        """ Запрос на блокировку сотрудника """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/DoRequestBlockCardHolder"

        try:
            result = requests.get(url, json=json_data, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    def get_photo(self, photo_name):
        """ Получить фотографию """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': ''}

        url = f"http://{self.host}:{self.port}/GetPhoto?photo_name={photo_name}"

        try:
            result = requests.get(url, timeout=2)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    # ФАЗА 3
    # 3 done
    def do_request_guest(self, json_data: dict):
        """ Запрос на создание пропуска гостю """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/DoCreateGuest"

        try:
            result = requests.get(url, json=json_data, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    # 3 done
    def do_block_guest(self, json_data: dict):
        """ Блокировка гостя """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/DoBlockGuest"

        try:
            result = requests.get(url, json=json_data, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    # 3 done
    def get_guests_status(self, json_data: dict):
        """ Запрос списка активных заявок на гостей """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/GetGuestStatus"

        try:
            result = requests.get(url, json=json_data, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    # 3 done
    def get_guests_list(self, json_data: dict):
        """ Запрос списка активных заявок на гостей """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/GetGuestsList"

        try:
            result = requests.get(url, json=json_data, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    # 3 done
    def do_change_status(self, json_data: dict):
        """ Запрос списка активных заявок на гостей """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/DoChangeStatus"

        try:
            result = requests.get(url, json=json_data, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    # 3 done
    def do_test_car_number(self, json_data: dict):
        """ Запрос списка активных заявок на гостей """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/DoTestCarNumber"

        try:
            result = requests.get(url, json=json_data, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
                ret_value['HEADER'] = dict(result.headers)
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value
