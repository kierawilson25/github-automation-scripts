# GitHub Issue Creator

Welcome! This automation script helps you bulk-create GitHub issues from a JSON file. Below are the instructions for getting started.

## How It Works

This script reads a list of issues from `issues.json` and automatically creates them in your GitHub repository. You can optionally assign them to a milestone, add labels, and assign them to yourself.

## Setup Instructions

**Step 1: Prepare Your Issues**

Open the `issues.json` file and add your issues. Each issue needs a title and description:
```json
[
  {
    "title": "Fix login bug",
    "body": "Users are unable to log in with special characters in passwords"
  },
  {
    "title": "Add dark mode",
    "body": "Implement dark mode toggle in settings"
  }
]
```

**Step 2: Configure Your Environment**

Copy the template file to create your configuration:
```bash
cp .env.example .env
```

Open `.env` and fill in your details:

- `GITHUB_TOKEN` - Create one at [github.com/settings/tokens](https://github.com/settings/tokens) (needs "repo" permission)
- `REPO_OWNER` - Your GitHub username
- `REPO_NAME` - The name of your repository
- `MILESTONE_TITLE` - (Optional) Name of milestone to assign issues to
- `ASSIGNEE` - (Optional) GitHub username to assign issues to
- `LABELS` - (Optional) Comma-separated labels like `bug,enhancement`

**Step 3: Install Required Packages**
```bash
pip3 install -r requirements.txt
```

**Step 4: Run the Script**
```bash
python3 create_issues.py
```

The script will create all your issues and show you the results!

---

**—— Kiera Wilson Automation ——**