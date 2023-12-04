from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
desired_caps['platformName'] = 'Android'  # Use 'iOS' para testes no iOS
desired_caps['deviceName'] = 'Nome do seu dispositivo'
desired_caps['automationName'] = 'UiAutomator2'  # Use 'XCUITest' para testes no iOS
desired_caps['appPackage'] = 'com.spotify.music'  # Use 'com.spotify.client' para testes no iOS
desired_caps['appActivity'] = 'com.spotify.music.MainActivity'  # Use 'com.spotify.client.StartupRouting' para testes no iOS

# Configurações específicas para Android
desired_caps['platformVersion'] = 'Versão do Android no seu dispositivo'

# Configurações específicas para iOS
# desired_caps['platformVersion'] = 'Versão do iOS no seu dispositivo'
# desired_caps['udid'] = 'UDID do seu dispositivo'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Aguarde a tela inicial do Spotify carregar
driver.implicitly_wait(10)

# Toque no botão 'Biblioteca' na barra de navegação inferior
library_button = driver.find_element_by_accessibility_id('Biblioteca')
library_button.click()

# Aguarde a tela da biblioteca carregar
driver.implicitly_wait(10)

# Toque na primeira música na biblioteca
first_song = driver.find_element_by_xpath('//android.widget.LinearLayout[1]')
first_song.click()

# Aguarde a música começar a tocar
driver.implicitly_wait(10)

driver.quit()


