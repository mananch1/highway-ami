# Task 6: MVP Completion and Git Collaboration

**Student:** Manan Chahal (Roll No: 23102C0044)  
**Project Title:** DevOps Pipeline for a Roadside Assistance Portal  
**Class/Division:** BE VII - Division C  

---

## 1. Feature 2 Scope: Summary Analytics Dashboard

**Branch:** `feature/dashboard-analytics`  
**Description:** Implement real-time operational analytics for dispatch administrators:
1. `DashboardSummary` DTO aggregating total volume, today's volume, active technician status, and average resolution time in minutes.
2. `DashboardController` exposing `/api/v1/dashboard/summary` protected with `ADMIN` role check.
3. Interactive frontend dashboard built using Recharts (`PieChart` for status breakdown, `BarChart` for incident categories).

---

## 2. Simulated Merge Conflict Creation & Resolution

To demonstrate robust Git collaboration skills as required by the course syllabus, a concurrent edit scenario was simulated on `src/main/resources/application.properties`:

### Conflict Scenario
1. **Branch A (`main`)** added security dialect settings:
   ```properties
   <<<<<<< HEAD
   spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.PostgreSQLDialect
   app.jwt.expiration-ms=86400000
   =======
   ```
2. **Branch B (`feature/dashboard-analytics`)** concurrently modified caching and timeout values:
   ```properties
   =======
   spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.PostgreSQLDialect
   app.jwt.expiration-ms=43200000
   app.dashboard.cache-ttl=300
   >>>>>>> feature/dashboard-analytics
   ```

### Resolution Strategy
The conflict markers were inspected, both configuration parameters were synthesized, and the verified resolution was committed:
```bash
git checkout main
git merge feature/dashboard-analytics
# Auto-merging src/main/resources/application.properties
# CONFLICT (content): Merge conflict in src/main/resources/application.properties
# Automatic merge failed; fix conflicts and then commit the result.

# Edit file to keep PostgreSQLDialect, 24h expiration, and cache settings
git add src/main/resources/application.properties
git commit -m "fix(merge): resolve configuration conflict in application.properties"
```

---

## 3. Release Baseline & Version Tagging

Upon verifying the entire MVP functionality and running all unit and Selenium tests, the release baseline was officially tagged:

```bash
# Create annotated release tag
git tag -a v1.0.0 -m "Release v1.0.0: Functional Roadside Assistance MVP with full role workflows and dashboard"

# Push tag to GitHub remote
git push origin v1.0.0

# Verify tagged commit
git describe --tags
# Output: v1.0.0
```

### Verified Release Capabilities
- [x] Public emergency roadside request with guest token
- [x] Round-robin automated technician dispatch
- [x] Role-based status progression (`REQUESTED` -> `AUTO_ASSIGNED` -> `IN_PROGRESS` -> `RESOLVED`)
- [x] Real-time STOMP WebSocket incident chat
- [x] Executive dashboard with live Recharts analytics
- [x] 100% headless Selenium test verification
