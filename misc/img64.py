import os
import base64


class PhotoReader:

    @staticmethod
    def take_photo(file_path='../test.jpg'):
        """ Получить фото в строковой base64 """
        ret_value = ''
        if os.path.isfile(file_path):
            with open(file_path, 'rb+') as file:
                ret_value = base64.b64encode(file.read()).decode()

        return ret_value


if __name__ == '__main__':
    print(PhotoReader.take_photo())
