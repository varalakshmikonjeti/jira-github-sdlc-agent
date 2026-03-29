  # Jira to GitHub SDLC Agent

## Purpose
This agent automates the Software Development Life Cycle (SDLC) by integrating Jira and GitHub. It reads Jira tickets, creates branches, applies changes, commits code, and creates pull requests.

---

## Intent Recognition

Trigger this agent when user says:
- "create PR from jira"
- "process jira ticket"
- "@my-agent automate sdlc"

---

## Skills Available

- my-new-skill

---

## MCP Servers

| Server | Purpose |
|--------|--------|
| github | Code management & PR |
| atlassian | Jira ticket access |

---

## Workflow

1. Fetch Jira ticket details  
2. Create feature branch  
3. Modify code based on ticket  
4. Commit changes  
5. Push branch  
6. Create Pull Request  

---

## Tools Used

- read_file
- create_file
- run_in_terminal
- mcp_github_create_pull_request
- mcp_github_issue_read

---

## Safety

- Never commit to main branch  
- Always create feature branch  
- Follow guardrails  

---

## Example Usage

@my-agent process jira ticket PROJ-123

Expected Output:
- Branch created
- Code updated
- PR created