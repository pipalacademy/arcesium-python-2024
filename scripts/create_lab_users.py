from selenium import webdriver
from selenium.webdriver.common.by import By
import typer
import time
import pathlib
import pandas as pd
from typing_extensions import Annotated

admin = "vikrant"
adminpassword = "vikrant42"

phrase = list("alskdjfhgqpwoeiruty")
allchars = [chr(i) for i in range(48, 124)]


def rotate(data, n):
    return data[n:] + data[:n]


table = {c: rotate(allchars, i) for i, c in enumerate(allchars)}


def pairs(text):
    s = len(phrase)
    if len(text) <= s:
        yield from zip(text, phrase)
    else:
        yield from zip(text[:s], phrase)
        yield from pairs(text[s:])


def encrypt(text):
    breaks = [i for i, c in enumerate(text) if c == " "]
    text = text.replace(" ", "")
    textc = [table[T][ord(P)-ord(allchars[0])] for T, P in pairs(text)]
    for b in breaks:
        textc.insert(b, " ")
    return "".join(textc)


def get_driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    return driver


def fill_details(driver, id_, text):
    element = driver.find_element(By.ID, id_)
    element.send_keys(text)


def click_button(driver, id_):
    button = driver.find_element(By.ID, id_)
    button.click()


def login(driver, username, password):
    authurl = "https://arcesium-lab.pipal.in/hub/"
    driver.get(authurl)
    fill_details(driver, "username_input", username)
    fill_details(driver, "password_input", password)
    click_button(driver, "login_submit")


def signup(driver, username, password):
    signupurl = "https://arcesium-lab.pipal.in/hub/signup"
    driver.get(signupurl)
    fill_details(driver, "username_input", username)
    fill_details(driver, "password_input", password)
    fill_details(driver, "password_confirmation_input", password)
    click_button(driver, "signup_submit")


def logout(driver, username):
    driver.get(f"https://arcesium-lab.pipal.in/user/{username}/logout/")


def create_user(username, password):
    driver = get_driver()
    signup(driver, username, password)

    login(driver, admin, adminpassword)
    authurl = f"https://arcesium-lab.pipal.in/hub/authorize/{username}"
    driver.get(authurl)
    logout(driver, admin)

    login(driver, username, password)
    time.sleep(3)
    logout(driver, username)
    driver.close()


def main(userfile: Annotated[typer.FileText,
                             typer.Argument(help="A csv file with username,passwd columns in it.")]):

    userdata = pd.read_csv(userfile, usecols=['username', 'passwd'])
    for username, password in userdata.values:
        print(username, password)
        create_user(username, password)


if __name__ == "__main__":
    typer.run(main)
