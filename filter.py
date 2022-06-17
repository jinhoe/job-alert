def get_webpage(page_num):
    browser.get(f"www.abc.com/page={page_num}")
    time.sleep(7)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    listings = soup.find_all(id=re.compile("^job-card-\d+"))
    browser.quit()




page_num = 0

# While loop
# Scrape listings

# Go to next page
page_num += 1

# Download next page
get_webpage(page_num+=1)

print()