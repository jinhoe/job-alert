# Chrome Driver Setup

## Step 1: Download Chrome Driver
Make sure Chrome and chromedriver are compatible
https://chromedriver.chromium.org/downloads

chromedriver_mac_arm64.zip	

## Step 2. Run Command
CMD to the download folder where the file is downloaded
````bash
sudo cp chromedriver /usr/local/bin
````

````bash
sudo xattr -d com.apple.quarantine /usr/local/bin/chromedriver
````
