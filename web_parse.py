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
            "Login ID": user_id.get_text(),
            "Repo Count": repo_count.get_text(),
            "Follower Count": follower_count.get_text(),
            "Member Since": member_since.get_text(),
        }])])

dataset.to_csv("parsed_files/dataset.csv", index=False)

unique_login_ids = dataset["Login ID"].drop_duplicates()
print(f"Number of unique login IDs: {len(unique_login_ids)}")
sample_size = len(dataset)
print(f"Sample size of the dataset: {sample_size}")

new_dataset = pandas.DataFrame()  # Create a new DataFrame for the unique login IDs

for file_name in glob.glob("html_files/*.html"):
    file = open(file_name, "r")
    soup = BeautifulSoup(file.read(), 'html.parser')
    file.close()

    unique_login_ids = soup.find_all("div", {"class": "userid"})
    repo_counts = soup.find_all("div", {"class": "repocount"})
    follower_counts = soup.find_all("div", {"class": "followercount"})
    member_sinces = soup.find_all("div", {"class": "membersince"})

    for unique_login_id, repo_count, follower_count, member_since in zip(unique_login_ids, repo_counts, follower_counts, member_sinces):
        new_dataset = pandas.concat([new_dataset, pandas.DataFrame.from_records([{
            "Login ID": unique_login_id.get_text(),
            "Repo Count": repo_count.get_text(),
            "Follower Count": follower_count.get_text(),
            "Member Since": member_since.get_text(),
        }])])

new_dataset = new_dataset.drop_duplicates(subset="Login ID")  # Remove duplicates from new_dataset

new_dataset.to_csv("parsed_files/new_dataset.csv", index=False)

print("waiting")
time.sleep(5)
