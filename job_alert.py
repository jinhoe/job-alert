import time
import re
import emails
import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  # Windows
from bs4 import BeautifulSoup
from decimal import Decimal


# Selenium chrome
if platform.system() == "Windows":
    chromedriver = Service('C:\Chromedriver\chromedriver.exe')
    browser = webdriver.Chrome(service=chromedriver)
else:  # Mac
    chrome_options = Options()  # Headless selenium chrome
    chrome_options.add_argument("--headless")  # Headless selenium chrome
    browser = webdriver.Chrome(options=chrome_options)
    #browser = webdriver.Chrome()  # With head selenium chrome

# Filter
coy_keywords = ["yahoo"]  # Exclude keyword in company name
job_keywords = ["automation", "devops", "python", "machine learning", "ai", "a.i.", "ci / cd", "ci/cd"]  # Include keyword in job title
exp_keywords = ["senior", "lead"]  # Exclude keyword in job title
expected_salary = 3000
email_body = ""
convert_lowercase = ""
page_num = 0


def get_webpage():
    global listings
    browser.get(f"https://www.mycareersfuture.gov.sg/search?search=devops&sortBy=new_posting_date&page={page_num}")
    time.sleep(7)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    listings = soup.find_all(id=re.compile("^job-card-\d+"))


def get_job_post():
    global email_body
    for listing in listings:
        # Get yesterday job post
        for date_posted in listing.find(attrs={"data-cy": "job-card-date-info"}):
            if date_posted.getText() == "Posted yesterday":
            #if date_posted.getText() == "Posted today":
                # Exclude company name with coy_keywords
                for company_name in listing.find('p'):
                    convert_lowercase = company_name.getText()
                    if any(word in convert_lowercase.lower() for word in coy_keywords):
                        pass
                    else:
                        # Include job title with job_keywords
                        for job_title in listing.find('span'):
                            convert_lowercase = job_title.getText()
                            if any(word in convert_lowercase.lower() for word in job_keywords):
                                # Exclude job title with exp_keywords
                                if any(word in convert_lowercase.lower() for word in exp_keywords):
                                    pass
                                else:
                                    # Exclude min_salary below expected_salary
                                    for salary_range in listing.select("div.lh-solid"):
                                        min_salary = salary_range.getText().rpartition('to')[0]
                                        min_salary_int = Decimal(re.sub(r'[^\d.]', '', min_salary))
                                        if min_salary_int < expected_salary:
                                            pass
                                        else:
                                            # Compose email_body
                                            email_body += company_name.getText() + "\n"
                                            email_body += job_title.getText() + "\n"
                                            max_salary = salary_range.getText().partition("to")[2]
                                            email_body += min_salary + " to " + max_salary + "\n"
                                            for link in listing.find_all('a'):
                                                email_body += "https://www.mycareersfuture.gov.sg" + link.get("href") + "\n\n"
                            else:
                                pass
            else:
                pass


get_webpage()

# Always check if last post is posted yesterday or today if not end loop
last_post = listings[-1].find(attrs={"data-cy": "job-card-date-info"})
while last_post.getText() in ["Posted yesterday", "Posted today"]:
    get_job_post()
    # Go to next page and get webpage data
    page_num += 1
    get_webpage()
    # Update last_post
    last_post = listings[-1].find(attrs={"data-cy": "job-card-date-info"})
else:
    get_job_post()
    browser.quit()
    #print(email_body)

    if email_body:
        #pass
        emails.curated_job("Your job opportunities on ", email_body)
    else:
        #pass
        emails.curated_job("No job opportunities on ", "No opportunities yet")

