# Project Presentation Specification (10 Slides)
**Project Title:** Automated DevOps CI/CD Pipeline & Highway Emergency Dispatch Platform  
**Candidate Name:** Manan Chahal  
**Roll No:** 23102C0044  
**Class / Division:** BE Computer Engineering — Semester VII (Div C)  
**Academic Year:** 2026–2027  
**Repository:** `https://github.com/mananch1/highway-ami.git`  
**Live Production URL:** `http://15.252.18.123/`  

---

## Slide 1: Title & Project Identity

### Visual Layout & Styling
- **Theme:** Deep Navy (`#0f172a`) background with crisp white typography and electric blue (`#1d4ed8`) accents.
- **Top Bar:** Institution Name, Department of Computer Engineering, Academic Year 2026–2027.
- **Center:** High-contrast project title in bold sans-serif, with an architectural badge: `Enterprise Multi-Node DevOps Implementation`.
- **Bottom Left:** Candidate Details.
- **Bottom Right:** Guide / Evaluator Details.

### Slide Body Content
- **Project Title:** Automated DevOps CI/CD Pipeline & Highway Emergency Dispatch Platform
- **Candidate:** Manan Chahal
- **Roll No:** 23102C0044
- **Branch / Division:** BE Computer Engineering (Div C)
- **Course:** DevOps Lab & Integrated Project (Course Code: CSL702 / CSP702)
- **Deployment Platform:** Amazon Web Services (AWS) — Asia Pacific (Mumbai) `ap-south-1`

### Speaker Notes (What to verbally say)
> *"Good morning, respected examiners and faculty. I am Manan Chahal, Roll Number 23102C0044. Today, I am presenting my DevOps project: an Automated DevOps CI/CD Pipeline powering an enterprise Highway Emergency Dispatch Platform. This project demonstrates the complete DevOps lifecycle—from agile requirement gathering, Git-flow branching, and multi-stage build automation to automated Selenium quality gating, Docker containerization, Ansible configuration management, and dual-node AWS cloud deployment."*

---

## Slide 2: Problem Statement & Industry Motivation

### Visual Layout & Styling
- **Layout:** Two-column split layout.
- **Left Column:** "Traditional Legacy Challenges" (marked with red indicator dots).
- **Right Column:** "DevOps-Driven Solution" (marked with green indicator dots).
- **Center Callout:** "Target: Zero-Downtime, Sub-Second Incident Routing, and 100% Automated Quality Gating."

### Slide Body Content
- **The Operational Challenge:**
  - Highway breakdowns require urgent assistance, but legacy dispatch relies on manual telephone routing and vague landmark descriptions.
  - Lack of automated continuous integration leads to untested code reaching production, causing service outages.
  - Manual server deployments cause extended downtime and configuration drift between environments.
- **The Engineering Solution:**
  - An instant, 1-click highway dispatch web application featuring scannable highway mile-marker QR codes that auto-populate incident telemetry without GPS dependencies.
  - A fully automated Jenkins declarative pipeline that runs unit and headless browser integration tests on every commit, preventing regressions from touching production.
  - Automated configuration management using Ansible to ensure immutable, reproducible deployments across AWS EC2 instances.

### Speaker Notes (What to verbally say)
> *"In emergency roadside scenarios, every second matters. Traditional roadside assistance portals suffer from two major problems: on the user side, drivers struggle to convey their exact location during a breakdown; on the operational side, development teams struggle with manual deployments that frequently break in production. Our platform addresses both. We built an emergency portal that uses highway marker QR codes for instant location capture, backed by a hardened, automated DevOps pipeline that guarantees only thoroughly tested code is deployed."*

---

## Slide 3: Project Objectives & DevOps Scope

### Visual Layout & Styling
- **Layout:** 4-quadrant grid displaying core DevOps pillars: Plan, Code & Build, Test & Gate, Deploy & Monitor.
- **Icons/Badges:** Minimalist geometric status badges.

### Slide Body Content
1. **Agile Planning & Source Control:** Implement Git-flow branching with structured commit conventions and release tagging (`v1.0.0-mvp`, `v1.0.0-aws`, `v1.1.0-cloud-qr`).
2. **Unified Multi-Tier Build Automation:** Automate both React frontend compilation (Node.js/npm) and Spring Boot Java 21 compilation into a monolithic, deployable `ROOT.war` using Maven.
3. **Continuous Automated Testing & Gating:** Integrate Spring Boot unit tests and headless Chrome Selenium E2E user journeys directly into the Jenkins pipeline to block faulty builds.
4. **Containerized Multi-Service Deployment:** Orchestrate Spring Boot and PostgreSQL 16 using Docker Compose with persistent storage volumes.
5. **Configuration Management & Cloud Hardening:** Utilize Ansible playbooks for zero-downtime rolling updates over private AWS VPC networks, completely secured with strict Security Groups.

### Speaker Notes (What to verbally say)
> *"Our project scope directly satisfies the 15 prescribed tasks of the DevOps syllabus. Our objectives were not just to write code, but to establish an immutable pipeline: code pushed to GitHub triggers automated compilation, automated testing in headless Linux browsers, automatic packaging, and Ansible-driven deployment to AWS. Every step is automated, traceable, and secure."*

---

## Slide 4: System Architecture & AWS Cloud Topology

### Visual Layout & Styling
- **Layout:** Architectural schematic diagram showing developer workstation, GitHub, AWS VPC, and the dual EC2 node layout.
- **Highlight:** Blue dashed boundary representing AWS Virtual Private Cloud (`ap-south-1`).

### Slide Body Content
- **Node 1: CI/CD Controller & Ansible Engine**
  - Instance: AWS EC2 `t3.small` (Ubuntu 24.04 LTS)
  - Services: Jenkins LTS 2.580.1, OpenJDK 21, Maven 3.9, Google Chrome Headless, Ansible Engine.
  - Security Group: Port 22 (SSH) & Port 8080 (Jenkins UI) restricted strictly to administrator IP.
- **Node 2: Production Host**
  - Instance: AWS EC2 `t3.small` (Ubuntu 24.04 LTS)
  - Services: Docker Engine 29.x, Docker Compose.
  - Multi-Container Stack: `road-helper-app` (Tomcat / Spring Boot, Port 80) and `roadhelper_db` (PostgreSQL 16, Port 5432).
  - Security Group: Port 80 public; Port 22 accessible **only** via internal VPC private IP (`172.31.15.50`) from Node 1.

```
[Developer] ──git push──> [GitHub] ──Webhook──> [AWS Node 1: Jenkins Controller]
                                                         │
                                                  Ansible over SSH
                                                 (VPC: 172.31.15.50)
                                                         ▼
                                            [AWS Node 2: Production Host]
                                            ├── Docker: road-helper-app (Port 80)
                                            └── Docker: roadhelper_db (Postgres)
```

### Speaker Notes (What to verbally say)
> *"Here is our cloud infrastructure on AWS Mumbai. We separated our architecture into two isolated EC2 nodes within an AWS VPC. Node 1 is our Jenkins CI Controller and Ansible Master. Node 2 is our Production Host running Docker Compose. Notice our security posture: production SSH is not exposed to the public internet—Ansible deploys over the internal private VPC subnet using private IP 172.31.15.50. This guarantees zero public attack surface on our production management port."*

---

## Slide 5: Agile Planning & Git Branching Strategy

### Visual Layout & Styling
- **Layout:** Horizontal Git branching timeline showing `feature/*` branches merging into `main`, tagged with milestone releases.
- **Table:** Sprint Backlog & Deliverable Matrix.

### Slide Body Content
- **Agile Scrum Methodology:**
  - User Stories broken into sprint deliverables covering guest callers, authenticated technicians, and dispatch coordinators.
  - Tracked via GitHub Issues, automated pull request workflows, and markdown Kanban boards.
- **Git Branching Strategy (Git-Flow):**
  - `main`: Production-ready, deployable source code.
  - `feature/guest-dispatch`: 1-click intake form and highway QR marker parser.
  - `feature/technician-console`: Technician availability toggle and WebSocket live chat.
  - `feature/aws-hardening`: Security group automation and dynamic `.env` injection.
- **Semantic Release Tagging:**
  - `v1.0.0-mvp`: Core functional portal baseline (Task 7 deliverable).
  - `v1.0.0-aws`: Verified AWS cloud deployment with Ansible automation.
  - `v1.1.0-cloud-qr`: Enhanced enterprise UI, QR placard generator, and automated test gating.

### Speaker Notes (What to verbally say)
> *"In accordance with Tasks 3, 5, 6, and 7 of our syllabus, we practiced strict Agile source control. Development occurred across isolated feature branches. Before merging into `main`, changes were tested locally. We tagged each verified milestone using semantic version tags on GitHub: `v1.0.0-mvp` established our baseline, and `v1.1.0-cloud-qr` represents our live production release. No code is committed directly without tracking."*

---

## Slide 6: Continuous Integration & Build Automation

### Visual Layout & Styling
- **Layout:** 3-stage visual pipeline flow with Maven and Node compilation callouts.
- **Code Block:** Highlighted snippet from `pom.xml` showing `frontend-maven-plugin`.

### Slide Body Content
- **Unified Build with Maven (`pom.xml`):**
  - Solved the challenge of deploying a React SPA + Spring Boot application as a single artifact.
  - **`frontend-maven-plugin` (v1.15.1):** Installs isolated Node.js (`v20.18.0`) and npm into `target/`, then executes `npm run build` inside `frontend/`.
  - **`maven-resources-plugin`:** Copies the compiled assets (`frontend/dist/`) into `target/classes/static/`.
  - **`spring-boot-maven-plugin`:** Packages the entire application, static UI, and embedded Tomcat into `ROOT.war`.
- **Jenkins Declarative Pipeline (`Jenkinsfile.aws`):**
  - `stage('Checkout Source')`: Fetches verified branch from Git.
  - `stage('Build & Unit Tests')`: Executes `./mvnw test` with JUnit 5 tests.
  - `stage('Package Application')`: Runs `./mvnw package -DskipTests` and archives `ROOT.war`.

### Speaker Notes (What to verbally say)
> *"For Task 8 and 9, we automated the entire build lifecycle using a single Declarative Jenkinsfile. A common issue in full-stack projects is managing separate frontend and backend deployments. We solved this using the `frontend-maven-plugin`. Maven downloads Node.js, compiles the React Vite frontend, embeds the static bundle into Spring Boot's static resources, and packages a unified `ROOT.war` in under 90 seconds. This guarantees that frontend and backend versions are always perfectly synchronized."*

---

## Slide 7: Continuous Testing & Automated Quality Gating

### Visual Layout & Styling
- **Layout:** Side-by-side comparison of Test Suite Metrics vs. The Live Failure Gating Experiment.
- **Callout Box:** Red alert box illustrating the deliberate bug experiment and screenshot capture.

### Slide Body Content
- **Comprehensive Multi-Tier Test Suite:**
  - **Unit Testing:** 4 Spring Boot unit tests (`IncidentServiceTest`, `RoadHelperApplicationTests`) validating business logic and repository transactions.
  - **E2E Browser Testing:** 5 automated journeys in [`RoadHelperSeleniumIT.java`](file:///D:/DOCS/VIT%20Ebooks/Fourth%20Year/Sem%207/DEVOPS/Project/src/test/java/com/mananc/road_helper/selenium/RoadHelperSeleniumIT.java) executing in Headless Chrome (`--headless=new`).
- **Automated Failure Gating Experiment (Proof of Concept):**
  - **The Experiment:** In commit `012856f`, we introduced a deliberate regression error banner (`Emergency Dispatch API Cluster Offline`) breaking the portal header.
  - **The Detection:** Selenium Journey 1 caught the assertion failure on `contains("Roadside Assistance Portal")`.
  - **Failure Artifact Archiving:** [`SeleniumScreenshotUtil`](file:///D:/DOCS/VIT%20Ebooks/Fourth%20Year/Sem%207/DEVOPS/Project/src/test/java/com/mananc/road_helper/selenium/SeleniumScreenshotUtil.java) captured `Journey1_GuestEmergency_*.png` and archived it in Jenkins.
  - **The Gating Action:** Jenkins halted the build at Stage 4. **Ansible Deploy (Stage 5) was completely skipped**, preventing broken code from touching production.
  - **The Recovery:** Commit `dcd379e` resolved the regression; Jenkins turned **GREEN** and deployed to AWS.

### Speaker Notes (What to verbally say)
> *"Continuous Testing—Tasks 10 and 11—is the core safety gate of any true DevOps pipeline. To prove to our examiners that our test gate works, we conducted a real experiment. We deliberately introduced a UI regression in commit `012856f`. When Jenkins ran, our headless Chrome Selenium test immediately caught the failure, captured a full browser screenshot showing the error, and halted the pipeline. Ansible deployment was blocked, keeping production 100% operational. Ten minutes later, we pushed the fix commit `dcd379e`, and the pipeline turned green and deployed automatically."*

---

## Slide 8: Containerization & Ansible CD Deployment

### Visual Layout & Styling
- **Layout:** Docker Compose architecture on the left; Ansible playbook execution flow on the right.
- **Status Badge:** `Healthcheck: HTTP 200 OK (Verified)`.

### Slide Body Content
- **Docker Multi-Container Architecture (`docker-compose.aws.yml`):**
  - **Web Application (`road-helper-app`):** Tomcat container hosting `ROOT.war` on Port 80/8080.
  - **Database (`roadhelper_db`):** PostgreSQL 16 Alpine container with named Docker volume (`postgres_data`) for permanent data persistence across container restarts.
- **Ansible Configuration Management (`ansible/playbook_aws.yml`):**
  - **Task 1–3:** Fact gathering and verifying Docker runtime on `172.31.15.50`.
  - **Task 4–5:** Synchronizes `docker-compose.aws.yml` and SCPs freshly built `ROOT.war`.
  - **Task 6–7:** Idempotent rolling container restart (`docker compose restart app`).
  - **Task 8:** Records ISO 8601 deployment metadata to `release_metadata.txt`.
  - **Task 9–10:** Automated healthcheck validation polling `http://127.0.0.1:80/` until HTTP 200 is confirmed.

### Speaker Notes (What to verbally say)
> *"For Tasks 12, 13, and 14, we implemented declarative containerization and idempotent deployment. We orchestrated our webapp and PostgreSQL database using Docker Compose, ensuring database data is persisted using Docker named volumes. Deployment is executed entirely by Ansible. Our playbook transfers the WAR artifact, triggers a rolling container restart, logs deployment timestamps, and runs an automated healthcheck retry loop. If Tomcat doesn't return HTTP 200 within 15 retries, Ansible fails the build."*

---

## Slide 9: Highway QR Marker Innovation & Enterprise UI

### Visual Layout & Styling
- **Layout:** Screenshot showcase of the live production UI: the Highway Marker Placard Generator, the clean intake form, and the 4-step dispatch tracker.
- **Badges:** `Zero Emojis`, `Corporate Design System`, `Mobile Responsive <= 768px`.

### Slide Body Content
- **Highway Mile-Marker QR System:**
  - Highway markers encode URL parameters: `http://15.252.18.123/?loc=NH-48+Km+42&type=FLAT_TIRE`.
  - Built-in SVG QR Placard Generator allows drivers and highway patrol to scan placards directly from their smartphone camera, instantly auto-populating incident details without GPS errors.
- **Enterprise Design Standards (Zero Emojis):**
  - Designed to strict corporate dispatch standards (AAA / Department of Transportation aesthetic).
  - Executive slate and navy color palette (`#0f172a`, `#1d4ed8`, `#cbd5e1`).
  - 100% vector SVG icons with zero consumer emojis.
- **Universal Device Responsiveness:**
  - Fully responsive breakpoints (`@media (max-width: 768px)`).
  - Mobile hamburger drawer, high-contrast touch targets, and vertical progress stepper (`Logged` $\rightarrow$ `Dispatched` $\rightarrow$ `En Route` $\rightarrow$ `Resolved`).

### Speaker Notes (What to verbally say)
> *"Here is our user-facing platform. We implemented an innovative Highway Mile-Marker QR system. Stranded motorists can simply point their smartphone camera at a physical highway placard, and our web portal automatically parses the corridor, marker number, and service category via URL query parameters. Furthermore, following professional software guidelines, we stripped all emojis and implemented a clean, corporate slate-and-navy design system that functions seamlessly on both desktop workstations and mobile smartphones."*

---

## Slide 10: Production Verification, Incident Defense & Conclusion

### Visual Layout & Styling
- **Layout:** Project Summary table, live evaluation metrics, and final conclusion callout.
- **Footer:** Direct links to live AWS IP and GitHub repository.

### Slide Body Content
- **Live AWS Production Verification:**
  - Verified live at **`http://15.252.18.123/`** (Port 80) and **`http://15.252.18.123:8080/`**.
  - All 15 tasks of `CMPN-C.xlsx` completed, documented, and verified.
- **Real-World Engineering & Cloud Defense:**
  - Successfully defended against an internet botnet exploit by terminating the contaminated VM, re-provisioning via automated script, and enforcing strict AWS Security Group IP restrictions (`My IP` only).
  - Demonstrated resilient zero-downtime rolling updates and private VPC networking.
- **Future Enhancements:**
  - Multi-region AWS deployment with Elastic Load Balancer (ALB) and Auto Scaling Groups (ASG).
  - Integration with highway department toll-plaza APIs and SMS dispatch notifications via AWS SNS.

### Speaker Notes (What to verbally say)
> *"To conclude, this project successfully bridges the gap between software development and cloud operations. We built a real-time, life-saving highway emergency system and proved every concept of the DevOps syllabus: automated multi-tier builds, automated quality gating with failure screenshots, immutable containerization, idempotent Ansible deployment, and real-world cloud security remediation. The application is running live right now on AWS Mumbai at 15.252.18.123. Thank you, and I am now open to your questions."*
