import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse


def parse_link():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-l', '--link', required=True)
    parser_args = parser.parse_args()
    return parser_args.link


def is_bitlink(link):
    headers = {"Authorization": f"Bearer {token}"}
    original_url = "https://api-ssl.bitly.com/v4/bitlinks/"
    urlparse_url = urlparse(link)
    netloc_path = f"{urlparse_url.netloc}{urlparse_url.path}"
    get_urlparse_url = requests.get(f"{original_url}{netloc_path}",
                        headers=headers).ok 
    return get_urlparse_url


def shorten_link(token, link):
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "long_url": link,
    }
    shorten_url = "https://api-ssl.bitly.com/v4/shorten"
    response = requests.post(shorten_url, json=params, headers=headers)
    response.raise_for_status()
    return response.json()["link"]


def count_clicks(token, link):
    headers = {"Authorization": f"Bearer {token}"}
    params = (
        ("unit", "month"),
        ("units", "-1"),
    )
    original_url = "https://api-ssl.bitly.com/v4/bitlinks/"
    urlparse_url = urlparse(link)
    netloc_path = f"{urlparse_url.netloc}{urlparse_url.path}"
    url = f"{original_url}{netloc_path}/clicks/summary"
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()["total_clicks"]


if __name__ == "__main__":
    load_dotenv()
    token = os.environ["BITLY_TOKEN"]
    link = parse_link()

    try:
        if is_bitlink(link):
            print("По Вашей ссылке прошли:", count_clicks(token, link), "раз(а)")
        else:
            print("Битлинк: ", shorten_link(token, link))
    except requests.exceptions.HTTPError:
        print("Вы ввели неправильную ссылку или неверный токен.")
    except requests.exceptions.ConnectionError:
        print("Невозможно соединиться с указанным ресурсом")
    except requests.exceptions.InvalidURL:
        print("Проверьте, введена ли ссылка после https://... или http://...")

