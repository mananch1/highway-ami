# Task 5: Feature Development with Branching

**Student:** Manan Chahal (Roll No: 23102C0044)  
**Project Title:** DevOps Pipeline for a Roadside Assistance Portal  
**Class/Division:** BE VII - Division C  

---

## 1. Feature 1 Scope & Objectives

**Feature Name:** Core Incident Lifecycle and Emergency Request Flow  
**Branch:** `feature/incident-crud`  
**Description:** Implement the primary business workflow of the Roadside Assistance Portal:
1. Public emergency incident submission without pre-registration.
2. Automated technician dispatch via round-robin queue.
3. Incident state persistence and query endpoints.
4. Auto-triggered mock notifications to emergency services.

---

## 2. Git Operations & Evidence

```bash
# 1. Create and switch to feature branch
git checkout main
git pull origin main
git checkout -b feature/incident-crud

# 2. Stage implementation files
git add src/main/java/com/mananc/road_helper/entity/
git add src/main/java/com/mananc/road_helper/repository/
git add src/main/java/com/mananc/road_helper/service/IncidentService.java
git add src/main/java/com/mananc/road_helper/controller/EmergencyController.java
git add src/main/java/com/mananc/road_helper/controller/IncidentController.java
git add frontend/src/pages/Landing.jsx
git add frontend/src/pages/EmergencyStatus.jsx

# 3. Commit with semantic conventional commit message
git commit -m "feat(incident): implement emergency guest request and round-robin dispatch"

# 4. Push feature branch to GitHub remote
git push -u origin feature/incident-crud
```

---

## 3. Pull Request & Review Evidence

- **Pull Request Title:** `PR #1: Implement Core Incident CRUD & Emergency Dispatch Workflow`
- **Source Branch:** `feature/incident-crud`
- **Target Branch:** `main`

### Code Review Checklist & Feedback
| Review Item | Status | Comments |
|-------------|--------|----------|
| **Stateless Security** | Passed | Guest tokens generated with 4-hour validity via `JwtTokenProvider.generateGuestToken()`. |
| **Concurrency & Availability** | Passed | Technician marked `isAvailable = false` inside `@Transactional` block to prevent duplicate assignment. |
| **Database Independence** | Passed | JPA queries designed without database-specific syntax; compatible with both PostgreSQL and H2. |
| **Unit Test Coverage** | Passed | `IncidentServiceTest` verifies round-robin assignment and emergency response creation. |

### Merge Execution:
```bash
git checkout main
git merge --no-ff feature/incident-crud -m "Merge pull request #1 from feature/incident-crud"
git push origin main
```
