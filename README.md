## SocialEarning-Bot
  Introducing a powerful tool designed to automate tasks on [socialearning.org](https://socialearning.org/) — from liking posts and following accounts to completing and submitting tasks effortlessly
  No more manual work, just seamless automation to boost your earnings and maximize efficiency!.
# 
## Security & Privacy  
Rest assured that your passwords are encrypted using Playwright and are not shared externally. Your credentials will be stored securely on your device, you can read more about Playwright on their [official documentation](https://playwright.dev/docs/auth#authentication)
#
## Features
- **X**: Automates likes, tweet views, retweets, and follows
  #### **Coming Soon**
  - **Telegram**: Joins groups and channels seamlessly
  - **Facebook**: Handles post likes, page likes, comments, video views, and follows effortlessly
  - **TikTok**: Automates video likes, views, comments, and follows
  - **Instagram**: Likes posts, follows pages, and posts comments
#
## Optional: Enable Auto Login
  If you want the bot to log in automatically when you're logged out, you can add your credentials to a JSON file `credentials.json`.
  ```
  "SocialEarning": {
          "email": "your_email@example.com",
          "password": "your_password"
  }
  ```
  Make sure this file is kept private and secure.
#
## Automatic Login Feature  
The bot supports automatic login to the following platforms:
- SocialEarning
  #### Coming Soon
    - X
    - Facebook
    - Instagram
#
## Add Verified Social Media ID
Add your **verified social media account ID** (e.g., X.com ID) from [socialearning.org](https://socialearning.org/) to `credentials.json`.  
```
"Twitter": {
    "media-id": "your_verified_social_media_account_ID"
}
```
This helps the bot correctly match and submit your tasks.
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
  python3 nexora.py --auth
  ```
  This will open a browser window. Do the following:
  - ✅ Log in to your SocialEarning.org account.
  - ✅ Log in to your X.com (Twitter) account.
  
  This step stores session cookies to allow the bot to run smoothly without repeated logins.
  #### 7. Run the Bot Normally  
  After completing authentication, run the bot without flags to start automation:
  ```
  python3 nexora.py
  ```
  The bot will now:
  - Auto-login (if needed)
  - Perform tasks on SocialEarning.org (likes, follows, submissions, etc.)
#
## ⚠️ Disclaimer
Avoid logging into your social media accounts while the bot is running.  
  #### Why?
  - It may trigger security alerts or **suspicious activity flags**.
  - Platforms can detect multiple sessions and block tasks.
  #### Recommendation
  - Let the bot finish before logging in manually.
  - If you must access your account, **stop the bot first**.
This helps keep your account safe and the bot running smoothly.
