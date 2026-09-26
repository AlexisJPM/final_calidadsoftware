from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

casos_prueba = [
    {
        "first_name": "Alexis",
        "last_name": "Panchi",
        "email": "alexis@ejemplo.com",
        "comments": "Mensaje de prueba"
    },
    {
        "first_name": "Juan",
        "last_name": "Romero",
        "email": "juan",
        "comments": "Segundo mensjae de prueba"
    },
    {
        "first_name": "Andy",
        "last_name": "Limaico",
        "email": "andy@ejemplo.com",
        "comments": "Tercer mensjae de prueba"
    },
    {
        "first_name": "Josue",
        "last_name": "Parrales",
        "email": "josuejemplo",
        "comments": "Cuarto mensjae de prueba"
    },
    {
        "first_name": "Bryan",
        "last_name": "Parrales",
        "email": "bryan@ejemplo.com",
        "comments": ""
    }
]

service = Service(executable_path="msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("https://webdriveruniversity.com")

tiempo_inicial = time.time()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "contact-us"))
    )

print(f"Tiempo de carga de la página: {time.time() - tiempo_inicial} segundos")

time.sleep(3)

contact_us_link = driver.find_element(By.ID, "contact-us")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", contact_us_link)
time.sleep(3)
driver.execute_script("arguments[0].click();", contact_us_link)

driver.switch_to.window(driver.window_handles[-1])

for caso in casos_prueba:
    tiempo_inicial = time.time()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='First Name']"))
        )

    print(f"Tiempo de carga de la página: {time.time() - tiempo_inicial} segundos")

    time.sleep(2)

    first_name_input = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
    first_name_input.send_keys(caso["first_name"])
    time.sleep(1)

    last_name_input = driver.find_element(By.XPATH, "//input[@name='last_name']")
    last_name_input.send_keys(caso["last_name"])
    time.sleep(1)

    email_input = driver.find_element(By.XPATH, "//input[@name='email']")
    email_input.send_keys(caso["email"])
    time.sleep(1)

    comments_input = driver.find_element(By.XPATH, "//textarea[@name='message']")
    comments_input.send_keys(caso["comments"])
    time.sleep(2)

    submit_button = driver.find_element(By.XPATH, "//input[@value='SUBMIT']")
    submit_button.click()

    tiempo_inicial = time.time()
    try:
        reply_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='contact_reply']/h1"))
            )
        print(f"Tiempo de respuesta del formulario: {time.time() - tiempo_inicial} segundos")
        mensaje = reply_element.text
    except TimeoutException:
        mensaje = "El formulario no se envio: el navegador bloqueo el envio por validacion nativa del campo (sin formato valido)."

    print(f"Caso {caso['first_name']} {caso['last_name']} (email: '{caso['email']}', comments: '{caso['comments']}'): {mensaje}")

    time.sleep(3)

    driver.get("https://webdriveruniversity.com/Contact-Us/contactus.html")

time.sleep(7)

driver.quit()
