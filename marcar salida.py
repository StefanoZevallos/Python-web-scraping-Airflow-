from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from selenium import webdriver
import time
import pendulum
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Funcion para entrar al buscador , colocar usuario y contraseña y clicker boton de salida
def marcacion_salida():
    driver = webdriver.Chrome("mnt/c/Users/Administrador/c/Users/Administrador/chrome.exe")
    driver.get("https://portal.grupokobsa.com.pe/usuario.app")
    time.sleep(2)
    username = driver.find_element("xpath", "//input[@placeholder='Usuario']")
    password = driver.find_element("xpath", "//input[@placeholder='Contraseña']")
    username.send_keys("xzevallos")
    password.send_keys("bLvhSJjJNmpd@i6$")
    time.sleep(2)
    submit = driver.find_element("xpath", "//button[@type='submit']").click()
    salida = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(("xpath", '//button[contains(text(), "Registrar Salida")]'))).click()
    time.sleep(2)

# Especificaciones de cuando a que hora se ejecutará el código
with DAG(
        dag_id='salida',
        description='Marcacion de entrada y salida',
        schedule='03 00 * * 1-7',
        start_date=pendulum.datetime(2022, 12, 27, tz="UTC")) as dag:


    t1 = PythonOperator(
        task_id='salida',
        python_callable=marcacion_salida)

    t1