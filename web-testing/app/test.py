from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("http://www.migala.mx")
#Chrome(executable_path='opt/WebDriver/bin/chromedriver')
"""
findElements(By)
print( driver.current_url )
print("Regresar")
driver.back()
print("Hacia adelante")
driver.forward()
print("Refrescar la página")
driver.refresh()
"""
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
search_box = driver.find_by_css_selector(".cb-search-field")
# Vinculos que aparecen cuando se hace la búsqueda

"""
navbar = driver.find_element(By.ID, "cb-nav-bar")
menu_items = navbar.find_elements_by_css_selector(".menu-item")
print("Secciones del menú principal")
print( menu_items)
for item in menu_items:
  print(item)
"""
#driver.switch_to.new_window("tab")
driver.quit()
