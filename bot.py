linkPechincha = "https://a.aliexpress.com/_mqMVDKt"


import os, time, random, string
from selenium import webdriver

resultado = 0
resultadoAntigo = 0
resultadoCount = 0
useProxy = False
randomDevice = False
proxyList = []
deviceList = []
if os.path.isfile("proxylist.txt"):
    useProxy = True
    with open("proxylist.txt", "r", encoding="utf8") as proxies:
        for line in proxies:
            if not ":" in line:
                continue
            else:
                proxyList.append(line.strip())
if os.path.isfile("devicelist.txt"):
    randomDevice = True
    with open("devicelist.txt", "r", encoding="utf8") as devices:
        for line in devices:
            deviceList.append(line.strip())
while True:
    try:
        chrome_options = webdriver.ChromeOptions()
        if randomDevice:
            selectedDevice = random.choice(deviceList)
            mobileEmulation = {"deviceName": selectedDevice}
        else:
            mobileEmulation = {"deviceName": "Nexus 5"}
        chrome_options.add_experimental_option("mobileEmulation", mobileEmulation)
        if useProxy:
            selectedProxy = random.choice(proxyList)
            chrome_options.add_argument("--proxy-server=%s" % selectedProxy)
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--mute-audio")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(45)
        N = 13
        randemail = (
            "".join(random.choices(string.ascii_uppercase + string.digits, k=N))
        ) + "@gmail.com"
        randpass = "".join(random.choices(string.ascii_uppercase + string.digits, k=N))
        driver.get(linkPechincha)
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[4]/div/a").click()
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[1]/div/ul/li[1]"
        ).click()
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div[4]/div[1]/input"
        ).send_keys(randemail)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div[4]/div[2]/input"
        ).send_keys(randpass)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div[4]/div[5]/a"
        ).click()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/header/span/i").click()
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[4]/div/a").click()
        time.sleep(3)
        driver.find_element_by_xpath(
            "/html/body/div[3]/div/div[2]/div/div/div/span"
        ).click()
        resultado = float(
            driver.find_element_by_xpath(
                "/html/body/div/div/div[2]/div[3]/div[3]/div[1]/div[3]/div/div/div/div[2]/div/div/div"
            )
            .get_attribute("innerHTML")
            .replace("%", "")
        )
        hr = time.localtime()
        if resultado > resultadoAntigo:
            resultadoAntigo = resultado
            resultadoCount = 0
        if resultado == resultadoAntigo:
            resultadoCount += 1
        if resultadoCount == 5:
            print("Problema com o link:" + linkPechincha)
            print(
                "Possivelmente você não configurou proxy/dispositivo corretamente e sua pechincha foi bloqueada."
            )
            print("Aguarde o tempo zerar ou crie outra conta e tente novamente.")
            exit(0)
        print(
            str(hr.tm_hour)
            + ":"
            + str(hr.tm_min)
            + ":"
            + str(hr.tm_sec)
            + " "
            + linkPechincha
            + " Foi ajudado! Progresso atual: ",
            resultado,
        )
        driver.close()
        del driver
        del chrome_options
    except Exception as e:
        print(
            str(time.localtime().tm_hour)
            + ":"
            + str(time.localtime().tm_min)
            + ":"
            + str(time.localtime().tm_sec)
        )
        print(
            "Algo deu errado e uma ajuda não foi enviada! Link atual: " + linkPechincha
        )
        if useProxy:
            print("Proxy Atual: " + selectedProxy)
        if randomDevice:
            print("Dispositivo Atual: " + selectedDevice)
        print(
            "A conexão pode ter sido bloqueada ou algum outro erro pode ter ocorrido. Erro original:"
        )
        print(e)
        driver.close()
        del driver
        del chrome_options


# EEEEEð''ðððððððµµµµµµµµµµ³•ðððððððððððððððððððððððððððEEEEEEEEEððððð '
# EEEEEEE¨•ððððððµµµµµµµµµµ¨ððððððððððEðððððððððððððððððEEEEEEðððððððð''
# ðEEEEEEE µððððµµµµµµµµµµ¨ðððððððððððððððEEEEððððððððEEEEEEEEEðððððµµ''
# ðððEEEEEE¨•ðððµµµµµµµµµ'³ðððððððððEEEEEEEEEEEEEðEEEEEEEEEEEEEEEððððð•¨
# EEEEEEEEEE¨'ðµµµµµµµµµµ ððððððððððEEEEEEEEEEEEEEEEEEEEEEEEEEEEðµ•'³ððð
# EEEEEEEEEEE•¨µµµµµµµµµ¨³ðððððððððEEEEEEEEE•'³'EEEEEEEEEEEµ¨¨¨¨¨¨¨³µ¨EE
# EðEEEEEEEEððð µµµµµµµµ¨''•ðEðEEððEEEEEEð¨³³³³³•ðEEEEEµ¨¨¨¨¨¨'•••¨EE'³E
# EEEEEEEEEEðððð•¨µµµµµµ¨'³³³'ððEðEEEEðð'³³³³³³³'ððð¨¨¨¨¨¨ðEEEð•••••ðE ð
# ððððEEEEEEEððððð¨³µµµµ¨¨³³³³³'ðEEEEE¨³³³³³³³³³³¨¨¨¨¨³EEEEEEE³¨µµµµµE ¨
# ððððEEEEEEEððððððð¨³µµµ¨'³³³³³³•ððð¨³³³³³³³³¨¨¨¨³ððð¨EEEEEE¨¨¨¨ððððµ '
# ððEð¨¨µðEEEEEðððð¨³³'¨•µ ³³³³³³³¨ð'³³³³³³³¨¨¨•ðððEEEðµEEðµµ¨¨¨¨•ðððð¨'
# ððE¨³³³³'µEEEEEE•³³³³³³'¨¨³³³³³³³³'³³³³³³¨¨ðEEEEEEEEEE'µµðððE¨¨µEEE ³'
# EE•³³³³³³³³'ðððð¨³³³³³³³³³³³³³³³³³³³³³³³³³'EEEEEEEEEEEE³ðððEEEEEE''' '
# Eð'³³³³³³³³³³¨ðð³³³³³³³³³³³³³³³³³³³³³³³³³³¨EEEEEEEEEEEEEE'ðEEEµ¨''' ðð
# ð'³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³¨ðEEEEEEEEEEEEEE'³'''' 'µ¨'
# '³³'¨¨¨¨¨'³'¨¨³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³'¨¨•µµ'¨''''''''³³¨'¨³³³
# ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'³³³³³³³³³³³³³³³³³''''³'³³³³³³³³³³³³³³³³³³³³³³³³¨¨³³³³³
# ''''''''³³³³³³³³'¨'³³³³³³³'³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³'³³³³³³
# ''''''''''³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³
# µ³¨'''''³³³³³³³³³³³³³³³³³'¨•ððð''³³³³³³³³³³³³³'¨³³³³³³³³³³³³³³³³³³³³³³
# ¨•µµ'¨'''³³³³³³³³³³³³³³³³³³³'¨'³³³³³³³³³³³³³³³'¨³³³³³³³³³³³³³³³³³³³³³³
# ''''¨³µ''³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³¨'³³³³³³³³³³³³³³³³³³³³³³³
# ¨'''''''¨³'³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³¨ðð'³³³³³³³³³³³³³³³³³³³³³³³
# ³'³³³³³³³³³''³³³³³³³³³³³³³³'¨•¨••••••••••••''•'³³³³³³³³³³³³³³³³³³³³³³³
# ³³³³³³³³³³³³³³³³³³³³'¨  ¨¨³•••'•••••••µµ••••¨³³³³³³³³³³³³³³³³³³³³³³³³³
# ³³³³³³³³³³³³³³³³³³³³³³³³³'³••µ••••µµµµµµµ•••¨³³³³³³³³³³³³³³³³³³³³³³¨¨'
# ³³³³³³³³³³³³³³³³³³³³³³³³³³¨µµµµ•µµµµµµµµµµ••'³³³³³³³³³³³³³³³³'¨'''''''
# ³³³³³³³³³³³³³³³³³³³³³³³³³³³³µµµµµµµµµµµµµµµµ'³³³³³³³³³'¨'³³³'³³'''''''
