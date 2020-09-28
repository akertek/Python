"""
random_steal.py

top-to-bottom.

https://www.random.org/integers/?num=100&min=1&max=100&col=5&base=10&format=html&rnd=new
"""

import requests
from bs4 import BeautifulSoup

__SETTINGS = {
    "base_url": "https://www.random.org/integers/",
    "num": 100,  # kac tane sayi
    "min": 1,
    "max": 100,
    "col": 1,
    "base": 10,
    "format": "html",  # plain de olabilir.
    "rnd": "new",
}


def build_url(settings):
    """
    Settings icindeki elemanari kullanarak hedef URL'yi olusturur.

    DRY

    :param settings:
    :return:
    """
    liste = []
    for k, v in settings.items():
        if k == "base_url":
            liste.append(v + "?")
        else:
            liste.append(str(k) + "=" + str(v) + "&")
    url = "".join(liste)

    # tarayicilar sonraki & isaretini hallediyor,
    # ama biz yine de kaldiralim.
    url = url[:-1]
    return url


def get_raw_html(settings):
    url = build_url(settings)
    print(url)
    raw_html = requests.get(url)
    return raw_html.text


def get_random_numbers(raw_html):
    """
    Sayıları bir list olarak döndürür.
    raw_html'i, beautiful soup ile parçalarına ayırır.
    
    :param raw_html
    
    """
    soup = BeautifulSoup(raw_html, 'html.parser')
    pre_tag = soup.find("pre", attrs={"class":"data"})
    data = pre_tag.string
    
    data1 = data.split("\n")
    if data1[-1].strip() == "":
        data1 = data1[:-1]
        
    data1 = [int(i) for i in data1]
  

def main():
    raw_html = get_raw_html(__SETTINGS)
    get_random_numbers(raw_html)
    # assert isinstance(numbers,list)
    # assert isinstance(numbers[0])
    print("done")

if __name__ == "__main__":
    main()











