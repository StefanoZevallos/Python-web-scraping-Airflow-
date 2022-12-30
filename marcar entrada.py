from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.utils import timezone
from selenium import webdriver
import time
import pendulum
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# funcion que abre el navegador , coloca el usuario y contraseña y marca asistencia
def marcacion_entrada():
    driver = webdriver.Chrome("mnt/c/Users/Administrador/c/Users/Administrador/chrome.exe")
    driver.get("https://portal.grupokobsa.com.pe/usuario.app")
    time.sleep(2)
    username = driver.find_element("xpath", "//input[@placeholder='Usuario']")
    password = driver.find_element("xpath", "//input[@placeholder='Contraseña']")
    username.send_keys("xzevallos")
    password.send_keys("bLvhSJjJNmpd@i6$")
    time.sleep(2)
    ingreso = driver.find_element("xpath", "//button[@type='submit']").click()
    time.sleep(2)
    entrada = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(("xpath", '//button[contains(text(), "Registrar Entrada")]'))).click()
    time.sleep(2)

# Especificaciones cuando y a que hora se ejecutará el código

with DAG(
        dag_id='entrada',
        description='Marcacion de entrada y salida',
        schedule='11 14 * * *',
        start_date=pendulum.datetime(2022, 12, 27,  tz="UTC")) as dag:

    t = PythonOperator(
        task_id='entrada',
        python_callable=marcacion_entrada)

    t