from selenium import webdriver
from selenium.webdriver.common.by import By

def HideMyName(O00OOO00O0O):
    O0OO00OO0O0 = webdriver.Chrome()
    O0OO000OO0O = 0
    for O0OO0O0OO0O in range(0, 6):
        if(O00OOO00O0O == 1):
            O0O00O0OO0O = "https://hidemy.name/tr/proxy-list/?type=h&start=0#list"
        if(O00OOO00O0O == 2):
            O0O00O0OO0O = "https://hidemy.name/tr/proxy-list/?type=s&start=0#list"
        if(O00OOO00O0O == 3):
            O0O00O0OO0O = "https://hidemy.name/tr/proxy-list/?type=4&start=0#list"
        if(O00OOO00O0O == 4):
            O0O00O0OO0O = "https://hidemy.name/tr/proxy-list/?type=5&start=0#list"
        
        O0O0OO0O00O = O0OO0O0OO0O * 64
        O0O0O00O0OO = O0O00O0OO0O.replace("0", str(O0O0OO0O00O))
        O0OO00OO0O0.get(O0O0O00O0OO)
        for OO0O0O00OO0 in range(1,65):
            try:
                OO0O0O0OOO0 = "tr[" + str(OO0O0O00OO0) + "]"
                O00O0O0OOO0 = "/html/body/div[1]/div[4]/div/div[4]/table/tbody/tr[1]/td[1]"
                O0OO0O0OOO0 = O00O0O0OOO0.replace("tr[1]", OO0O0O0OOO0)
                O0OO0O0O0O0 = O0OO00OO0O0.find_element(By.XPATH, value=O0OO0O0OOO0).text
                O00O0O0O0O0 = O0OO0O0OOO0.replace("td[1]", "td[2]")
                O00O0OOO0O0 = O0OO00OO0O0.find_element(By.XPATH, value=O00O0O0O0O0).text
                O00O0OOO000 = O0OO0O0O0O0 + ":" + O00O0OOO0O0
                if(O00OOO00O0O == 1):
                    open("./proxys/http.txt", "a").write(O00O0OOO000 + "\n")
                if(O00OOO00O0O == 2):
                    open("./proxys/https.txt", "a").write(O00O0OOO000 + "\n")
                if(O00OOO00O0O == 3):
                    open("./proxys/socks4.txt", "a").write(O00O0OOO000 + "\n")
                if(O00OOO00O0O == 4):
                    open("./proxys/socks5.txt", "a").write(O00O0OOO000 + "\n")
                O0OO000OO0O = O0OO000OO0O + 1
            except:
                break
    print(str(O0OO000OO0O) + " proxy saved in ./proxys folder")

