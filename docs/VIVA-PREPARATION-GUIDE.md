# Comprehensive DevOps Viva Preparation Guide
**Candidate:** Manan Chahal (Roll No: 23102C0044)  
**Project:** Roadside Assistance & Highway Emergency Dispatch Portal (`highway-ami`)  
**Target Environment:** AWS Mumbai (`ap-south-1`) Multi-Node Architecture  
**Repository:** `https://github.com/mananch1/highway-ami.git`

---

## 1. Project Architecture & End-to-End Workflow

### High-Level Architecture
```
 Developer Workstation (Windows 11)
      │
      │  git push origin main
      ▼
 GitHub Repository (`highway-ami`)
      │
      │  Webhook Trigger (POST /github-webhook/)
      ▼
 [Node 1: AWS EC2 - Jenkins Controller & Ansible Master] (t3.small, Ubuntu 24.04)
      ├── 1. Checkout Source (`main` branch)
      ├── 2. Build & Unit Tests (`./mvnw test` + Java 21 + JUnit 5)
      ├── 3. Package Application (`frontend-maven-plugin` bundles React → `ROOT.war`)
      ├── 4. Headless Selenium E2E Tests (Headless Chrome in Linux, 5 Journeys)
      │      └── Failure Gating: Halts on failure, archives screenshot to Jenkins
      └── 5. Ansible Deployment (`ansible/playbook_aws.yml` over internal AWS VPC SSH)
                  │
                  ▼
 [Node 2: AWS EC2 - Production Host] (t3.small, Ubuntu 24.04, Docker 29.x)
      ├── Docker Compose Multi-Container Stack:
      │      ├── PostgreSQL 16 Database (`roadhelper_db`, persistent volume)
      │      └── Apache Tomcat / Spring Boot Webapp (`road-helper-app`, Port 80/8080)
      ├── Rolling Zero-Downtime Container Restart
      ├── Automated Health Check Retries (`http://127.0.0.1:80/` HTTP 200)
      └── Deployment Metadata Logging (`release_metadata.txt`)
```

---

## 2. Core DevOps Tech Stack & Project Implementation

| Technology | Role in Project | Specific Project Implementation |
| :--- | :--- | :--- |
| **Git & GitHub** | Version Control & CI Triggers | Feature branching, release tags (`v1.0.0-mvp`, `v1.0.0-aws`, `v1.1.0-cloud-qr`), Webhooks with dedicated endpoints. |
| **Java 21 & Spring Boot 4** | Backend REST & WebSocket Core | Spring WebMVC, Spring Security (JWT auth), Spring Data JPA, SockJS/STOMP WebSockets for live driver-technician chat. |
| **React 18 & Vite** | Responsive Enterprise Frontend | Single-Page Application (SPA) with zero emojis, Highway QR Code auto-fill parameter parsing (`?loc=...&type=...`), 4-step dispatch progress stepper. |
| **Maven** | Build Automation & Dependency Lifecycle | Multi-tier lifecycle: runs `frontend-maven-plugin` (Node 20 + npm build), copies `dist/` to `classes/static/`, and packages monolithic `ROOT.war`. |
| **Selenium WebDriver** | Continuous E2E Browser Testing | Headless Chrome in Linux CI, executes 5 real user journeys (Guest emergency intake, Customer auth, Technician dispatch, Admin analytics, Search). |
| **Jenkins** | Continuous Integration & Automated Gating | Declarative Pipeline (`Jenkinsfile.aws`), automated test gating, JUnit XML result publisher, artifact archiving for failure screenshots. |
| **Docker & Compose** | Container Runtime & Multi-Service Orchestration | `docker-compose.aws.yml` orchestrates Spring Boot app + PostgreSQL 16 container network with named volumes and restart policies. |
| **Ansible** | Idempotent Configuration Management | `ansible/playbook_aws.yml` provisions directories, syncs compose files, SCPs WAR artifact, restarts containers, logs metadata, and polls healthchecks. |
| **AWS Cloud (EC2)** | Cloud Infrastructure & Networking | Dual-node setup in Mumbai (`ap-south-1`) inside a VPC, strict Security Group isolation (controller to prod over private IP `172.31.15.50`), zero IP leakage in Git. |

---

## 3. The 15 Academic Tasks Breakdown (`CMPN-C.xlsx`)

If the examiner asks: *"Walk me through the 15 tasks of your DevOps syllabus"*, answer concisely:

1. **Task 1: DevOps Pipeline Definition:** Defined high-level architecture for a high-availability Roadside Assistance Portal.
2. **Task 2: Problem Scope:** High latency in emergency dispatch solved via instant guest 1-click routing and highway QR markers.
3. **Task 3: Agile Planning:** Sprint backlog, user stories, and DevOps Kanban workflow documented in `docs/Task-02`.
4. **Task 4: Requirements & Tech Stack:** Java 21, React, Spring Boot, Docker, Ansible, Jenkins, Selenium.
5. **Task 5: Git Repository Setup:** Initialized GitHub repository with `.gitignore`, issue templates, and README.
6. **Task 6: Feature Branching:** Implemented Git-flow model (`feature/guest-dispatch`, `feature/technician-console`, `main`).
7. **Task 7: MVP Baseline & Git Tagging:** Tagged official milestone releases (`v1.0.0-mvp`, `v1.0.0-aws`, `v1.1.0-cloud-qr`).
8. **Task 8: Jenkins CI Job Configuration:** Configured pipeline polling, automated workspace cleans, and build environment tuning.
9. **Task 9: Pipeline as Code:** Implemented declarative syntax in `Jenkinsfile.aws`.
10. **Task 10: Selenium E2E Testing:** Automated 5 browser journeys with headless Chrome and failure screenshot capture.
11. **Task 11: Continuous Testing & Gating:** JUnit XML test reports integrated into Jenkins; build halts on test failure.
12. **Task 12: Docker Multi-Container Lifecycle:** Configured Dockerfile and `docker-compose.aws.yml` for database + web service.
13. **Task 13: Container Registry Integration:** Docker Hub automated repository tags (`mananch1/road-helper`).
14. **Task 14: Ansible Configuration Management:** Playbook automation for artifact deployment and container state enforcement.
15. **Task 15: Automated Provisioning & Validation:** Post-deployment HTTP 200 healthcheck loop with automated retry logic.

---

## 4. Top Examiner Questions & Model Answers

### Category A: Core DevOps Philosophy & Architecture

#### Q1: What is the core difference between Agile and DevOps?
> **Model Answer:**  
> Agile focuses on iterative software development, rapid feature delivery, and close collaboration between developers and product managers. DevOps extends Agile into operations—bridging the gap between Development and Operations through automation, continuous integration, continuous delivery (CI/CD), infrastructure as code, and automated monitoring. Agile delivers working code; DevOps ensures working code runs reliably in production.

#### Q2: What is the difference between Continuous Delivery and Continuous Deployment?
> **Model Answer:**  
> - **Continuous Delivery:** Code is continuously built, tested, and packaged so that every commit is always in a deployable state. Deploying to production requires an explicit trigger or business approval.  
> - **Continuous Deployment:** Every commit that passes the automated CI/CD pipeline and automated test gates is deployed directly into production with zero manual intervention.  
> In our project, Jenkins and Ansible execute **Continuous Deployment** to AWS production upon pushing to `main`.

#### Q3: Why did you choose Pipeline as Code (`Jenkinsfile`) over classic freestyle UI jobs?
> **Model Answer:**  
> 1. **Version Control:** Pipeline definitions are stored alongside source code in Git, allowing peer reviews, commit history, and rollbacks.  
> 2. **Disaster Recovery:** If the Jenkins server crashes or is reprovisioned, the pipeline is instantly recreated by pointing to the repository.  
> 3. **Auditability & Traceability:** Every change to the build, test, or deployment logic is tracked via commit logs.

---

### Category B: Maven, React & Build Automation

#### Q4: How does your React frontend get compiled and packaged with your Spring Boot backend?
> **Model Answer:**  
> We use the **`frontend-maven-plugin`** in our `pom.xml`. During Maven's `compile` phase:
> 1. It downloads isolated Node.js (`v20.18.0`) and npm into `target/`.
> 2. It executes `npm install` and `npm run build` inside `frontend/`.
> 3. Maven's `maven-resources-plugin` copies the compiled static assets (`frontend/dist/`) into `target/classes/static/`.
> 4. Spring Boot bundles everything into a unified `ROOT.war`, which is served by Tomcat on port 80/8080.

#### Q5: Why did you package the project as a `WAR` instead of a standalone `JAR`?
> **Model Answer:**  
> A `WAR` file allows standard deployment into enterprise servlet containers (like Apache Tomcat). It provides flexibility: it can be executed as a standalone executable via Spring Boot's embedded Tomcat (`java -jar road-helper.war`) or deployed into standard multi-tenant application servers in corporate data centers.

---

### Category C: Continuous Testing & Selenium E2E Automation

#### Q6: Why did you use headless mode for Selenium in your Jenkins pipeline?
> **Model Answer:**  
> Linux EC2 instances run without a Graphical User Interface (X11 display server). Running standard Chrome would fail with `No DISPLAY environment variable`. Headless mode (`--headless=new`) allows Chrome to render DOM trees, execute JavaScript, simulate mouse clicks, and take full-page screenshots in memory without needing a physical monitor.

#### Q7: How does your pipeline implement "Automated Quality Gating"?
> **Model Answer:**  
> In `Jenkinsfile.aws`, the `Selenium E2E Tests` stage runs before `Ansible Deploy to AWS Prod`. If any of the 5 browser journeys fail (e.g., an assertion fails or an element times out), the stage throws an error. Jenkins marks the build **FAILED**, triggers the `post { failure }` action, archives the failure screenshot, and **halts execution immediately**, ensuring broken code is blocked before Ansible touches production.

#### Q8: Can you explain the deliberate bug experiment you conducted in your pipeline?
> **Model Answer:**  
> To verify that our Selenium test gate actually catches regressions and protects production:
> 1. We introduced a deliberate regression in commit `012856f` (an error banner and broken heading on the emergency intake form).
> 2. When Jenkins ran, `Journey 1` failed assertion `contains("Roadside Assistance Portal")`.
> 3. Selenium's `SeleniumScreenshotUtil` caught the exception, captured `Journey1_GuestEmergency_*.png`, and Jenkins archived the screenshot as a build artifact.
> 4. Jenkins halted the pipeline, skipping the Ansible deploy stage. Production remained safe on the previous working build.
> 5. Ten minutes later, commit `dcd379e` resolved the regression. Jenkins built it, all 5 tests passed, and Ansible successfully updated production.

---

### Category D: Containerization & Docker Compose

#### Q9: What is the difference between a Docker container and a Virtual Machine?
> **Model Answer:**  
> A Virtual Machine virtualizes physical hardware via a hypervisor (e.g., KVM, VMware), requiring a complete guest operating system, kernel, and dedicated RAM/CPU allocation. A Docker container virtualizes at the OS level, sharing the host Linux kernel while isolating processes via Linux `namespaces` (for PID, network, mount) and `cgroups` (for resource limits). Containers start in seconds and use negligible overhead.

#### Q10: How do you prevent data loss in PostgreSQL when the container restarts?
> **Model Answer:**  
> In `docker-compose.aws.yml`, we use a Docker named volume (`postgres_data:/var/lib/postgresql/data`). Even if the database container is stopped, removed, or recreated during an application update, the underlying database files persist on the host EC2 disk and are reattached immediately upon restart.

---

### Category E: Ansible & Configuration Management

#### Q11: What is "Idempotence" in Ansible, and why is it crucial?
> **Model Answer:**  
> Idempotence means running an Ansible playbook once or a hundred times produces the exact same end state without causing duplicate actions or unintended side effects. If a directory already exists, Ansible reports `ok` instead of throwing an error or re-creating it. In our playbook (`ansible/playbook_aws.yml`), Task 7 only restarts the container `when: war_copy.changed`—meaning if the WAR file did not change, the running container is not unnecessarily restarted.

#### Q12: Why use Ansible instead of a custom bash script for deployment?
> **Model Answer:**  
> 1. **Idempotency & State Enforcement:** Bash scripts execute imperatively and fail if a step isn't manually guarded. Ansible defines desired state declaratively.  
> 2. **Agentless Architecture:** Ansible uses standard SSH; no background agent needs to run on target servers.  
> 3. **Built-in Error Handling & Rollbacks:** Ansible provides structured tasks, facts gathering, handlers, and retry loops (e.g., our Task 9 automated healthcheck retry).

---

### Category F: Cloud Security & Real-World Incident Handling

#### Q13: What happened during the Azure / AWS security incident, and how did you resolve it?
> **Model Answer:**  
> - **The Issue:** Initially, port 8080 was opened to `0.0.0.0/0` (Anywhere) on the cloud server. Within hours, automated internet botnets scanning public IP ranges compromised the VM and injected an unauthorized binary (`blacked.x86`, a Mirai variant) that generated outbound flood traffic.  
> - **The Root Cause:** Exposing management ports (8080/SSH) to the entire public internet without network-level restrictions.  
> - **Remediation & Hardening:**  
>   1. Terminated the contaminated instance immediately (security best practice: immutable infrastructure over trying to clean malware).  
>   2. Re-provisioned a clean, hardened instance using our automated setup script (`aws_setup_jenkins_vm.sh`).  
>   3. Enforced strict **AWS Security Groups**: Port 8080 and Port 22 are locked to **`My IP` only**.  
>   4. Inter-node communication (Jenkins Controller to Production Host) communicates strictly over **AWS private VPC IPs (`172.31.15.50`)**, making production SSH completely invisible to the internet.  
>   5. Removed all credentials and private IP addresses from Git, injecting them dynamically via `/var/lib/jenkins/.env`.

#### Q14: What is the difference between an AWS Security Group and a Network ACL (NACL)?
> **Model Answer:**  
> - **Security Group:** Operates at the **instance level**, is **stateful** (if inbound traffic is allowed, outbound response is automatically allowed regardless of outbound rules), and supports only `ALLOW` rules.  
> - **Network ACL:** Operates at the **subnet level**, is **stateless** (inbound and outbound rules must be explicitly configured for two-way communication), and supports both `ALLOW` and `DENY` rules evaluated in numbered order.

---

## 5. Golden Cheat Sheet for the Viva

| Keyword | 1-Sentence Quick Definition |
| :--- | :--- |
| **CI (Continuous Integration)** | Automatically building and testing code on every push to detect integration errors early. |
| **CD (Continuous Delivery)** | Keeping code in a constantly deployable state, verified by automated end-to-end tests. |
| **Declarative Pipeline** | A structured, syntax-checked Jenkins pipeline (`pipeline { agent any stages { ... } }`). |
| **Selenium WebDriver** | A browser automation framework to validate actual user behavior (clicks, forms, navigation). |
| **Docker Compose** | A tool for defining and running multi-container Docker applications via a single YAML file. |
| **Ansible Playbook** | A YAML file containing tasks that declare the desired state of managed servers over SSH. |
| **Idempotence** | The property where repeated executions result in the same system state without errors. |
| **Headless Browser** | A web browser without a GUI, executing in memory for high-speed automated testing in CI. |
| **VPC (Virtual Private Cloud)** | A logically isolated virtual network dedicated to your AWS account. |
| **Security Group** | A virtual stateful firewall controlling inbound and outbound traffic for an EC2 instance. |
