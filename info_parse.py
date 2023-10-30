import json
import pandas 
import os
import glob
import requests
import time
import datetime

if not os.path.exists("parsed_files"):
    os.mkdir("parsed_files")

dataset2 = pandas.DataFrame()

f = open("token", "r")
token = f.read()
f.close()


for json_file_name in glob.glob("json_files/*.json"):
    
        f = open(json_file_name, "r")
        json_data = json.load(f)
        f.close()

        login = json_data['login']
        avatar_url = json_data['avatar_url']
        url = json_data['url']
        followers = json_data['followers']
        name = json_data['name']
        company = json_data['company']
        blog = json_data['blog']
        email = json_data['email']
        hireable = json_data['hireable']
        bio = json_data['bio']
        created_at = json_data['created_at']
        updated_at = json_data['updated_at']
        location = json_data['location']
        public_repos = json_data['public_repos']
        following = json_data['following']
        

        row = pandas.DataFrame.from_records([{
            'login': login,
            'avatar_url': avatar_url,
            'url': url,
            'followers': followers,
            'name': name,
            'company': company,
            'blog': blog,
            'location': location,
            'email': email,
            'hireable': hireable,
            'bio': bio,
            'created_at': created_at,
            'updated_at': updated_at,
            'public_repos': public_repos,
            'following':following
        }])

        dataset2 = pandas.concat([dataset2, row])
   
dataset2.to_csv("parsed_files/github_user_data.csv", index=False)

#to compare two datasets:
mean_public_repos = dataset2['public_repos'].mean()
print("Mean of public_repos in 2023:", mean_public_repos)
mean_followers = dataset2['followers'].mean()
print("Mean of followers in 2023:", mean_followers)

dataset1= pandas.read_csv("parsed_files/new_dataset.csv")
mean_public_repos = dataset1['Repo_Count'].mean()
print("Mean of public_repos in 2022:", mean_public_repos)
# Clean the 'Follower_Count' column by removing non-numeric characters
dataset1['Follower_Count'] = dataset1['Follower_Count'].str.replace(r'\D', '', regex=True)

# Convert the cleaned column to numeric
dataset1['Follower_Count'] = pandas.to_numeric(dataset1['Follower_Count'], errors='coerce')

# Calculate the mean
mean_followers = dataset1['Follower_Count'].mean()

print("Mean of followers in 2022:", mean_followers)



time.sleep(10)
