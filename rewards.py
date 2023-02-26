"""
Microsoft rewards search bot. Programmed by Emmanuel Azadze on 02/11/2023 (Sat)
"""
import os, sys, time, random, copy, string, re, threading
from datetime import datetime as dt, timedelta as td
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from __init__ import *

#################################################################################################################################################
#                                                         Environment Variables                                                                 #
#################################################################################################################################################
logger = getlogger()
CHARLIST = string.ascii_lowercase                                           # used to generate random words
POINTSPERSEARCH = 5                                                         # points per Bing search
TIMEPERSEARCH= 14.4                                                         # seconds per Bing search

def main(delay: int = 30, futurebool: bool = False, bonus: int = 0, wait2exit: int = 15, browser_agent = 'edge', max_random_time: int = 10, test: int = 0, loglevel: str = LOGLEVEL, shuffle: bool = True):
    """
    Main fun. User agent = 0 for desktop computer, 1 for android mobile user agent.
    """
    logger.setLevel(loglevelconverter(loglevel))
    if bool(int(futurebool)):
        sleepbeforesearch = timetill(max_random_time = max_random_time*60)
    else:
        sleepbeforesearch = delay
    timer(sleepbeforesearch)
    num1, num2 = scorecounter()
    searchbots(delay = 15, futurebool = False, num1 = num1, num2 = num2, bonus = bonus, browser_agent = browser_agent, wait2exit = wait2exit, max_random_time = max_random_time, test = test, loglevel = loglevel, shuffle = shuffle)

def searchbot(words: int, wait: int = 10, browser_agent: str = 'edge', user_agent: int = 0, wait_very_slow: int = 10, wait_slow: int = 7, wait_default: int = 5, wait_fast: int = 3, wait_very_fast: int = 1, test: int = 0, loglevel: str = LOGLEVEL, link: str = 'https://www.bing.com/'):
    """
    Bing rewards search bot. Opens a web browser driver and searches on Bing to get Bing rewards points.
    """
    logger.setLevel(loglevelconverter(loglevel))
    if not type(words) == []:
        words = wordsgen(int(words))
    logger.debug(f'wait_very_slow: {wait_very_slow}, wait_slow: {wait_slow}, wait_default: {wait_default}, wait_fast: {wait_fast}, wait_very_fast: {wait_very_fast}, test: {test}')
    logger.debug(f'Applying settings: wait: {wait} seconds, user_agent: {user_agent}, browser_agent: {browser_agent}')
    logger.info(f'Searching {len(words)} words:\n{words}')
    logger.debug(f'Initializing WebBrowser class')
    WebBrowser.init()                                                       # initialize WebBrowser class
    browser = WebBrowser(browser_agent)
    
    if not bool(int(test)):
        logger.debug(f'No test flag detected. This is a real search.')
        if int(user_agent) == 1:
            try:
                driver = browser.Browser(service = browser.service, options = browser.options_mob)
                logger.debug(f'driver = {browser.browser_agent}, service = browser.service, options = browser.options_mob')
                logger.info(f'User agent change successful. User agent has been set to mobile')
            except:
                driver = browser.Browser(service = browser.service, options = browser.options)
                logger.debug(f'driver = {browser.browser_agent}, service = browser.service, options = browser.options')
                logger.info(f'User agent change was not successful. User agent has been set to default desktop')
        else:
            driver = browser.Browser(service = browser.service, options = browser.options)
            logger.debug(f'driver = {browser.browser_agent}, service = browser.service, options = browser.options')
            logger.info(f'No user change requested. User agent has been set to default desktop')
        
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        logger.debug(f'driver.execute_script("Object.defineProperty(navigator, \'webdriver\', get: () => undefined)")')
        # driver.maximize_window()
        driver.get(link)
        logger.info(f'Obtaining website: "{link}"')
        assert "Bing" in driver.title
        logger.debug('Asserting "Bing" in driver.title')
        
        try:
            sleepbeforesearch = int(new_num_fun(wait))
        except ValueError:
            sleepbeforesearch = int(new_num_fun(wait_very_slow))
            
        logger.info(f'Sleeping for {time.strftime("%H hours, %M minutes, and %S seconds", time.gmtime(sleepbeforesearch))} before starting search')
        time.sleep(sleepbeforesearch)
        
        for j, word in enumerate(words):
            element = driver.find_element(browser.By.NAME, "q")
            logger.debug('Finding search bar')
            time.sleep(wait_very_fast)
            element.clear()
            logger.debug('Clearing contents in search bar')
            time.sleep(wait_very_fast)
            element.send_keys(word)
            logger.debug(f'Sending word {j+1} of {len(words)}: "{word}")')
            time.sleep(wait_default)
            element.send_keys(browser.Keys.RETURN)
            logger.debug(f'Sending enter key')
            # assert "No results found." not in driver.page_source
            time.sleep(new_num_fun(wait_default))
        logger.info('Search complete. Closing webdriver')
        driver.close()
    else:
        if int(test) == 1:
            logger.info('Testing detected! Running with timer on')
        else:
            logger.info('Testing detected! Running with timer off')
        
        if int(user_agent) == 1:
            try:
                logger.debug(f'driver = {browser.browser_agent}, service = browser.service, options = browser.options_mob')
                logger.info(f'User agent change successful. User agent has been set to mobile.')
            except:
                logger.debug(f'driver = {browser.browser_agent}, service = browser.service, options = browser.options')
                logger.info(f'User agent change was not successful. User agent has been set to default desktop.')
        else:
            logger.debug(f'driver = {browser.browser_agent}, service = browser.service, options = browser.options')
            logger.info(f'No user change requested. User agent has been set to default desktop.')
        
        logger.info(f'Obtaining website: "{link}")')
        logger.debug('Asserting "Bing" in driver.title')
        
        try:
            if int(test) == 1:
                time.sleep(new_num_fun(wait))
        except:
            if int(test) == 1:
                time.sleep(new_num_fun(wait_very_slow))
        
        for j, word in enumerate(words):
            logger.debug('Finding search bar')
            if int(test) == 1:
                time.sleep(wait_very_fast)
            logger.debug('Clearing contents in search bar')
            if int(test) == 1:
                time.sleep(wait_very_fast)
            logger.debug(f'Sending word {j+1} of {len(words)}: "{word}"')
            if int(test) == 1:
                time.sleep(wait_default)
            logger.debug('Sending enter key')
            if int(test) == 1:
                time.sleep(new_num_fun(wait_default))
        logger.info('Search complete. Closing webdriver')

def searchbots(delay: int = 0, futurebool: bool = False, num1: int = 30, num2: int = 20, bonus: int = 0, wait2exit: int = 15, test: int = 0, max_random_time: int = 60, browser_agent: str = 'edge', loglevel: str = LOGLEVEL, shuffle: bool = True):
    """
    Runs more than one instance of search bot at a time.
    """
    logger.setLevel(loglevelconverter(loglevel))
    logger.debug(f'delay: {delay}, futurebool: {futurebool}, wait2exit: {wait2exit}, shuffle: {shuffle}')
    logger.debug(f'Initiating 2 instances of seachbot')
    
    if bool(int(futurebool)):
        timedelta = timetill(hours = 8, minutes = 1, seconds = 0, utcbool = True, max_random_time = max_random_time*60)
    else:
        timedelta = int(delay + wait2exit)
    
    kwargs1 = {'wait': timedelta, 'words': num1, 'browser_agent': browser_agent, 'user_agent': 0, 'test': test, 'loglevel': loglevel}
    kwargs2 = {'wait': timedelta, 'words': num2, 'browser_agent': browser_agent, 'user_agent': 1, 'test': test, 'loglevel': loglevel}
    kwargs = [kwargs1, kwargs2]
    
    if bool(int(shuffle)):
        random.shuffle(kwargs)
    
    for k, kwarg in enumerate(kwargs):
        if k == 0:
            kwarg['words'] = int(kwarg['words'] + bonus)
        else:
            kwarg['wait'] = int(kwarg['wait'] + kwargs[k-1]['words']*TIMEPERSEARCH)
    
    jobs = [threading.Thread(target = searchbot, kwargs = kwarg) for kwarg in kwargs]
    logger.info(f'Starting {len(jobs)} searchbots for today')
    logger.debug(f'Kwargs: {kwargs}')
    
    for job in jobs:
        job.start()
        time.sleep(new_num_fun(10))
    
    for job in jobs:
        job.join()
    
    logger.info(f'Searchbots complete. Have a nice day. :)')
    
def wordgen(word_length: int = 6, char_list = CHARLIST) -> [str]:
    """
    Random word generator. Returns a random word of specified length.
    """
    word = ''
    for j in range(word_length):
        word += random.choice(char_list)
    
    return word

def wordsgen(word_count: int = 30, word_length: int = 6, loglevel: str = LOGLEVEL) -> [str]:
    """
    Random words generator. Distribution is normal meaning outcomes are on a Gaussian probability curve.
    """
    logger.setLevel(loglevelconverter(loglevel))
    words = []; all_words = []
    len_all_words = int(1.2*word_count + 1)
    
    for k in range(len_all_words):
        word = wordgen(word_length = new_num_fun(word_length))
        all_words.append(word)
    
    for k in range(word_count):
        word = all_words.pop()
        if word not in all_words:
            words.append(word)
    logger.debug(f'Words: {words}')
    return words

def new_num_fun(num: int, mu: int = 0, sigma: float = 0.65, abs_bool: bool = False) -> int:
    """
    Adds random noise to a number using normal distribution and returns the new number.
    """
    if abs_bool:
        new_num = abs(round(num + random.normalvariate(mu,sigma)))
    else:
        new_num = round(num + random.normalvariate(mu,sigma))
    
    return new_num
    
def scorecounter(browser_agent: str = 'edge', link: str = 'https://rewards.bing.com/pointsbreakdown', pointspersearch: int = POINTSPERSEARCH, wait: int = 7) -> [int]:
    """
    Returns number of searches left to be searched for search points on desktop and mobile.
    """
    WebBrowser.init()
    browser = WebBrowser(browser_agent)
    driver = browser.Browser(service = browser.service, options = browser.options)
    driver.get(link)
    time.sleep(int(wait))
    searches = []
    
    for k, element in enumerate(driver.find_elements(browser.By.CLASS_NAME, 'circleContainer.medium')):
        title = element.get_dom_attribute('title')
        if 'points' in title and '/' in title:
            amount, total = [intisolator(item) for item in title.split('/')]
            searches.append(int((total - amount) / POINTSPERSEARCH))
        
    return searches

class WebBrowser:
    """
    Web browser class to store web browser driver, options, methods, and keys.
    """
    @classmethod
    def init(cls):
        """
        Common properties or resources
        """
        cls.webdriver = webdriver
        cls.Keys = Keys
        cls.By = By
    
    def __init__(self, browser_agent: str = 'edge', use_profile: bool = False):
        """
        Instance init method
        """
        if 'chrome' in browser_agent.lower():
            from selenium.webdriver import Chrome as Browser
            from selenium.webdriver.chrome.options import Options
            from selenium.webdriver.chrome.service import Service
            
            self.exe_path = CHROMEEXEPATH
            self.profile = CHROMEPROFILE
            self.arg_mob = f'user-agent={"Mozilla/5.0 (Linux; Android 12.1.0; Pixel Build/OPM4.171019.021.D1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36 EdgA/42.0.0.2057"}'
            self.arg_bot = '--disable-blink-features=AutomationControlled'
            self.arg_log = '--log-level=3'
            self.options = Options()
            self.service = Service()
            self.options.add_argument(self.arg_bot)
            self.options.add_argument(self.arg_log)
            self.options.add_experimental_option('useAutomationExtension', False)
            self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
            # self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
            
            self.browser_agent = 'Chrome'
        
        elif 'firefox' in browser_agent.lower():
            from selenium.webdriver import Firefox as Browser
            from selenium.webdriver.firefox.options import Options
            from selenium.webdriver.firefox.service import Service
            
            self.exe_path = FIREFOXEXEPATH
            self.profile = FIREFOXPROFILE
            self.arg_mob = f'user-agent={"Mozilla/5.0 (Linux; Android 12.1.0; Pixel Build/OPM4.171019.021.D1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36 EdgA/42.0.0.2057"}'
            self.arg_bot = '--disable-blink-features=AutomationControlled'
            self.arg_log = '--log-level=3'
            self.options = Options()
            self.service = Service()
            self.options.add_argument(self.arg_bot)
            self.options.add_argument(self.arg_log)
            
            self.browser_agent = 'Firefox'
        
        elif 'safari' in browser_agent.lower():
            from selenium.webdriver import Safari as Browser
            from selenium.webdriver.safari.options import Options
            from selenium.webdriver.safari.service import Service
            
            self.exe_path = SAFARIEXEPATH
            self.profile = SAFARIPROFILE
            self.arg_mob = f'user-agent={"Mozilla/5.0 (Linux; Android 12.1.0; Pixel Build/OPM4.171019.021.D1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36 EdgA/42.0.0.2057"}'
            self.arg_bot = '--disable-blink-features=AutomationControlled'
            self.arg_log = '--log-level=3'
            self.options = Options()
            self.service = Service()
            self.options.add_argument(self.arg_bot)
            self.options.add_argument(self.arg_log)
            
            self.browser_agent = 'Safari'
        
        else:
            from selenium.webdriver import Edge as Browser
            from selenium.webdriver.edge.options import Options
            from selenium.webdriver.edge.service import Service
            
            self.exe_path = MSEDGEEXEPATH
            self.profile = MSEDGEPROFILE
            self.arg_mob = f'user-agent={"Mozilla/5.0 (Linux; Android 12.1.0; Pixel Build/OPM4.171019.021.D1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36 EdgA/42.0.0.2057"}'
            self.arg_bot = '--disable-blink-features=AutomationControlled'
            self.arg_log = '--log-level=3'
            self.options = Options()
            self.service = Service()
            self.options.add_argument(self.arg_bot)
            self.options.add_argument(self.arg_log)
            self.options.add_experimental_option('useAutomationExtension', False)
            self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
            # self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
            
            self.browser_agent = 'Edge'
        
        if bool(int(use_profile)):
            self.options.add_argument(f'user-data-dir={self.profile}')
        
        self.options_mob = copy.deepcopy(self.options)
        self.options_mob.add_argument(self.arg_mob)
        self.Browser = Browser
        self.Options = Options
        self.Service = Service
        
        """
        # for future functionality
        url = driver.command_executor._url       #"http://127.0.0.1:60622/hub"
        session_id = driver.session_id            #'4e167f26-dc1d-4f51-a207-f761eaf73c31'
        driver = webdriver.Remote(command_executor=url,desired_capabilities={})
        driver.close()   # this prevents the dummy browser
        driver.session_id = session_id
        """

if __name__=='__main__':
    main()