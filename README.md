# Problem
Going through tons of job posting in MyCareersFuture portal has been a daily morning chore for me. Despite the site having a job alert feature, it does not serve my needs. So I decided to take this opportunity to practice my Git and Python skills.

What I want is to receive an email of curated job posting every morning.

# Solution
I used Selenium and Beautiful Soup in the Python script to extract job posting that matches my four pre-defined variables and then send it to my email.

This script will run daily at 8:15am on my MacBook using Cronjob. As my Macbook sleeps when inactive, I have to use MacOs System Preference to schedule a Wake and Sleep time like this:

1. 8:14am MacBook wakes up
2. 8:15am Run Python script
3. 8:16am MacBook goes back to sleep

The action happens when I'm preparing my son for school. I love automation!
The following four pre-defined variables condition must match in order to be listed in the email:

<b>coy_keywords</b> - Exclude keyword in company name. For some reasons, I do not want job post by recruitment firm so the company name should not have "recruitment" related word in it. Or some other company I do not wish to work for.

<b>job_keywords</b> - Include keyword in job title. Obviously the job title must have the keywords I'm looking for. Such as "machine learning", "devops", etc.

<b>exp_keywords</b> - Exclude keyword in job title. I'm looking for a junior role, so the job title should not have words like "senior", "lead", etc.

<b>expected_salary</b> - If the minimum salary is below my expected amount, the job post will be ignore.

<b>my_exp</b> - Exclude job experience more than my_exp (years)

Below is the daily curated job posting email I receive in my inbox now.

![alt text](https://github.com/jinhoe/job-alert/blob/master/job-alert-email-screenshot.png?raw=true)

# Next Challenge
When this project is working well, I proudly offered to help my wife shorten her job searching time. However she threw me another request. "What about JobStreet?", she asked.

<b>Challenge Accepted!</b>

On top of that, I asked a friend of mine who is working in HR which other popular job seeking platform. He told me LinkedIn Jobs is another common platform used by recruitment firm. So my next challenge would be adding JobStreet and LinkedIn Jobs into the script!
