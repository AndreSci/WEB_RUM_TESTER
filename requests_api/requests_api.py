import requests


class TestRequestRum:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def request_employees(self, guid):
        """ Получаем список сотрудников по GUID компании """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/RequestEmployees?GUIDCompany={guid}"

        try:
            result = requests.get(url, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()

            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    def add_account(self, guid, units):
        """ Переместить п.е. от компании к сотруднику """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/AddAccount?guid={guid}&units={units}"

        try:
            result = requests.get(url, timeout=5)

            if result.status_code == 200:

                ret_value = result.json()
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    def remove_account(self, guid, units):
        """ Переместить п.е. от сотрудника к компании """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/RemoveAccount?guid={guid}&units={units}"

        try:
            result = requests.get(url, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    def do_request_create_card_holder(self, json_data: dict):
        """ Создает сотрудника """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/DoRequestCreateCardHolder"

        try:
            result = requests.get(url, json=json_data, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    def set_contacts(self, guid, phone, email):
        """ Переместить п.е. от сотрудника к компании """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/SetContacts?guid={guid}&phone={phone}&email={email}"

        try:
            result = requests.get(url, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    def get_photo(self, photo_name):
        """ Получить фотографию """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/GetPhoto?photo_name={photo_name}"

        try:
            result = requests.get(url, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()
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
            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    def remove_car_employee(self, guid, id_number):
        """ Отвязать номер от сотрудника """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/RemoveCarEmployee?guid={guid}&fplateid={id_number}"

        try:
            result = requests.get(url, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()

            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    # get_request_create_card_holder

    def get_request_create_card_holder(self, json_data: dict):
        """ Получить список заявок """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/GetRequestCreateCardHolder"

        try:
            result = requests.get(url, json=json_data, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()

            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value

    def get_request_replace_card_holder(self, json_data: dict):
        """ Запрос на перевыпуск """

        ret_value = {"RESULT": 'ERROR', "DESC": '', 'DATA': None}

        url = f"http://{self.host}:{self.port}/DoRequestReplaceCard"

        try:
            result = requests.get(url, json=json_data, timeout=5)

            if result.status_code == 200:
                ret_value = result.json()

            else:
                ret_value['DESC'] = f"Статус код: {result.status_code}"

        except Exception as ex:
            ret_value['DESC'] = f"Исключение при обращении к серверу: {ex}"

        return ret_value
