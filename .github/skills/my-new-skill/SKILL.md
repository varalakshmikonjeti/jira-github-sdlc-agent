# Jira to GitHub Skill

## Purpose
Implements the SDLC automation from Jira ticket to GitHub PR.

---

## Step 1: Fetch Jira Ticket

- Use Atlassian MCP server
- Get ticket details (title, description)

---

## Step 2: Create Feature Branch

Command:
git checkout -b feature/<ticket-id>

Example:
feature/PROJ-123

---

## Step 3: Modify Code

- Read existing files
- Apply changes based on ticket description

---

## Step 4: Commit Changes

Commands:
git add .
git commit -m "Implemented changes for <ticket-id>"

---

## Step 5: Push Branch

Command:
git push origin feature/<ticket-id>

---

## Step 6: Create Pull Request

- Use GitHub MCP
- Create PR from feature branch → main

---

## Error Handling

- If Jira ticket not found → stop
- If branch exists → ask user
- If commit fails → show error

---

## Output

- Branch created
- Changes committed
- PR link generated