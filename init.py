import os
from browser import browser
from linkedinFunctions import login, searchJob


if __name__ == '__main__':
    print("Web-auto-controlled.")

login_url = "https://www.linkedin.com/uas/login?fromSignIn=true&amp;trk=cold_join_sign_in"
job_url = "https://www.linkedin.com/jobs/"
user = os.environ['USER_NAME']
password = os.environ['USER_PASSWORD']
jobTittle = os.environ['JOB_TITLE']
city = os.environ['CITY']
page = 1
certain = True

login(login_url, user, password)

searchJob(job_url, jobTittle, city)



# browser.quit();
# print("Script end.")
