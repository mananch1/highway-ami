# Task 7: Jenkins Installation and Continuous Integration Job

**Student:** Manan Chahal (Roll No: 23102C0044)  
**Project Title:** DevOps Pipeline for a Roadside Assistance Portal  
**Class/Division:** BE VII - Division C  

---

## 1. Jenkins Environment & Setup

- **Platform:** Windows 11 Native Installation
- **Jenkins Version:** LTS
- **Service Name:** `Jenkins` (configured on default port `8080` or alternate port `8085` if port 8080 is used by app)
- **Java Home:** `C:\Program Files\Java\jdk-21`
- **Maven Home:** Configured in Jenkins Global Tool Configuration as `Maven-3.9`

---

## 2. CI Job Configuration

1. **Job Type:** Freestyle Project / Maven Project named `Roadside-Assistance-CI`
2. **Source Code Management:**
   - Repository URL: `https://github.com/mananch1/highway-ami.git`
   - Branch Specifier: `*/main`
3. **Build Triggers:**
   - GitHub hook trigger for GITScm polling
   - Poll SCM: `H/5 * * * *` (Every 5 minutes)
4. **Build Steps:**
   - Invoke Maven Top-Level Targets: `clean test-compile test war:war`
5. **Post-Build Actions:**
   - **Archive the artifacts:** `target/*.war`
   - **Publish JUnit test result report:** `**/surefire-reports/*.xml`

---

## 3. Successful Build Log Evidence

```
Started by user Manan Chahal
Running as SYSTEM
Building in workspace C:\ProgramData\Jenkins\.jenkins\workspace\Roadside-Assistance-CI
The recommended git tool is: NONE
using credential github-auth
 > git.exe rev-parse --resolve-git-dir C:\ProgramData\Jenkins\.jenkins\workspace\Roadside-Assistance-CI\.git
Fetching changes from the remote Git repository
 > git.exe config remote.origin.url https://github.com/mananch1/highway-ami.git
Fetching upstream changes from origin
 > git.exe fetch --tags --force --progress -- origin +refs/heads/*:refs/remotes/origin/*
Checking out Revision 6cab87b... (origin/main)
[Roadside-Assistance-CI] $ .\mvnw.cmd clean test war:war
[INFO] Scanning for projects...
[INFO] Building road-helper 0.0.1-SNAPSHOT [war]
[INFO] --- frontend-maven-plugin:1.15.1:npm (npm run build) ---
[INFO] dist/index.html                   0.41 kB
[INFO] dist/assets/index-1eXzAZLU.js   704.88 kB
[INFO] --- compiler:3.15.0:compile ---
[INFO] Compiling 44 source files with javac [release 21] to target\classes
[INFO] --- surefire:3.5.6:test ---
[INFO] Running com.mananc.road_helper.RoadHelperApplicationTests
[INFO] Tests run: 1, Failures: 0, Errors: 0, Skipped: 0
[INFO] Running com.mananc.road_helper.service.IncidentServiceTest
[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0
[INFO] --- war:3.5.1:war ---
[INFO] Building war: target\road-helper-0.0.1-SNAPSHOT.war
[INFO] BUILD SUCCESS
[INFO] Total time: 54.218 s
Archiving artifacts: target/road-helper-0.0.1-SNAPSHOT.war
Recording test results: 4 tests passed, 0 failures.
Finished: SUCCESS
```
