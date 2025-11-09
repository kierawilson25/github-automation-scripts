import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file in the same directory
load_dotenv()

# Configuration
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_OWNER = os.getenv( 'REPO_OWNER')
REPO_NAME = os.getenv( 'REPO_NAME')
ISSUES_FILE = 'issues.json'
MILESTONE_TITLE = os.getenv('MILESTONE_TITLE') # Optional
ASSIGNEE = os.getenv('ASSIGNEE')  # Optional
LABELS = os.getenv('LABELS')  # Optional
PROJECT_NUMBER = os.getenv('PROJECT_NUMBER')  # Optional


# Validate required envorinment variables
required_vars = ['GITHUB_TOKEN', 'REPO_OWNER', 'REPO_NAME', 'ISSUES_FILE']
missing_vars = [var for var in required_vars if not os.getenv(var)] # Loop through required vars and check if it is in the env variables

if missing_vars:
    print("Error: Missing required environment variables : ")
    for var in missing_vars:
        print(f" - {var}")
    print("\n Please check your .env file and ensure all required variables are set.")
    exit(1)
    
# Read issues from JSON file
try:
    with open(ISSUES_FILE, 'r') as file:
        issues = json.load(file)
except FileNotFoundError:
    print(f"Error: Issues file '{ISSUES_FILE}' not found")
    print("Please ensure the file exists in the current directory")
    exit(1)
except json.JSONDeocdeError:
    print(f"Error: '{ISSUES_FILE}' is not valid JSON")
    print("Please check the file formmat")
    exit(1)
    
# GitHub API endpoint
api_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Get the milestone number if specified
milestone_number = None
if MILESTONE_TITLE:
    milestones_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/milestones"
    
    # Fetch milestones from the repository
    try:
        response = requests.get(milestones_url, headers=headers)
        response.raise_for_status()
        milestones = response.json()
    except requests.exceptions.RequestException as error: 
        print("Error: Failed to fetch milestones from Github")
        print(f"Details: {error}")
        exit(1)
        
    for milestone in milestones: 
        if milestone['title'] == MILESTONE_TITLE:
            milestone_number = milestone['number']
            break
    
    if milestone_number:
        print(f"Found milestone: {MILESTONE_TITLE} (Milestone number: {milestone_number})")
    else:
        print(f"Warning: Milestone '{MILESTONE_TITLE}' not found.")
        exit(1)
        
# Create each issue
for issue in issues:
    data = {
        "title": issue["title"],
        "body": issue["body"]
    }
    
    # Add optional fields if they exist
    if milestone_number:
        data["milestone"] = milestone_number
    if ASSIGNEE:
        data["assignees"] = [ASSIGNEE]
    if LABELS:
        data["labels"] = [label.strip() for label in LABELS.split(',')]
        
    response = requests.post(api_url, headers=headers, json=data)
    
    if response.status_code == 201:
        issue_number = response.json().get('number')
        print(f" ✓ Created issue #{issue_number}: {issue['title']}")
    else:
        print(f" ✗ Failed to create issue: {issue['title']}")
        print(f" Error: {response.json()}")
        
print("\n✨ Script Complete! ✨")
print("\n —— Kiera Wilson Automation ——")

        