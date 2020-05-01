import os
import sys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from browser import browser

def login(login_url, user_email, user_password):
    print("Environment set")
    browser.get(login_url)
    print("Starting login")
    sleep(2)
    input = browser.find_element_by_id('username')
    password = browser.find_element_by_id('password')
    input.send_keys(user_email)
    password.send_keys(user_password)
    input.send_keys(Keys.ENTER)
    print("Login success")
    sleep(2)

def searchJob(job_url, jobTittle, city):
    print("Starting job searching")
    browser.get(job_url)
    sleep(0.2)
    try:
        search_jobs = browser.find_elements_by_xpath("//input[@placeholder='Search by title, skill, or company']")
        search_jobs[0].send_keys(jobTittle)
    except Exception as e:
        raise
    try:
        search_location = browser.find_elements_by_xpath("//input[@placeholder='City, state, or zip code']")
        search_location[0].send_keys(city)
        search_location[0].send_keys(Keys.ENTER)
    except Exception as e:
        raise
    print("Job searching success")
    sleep(3)
