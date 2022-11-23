import requests
from bs4 import BeautifulSoup
import re
import csv


def get_content(url):
    req = requests.get(url)
    return req.text

def refined(s):
    res = re.sub(r"\D+", "", s)
    return res

def write_csv(data):
    with open('csv_file.csv', 'a') as fl:
        writer = csv.writer(fl, lineterminator="\r")
        writer.writerow((data['name'], data['img'], data['pr_linck'], data['prais']))


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    carta1 = soup.find_all("div",class_="product bg-white shadow-sm mb-3 mb-lg-4 rounded overflow-hidden d-flex "
                                        "flex-column p-sm-2 p-1")


    for i in carta1:
        linc = "https://allithave.ru" + i.find("a")["href"]
        price = i.find("div", class_="price").text
        img = i.find("img")["src"]
        title = i.find("div", class_="name flex-grow-1 mt-1").text
        r = refined(price)

        data = {'name': title, 'img': img, 'pr_linck': linc, 'prais': r}
        write_csv(data)


def main():
    url = "https://allithave.ru/catalog/osveschenie-18060"
    (get_data(get_content(url)))


if __name__ == "__main__":
    main()
