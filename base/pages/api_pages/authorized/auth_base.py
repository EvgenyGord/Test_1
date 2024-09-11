import allure
import requests

from base.models_api_pydantic.auth.model_auth_v1 import AuthorizedResponseSuccess, AuthorizedResponseError
from base.models_api_pydantic.auth.model_delete_v1_user import User_Delete_Response
from base.models_api_pydantic.auth.model_get_user import User_Get_Response
from base.models_api_pydantic.auth.model_post_v1_token_generate import GenerateTokenResponse
from base.models_api_pydantic.auth.model_post_v1_user import User_Response
from settings import Settings


class AuthBase:
    def __init__(self, username: str, password: str):
        """
        Инициализирует объект класса AuthBase, устанавливая имя пользователя, пароль и заголовки для HTTP-запросов.

        :param username: Имя пользователя для авторизации.
        :param password: Пароль пользователя для авторизации.

        Атрибуты:
        - username (str): Имя пользователя, которое будет использоваться в запросах.
        - password (str): Пароль пользователя, который будет использоваться в запросах.
        - headers (dict): Заголовки HTTP-запросов, включая тип контента и принимаемый формат.
        - base_url (str): Базовый URL API, полученный из класса Settings.
        """
        self.username = username
        self.password = password
        self.headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        self.base_url = Settings().base_url


    def get_authorized_endpoint(self):
        """
        Возвращает полный URL для выполнения POST-запроса авторизации пользователя.

        :return: Строка с полным URL для авторизации пользователя.
        """
        return f"{self.base_url}/Account/v1/Authorized"

    def get_generate_token_endpoint(self):
        """
        Возвращает полный URL для выполнения POST-запроса генерации токена пользователя.

        :return: Строка с полным URL для генерации токена пользователя.
        """
        return f"{self.base_url}/Account/v1/GenerateToken"

    def get_user_endpoint(self):
        """
        Возвращает полный URL для выполнения POST-запроса создания пользователя.

        :return: Строка с полным URL для создания пользователя.
        """
        return f"{self.base_url}/Account/v1/User"

    def get_delete_user_endpoint(self, id):
        """
        Возвращает полный URL для выполнения POST-запроса создания пользователя.

        :return: Строка с полным URL для создания пользователя.
        """

        return f"{self.base_url}/Account/v1/User/{id}"

    def get_get_user_endpoint(self, id):
        """
        Возвращает полный URL для выполнения GET-запроса создания пользователя.

        :return: Строка с полным URL для создания пользователя.
        """

        return f"{self.base_url}/Account/v1/User/{id}"


    @allure.step("Формирование данных для запроса")
    def form_request_data(self, endpoint):
        """
        Формирует данные для POST-запроса и возвращает их вместе с полным URL.

        :param endpoint: Полный URL, на который будет отправлен запрос.
        :return: Кортеж, содержащий данные запроса в формате словаря и полный URL.

        Формируемый запрос включает в себя:
        - userName: Имя пользователя, переданное при инициализации класса.
        - password: Пароль пользователя, переданный при инициализации класса.

        Также в Allure-отчёт прикрепляется команда для выполнения запроса через curl.
        """
        data = {
            "userName": self.username,
            "password": self.password
        }
        url = endpoint
        allure.attach(
            f"curl -X 'POST' '{url}' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{data}'",
            name="Curl for Postman", attachment_type=allure.attachment_type.TEXT)
        return data, url

    @allure.step("Формирование данных для запроса DELETE")
    def form_request_data_delete(self, endpoint):
        """
        Формирует данные для DELETE-запроса и возвращает их вместе с полным URL.

        """
        data = {
            "userName": self.username,
            "password": self.password
        }
        url = endpoint
        allure.attach(
            f"curl -X 'DELETE' '{url}' -H 'accept: application/json'",
            name="Curl for Postman", attachment_type=allure.attachment_type.TEXT)
        return data, url

    @allure.step("Отправка POST-запроса")
    def send_post_request(self, data, url):
        """
        Отправляет POST-запрос на указанный URL с предоставленными данными и возвращает ответ сервера.

        :param data: Данные запроса в формате словаря.
        :param url: Полный URL для отправки POST-запроса.
        :return: Объект ответа от сервера.

        В Allure-отчёт прикрепляется:
        - Ответ сервера в текстовом формате.
        - Сырой запрос, отправленный на сервер.
        - Полный URL запроса.
        - Код статуса HTTP-ответа.
        """
        response = requests.post(url, headers=self.headers, json=data)
        allure.attach(response.text, name="Ответ сервера", attachment_type=allure.attachment_type.JSON)
        allure.attach(response.request.body.decode(), name="Сырой запрос", attachment_type=allure.attachment_type.JSON)
        allure.attach(url, name="URL запроса", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Status Code: {response.status_code}", name="Код статуса",
                      attachment_type=allure.attachment_type.TEXT)
        return response

    @allure.step("Отправка DELETE-запроса")
    def send_delete_request(self, data, url):
        """
        Отправляет DELETE-запрос на указанный URL с предоставленными данными и возвращает ответ сервера.

        :param data: Данные запроса в формате словаря.
        :param url: Полный URL для отправки DELETE-запроса.
        :return: Объект ответа от сервера.

        В Allure-отчёт прикрепляется:
        - Ответ сервера в текстовом формате.
        - Сырой запрос, отправленный на сервер.
        - Полный URL запроса.
        - Код статуса HTTP-ответа.
        """
        response = requests.delete(url, headers=self.headers, json=data)
        allure.attach(response.text, name="Ответ сервера", attachment_type=allure.attachment_type.JSON)
        allure.attach(response.request.body.decode(), name="Сырой запрос", attachment_type=allure.attachment_type.JSON)
        allure.attach(url, name="URL запроса", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Status Code: {response.status_code}", name="Код статуса",
                      attachment_type=allure.attachment_type.TEXT)
        return response

    @allure.step("Отправка GET-запроса")
    def send_get_request(self, data, url):
        """
        Отправляет GET-запрос на указанный URL с предоставленными данными и возвращает ответ сервера.

        :param data: Данные запроса в формате словаря.
        :param url: Полный URL для отправки GET-запроса.
        :return: Объект ответа от сервера.

        В Allure-отчёт прикрепляется:
        - Ответ сервера в текстовом формате.
        - Сырой запрос, отправленный на сервер.
        - Полный URL запроса.
        - Код статуса HTTP-ответа.
        """
        response = requests.get(url, headers=self.headers, json=data)
        allure.attach(response.text, name="Ответ сервера", attachment_type=allure.attachment_type.JSON)
        allure.attach(response.request.body.decode(), name="Сырой запрос", attachment_type=allure.attachment_type.JSON)
        allure.attach(url, name="URL запроса", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Status Code: {response.status_code}", name="Код статуса",
                      attachment_type=allure.attachment_type.TEXT)
        return response

    @allure.step("Валидация успешного ответа")
    def validate_success_response(self, response):
        """
        Валидирует успешный ответ сервера для запроса авторизации.

        :param response: Объект ответа от сервера.

        Метод проверяет, что значение поля "value" в ответе равно True. В случае успеха
        в консоль выводится сообщение "Успешная авторизация: True". Также добавляется
        запись в Allure-отчёт с деталями успешного ответа.
        """
        result = AuthorizedResponseSuccess.parse_obj({"value": response.json()})
        assert result.value is True, "Ожидался ответ 'true', но получено другое значение"
        print("Успешная авторизация: True")
        allure.attach(f"Ответ успешен: {result.value}", name="Валидация успешного ответа",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Валидация успешного ответа получения токена")
    def validate_token_response(self, response):
        """
        Валидирует успешный ответ сервера для запроса генерации токена.

        :param response: Объект ответа от сервера.

        Метод проверяет, что поле "status" в ответе равно "Success". В случае успеха
        в консоль выводится сообщение со сгенерированным токеном. Также добавляется
        запись в Allure-отчёт с деталями успешного ответа, включая токен, дату истечения,
        статус и результат.
        """
        result = GenerateTokenResponse.parse_obj(response.json())
        assert result.status == "Success", f"Ожидался статус 'Success', но получено: {result.status}"
        print(f"Токен успешно сгенерирован: {result.token}")
        allure.attach(
            f"Токен: {result.token}\nИстекает: {result.expires}\nСтатус: {result.status}\nРезультат: {result.result}",
            name="Валидация успешного ответа",
            attachment_type=allure.attachment_type.TEXT)

    @allure.step("Валидация успешного ответа создания пользователя")
    def validate_create_user_response(self, response):
        """
        Валидирует успешный ответ сервера для запроса создания пользователя.

        :param response: Объект ответа от сервера.

        Метод проверяет, что поле "username" в ответе равно тому что мы ввели при отправке запроса. В случае успеха
        в консоль выводится сообщение, что пользователь успешно создан. Также добавляется
        запись в Allure-отчёт с деталями успешного ответа, включая токен, дату истечения,
        статус и результат.
        """
        result = User_Response.parse_obj(response.json())
        assert result.username == self.username, f"Ожидалось имя пользователя {self.username}, но получено: {result.username}"
        print(f"Пользователь с именем: {result.username} успешно создан")
        allure.attach(
            f"ID пользователя {result.userID}\n Имя пользователя: {result.username}",
            name="Валидация успешного ответа",
            attachment_type=allure.attachment_type.TEXT)

    @allure.step("Валидация успешного ответа удаления пользователя")
    def validate_delete_user_response(self, response):

        result = User_Delete_Response.parse_obj(response.json())
        assert result.username == self.username, f"Ожидалось имя пользователя {self.username}, но получено: {result.username}"
        print(f"Пользователь с именем: {result.username} успешно удален")
        allure.attach(
            f"ID пользователя {result.userID}\n Имя пользователя: {result.username}",
            name="Валидация успешного ответа",
            attachment_type=allure.attachment_type.TEXT)

    @allure.step("Валидация успешного ответа получения информации о пользователе")
    def validate_get_user_response(self, response):

        result = User_Get_Response.parse_obj(response.json())
        assert result.username == self.username, f"Ожидалось имя пользователя {self.username}, но получено: {result.username}"
        print(f"Пользователь с именем: {result.username} успешно удален")
        allure.attach(
            f"ID пользователя {result.userID}\n Имя пользователя: {result.username}",
            name="Валидация успешного ответа",
            attachment_type=allure.attachment_type.TEXT)

    @allure.step("Валидация ошибки")
    def validate_error_response(self, response):
        """
        Валидирует ошибочный ответ сервера.

        :param response: Объект ответа от сервера.

        Метод проверяет, что код ошибки равен 0 и сообщение об ошибке является строкой.
        В случае ошибки выводится сообщение с кодом и текстом ошибки в консоль.
        Также добавляется запись в Allure-отчёт с деталями ошибки.
        """
        error_response = AuthorizedResponseError.parse_obj(response.json())
        assert error_response.code == 0, "Ожидался код ошибки '0'"
        assert isinstance(error_response.message, str), "Сообщение об ошибке должно быть строкой"
        print(f"Ошибка: Код - {error_response.code}, Сообщение - {error_response.message}")
        allure.attach(f"Код ошибки: {error_response.code}, Сообщение: {error_response.message}",
                      name="Валидация ошибки", attachment_type=allure.attachment_type.TEXT)

    def validate_response(self, response, success_validator):
        """
        Валидирует ответ сервера, используя предоставленный валидатор успешного ответа.

        :param response: Объект ответа от сервера.
        :param success_validator: Функция для валидации успешного ответа.

        Метод проверяет статус-код ответа. Если статус 200, то вызывается функция success_validator
        для дальнейшей валидации. Если статус отличается от 200, выводится информация об ошибке в консоль
        и Allure-отчёт, после чего тест завершается с ошибкой.
        """
        with allure.step("Проверка статуса и валидация ответа"):
            if response.status_code == 200:
                success_validator(response)
                print("Тест успешен: Статус код 200")
            else:
                print(f"Неожиданный статус ответа: {response.status_code}")
                print(f"Ответ сервера: {response.text}")
                allure.attach(response.text, name="Ответ сервера", attachment_type=allure.attachment_type.JSON)
                assert False, f"Неожиданный статус ответа: {response.status_code}"

    def validate_create_response(self, response, success_validator):
        """
        Валидирует ответ сервера, используя предоставленный валидатор успешного ответа.

        :param response: Объект ответа от сервера.
        :param success_validator: Функция для валидации успешного ответа.

        Метод проверяет статус-код ответа. Если статус 201, то вызывается функция success_validator
        для дальнейшей валидации. Если статус отличается от 201, выводится информация об ошибке в консоль
        и Allure-отчёт, после чего тест завершается с ошибкой.
        """
        with allure.step("Проверка статуса и валидация ответа"):
            if response.status_code == 201:
                success_validator(response)
                print("Тест успешен: Статус код 201")
            else:
                if response.status_code == 406:
                    print('User exists! пользователь уже создан попробуйте ввести другое имя!')
                    print(f"Ответ сервера: {response.text}")
                    allure.attach(response.text, name="Ответ сервера", attachment_type=allure.attachment_type.JSON)
                    assert False, f"Неожиданный статус ответа: {response.status_code}"

                else:
                    print(f"Неожиданный статус ответа: {response.status_code}")
                    print(f"Ответ сервера: {response.text}")
                    allure.attach(response.text, name="Ответ сервера", attachment_type=allure.attachment_type.JSON)
                    assert False, f"Неожиданный статус ответа: {response.status_code}"
