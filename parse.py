import csv

from selenium import webdriver
from selenium.webdriver.common.by import By

from config import link, num_of_pages
from write_to_sheet import csv_to_sheet


def write_to_csv(data):
    with open("apartmens.csv", "a", encoding='UTF8', newline="") as f:
        writer = csv.writer(f)

        for row in data:
            writer.writerow(row)


def parse_page():
    apartmens = driver.find_elements(By.CLASS_NAME, "css-1sw7q4x")

    ads = []
    for apartment in apartmens[:-1]:
        name_and_price = apartment.find_element(By.CLASS_NAME, "css-u2ayx9")
        name = name_and_price.find_element(By.TAG_NAME, "h6").text
        price = apartment.find_element(By.TAG_NAME, "p").text

        street_and_area = apartment.find_element(By.CLASS_NAME, "css-odp1qd")
        street = street_and_area.find_element(By.TAG_NAME, "p").text.split("-")[0]
        area = street_and_area.find_element(By.TAG_NAME, "div").text

        ads.append([
            name,
            price,
            street,
            area
        ])

    return ads


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(link)
    write_to_csv(parse_page())

    for page in range(2, num_of_pages + 1):
        driver.get(link + "?page=" + str(page))
        write_to_csv(parse_page())

    driver.close()

    csv_to_sheet()
