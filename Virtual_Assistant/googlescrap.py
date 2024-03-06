import requests
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

classes = ["zCubwf", "hgKElc", "LTKOO sY7ric", "Z0LcW", "gsrt vk_bk FzvWSb YwPhnf", "pclqee", "tw-Data-text tw-text-small tw-ta",
           "IZ6rdc", "O5uR6d LTKOO", "vlzY6d", "webanswers-webanswers_table__webanswers-table",
           "dDoNo ikb4Bb gsrt", "sXLaOe", "LWkfKe", "VQF4g", "qv3Wpe", "kno-rdesc"]

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'

def online_scraper(query, print_results=True):
    query = query.replace(" + ", " plus ")
    query = query.replace(" - ", " minus ")
    url = "https://www.google.co.in/search?q=" + query
    headers = {'User-Agent': user_agent}

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    results = []
    for class_name in classes:
        try:
            result = soup.find(class_=class_name).get_text()
            if print_results:
                print(f"{Fore.GREEN}{result}")
            results.append(result)
        except Exception:
            pass

    if not results:
        results.append("No information found.")

    return results



