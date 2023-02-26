"""
Microsoft rewards search bot. Programmed by Quantum Emman on 02/11/2023 (Sat)
"""
import time, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

def main(wait: int = 5, num_words: int = 15, user_agent: int = 0):
    """
    Main fun. User agent = 0 for desktop computer, 1 for android mobile user agent
    """
    words = wordsgen(int(num_words))
    print(">> Using {} words for today. The words are:\n{}".format(num_words, words))
    print(">> Applying settings: wait: {} seconds, user_agent: {}. Opening and running search bot...".format(wait, user_agent))
    searchbot(words = words, wait = wait, user_agent = user_agent)
    print(">> Search completed successfully. You can sleep now.")

def new_num_fun(num: int, mu: int = 0, sigma: float = 0.65) -> int:
    """
    Adds random noise to a number using normal distribution and returns the new number.
    """
    return max(1, num + round(random.normalvariate(mu,sigma)))

def wordsgen(num_words: int = 35, word_length: int = 6, mu: int = 0, sigma: float = 0.65) -> [str]:
    """
    Random words generator. Distribution is normal.
    """
    words = []
    char_list = 'abcdefghijklmnopqrstuvwxyz'
    new_num_words = new_num_fun(num = num_words, mu = mu, sigma = sigma)
    
    for k in range(new_num_words):
        word = ''
        new_word_length = new_num_fun(word_length, mu = mu, sigma = sigma)
        for j in range(new_word_length):
            word += random.choice(char_list)
        words.append(word)
    # print(words)
    return words

def searchbot(words: [str], wait: int = 5, user_agent: int = 0, mu: int = 0, sigma: float = 0.65, wait_slow = 10, wait_default = 5, wait_fast = 3, wait_very_fast = 1):
    """
    Bing rewards search bot.
    """
    if int(user_agent) == 1:
        try:
            args = f'user-agent={"Mozilla/5.0 (Linux; Android 8.1.0; Pixel Build/OPM4.171019.021.D1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36 EdgA/42.0.0.2057"}'
            options = Options()
            options.add_argument(args)
            driver = webdriver.Edge(options = options)
            print(">> User agent change successful. User agent has been set to mobile.")
        except:
            driver = webdriver.Edge()
            print(">> User agent change was not successful. User agent has been set to default desktop.")
    else:
        driver = webdriver.Edge()
        print(">> No user change requested. User agent has been set to default desktop.")
    # driver.maximize_window()
    driver.get("https://www.bing.com/")
    
    assert "Bing" in driver.title
    try:
        time.sleep(new_num_fun(wait))
    except:
        time.sleep(new_num_fun(wait_slow))
    for word in words:
        elem = driver.find_element(By.NAME, "q")
        time.sleep(wait_very_fast)
        elem.clear()
        time.sleep(wait_fast)
        elem.send_keys(word)
        time.sleep(wait_fast)
        elem.send_keys(Keys.RETURN)
        # assert "No results found." not in driver.page_source
        time.sleep(new_num_fun(wait_default))
    driver.close()
   
if __name__=='__main__':
    main()