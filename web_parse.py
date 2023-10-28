import pandas
import os
import re
import glob
from bs4 import BeautifulSoup

if not os.path.exists("parsed_files"):
    os.mkdir("parsed_files")

dataset = pandas.DataFrame()

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
            "userid": user_id.get_text(),
            "repocount": repo_count.get_text(),
            "followercount": follower_count.get_text(),
            "membersince": member_since.get_text(),
        }])])

dataset.to_csv("parsed_files/dataset.csv", index=False)
