## SocialEarning-Bot
  Introducing a powerful tool designed to automate tasks on [socialearning.org](https://socialearning.org/) — from liking posts and following accounts to completing and submitting tasks effortlessly
  No more manual work, just seamless automation to boost your earnings and maximize efficiency!.
# 
## Security & Privacy  
Rest assured that your passwords are encrypted using Playwright and are not shared externally. Your credentials will be stored securely on your device, you can read more about Playwright on their [official documentation](https://playwright.dev/docs/auth#authentication)

If you prefer, you can add your SocialEarning login details to the passwd.json file. This will allow the bot to log in automatically in case you're logged out, making the process smoother.
#
## Action Requred
  Please provide your SocialEarning login details in the passwd.json file. This is Optional, for the bot login to your account automatically else login manually using **--auth** flag
#
## Features
- **X**: Automates likes, tweet views, retweets, and follows
  #### **Coming Soon**
  - **Telegram**: Joins groups and channels seamlessly
  - **Facebook**: Handles post likes, page likes, comments, video views, and follows effortlessly
  - **TikTok**: Automates video likes, views, comments, and follows
  - **Instagram**: Likes posts, follows pages, and posts comments

## Automatic Login Feature  
The bot supports automatic login to the following platforms:
- SocialEarning
  #### Coming Soon
    - X
    - Facebook
    - Instagram

Please note that the bot **won't be able to perform any tasks** on social media accounts you haven't logged into yet. For any social account you haven't logged into, cookies won't be saved, and a login will be required.
#
## Disclaimer  
- To ensure the safe and uninterrupted operation of the bot, please avoid logging into your social media accounts while the bot is running.
  #### Why This Is Important
    - Accessing your social media accounts while the bot is active might cause your account to get flagged.

  #### This happens because
    - **Security Alerts**: Platforms may consider this suspicious and flag your account for unusual activity.
    - **Multiple Sessions**: Social media platforms may detect simultaneous operations from different locations or devices.
 
  #### Recommendations
    - Allow the bot to complete its tasks without manual interference.
    - Only log in to your accounts after the bot has finished running.
    - If you need to access your accounts urgently, stop the bot first to avoid conflicts.

By following these precautions, you help ensure the smooth operation of the bot and protect your accounts from being flagged.
#
## Optional: Enable Auto Login
  If you want the bot to log in automatically when you're logged out, you can add your credentials to a JSON file `credentials.json`.
  ```
  {
    "email": "your_email@example.com",
    "password": "your_password"
  }
  ```
  Make sure this file is kept private and secure.
#
## Provide Your Verified Social Media Account IDs  
To ensure seamless operation, please input the IDs of your verified social media accounts on [socialearning.org](https://socialearning.org/) in the passwd.json file.
This is required for the bot to correctly identify your accounts and submit tasks.
#
## Exit Program  
To End running session, kindly Press `CTRL+C`
#
## ⚙️ Installation Guide
  Follow the steps below to install and set up the SocialEarning Referral Booster Bot:
  #### 1. System Requirements
  - PC with a Linux-based OS (Ubuntu recommended)
  - Python 3.8 or higher
  - Git installed
 > 💡 Need help setting up Ubuntu? [Watch this guide](https://youtu.be/FdsB5gTVMTk?si=fqH01fVLkkhDhScg)

  #### 2. Clone the Repository  
     git clone https://github.com/Mr-Frst/SocialEarning-Bot
     cd SocialEarning-Bot
  #### 3. Install Dependencies
     pip install -r requirements.txt
  #### 5. Install Chromium (for Playwright)
     playwright install chromium
  #### 6. Authenticate Your SocialEarning & X.com Accounts
  Before using the bot, you must authenticate your session:
  ```
  python3 Socail-Earning.py --auth
  ```
  This will open a browser window. Do the following:
  - ✅ Log in to your SocialEarning.org account.
  - ✅ Log in to your X.com (Twitter) account.
  - ✅ Ensure your verified X (Twitter) account is added and active on your SocialEarning.org profile.  
  
  This step stores session cookies to allow the bot to run smoothly without repeated logins.
