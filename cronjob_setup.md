# Cronjob Setup test

## Give Cron Permission
1. System Preferences > Security & Privacy > Full Disk Access
2. Add cron at /usr/sbin/cron

## Grontab Guru
https://crontab.guru
1. Get cron schedule expression
2. For every day 8:15am is 15 8 * * *

## Terminal
1. Open Terminal then navigate to script directory
````bash
pwd
````
/users/jinhoe/documents/personal\ projects/job\ alert/job-alert.py
````bash
which python3
````
/Users/jinhoe/.local/share/virtualenvs/Job_Alert-dz0OG5uq/bin/python3

## Crontab
1. Edit crontab
````bash
crontab -e
````
2. Press `i` and insert following command
````bash
SHELL=/bin/bash
PATH=/usr/local/bin/:/usr/bin:/usr/sbin
0 8 * * 1-7 /Users/jinhoe/.local/share/virtualenvs/Job_Alert-dz0OG5uq/bin/python3 /users/jinhoe/documents/personal\ projects/job\ alert/job_alert.py
````
3. Press `ESC`, `:wq` then `ENTER`
4. Verify cronjob
````bash
crontab -l
````

## Schedule Wake & Sleep
1. System Preferences > Battery > Schedule
