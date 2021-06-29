import time
from selenium import webdriver
from pywinauto import application
from selenium.webdriver.chrome.options import Options
import pyautogui
from random import randint
import os

def absen(userinput, token, p):
    username = str(userinput)
    password = 'siswa'+username
    
    #login ke halaman pjj smkn 8 
    driver = webdriver.Chrome('d:/bot login/chromedriver.exe')
    driver.get('https://pjj.smkn8semarang.sch.id/login')
    user = driver.find_element_by_id('username default-01')
    user.send_keys(username)
    password_send = driver.find_element_by_id('password')
    password_send.send_keys(password)
    login_button = driver.find_element_by_css_selector('button.btn-block')
    login_button.click()
    time.sleep(5)

    #absen dan isi token 
    driver.get('https://pjj.smkn8semarang.sch.id/student')
    token_send = driver.find_element_by_name('student_token')
    token_send.send_keys(token)
    kegiatan_send = driver.find_element_by_name('student_text')
    kegiatan_send.send_keys(kegiatan[p])
    time.sleep(5)

    jejak_button = driver.find_element_by_css_selector('input.btn-primary')
    jejak_button.click()
    time.sleep(5)
    ss = pyautogui.screenshot()
    ss.save(r'C:/Users/capricorn/Pictures/ss1.png')
    print(username)
    print(kegiatan[p])

def whatsapp(nomor, p):
    # options = webdriver.ChromeOptions()
    # options.add_argument("--user-data-dir=/home/username/.config/google-chrome")
    # driver = webdriver.Chrome(executable_path="d:/bot login/chromedriver.exe", chrome_options=options)
    driver = webdriver.Chrome('d:/bot login/chromedriver.exe')


    driver.get('https://web.whatsapp.com/send?phone='+nomor)
    
    file_path = "C:/Users/capricorn/Pictures/ss1.png"#file path
    time.sleep(20)
    from time import sleep
    #sending image to whatsapp
    attachment_section = driver.find_element_by_xpath('//div[@title = "Attach"]')
    attachment_section.click()
    image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(file_path)

    time.sleep(2)
    caption = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]")
    caption.send_keys('kamu sudah saya absenin dengan kegiatan ' + kegiatan[p] + ' tidur yang nyenyak ya :)"' )
    time.sleep(5)


def pjj(i, token, p):

    absen(murid[i][0:4], token, p)
    i += 1
    os.system("taskkill /im chromedriver.exe /f")

    # print(i,murid[i])
    whatsapp(murid[i], p)
    os.system("taskkill /im chromedriver.exe /f")
#////////////////////////////////////////////////////////////////////////////////////////////////////

app = application.Application()
text = open('token.txt')
text = text.readlines()

murid = open('nama.txt', 'r')
murid =  murid.readlines()

kegiatan = open('alasan.txt', 'r')
kegiatan = kegiatan.readlines()
p = randint(0,len(kegiatan)-1)

seconds = time.time()
local_time = time.ctime(seconds)
jam_pertama = local_time[11:19]
jam_kedua = "08:30:30"
jam_ketiga = '09:30:30'

while(True):
    seconds = time.time()
    local_time = time.ctime(seconds)
    print(local_time[11:19])
    time.sleep(1)
    gambar = 1
    i = 0

    if local_time[11:19] == jam_pertama:

        while i < (len(murid) - 1):
            kegiatan = open('alasan.txt', 'r')
            kegiatan = kegiatan.readlines()
            p = randint(0,len(kegiatan)-1)
            
            pjj(i, text[0], p)
            i += 2
    
    
    if local_time[11:19] == jam_kedua:

        while i < (len(murid) - 1):

            kegiatan = open('alasan.txt', 'r')
            kegiatan = kegiatan.readlines()
            p = randint(0,len(kegiatan)-1)
            
            pjj(i, text[0], p)
            i += 2
    
    if local_time[11:19] == jam_ketiga:
        print(len(murid))
        

        while i < (len(murid) - 1):

            kegiatan = open('alasan.txt', 'r')
            kegiatan = kegiatan.readlines()
            p = randint(0,len(kegiatan)-1)
            
            pjj(i, text[0], p)
            i += 2
    
            
                    
    else :
        continue