from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import sys

url = 'https://cdcs.ur.rochester.edu/'

option = webdriver.ChromeOptions()
option.add_argument(' - incognito')
browser = webdriver.Chrome(
    executable_path='/home/dylan/Desktop/Github Repos/Course-Recommendation-Engine/chromedriver_linux64/chromedriver',
    options=option
)
browser.get('https://cdcs.ur.rochester.edu/')

terms = browser.find_element_by_id('ddlTerm').find_elements_by_tag_name('option')

# try:
for term in terms[1:]:
    term.click()

    num_school = len(browser.find_element_by_id('ddlSchool').find_elements_by_tag_name('option'))
    for i in range(1, num_school):
        schools = browser.find_element_by_id('ddlSchool').find_elements_by_tag_name('option')
        school = schools[i]
        school.click()
        # wait = WebDriverWait(browser, 3)
        # wait.until(EC.element_to_be_clickable((By.ID, 'ddlDept')))
        time.sleep(3)

        num_subject = len(browser.find_element_by_id('ddlDept').find_elements_by_tag_name('option'))
        for j in range(1, num_subject):
            subjects = browser.find_element_by_id('ddlDept').find_elements_by_tag_name('option')
            subject = subjects[j]
            print(subject.text)
            subject.click()

            search = browser.find_element_by_id('btnSubmit')
            search.click()

            time.sleep(3)
            courses = browser.find_elements_by_xpath('//*[@id="UpdatePanel4"]/table/tbody/tr/td[3]/table')
            for course in courses:
                rows = course.find_elements_by_xpath('.//tbody/tr')
                for row in rows:
                    cells = row.find_elements_by_xpath('.//td')
                    for cell in cells:
                        if isinstance(cell.text, str) and cell.text != "":
                            print(cell.text.strip())
                print('-------------')
            browser.close()
            sys.exit(0)
# except Exception as e:

#     print(e)
browser.close()
