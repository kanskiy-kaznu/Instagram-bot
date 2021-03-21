from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
from selenium.webdriver.chrome.options import Options


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

# driver = webdriver.Chrome()


driver.get('https://www.instagram.com/')

print("Вы успешно вошли на сайт")

sleep(5)
login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')

login.send_keys('login')

password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

password.send_keys('password')



sleep(5)
login_input = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')


login_input.send_keys(Keys.RETURN)

sleep(10)

print("Вы авторизовались")


oshibka = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
oshibka.send_keys(Keys.RETURN)

search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')

search.send_keys('#взаимныеподписки')
search.send_keys(Keys.ENTER)

sleep(10)


# next_image = driver.find_element_by_xpath('//a[@class="_65Bje  coreSpriteRightPaginationArrow"]').click()

# next_image.send_keys(Keys.RETURN)



search_one = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
search_one.send_keys(Keys.ENTER)

print("Удачно вошли по хэштегу")

sleep(15)


pictures = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a')

pictures.send_keys(Keys.RETURN)

# pictures = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a')

sleep(15)

# next_image = driver.find_element_by_xpath('//a[@class=" _65Bje  coreSpriteRightPaginationArrow"]').click()
for vertical in range(1, 17):
    for gorizontal in range(1, 4):
        pictures = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div/div[' + str(vertical) + ']/div[' + str(gorizontal) + ']/a')


        pictures.send_keys(Keys.RETURN)

        sleep(50)

        like = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')

        like.send_keys(Keys.RETURN)

        sleep(50)

        following = driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')

        following.send_keys(Keys.RETURN)

        sleep(50)

        exit = driver.find_element_by_xpath(
            '/html/body/div[4]/div[3]/button'
        )

        exit.send_keys(Keys.RETURN)

        sleep(50)

    print(vertical * 3)

print('Функция окончена')


driver.close()






