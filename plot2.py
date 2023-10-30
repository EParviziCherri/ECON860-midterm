import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

dataset = pd.read_csv("parsed_files/github_user_data.csv")
dataset['created_at'] = pd.to_datetime(dataset['created_at'])

# Continue with your code to add noise to 'created_at' column

plt.figure(figsize=(10, 6))

# Create a scatterplot with noisy data
plt.scatter(dataset['created_at'], dataset['following'], c='blue', alpha=0.5)

# Set the X-axis labels with appropriate formatting
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))  # Format the X-axis as 'YYYY-MM-DD'
plt.xticks(rotation=45)  # Rotate X-axis labels for readability

# Add labels and a title
plt.xlabel('Date Created')
plt.ylabel('Number of following')
plt.title('Scatterplot of Date Created following')

# Set the y-axis limits to start from 0
#plt.ylim(0, dataset['num_repos'].max() + 10)

# Save the plot as an image file (e.g., in PNG format)
plt.savefig('scatterplot2.png')

# Show the plot
plt.show()
