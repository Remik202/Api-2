import requests
import os
from urllib.parse import urlparse
import argparse
from dotenv import load_dotenv


def shorten_link(token, url):
    api_url = "https://api.vk.com/method/utils.getShortLink"
    params = {
        "url": url,
        "access_token": token,
        "v": "5.199",
    }
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    content = response.json()
    if "error" in content:
        raise requests.exceptions.RequestException(content["error"]["error_msg"])
    return content["response"]["short_url"]


def count_clicks(token, short_url):
    api_url = "https://api.vk.com/method/utils.getLinkStats"
    parsed_url = urlparse(short_url)
    key = parsed_url.path.lstrip("/")
    params = {"key": key, "access_token": token, "v": "5.199", "extended": 1}
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    content = response.json()
    if "error" in content:
        raise requests.exceptions.RequestException(content["error"]["error_msg"])
    stats = content["response"]["stats"]
    clicks = sum(day["views"] for day in stats)
    return clicks


def is_shorten_link(token, url):
    parsed_url = urlparse(url)
    if parsed_url.netloc != "vk.cc":
        return False
    key = parsed_url.path.lstrip("/")
    api_url = "https://api.vk.com/method/utils.getLinkStats"
    params = {"key": key, "access_token": token, "v": "5.199"}
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    content = response.json()
    return "error" not in content


if __name__ == "__main__":
    load_dotenv()
    try:
        token = os.getenv("VK_TOKEN")
    except KeyError:
        print("Ошибка: Не указана переменная окружения VK_TOKEN.")
        exit()

    url = input("Введите ссылку для сокращения или подсчета кликов: ")  

    try:
        if is_shorten_link(token, url):
            clicks = count_clicks(token, url)
            print("Переходы:", clicks)
        else:
            short_url = shorten_link(token, url)
            print("Сокращенная ссылка:", short_url)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка: {e}")