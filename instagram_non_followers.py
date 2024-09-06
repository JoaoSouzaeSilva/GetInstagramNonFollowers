import instaloader
import os
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_non_followers(username):
    # Initialize Instaloader
    L = instaloader.Instaloader()

    # Get credentials from environment variables
    insta_username = os.getenv('INSTAGRAM_USERNAME')
    insta_password = os.getenv('INSTAGRAM_PASSWORD')

    # Define the session file path
    session_file = f'{insta_username}.session'

    # Load session if available, otherwise log in and save session
    if os.path.exists(session_file):
        print(f"Loading session for {insta_username}...")
        L.load_session_from_file(insta_username)
    else:
        print("Logging in and creating a new session...")
        L.login(insta_username, insta_password)
        L.save_session_to_file()

    # Load the profile of the target user
    profile = instaloader.Profile.from_username(L.context, username)

    # Get the list of followees (people the user follows) with a delay to avoid rate-limiting
    print("----- Fetching followees -----")
    followees = set()
    for followee in profile.get_followees():
        followees.add(followee.username)
        print(followee.username)
    print(f"----- Fetched {len(followees)} followees -----")

    # Get the list of followers (people who follow the user) with a delay to avoid rate-limiting
    print("----- Fetching followers -----")
    followers = set()
    for follower in profile.get_followers():
        followers.add(follower.username)
        print(follower.username)
    print(f"----- Fetched {len(followers)} followers -----")

    # Find users who are followed by the user but do not follow back
    non_followers = followees - followers
    if non_followers:
        print(f"----- Users followed by {username} but not following back -----")
        for user in non_followers:
            print(user)
    else:
        print(f"----- All users followed by {username} are following back -----")

if __name__ == "__main__":
    # Prompt the user for the target username
    target_username = input("Enter the target Instagram username: ")
    get_non_followers(target_username)
