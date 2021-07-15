# LinkedinWebScrape
This is a script used to scrape the information from a LinkedIn profile using a provided account and using selenium

## Table of Contents
* [General info](#general-information)
* [Technologies](#technologies)
* [Setup](#setup)
* [Example of Usage](#example-of-usage)

## General Information
The aim of this project is to be able to quickly grab data from a LinkedIn profile and export it in a json format to
train machine learning models on the information provided.

## Technologies
Project is created with:
- Python 3.8
- Selenium
- BeautifulSoup

## Setup
To run this script simply download the repo, load it into an IDE of your choice and click run, or run the `LinkedinAPI.py` file
from your command line using `Python 3.8`
    
### Example of Usage

```
temp = LinkedinWebScrape('C:/Users/temp/Desktop/chromedriver.exe','temp@gmail.com','password')

temp.login()
soup = temp.load_html('https://www.linkedin.com/in/temp/')
temp.scrape_skills(soup)
temp.scrape_course(soup)
temp.scrape_name(soup)
temp.scrape_certificate(soup)
temp.scrape_volunteer(soup)
temp.scrape_education(soup)
temp.scrape_experience(soup)
temp.file_save()
```
The JSON output from this file will look like the following
```
{
      "Temp": {
            "Experience": [
                  {
                        "Role": "Quality Assurance Automation Engineer",
                        "Company Name": "Ztech studios",
                        "Description": "Working on the automation of the cloud based web application for AWS. AutomatedIntegration/API testing using POSTMAN, Unit level automated testing usingMocha/Chai and Front-end/Browser automated testing with selenium webdriver. Myfocus is towards automating the testing of cloud based web application\n  \n      \n\u2026\n\n          see more"
                  },
                  {
                        "Role": "Intern",
                        "Company Name": "QUEST, Software Quality Engineering & Testing Laboratory",
                        "Description": "Worked on Selenium, which is a suite of tools to automate web browsers across many platforms. I updated the functionality of the Selenium IDE by running the multiple scripts automatically from a java based tool. This tools generate the important test data for the test scripts and executes the scripts via selenium IDE.\n  \n      \n\u2026\n\n          see more"
                  }
            ],
            "Education": [
                  {
                        "Education Name": "Queen's University",
                        "Education Level": "Doctor of Philosophy - PhD",
                        "Education Description": ""
                  },
                  {
                        "Education Name": "National University of Computer and Emerging Sciences",
                        "Education Level": "Master's degree",
                        "Education Description": "Bronze Medalist"
                  },
                  {
                        "Education Name": "National University of Computer and Emerging Sciences",
                        "Education Level": "Bachelor's degree",
                        "Education Description": ""
                  }
            ],
            "Certifications": [
                  {
                        "Certificate Name": "\n    ISTQB CTAL (certifies tester advanced level)\n  ",
                        "Certification Issuer": "Issued Aug 2017No Expiration Date",
                        "Certificate ID": ""
                  },
                  {
                        "Certificate Name": "\n    ISTQB Certified Foundation Level Tester (CTFL)\n  ",
                        "Certification Issuer": "ISTQB - International Software Testing Qualifications Board",
                        "Certificate ID": ""
                  }
            ],
            "Volunteer": [
                  {
                        "Volunteer Role": "Head operations, Fast Computing Society",
                        "Volunteer Cause": "\nEducation\n",
                        "Volunteer Organization": "FAST-NUCES"
                  },
                  {
                        "Volunteer Role": "Volunteer at Nascon '14",
                        "Volunteer Cause": "\nEducation\n",
                        "Volunteer Organization": "FAST-NUCES"
                  }
            ],
            "Courses": [
                  {
                        "Course Name": "Advanced Programming(java)"
                  },
                  {
                        "Course Name": "Business Intelligence"
                  },
                  {
                        "Course Name": "Data Warehousing"
                  },
                  {
                        "Course Name": "Geographic information system"
                  },
                  {
                        "Course Name": "Mobile Computing"
                  },
                  {
                        "Course Name": "Software Testing"
                  },
                  {
                        "Course Name": "Web Programming(asp.net)"
                  },
                  {
                        "Course Name": "English"
                  },
                  {
                        "Course Name": "Urdu"
                  },
                  {
                        "Course Name": "Fault Model & Mutation Analysis for Functional testing of platform games"
                  },
                  {
                        "Course Name": "Automated Game Testing Tool (Final Year Project)"
                  },
                  {
                        "Course Name": "Bronze Medal"
                  }
            ],
            "Skills": [
                  {
                        "Skill Name:": "Java"
                  },
                  {
                        "Skill Name:": "C#"
                  },
                  {
                        "Skill Name:": "Web Development"
                  },
                  {
                        "Skill Name:": "Software Development"
                  },
                  {
                        "Skill Name:": "Software Testing"
                  },
                  {
                        "Skill Name:": "ASP.NET"
                  },
                  {
                        "Skill Name:": "C++"
                  },
                  {
                        "Skill Name:": "Microsoft SQL Server"
                  },
                  {
                        "Skill Name:": "Selenium"
                  },
                  {
                        "Skill Name:": "JavaScript"
                  },
                  {
                        "Skill Name:": "HTML"
                  }
            ]
      }
}
```



 
