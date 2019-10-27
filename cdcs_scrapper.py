from selenium import webdriver
import time
import json

url = 'https://cdcs.ur.rochester.edu/'

option = webdriver.ChromeOptions()
option.add_argument(' - incognito')
browser = webdriver.Chrome(
    executable_path='/Users/dle8/Desktop/Course-Recommendation-Engine/chromedriver',
    options=option
)
browser.get('https://cdcs.ur.rochester.edu/')

num_term = len(browser.find_element_by_id('ddlTerm').find_elements_by_tag_name('option'))

# <span id="rpResults_ctl01_lblCNum">AME 141</span>
# <span id="rpResults_ctl01_lblTitle">Fundamentals of Digital Audio</span>
# <span id="rpResults_ctl01_lblTerm">Spring 2020</span>
# <span id="rpResults_ctl01_lblCredits">  4.0</span>
# <span id="rpResults_ctl01_lblDesc">This course covers the fundamentals of manipulating and encoding sound in a digital format. Mathematical representations of digital signals are introduced and the effects of simple filters are analyzed in the context of audio. This course further provides students with an introduction to programming in Matlab through a series of assignments exploring sound synthesis algorithms and audio effects processing.</span>
# < span id = "rpResults_ctl03_lblClusters" > N4AME001 < / span >
# <span id="rpResults_ctl05_lblRestrictions">[A] Instructor's permission required</span>
# <span id="rpResults_ctl05_lblPrerequisites">Not open to First Year students</span>

data = {}


def return_one_elem(arr):
    if len(arr) > 0:
        return arr[0].text
    return ""


with open('courses_fall.json', 'w') as outfile:
    for k in range(2, 3):
        terms = browser.find_element_by_id('ddlTerm').find_elements_by_tag_name('option')
        term = terms[k]
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
                # print(subject.text)
                subject.click()

                main_course = browser.find_element_by_id('ddlTypes').find_elements_by_tag_name('option')
                main_course[1].click()

                search = browser.find_element_by_id('btnSubmit')
                search.click()

                time.sleep(3)

                prev = 0

                for course_id in range(10000):
                    course = {}
                    id = str(course_id)
                    if course_id < 10:
                        id = "0" + id
                    code = browser.find_elements_by_id("rpResults_ctl{}_lblCNum".format(id))
                    code = return_one_elem(code)
                    if code == "":
                        if course_id - prev > 2:
                            break
                        else:
                            continue
                    prev = course_id
                    course['code'] = code
                    name = browser.find_elements_by_id("rpResults_ctl{}_lblTitle".format(id))
                    course['name'] = return_one_elem(name)
                    teaching_period = browser.find_elements_by_id("rpResults_ctl{}_lblOffered".format(id))
                    course['teaching_period'] = return_one_elem(teaching_period)
                    credit_points = browser.find_elements_by_id("rpResults_ctl{}_lblCredits".format(id))
                    course['credit_points'] = return_one_elem(credit_points)
                    clusters = browser.find_elements_by_id("rpResults_ctl{}_lblClusters".format(id))
                    course['clusters'] = return_one_elem(clusters)
                    course_restrictions = browser.find_elements_by_id("rpResults_ctl{}_lblRestrictions".format(id))
                    course['course_restrictions'] = return_one_elem(course_restrictions)
                    prereq = browser.find_elements_by_id("rpResults_ctl{}_lblPrerequisites".format(id))
                    course['prereq'] = return_one_elem(prereq)
                    description = browser.find_elements_by_id("rpResults_ctl{}_lblDesc".format(id))
                    course['description'] = return_one_elem(description)
                    if code not in data:
                        data[code] = []
                    data[code].append(course)

    json.dump(data, outfile)
    outfile.close()

browser.close()
