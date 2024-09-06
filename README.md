# Instagram Follower Checker

This Python script allows you to check which users you follow on Instagram but who do not follow you back. It uses the `instaloader` library to interact with Instagram and securely manages your credentials using environment variables.

## Features
- Fetches the list of users you follow.
- Fetches the list of users who follow you back.
- Outputs the list of users you follow that do not follow you back.

## Prerequisites

Make sure you have the following installed:
- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)

## Setup Instructions

### Step 1: Clone the Repository

First, clone this repository to your local machine and navigate into the project directory:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### Step 2: Clone the Repository

Next, install the required Python libraries. Run the following command to install dependencies from the requirements.txt file:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

The primary dependency is the instaloader package, which allows you to interact with Instagram.


### Step 3: Set Up Environment Variables

To securely store your Instagram credentials, create a .env file in the root of your project by copying the .env.example file:

```bash
cp .env.example .env
```

Now open the newly created .env file and add your Instagram credentials:

```bash
INSTAGRAM_USERNAME=your_instagram_username
INSTAGRAM_PASSWORD=your_instagram_password
```

### Step 4: Run the script

After setting up your .env file with your credentials, you can run the script by executing:

```bash
python3 your_script.py
``` 

When prompted, enter the Instagram username of the account you want to analyze.

```bash
Enter the target Instagram username:
```

The script will fetch the list of users that the target account follows and compare it with the list of their followers, printing the names of those who don't follow back.

## Notes

1. **Environment Security:** 
   - Your Instagram credentials are stored in the `.env` file, which is ignored by Git to prevent accidental exposure. 
   - **Never share your `.env` file** or your credentials with others.
   
2. **Rate Limits:** 
   - Instagram enforces rate limits on requests. If you hit these limits, the script may take longer to run, or you may have to wait before retrying.
   
3. **Session File:** 
   - The script uses a session file to avoid logging in repeatedly. The session file is named after your Instagram username (e.g., `your_instagram_username.session`).
   - Keep this session file secure as it contains your login session.
   - If you want to log out, simply delete the session file from the project directory, and the script will prompt for login credentials the next time you run it.
