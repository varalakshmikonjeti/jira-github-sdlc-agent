from dotenv import load_dotenv
import os
import requests

# ✅ ADD THIS LINE
load_dotenv()

# Load environment variables
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
JIRA_URL = os.getenv("JIRA_URL")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")


# -----------------------------
# Fetch Jira Ticket
# -----------------------------
def get_jira_ticket(ticket_id):
    url = f"{JIRA_URL}/rest/api/3/issue/{ticket_id}"
    auth = (JIRA_USERNAME, JIRA_API_TOKEN)

    response = requests.get(url, auth=auth)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch Jira ticket: {response.text}")

    data = response.json()
    return {
        "key": data["key"],
        "summary": data["fields"]["summary"],
        "description": data["fields"].get("description", "")
    }


# -----------------------------
# Create Git Branch
# -----------------------------
def create_branch(ticket_id):
    branch_name = f"feature/{ticket_id}"
    os.system(f"git checkout -b {branch_name}")
    return branch_name


# -----------------------------
# Commit Changes
# -----------------------------
def commit_changes(ticket_id):
    os.system("git add . -- ':!.env'")
    os.system(f'git commit -m "Changes for {ticket_id}"')


# -----------------------------
# Push Branch
# -----------------------------
def push_branch(branch_name):
    os.system(f"git push origin {branch_name}")


# -----------------------------
# Create GitHub PR
# -----------------------------
def create_github_pr(repo, branch):
    url = f"https://api.github.com/repos/{repo}/pulls"

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }

    data = {
        "title": f"PR for {branch}",
        "head": branch,
        "base": "main"
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 201:
        raise Exception(f"PR creation failed: {response.text}")

    return response.json()["html_url"]


# -----------------------------
# Main Flow
# -----------------------------
def run(ticket_id, repo):
    print("Fetching Jira ticket...")
    ticket = get_jira_ticket(ticket_id)

    print("Creating branch...")
    branch = create_branch(ticket_id)

    print("Committing changes...")
    commit_changes(ticket_id)

    print("Pushing branch...")
    push_branch(branch)

    print("Creating PR...")
    pr_url = create_github_pr(repo, branch)

    print(f"✅ PR Created: {pr_url}")


if __name__ == "__main__":
    ticket_id = input("Enter Jira Ticket ID: ")
    repo = input("Enter GitHub repo (username/repo): ")

    run(ticket_id, repo)