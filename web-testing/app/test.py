from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("http://www.migala.mx")
print("Encontrando elementos comúnes en la página web")
print( driver.current_url )
print("Regresar")
driver.back()
print("Hacia adelante")
driver.forward()
print("Refrescar la página")
driver.refresh()
print(f"Título: {driver.title}")
# Vínculos de contacto
print("Vínculos de contacto")
contact = driver.find_element_by_css_selector(".cb-top-nav")
contact.find_element_by_id("menu-item-1553").click()
driver.back()
contact = driver.find_element_by_css_selector(".cb-top-nav")
contact.find_element_by_id("menu-item-1554").click()
driver.back()
# Botón de búsqueda, se espera que obtenga un modal
driver.find_element_by_id("cb-s-trigger-gen").click()
search_box = driver.find_element_by_css_selector(".cb-search-field")

driver.find_element_by_css_selector(".cb-close-m").click()

# Vínculos de menú principal
print("Vínculos de menú principal")
driver.find_element_by_id("menu-item-1687").click()
driver.back()
driver.find_element_by_id("menu-item-1690").click()
driver.back()
driver.find_element_by_id("menu-item-1688").click()
driver.back()
driver.find_element_by_id("menu-item-1692").click()
driver.back()
driver.find_element_by_id("menu-item-1689").click()
driver.back()
driver.find_element_by_id("menu-item-1691").click()
driver.back()

# Vinculos de publicaciones
driver.find_element_by_xpath('//a[contains(@href, "amasando")]')
driver.find_element_by_xpath('//a[contains(@href, "panorama")]')
driver.find_element_by_xpath('//a[contains(@href, "magia")]')
driver.find_element_by_xpath('//a[contains(@href, "metamorfosis")]')
driver.find_element_by_xpath('//a[contains(@href, "neoliberalismo")]')
driver.find_element_by_xpath('//a[contains(@href, "jojos")]')
driver.find_element_by_xpath('//a[contains(@href, "simbolismo")]')
driver.find_element_by_xpath('//a[contains(@href, "casas")]')
driver.find_element_by_xpath('//a[contains(@href, "matate")]')
driver.find_element_by_xpath('//a[contains(@href, "pintura")]')

try:
  driver.find_element_by_css_selector(".dona")
except:
  print("Elemento no existe, pero debe existir")

# En busqueda de la página huérfana
try:
  driver.find_element_by_xpath('//a[contains(@href,"tianguis")]')
  print("La página puede encontrarse dentro del principal")
except:
  print("La página es huérfana")

driver.get("http://tianguis.migala.mx")
driver.quit()
