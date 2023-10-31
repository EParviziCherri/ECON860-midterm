# ECON860-midterm
part1:
I started with requesting to get data from the website and then used the information from the request to parse the Login IDs.
I add my token into .gitignore file , to keep it hidden to the other users.
Web_request.py: 
1- I checked if a folder named "html_files" exists, and if not, I creates this folder using os.mkdir("html_files").
2- I opened a file named "token" in read mode and reads its content into the variable token (in order to have access to more GitHub usernames).
3- I defined a dictionary called headers that contains HTTP headers, including 'accept', 'User-Agent', 'accept-language', and 'referer'. These headers can be used for HTTP requests to mimic a web browser.
4- I entered a loop that runs once (due to for i in range(0,1):), in which it performs the following steps:
a. I generated a timestamp in the format "YYYYMMDDHHMMSS" and stores it in the variable current_time using datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S").
b. I opened a file in the "html_files" folder with a filename based on the current_time variable.
c. I created a new requests.Session() object and sends an HTTP GET request to the URL specified in the access_point variable, using the headers defined in the headers dictionary. The HTML content of the response is stored in the html variable.
d. I writed the HTML content to the file created in step.
e. I printed "waiting" to the console and then waits for 60 seconds using time.sleep(60).


Web_parse.py:
the code is designed to scrape data from multiple HTML files, create datasets, and export them to CSV files. It also ensures that there are no duplicate & invalid login IDs in the new dataset. This code would be useful for collecting and processing data from HTML files.
1.	I set up the necessary libraries and environment for web scraping and data manipulation.
2.	I retrieved data from HTML files in the "html_files" folder. These HTML files contain information about GitHub users, including login IDs, repository counts, follower counts, and member since.
3.	I created a Pandas DataFrame named "dataset" to store this extracted data, and I saved it to a CSV file in the "parsed_files" folder.
4.	I conducted data validation by checking the validity of GitHub user IDs by making requests to the GitHub API for each user. Valid and invalid user IDs were segregated.
5.	I created a new DataFrame named "new_dataset" to store valid user information, removed duplicates, and saved it to a separate CSV file in the "parsed_files" folder. The code also introduced some data cleaning by stripping spaces from the DataFrame.


Number of unique login IDs: 696
Sample size of the dataset: 746 (before cleaning)
number of invalid login IDs :252
number of login IDs with invalid/missing information: 254 (2 IDs with invalid URL)
Sample size after being clean and with valid IDs : 442






Part2:
I downloaded the valid Login ID from the previous new_dataset.csv from the GitHub Api website within info_request.py codes & within info_parsed.py, I parsed the downloaded Login ID to get more information from them and saved the data into a .csv file.

Info_request.py:
This Python script is designed to interact with the GitHub API to fetch user profile data. Here's a summary of its functions:
I checked if a folder named "json_files" exists and creates it if not. This directory is used to store JSON files containing user data. The script reads a dataset from a CSV file containing GitHub login IDs. I read a GitHub API token from a file, required for authentication.
For each login ID in the dataset, I constructed a GitHub API endpoint and sent an HTTP GET request to fetch the user's data. If the data hasn't been previously downloaded (file does not exist), it saves the user data to a JSON file with a filename based on the user's login ID.
I handled exceptions and prints messages if there are errors during the process, such as unsuccessful API requests. After each user request, the script pauses for 5 seconds to prevent excessive requests to the GitHub API.

Info_parse.py:
I checked if a folder named "parsed_files" exists and created it if it doesn't. The script iterates through JSON files in the "json_files" folder, which presumably contain data retrieved from GitHub user profiles. For each JSON file, I extracted specific user-related information such as avatar_url, url, followers, following, number of repositories, login, name, company, blog, email, hireable, bio, created_at , and updated_at.
The extracted data for each user is printed to the console, and a new row of data is added to a pandas DataFrame for further processing. The individual data rows are concatenated into a single DataFrame. 
 To compare the dataset in part 1&part 2: since the first dataset is for 2022 consequently member_since is one year less than created_at.  And similarly, I have less follower count and repository count in the first dataset compared to the second one. I have more columns and information in the new_dataset.csv. I wrote the mean function to compare the mean of two datasets. As we can see the means are bigger in 2023 due to more repositories and more followers.
Mean of public_repos in 2023: 178.0656108597285
Mean of followers in 2023: 465.1877828054299
Mean of public_repos in 2022: 140.77702702702703
Mean of followers in 2022: 440.47297297297297

Part3:
I used import ‘matplotlib.pyplot as plt’ library to plot scatterplots, I add noise to the variables to see their relationship more accurate, then saved the plot as an image file (e.g., in PNG format):
Plot1: I put number of public repositories on the X aces and number of followers on the Y aces. I expected to see that there is a positive correlation between these two variables, holding other variables constant. Because people with higher number of repositories are generally considered more noteworthy or influential within the GitHub community and consequently, they should have more followers. But I didn’t see a linear relationship between these two variables. It might be some variables in the error terms that have effect on followers and is correlated to number of repositories and is not in our model. Or there might not be enough variation in number of repositories(X). These are violations to our assumptions, and we can’t interpret causality.

Plot2: I added Date Created on the X aces and Number of Following on the Y aces, I was expected to see the more time has passed since the user created his/her account, the more following she/he might have. For some users, it is true but there are some old users with 0 following. I am thinking maybe some GitHub users had created account for specific courses or purpose and there are not active GitHub usernames. As I mentioned in the first plot it is a violation to the zero conditional mean assumption and we cannot interpret causality.


Please be informed that I used Chatgpt as a collaborator to fix my errors and I added comments to those specific lines. And I used Chatgpt to organize my summary statistically well.
 Thank you,
