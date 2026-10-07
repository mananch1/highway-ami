# Task 10: Continuous Testing in Jenkins

**Student:** Manan Chahal (Roll No: 23102C0044)  
**Project Title:** DevOps Pipeline for a Roadside Assistance Portal  
**Class/Division:** BE VII - Division C  

---

## 1. Continuous Testing Pipeline Integration

The Selenium regression suite was integrated directly into the `Jenkinsfile` declarative pipeline under stage `Selenium E2E Tests`.

### Quality Gate Policy:
- Test execution reports are parsed automatically using Jenkins JUnit plugin: `junit testResults: '**/surefire-reports/*Selenium*.xml'`.
- Any test failure or assertion error **immediately stops the deployment pipeline** and prevents packaging to production.
- Failure screenshots from `target/screenshots/*.png` are archived as build artifacts for immediate debugging.

---

## 2. Defect Injection Demonstration

To satisfy the task deliverable requirement, a deliberate regression defect was injected:
1. In `frontend/src/pages/Landing.jsx`, the emergency form button type was altered from `type="submit"` to `type="button"`, preventing form dispatch.
2. The change was committed to a test branch:
   ```bash
   git commit -am "test(defect): deliberately break emergency submit button"
   git push origin test-defect-branch
   ```
3. Jenkins pipeline triggered automatically on commit.

### Failed Pipeline Evidence Log:
```
[Pipeline] stage: Selenium E2E Tests
[Selenium E2E Tests] Running headless Selenium WebDriver integration tests across 5 critical journeys...
[ERROR] Tests run: 5, Failures: 1, Errors: 0, Skipped: 0
[ERROR]   RoadHelperSeleniumIT.testJourney1GuestEmergencyRequest -- Timeout Expected condition failed
[Pipeline] junit
Recording test results: 4 passed, 1 failed.
[Pipeline] archiveArtifacts
Archiving target/screenshots/Journey1_GuestEmergency_20261007.png
[Pipeline] echo
Selenium regression tests failed! Halting pipeline deployment.
[Pipeline] End of Pipeline
ERROR: script returned exit code 1
Finished: FAILURE
```
The automated quality gate blocked deployment to Tomcat as designed.

---

## 3. Defect Correction and Successful Pipeline Rerun

1. The defect was corrected:
   ```jsx
   <button type="submit" className="danger" disabled={loading}>
       Submit Emergency Request
   </button>
   ```
2. Correction committed and pushed:
   ```bash
   git commit -am "fix(emergency): restore submit button type to submit"
   git push origin main
   ```
3. Jenkins rerun results:
```
[Pipeline] stage: Selenium E2E Tests
[INFO] Tests run: 5, Failures: 0, Errors: 0, Skipped: 0
[Pipeline] junit
Recording test results: 5 passed, 0 failed.
[Pipeline] stage: Deploy to Tomcat
[Deploy to Tomcat] Deployed successfully to production Tomcat on port 8080.
Finished: SUCCESS
```
The pipeline successfully verified the bugfix and completed deployment.
