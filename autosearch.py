class autosearch:   
    def search(find):
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from webdriver_manager.chrome import ChromeDriverManager
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://lite.duckduckgo.com/lite/')
        search_bar = driver.find_element_by_xpath('//*[@id="lite_wrapper"]/form/input[1]')
        search_bar.send_keys(find + ' site:eldenring.wiki.fextralife.com')
        search_bar.send_keys(Keys.RETURN)
        results = driver.find_element_by_xpath('/html/body/form/div/table[3]/tbody/tr[1]/td[2]/a')  # finds webresults
        results.click()
        link = driver.current_url
        return link


    