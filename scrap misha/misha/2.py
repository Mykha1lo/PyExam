import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


def get_names(driver):
    # Знаходимо елементи з класом `product__title-left.product__title-collapsed.ng-star-inserted`
    names = driver.find_elements(By.CSS_SELECTOR, ".product__title-left.product__title-collapsed.ng-star-inserted")

    # Створюємо список для зберігання даних
    data = []

    # Ітеруємося по елементах і вилучаємо дані
    for name in names:
        try:
            data.append(name.text)
        except NoSuchElementException as e:
            # Виводимо повідомлення про помилку, якщо елемент не знайдено
            print(f"Не вдалося знайти елемент з класом `product__title-left h1.product__title-collapsed.ng-star-inserted`: {e}")

    return data


def get_prices(driver):
    # Знаходимо елементи з класом `product__price`
    prices = driver.find_elements(By.CSS_SELECTOR, ".product-price__big.product-price__big-color-red")

    # Створюємо список для зберігання даних
    data = []

    # Ітеруємося по елементах і вилучаємо дані
    for price in prices:
        try:
            data.append(price.text)
        except NoSuchElementException as e:
            # Виводимо повідомлення про помилку, якщо елемент не знайдено
            print(f"Не вдалося знайти елемент з класом `product__price`: {e}")

    return data


def main():
    # Вказуємо URL веб-сторінки
    url = "https://rozetka.com.ua/ua/asus-90nr0cy1-m004l0/p388356138/"

    # Створюємо екземпляр веб-драйвера Edge
    driver = selenium.webdriver.Edge()

    # Відкриваємо веб-сторінку
    driver.get(url)

    # Додаємо очікування загрузки елементів
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".product-price__big.product-price__big-color-red"))
    )

    # Вилучаємо дані з веб-сторінки
    names = get_names(driver)
    prices = get_prices(driver)

    # Виводимо на екран імена і ціни
    print("Імена:")
    for name in names:
        print(name)

    print("Ціни:")
    for price in prices:
        print(price)

    # Змінюємо формат запису даних у файл CSV
    with open("data.csv", "w", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")

        # Записуємо заголовок у файл CSV
        writer.writerow(["Ім'я", "Ціна"])
        
        # Записуємо дані у файл CSV, використовуючи функцію zip для об'єднання імен і цін
        writer.writerows(zip(names, prices))


if __name__ == "__main__":
    main()
