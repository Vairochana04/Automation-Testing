from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/browser-windows")
main_window = driver.current_window_handle
tab_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "tabButton"))
)
tab_button.click()
WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
all_windows = driver.window_handles
for handle in all_windows:
    if handle != main_window:
        driver.switch_to.window(handle)
        break
print("New tab title:", driver.title)
driver.close()
driver.switch_to.window(main_window)
print("Back to main window:", driver.title)
driver.quit()
