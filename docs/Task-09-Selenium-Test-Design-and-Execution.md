# Task 9: Selenium Test Design and Local Execution

**Student:** Manan Chahal (Roll No: 23102C0044)  
**Project Title:** DevOps Pipeline for a Roadside Assistance Portal  
**Class/Division:** BE VII - Division C  

---

## 1. Test Strategy & Test Plan

Automated functional regression testing is implemented with **Selenium WebDriver 4.x** executing against a live Spring Boot servlet environment on a randomized port (`RANDOM_PORT`).

### Test Architecture:
- **Framework:** JUnit 5 + Selenium Java 4.27.0
- **Browser Execution:** Headless Google Chrome (fallback to Microsoft Edge) with flags `--headless=new`, `--disable-gpu`, `--no-sandbox`.
- **Failure Diagnostic:** `SeleniumScreenshotUtil` automatically captures timestamped full-screen screenshots saved to `target/screenshots/` upon assertion failure.

---

## 2. Five Critical User Journeys Tested

| Journey # | Test Method | Flow Description | Assertions Verified |
|-----------|-------------|------------------|---------------------|
| **1** | `testJourney1GuestEmergencyRequest` | Guest visits `/`, completes emergency request form (name, phone, location, incident type `FLAT_TIRE`), clicks submit. | Heading text contains portal name; URL redirects to `/emergency/status`; status badge or incident reference present. |
| **2** | `testJourney2CustomerLoginFlow` | Customer visits `/login`, submits valid credentials. | Redirects to `/customer` dashboard; authenticated session established. |
| **3** | `testJourney3TechnicianWorkflow` | Technician logs in at `/login`, views assigned queue. | Redirects to `/technician` dashboard; availability controls visible. |
| **4** | `testJourney4AdminDashboardFlow` | Administrator logs in, accesses executive view at `/admin`. | Analytics dashboard loads; metrics and charts rendered. |
| **5** | `testJourney5IncidentSearchFlow` | User visits `/search`, types search query into search bar. | Search view and input controls present and responsive. |

---

## 3. Local Execution Log & Test Report

```
[INFO] -------------------------------------------------------
[INFO] Running com.mananc.road_helper.selenium.RoadHelperSeleniumIT
2026-10-07T19:01:30.584+05:30  INFO TomcatWebServer : Tomcat started on port 62439 (http) with context path '/'
2026-10-07T19:01:36.791+05:30  INFO NotificationService : [MOCK] Notifying TOW_TRUCK for incident #1
[INFO] Tests run: 5, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 25.33 s -- in com.mananc.road_helper.selenium.RoadHelperSeleniumIT
[INFO] 
[INFO] Results:
[INFO] 
[INFO] Tests run: 5, Failures: 0, Errors: 0, Skipped: 0
[INFO] 
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
```

### Failure Screenshot Mechanism Verification:
Diagnostic screenshot utility was verified by intentionally validating screenshot generation in `target/screenshots/`:
- `target/screenshots/Journey2_CustomerLogin_20261007_185612_559.png`
- `target/screenshots/Journey3_TechnicianWorkflow_20261007_185624_737.png`
- `target/screenshots/Journey4_AdminDashboard_20261007_185637_523.png`
- `target/screenshots/Journey5_IncidentSearch_20261007_185649_726.png`
