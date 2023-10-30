import pandas
import os
import re
import glob
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import datetime

if not os.path.exists("parsed_files"):
    os.mkdir("parsed_files")

dataset = pandas.DataFrame()

f = open("token", "r")
token = f.read()
f.close()

github_session = requests.Session()
github_session.auth = ("EParviziCherri ", token)

for file_name in glob.glob("html_files/*.html"):
    file = open(file_name, "r")
    soup = BeautifulSoup(file.read(), 'html.parser')
    file.close()

    user_ids = soup.find_all("div", {"class": "userid"})
    repo_counts = soup.find_all("div", {"class": "repocount"})
    follower_counts = soup.find_all("div", {"class": "followercount"})
    member_sinces = soup.find_all("div", {"class": "membersince"})

    for user_id, repo_count, follower_count, member_since in zip(user_ids, repo_counts, follower_counts, member_sinces):
        dataset = pandas.concat([dataset, pandas.DataFrame.from_records([{
            "Login_ID": user_id.get_text(),
            "Repo_Count": repo_count.get_text(),
            "Follower_Count": follower_count.get_text(),
            "Member_Since": member_since.get_text(),
        }])])

dataset.to_csv("parsed_files/dataset.csv", index=False)

unique_login_ids = dataset["Login_ID"].unique()
print(f"Number of unique login_IDs: {len(unique_login_ids)}")
sample_size = len(dataset)
print(f"Sample size of the dataset: {sample_size}")


valid_ids = []
invalid_ids = []
base_url = "https://api.github.com/users/"
#github_session = requests.Session()

for user_id in unique_login_ids:
    user_profile_url = f"{base_url}{user_id.strip()}"       
    response = github_session.get(user_profile_url) 
    print(response.status_code)
    print(user_profile_url)
    if response.status_code == 200:
        valid_ids.append(user_id)
    else:
        invalid_ids.append(user_id)

valid_dataset = dataset[dataset["Login_ID"].isin(valid_ids)] # Filter the dataset to keep only valid login IDs
invalid_dataset = dataset[dataset["Login_ID"].isin(invalid_ids)]
num_invalid_ids = len(invalid_ids)    # Count the number of invalid Login IDs
print(f"Number of invalid Login_IDs: {num_invalid_ids}")

new_dataset = pandas.DataFrame()  # Create a new DataFrame for the unique login IDs

for file_name in glob.glob("html_files/*.html"):
    file = open(file_name, "r")
    soup = BeautifulSoup(file.read(), 'html.parser')
    file.close()

    valid_datasets= soup.find_all("div", {"class": "userid"})
    repo_counts = soup.find_all("div", {"class": "repocount"})
    follower_counts = soup.find_all("div", {"class": "followercount"})
    member_sinces = soup.find_all("div", {"class": "membersince"})

    for valid_dataset, repo_count, follower_count, member_since in zip(valid_datasets, repo_counts, follower_counts, member_sinces):
        new_dataset = pandas.concat([new_dataset, pandas.DataFrame.from_records([{
            "Login_ID": valid_dataset.get_text(),
            "Repo_Count": repo_count.get_text(),
            "Follower_Count": follower_count.get_text(),
            "Member_Since": member_since.get_text(),
        }])])

new_dataset = new_dataset.drop_duplicates(subset="Login_ID")  # Remove duplicates from new_dataset
new_dataset = new_dataset[new_dataset["Login_ID"].isin(valid_ids)]  # Filter for valid user IDs

new_dataset = new_dataset.apply(lambda x: x.str.strip() if x.dtype == "object" else x) #remove spaces




new_dataset.to_csv("parsed_files/new_dataset.csv", index=False)

print("waiting")
time.sleep(5)
