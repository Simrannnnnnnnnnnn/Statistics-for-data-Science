import os
import subprocess
from datetime import datetime, timedelta

# Define the repository and folder names
repo_name = "statistics_for_data_science"
folders = [
    "introduction",
    "descriptive_statistics",
    "probability_basics",
    "probability_distribution",
    "sampling_and_sampling_distribution",
    "inferential_statistics",
    "correlation_and_regression",
    "advanced_statistics",
]

# Dates for simulation
start_date = datetime(2024, 9, 1)
end_date = datetime(2024, 10, 1)
date_increment = (end_date - start_date) / len(folders)

# Initialize Git repository
if not os.path.exists(repo_name):
    os.makedirs(repo_name)
os.chdir(repo_name)
subprocess.run(["git", "init"])

# Create and commit each folder with backdated commits
for i, folder in enumerate(folders):
    os.makedirs(folder, exist_ok=True)
    commit_date = start_date + i * date_increment
    formatted_date = commit_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Add folder and commit
    subprocess.run(["git", "add", folder])
    subprocess.run([
        "git", "commit", "-m", f"Add {folder}",
        "--date", formatted_date,
        "--author-date", formatted_date
    ])

# Advance the repository timeline to 1st October 2024
final_date = end_date.strftime("%Y-%m-%d %H:%M:%S")
subprocess.run([
    "git", "commit", "--allow-empty", "-m", "Advance to 1st October 2024",
    "--date", final_date,
    "--author-date", final_date
])

# Instructions to push the repository
print("\nRepository initialized with backdated commits.")
print("Run the following commands to push it to GitHub:")
print("git remote add origin <your-repo-url>")
print("git branch -M main")
print("git push -u origin main")

