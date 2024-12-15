from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random
import string

# this is the session wide link
link = 'http://localhost:8000/join/rezozizu'

def build_driver():
    # Set up the driver
    return webdriver.Chrome() #(ChromeDriverManager().install())


def check_exists_by_xpath(driver, xpath):
    try:
        x = driver.find_element(By.XPATH, xpath)
        if x.is_displayed():
            return 1
    except NoSuchElementException:
        return 0

def welcome_page(driver):
    # Give input to the entry question - find the element by its id
    entry_question_id = 'id_entry_question'
    entry_question_input = 'Testing Input for Entry Question'
    driver.find_element(By.ID, entry_question_id).send_keys(entry_question_input)
    # eligible
    eligible = driver.find_elements(By.NAME, 'eligible_question')
    rand_selection = random.randint(0, len(eligible) - 1)
    eligible[rand_selection].click()
    # next button
    driver.find_element(By.XPATH, '//*[@id ="form"]/div/button').click()
    return rand_selection

def quota_page(driver):
    xpath = "//*[@id='id_age_question']"
    age = random.randint(16,99)
    driver.find_element(By.XPATH, xpath).send_keys(str(age))
    # gender field
    gender = driver.find_elements(By.NAME, 'gender')
    rand_selection = random.randint(0, len(gender) - 1)
    gender[rand_selection].click()
    # next
    driver.find_element(By.XPATH, '//*[@id ="form"]/div/button').click()


#def onlyOneGroup(driver):
    # Find the element by its tag
#    driver.find_element(By.TAG_NAME, 'button').click()

def survey_page(driver):  #self
    #if self.player.group_assignment == 0:
        # vision
    #    vision = driver.find_elements(By.NAME, 'vision')
    #    vision_random = random.randint(0, len(vision) - 1)
    #    vision[vision_random].click()
    #else:
    #    # rorschach
    #    rorschach_xpath = "//*[@id='id_rorschach_question']"
    #    rorschach_entry = "majom"
    #    driver.find_element(By.ID, rorschach_xpath).send_keys(rorschach_entry)
    # work
    work = driver.find_elements(By.NAME, 'work')
    work_random = random.randint(0, len(work) - 1)
    work[work_random].click()
    # music field
    music_xpath = "//*[@id='id_music_question']"
    music = random.randint(1,23)
    driver.find_element(By.XPATH, music_xpath).send_keys(str(music))
    # song field
    song_question_id = 'id_song_question'
    song_question_entry = "paint it black"
    driver.find_element(By.ID, song_question_id).send_keys(song_question_entry)
    # next button
    driver.find_element(By.XPATH, '//*[@id ="form"]/div/button').click()

def popout_page(driver):
    # two radio buttons
    yes = '//*[@id="bandYes"]'
    no = '//*[@id="bandNo"]'
    select = random.randint(0, 1)
    input_text = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(1, 10)))
    if select == 0:
        driver.find_element(By.XPATH, yes).click()
        # yes - why?
        driver.find_element(By.XPATH, '//*[@id="divYes"]/input').send_keys(input_text)
    else:
        driver.find_element(By.XPATH, no).click()
        # no - why not?
        driver.find_element(By.XPATH, '//*[@id="divNo"]/input').send_keys(input_text)
    # next button
    driver.find_element(By.XPATH, '//*[@id ="form"]/div/button').click()


def end_of_survey(driver):
    # submit button
    driver.find_element(By.XPATH, '//*[@id ="form"]/div/button').click()


def run_bots(no_times, link):
    driver = build_driver()  # initialize the driver
    for i in range(no_times):  # go through the survey several times
        driver.get(link)  # open the browser to the url of your survey
        # check if one can do th survey(e.g. if quota is full start page is not shown(in our case 20 participants)
        if check_exists_by_xpath(driver, "//*[@id='id_entry_question']") == 1:
            x = welcome_page(driver) # check whether they are eligible
            if x == 1:  # then they are not eligible, otherwise no next page
                continue
        quota_page(driver) # demo-page(age, gender etc)
        survey_page(driver)
#       # check if extra site is shown to you shown
        #if check_exists_by_xpath(driver, '//*[@id="form"]/div/h3') == 1:
        #    onlyOneGroup(driver)
        popout_page(driver)
        end_of_survey(driver)
    print("Success!")


run_bots(no_times=20, link=link)
