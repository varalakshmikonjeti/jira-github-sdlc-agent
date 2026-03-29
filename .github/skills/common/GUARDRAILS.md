---
name: guardrails
description: Critical guardrails that apply to ALL operations and ALL skills.
---

# Critical Guardrails

## 1. Branch Management (MANDATORY)

NEVER commit directly to main/master/develop branches.

### Required Workflow

1. Check branch:
   git rev-parse --abbrev-ref HEAD

2. Create feature branch:
   feature/<description>

3. Work only on feature branch

4. Push branch and create PR

---

## 2. Failure Handling

If ANY command fails:

- STOP immediately
- Show exact error
- DO NOT guess values
- DO NOT retry automatically

---

## 3. File Safety

- Check before overwriting files
- Ask user confirmation
- Backup important files

---

## 4. Security Rules

- Never commit secrets
- Use environment variables
- Do not expose tokens

---

## 5. Testing

- Run tests before commit
- Validate output
- Do not skip validation

---

## 6. Git Safety Script

CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

if [[ "$CURRENT_BRANCH" == "main" ]]; then
  echo "ERROR: Cannot commit to main branch!"
  exit 1
fi