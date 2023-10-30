import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv("parsed_files/github_user_data.csv")

# Add noise 
noise_level = 10  # Adjust the noise level as needed
dataset['public_repos'] += np.random.uniform(-noise_level, noise_level, len(dataset))
dataset['followers'] += np.random.uniform(-noise_level, noise_level, len(dataset))  # Corrected this line

plt.figure(figsize=(10, 6))

# Create a scatterplot with noisy data
plt.scatter(dataset['public_repos'], dataset['followers'], c='blue', alpha=0.5)

# Add labels and a title
plt.xlabel('Number of Public Repositories')
plt.ylabel('Number of followers')
plt.title('Scatterplot of followers vs. Number of Public Repositories')

# Set the y-axis limits to start from 0
#plt.ylim(0, dataset['num_stars'].max() + 10)

# Save the plot as an image file (e.g., in PNG format)
plt.savefig('scatterplot1.png')

# Show the plot
plt.show()



