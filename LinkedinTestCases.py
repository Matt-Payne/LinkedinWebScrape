# For testing please use this link "https://www.linkedin.com/in/osamaehsan/"

def course_test(course_list):
    assert course_list == [                  {
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
                  }], "Failed test incorrect output for courses"


def skills_test(skills_list):
    assert skills_list == [
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
            ], "Failed test incorrect output for skills"


def experience_test(experience_list):
    assert experience_list == [
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
            ], "Failed test incorrect output for experience"


def education_test(education_list):
    assert education_list == [
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
            ], "Failed test incorrect output for education"


def certification_test(certification_list):
    assert certification_list == [
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
            ], "Failed test incorrect output for certifications"


def volunteer_test(volunteer_list):
    assert volunteer_list == [
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
            ], "Failed test incorrect output for volunteering"


def name_test(name):
    assert name == "Osama Ehsan", "Failed test incorrect output for name"


