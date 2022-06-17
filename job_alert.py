import time, re, emails
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from decimal import Decimal
from selenium.webdriver.chrome.service import Service  # Windows
import platform


# Headless selenium chrome
chrome_options = Options()  # Mac
chrome_options.add_argument("--headless")  # Mac
#chrome_options.add_argument("--disable-gpu")
#chrome_options.headless = True

"""
def get_webpage(page_num):
    browser.get(f"https://www.mycareersfuture.gov.sg/search?search=devops&sortBy=new_posting_date&page={page_num}")
    time.sleep(7)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    listings = soup.find_all(id=re.compile("^job-card-\d+"))
    browser.quit()
"""
if platform.system() == "Windows":
    chromedriver = Service('C:\Chromedriver\chromedriver.exe')
    browser = webdriver.Chrome(service=chromedriver)
else:
    browser = webdriver.Chrome(options=chrome_options)
    #browser = webdriver.Chrome()  # With head selenium chrome

coy_keywords = ["yahoo"]  # Exclude keyword in company name
job_keywords = ["automation", "devops", "python", "machine learning", "ai", "a.i.", "ci / cd", "ci/cd"]  # Include keyword in job title
exp_keywords = ["senior", "lead"]  # Exclude keyword in job title
expected_salary = 3000
email_body = ""
convert_lowercase = ""
page_num = 0


browser.get(f"https://www.mycareersfuture.gov.sg/search?search=devops&sortBy=new_posting_date&page={page_num}")
time.sleep(7)
soup = BeautifulSoup(browser.page_source, "html.parser")
listings = soup.find_all(id=re.compile("^job-card-\d+"))
browser.quit()

#for listing in listings:
# Always check if last post is posted yesterday

last_post = listings[-1].find(attrs={"data-cy": "job-card-date-info"})
test = ""
test = last_post.getText()

#While (test = "Posted yesterday") or ("Posted today"):
while test in ["Posted yesterday", "Posted today"]:
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
    # Go to next page
    page_num += 1
    # Download webpage
    chromedriver = Service('C:\Chromedriver\chromedriver.exe')
    browser = webdriver.Chrome(service=chromedriver)
    browser.get(f"https://www.mycareersfuture.gov.sg/search?search=devops&sortBy=new_posting_date&page={page_num}")
    time.sleep(7)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    listings = soup.find_all(id=re.compile("^job-card-\d+"))
    browser.quit()

    last_post = listings[-1].find(attrs={"data-cy": "job-card-date-info"})
    test = ""
    test = last_post.getText()

else:
    for listing in listings:
        # Get yesterday job post
        for date_posted in listing.find(attrs={"data-cy": "job-card-date-info"}):
            if date_posted.getText() == "Posted yesterday":
                # if date_posted.getText() == "Posted today":
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
                                                email_body += "https://www.mycareersfuture.gov.sg" + link.get(
                                                    "href") + "\n\n"
                            else:
                                pass
            else:
                pass

    print(email_body)
"""
    if email_body:
        pass
        #emails.job_available(email_body)
    else:
        pass
        #emails.job_unavailable()
"""
