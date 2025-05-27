# Сокращение ссылок и подсчет переходов с помощью VK

## Описание проекта
Проект предназначен для сокращения ссылок через сервис VK, а так же для подсчета переходов по сокращенным ссылкам.

## Как установить
Python3 должен быть установлен. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

```pip install -r requirements.txt```

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.

* Для работы с методами VK API требуется [сервисный ключ](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/tokens/service-token):
>Вы можете найти токен в поле Cервисный ключ доступа раздела Приложение Ключ помещаем в .env файл, используя load_dotenv и os
```python
load_dotenv()
token = os.environ["VK_SERVICE_KEY"]
```
* метод [utils.getShortLink](https://dev.vk.com/ru/method/utils.getShortLink) используется для сокращения ссылок
* метод [utils.getLinkStats](https://dev.vk.com/ru/method/utils.getLinkStats) используется для получения информации по ссылке и подсчета переходов

## Как пользоваться
1. Запускаем програму в командной строке, указывая ссылку.
```python main.py https://dvmn.org/modules```

2. В реультате получаем:
    * Если ссылка обычная, метод utils.getShortLink её сокращает:
      >Сокращенная ссылка: https://vk.cc/cvPDMl

    * Если ссылка сокращенная, метод utils.getLinkStats показывает количество переходов по ней:
      >Количество переходов: 6

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).
