# imports
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import json



class LinkedinWebScrape():
    name_final = ''
    experience_final = []
    education_final = []
    volunteer_final = []
    certificate_final = []
    course_final = []
    skills_final = []
    driver = ''



    def __init__(self, driver_location, username, password):
        self.driver_location = driver_location
        self.username = username
        self.password = password

    # returns the beautifulsoup html parsed instance
    def login(self):
        global driver
        driver = webdriver.Chrome(self.driver_location)

        # driver.get method() will navigate to a page given by the URL address
        driver.get('https://www.linkedin.com/checkpoint/rm/sign-in-another-account?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

        # locate email form by_class_name
        username = driver.find_element_by_name('session_key')

        # send_keys() to simulate key strokes
        username.send_keys(self.username)

        # sleep for 0.5 seconds
        sleep(0.5)

        # locate password form by_class_name
        password = driver.find_element_by_name('session_password')

        # send_keys() to simulate key strokes
        password.send_keys(self.password)
        sleep(0.5)

        # locate submit button by_xpath
        sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

        # .click() to mimic button click
        sign_in_button.click()
        sleep(1)
        try:
            not_now_button = driver.find_element_by_class_name('btn__secondary--large-muted')
            not_now_button.click()
            sleep(1)
        except:
            pass

    def load_html(self,url):
        global driver
        global name_final
        global experience_final
        global education_final
        global certificate_final
        global volunteer_final
        global course_final
        global skills_final
        name_final = ''
        experience_final = []
        education_final = []
        certificate_final = []
        volunteer_final = []
        course_final = []
        skills_final = []
        driver.get(url)
        scroll = driver.find_element_by_tag_name('html')
        scroll.send_keys(Keys.END)
        sleep(1)
        scroll.send_keys(Keys.PAGE_UP)
        sleep(1)
        scroll.send_keys(Keys.PAGE_UP)
        sleep(1)
        try:
            skills_show_more = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div/div[6]/div/section/div[2]/button')
            ActionChains(driver).move_to_element(skills_show_more).perform()
            sleep(0.5)
            skills_show_more.click()
        except:
            pass
        sleep(1)
        html = driver.page_source

        soup = bs(html, 'html.parser')

        return soup

    def get_courses(self):
        global course_final
        return course_final

    def get_skills(self):
        global skills_final
        return skills_final

    def get_experiences(self):
        global experience_final
        return experience_final

    def get_educations(self):
        global education_final
        return education_final

    def get_certifications(self):
        global certificate_final
        return certificate_final

    def get_volunteering(self):
        global volunteer_final
        return volunteer_final

    def get_name(self):
        global name_final
        return name_final


    def scrape_name(self, soup):
        global name_final
        # Grabs Name Information
        name = soup.find(lambda tag: tag.name == 'h1' and tag.has_attr('class'))
        name_final = name.get_text().strip()

    def scrape_experience(self, soup):
        global experience_final
        # Grabs Experience Information
        experience_list = soup.find_all(lambda tag: tag.name == 'section' and tag.has_attr('class') and tag['class'][0] == 'pv-profile-section__card-item-v2' and
                                                    tag['class'][1] == 'pv-profile-section' and tag['class'][2] == 'pv-position-entity' and tag['class'][3] == 'ember-view')
        for experience in experience_list:
            try:
                role = experience.find(lambda tag: tag.name == 'h3' and tag.has_attr('class') and tag['class'][0] == 't-16' and
                                                        tag['class'][1] == 't-black' and tag['class'][2] == 't-bold')
            except:
                role = ''
                pass
            try:
                company_name = experience.find(lambda tag: tag.name == 'p' and tag.has_attr('class') and tag['class'][0] == 'pv-entity__secondary-title'
                                                            and tag['class'][1] == 't-14' and tag['class'][2] == 't-black' and
                                                            tag['class'][3] == 't-normal')
            except:
                company_name = ''
                pass
            try:
                description = experience.find(lambda tag: tag.name == 'div' and tag.has_attr('class') and tag['class'][0] == 'inline-show-more-text')
            except:
                description = ''
                pass
            try:
                experience_final.append({'Role': role.get_text().strip(),'Company Name': company_name.get_text().strip(), 'Description': description.get_text().strip()})
            except:
                pass

    def scrape_education(self, soup):
        global education_final

        # Grabs Education Information
        education_list = soup.find_all(lambda tag: tag.name == 'li' and tag.has_attr('class') and tag['class'][0] == 'pv-profile-section__list-item'
                                                   and tag['class'][1] == 'pv-education-entity' and tag['class'][2] == 'pv-profile-section__card-item' and tag['class'][3] == 'ember-view')
        for education in education_list:
            education_name = education.find(lambda tag: tag.name == 'h3' and tag.has_attr('class') and tag['class'][0] == 'pv-entity__school-name')
            education_level = education.find(lambda tag: tag.name == 'span' and tag.has_attr('class') and tag['class'][0] == 'pv-entity__comma-item')
            try:
                education_description = education.find(lambda tag: tag.name == 'p' and tag.has_attr('class') and tag['class'][0] == 'pv-entity__description')
            except:
                education_description = education.find(lambda tag: tag.name == 'span' and tag.has_attr('class') and tag['class'][0] == 'activities-societies')
                pass
            try:
                education_final.append({'Education Name': education_name.get_text().strip(),
                                        'Education Level': education_level.get_text().strip(),
                                        'Education Description': education_description.get_text().strip()})
            except AttributeError:
                education_final.append({'Education Name': education_name.get_text().strip(),
                                        'Education Level': education_level.get_text().strip(),
                                        'Education Description': ''})

    def scrape_certificate(self, soup):
        global certificate_final
        # Grabs Certificate Information
        certificate_list = soup.find_all(lambda tag: tag.name == 'div' and tag.has_attr('class') and tag['class'][0] == 'pv-profile-section__card-item')

        for certificate in certificate_list:
            certificate_name = certificate.find(lambda tag: tag.name == 'h3' and tag.has_attr('class') and tag['class'][0] == 't-16' and tag['class'][1] == 't-bold')
            certificate_info = certificate.find_all(lambda tag: tag.name == 'span' and not(tag.has_attr('class')))
            certification_issuer = certificate_info[0].get_text().strip()
            try:
                certificate_id = certificate_info[2].get_text().strip()
            except:
                certificate_id = ''
                pass
            certificate_final.append({'Certificate Name': certificate_name.get_text(), 'Certification Issuer': certification_issuer, 'Certificate ID': certificate_id})

    def scrape_volunteer(self,soup):
        global volunteer_final
        # Grabs Volunteer Information
        volunteer_list = soup.find_all(lambda tag: tag.name == 'li' and tag.has_attr('class') and tag['class'][0] == 'pv-profile-section__list-item'
                                                   and tag['class'][1] == 'pv-volunteering-entity')
        for volunteer in volunteer_list:
            volunteer_role = volunteer.find(lambda tag: tag.name == 'h3' and tag.has_attr('class') and tag['class'][0] == 't-16' and tag['class'][1] == 't-black' and tag['class'][2] == 't-bold')
            volunteer_organization = volunteer.find(lambda tag: tag.name == 'span' and tag.has_attr('class') and tag['class'][0] == 'pv-entity__secondary-title')
            volunteer_cause = volunteer.find(lambda tag: tag.name == 'span' and tag.has_attr('class') and tag['class'][0] == 'pv-volunteer-causes')
            volunteer_final.append({'Volunteer Role': volunteer_role.get_text(),'Volunteer Cause': volunteer_cause.get_text(),'Volunteer Organization': volunteer_organization.get_text()})

    def scrape_course(self,soup):
        global course_final
        # Grabs Course Information
        course_list = soup.find_all(lambda tag: tag.name == 'li' and tag.has_attr('class') and tag['class'][0] == 'pv-accomplishments-block__summary-list-item')
        for course in course_list:
            course_final.append({'Course Name': course.get_text()})

    def scrape_skills(self,soup):
        global skills_final
        skills_list = soup.find_all(lambda tag: tag.name == 'span' and tag.has_attr('class') and tag['class'][0] == 'pv-skill-category-entity__name-text')
        for skill in skills_list:
            skills_final.append({'Skill Name:': skill.get_text().strip()})

    def file_save(self):
        global name_final
        global experience_final
        global education_final
        global certificate_final
        global volunteer_final
        global course_final
        global skills_final
        out_file = open("data.json", "w")
        output = {
            name_final: {
                "Experience": experience_final,
                "Education": education_final,
                "Certifications": certificate_final,
                "Volunteer": volunteer_final,
                "Courses": course_final,
                "Skills": skills_final
            }
        }
        json.dump(output, out_file, indent = 6)
        out_file.close()
