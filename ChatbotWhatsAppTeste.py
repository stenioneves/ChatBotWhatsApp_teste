from selenium import webdriver
import time

class BotWhatsApp:
    def __init__(self):
        self.texto=" Bom dia! 🤩😎" + "*Texto automatico*"
        self.grupo= "Teste"
        options= webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver =webdriver.Chrome(executable_path=r'./chromedriver')
    def TextoInicio(self):
        grupo =self.driver.find_element_by_xpath("")    
