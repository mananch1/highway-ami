# Task 15: Consolidated DevOps Project Report

**Project Title:** DevOps Pipeline for a Roadside Assistance Portal  
**Student Name:** Manan Chahal  
**Student Roll No / ID:** 23102C0044  
**Class / Division:** BE VII - Division C  
**Academic Year:** 2026-27 ODD Sem  
**Department:** Computer Engineering  
**Institution:** Vidyalankar Institute of Technology  
**Repository:** [https://github.com/mananch1/highway-ami](https://github.com/mananch1/highway-ami)  

---

## 1. Executive Summary

This project delivers an enterprise-grade **Roadside Assistance Portal (`road-helper`)** along with an automated, end-to-end **DevOps Pipeline** fulfilling all 15 syllabus tasks specified in the curriculum.

The application combines a modern **React 18 Single-Page Application (Vite)** with a robust **Java 21 Spring Boot 4.x/3.x** backend packaged as a single deployable WAR on Apache Tomcat 10. Key application features include:
1. **Public Emergency Dispatch Flow**: Zero-friction roadside assistance request creation for motorists in distress without mandatory pre-registration.
2. **Automated Dispatch Engine**: High-efficiency round-robin technician queue matching.
3. **Real-Time Interactive Chat**: Dedicated STOMP over SockJS WebSocket channel per incident.
4. **Role-Based Workflow Management**: Dynamic state progression enforced across Customers, Technicians, and Administrators.
5. **Operational Analytics Dashboard**: Real-time KPI summaries and interactive Recharts data visualizations.

The DevOps pipeline automates every lifecycle stage from code commit to containerized cloud deployment:
- **Version Control**: GitHub Flow branching, pull requests, and semantic version tagging (`v1.0.0`).
- **Continuous Integration**: Jenkins automated compilation, artifact archiving, and unit testing.
- **Continuous Testing Quality Gate**: 5 critical end-to-end Selenium WebDriver user journeys executed headless in Google Chrome and Microsoft Edge with automated failure screenshot capture.
- **Containerization**: Multi-stage `Dockerfile` and multi-service `docker-compose.yml`.
- **Continuous Delivery**: Automated Docker image building, version tagging, Docker Hub registry publication, and zero-downtime container replacement (`Jenkinsfile.docker`).
- **Configuration Management & Reliability**: Agentless Ansible playbooks (`playbook.yml`, `rollback.yml`) enforcing idempotent environment provisioning and automated rollback recovery.

---

## 2. 15-Task Deliverables Compliance Matrix

| Task # | Task Title | Primary Deliverable | Status |
|--------|------------|---------------------|:------:|
| **Task 1** | Problem Definition and Scope | Problem statement, stakeholder analysis, objectives, constraints, 15-task scope (`docs/Task-01...`) | **Completed** |
| **Task 2** | Agile Planning & DevOps Workflow | User stories, acceptance criteria, Kanban plan, Definition of Done, DevOps lifecycle diagram (`docs/Task-02...`) | **Completed** |
| **Task 3** | Requirements & Technology Setup | SRS summary, use-case diagram, architecture diagram, data model/API list, working local setup (`docs/Task-03...`) | **Completed** |
| **Task 4** | Git & GitHub Repo Initialization | GitHub repository URL, README, `.gitignore`, folder structure, issue templates, branch policy (`docs/Task-04...`) | **Completed** |
| **Task 5** | Feature Development with Branching | Core incident workflow on feature branch, PR review evidence, and clean merge (`docs/Task-05...`) | **Completed** |
| **Task 6** | MVP Completion & Git Collab | Functional MVP, merge conflict creation & resolution, release tagging `v1.0.0` (`docs/Task-06...`) | **Completed** |
| **Task 7** | Jenkins CI Job | Jenkins installation, GitHub repository connection, automated build trigger, archived WAR artifact (`docs/Task-07...`) | **Completed** |
| **Task 8** | Pipeline as Code & Deployment | Declarative `Jenkinsfile`, parameterized deployment stages, Tomcat server deployment (`docs/Task-08...`) | **Completed** |
| **Task 9** | Selenium Test Design & Execution | 5 critical user journeys, assertions, failure screenshot utility, Maven local execution (`docs/Task-09...`) | **Completed** |
| **Task 10** | Continuous Testing in Jenkins | Selenium suite integrated in Jenkins, automated test reports, deliberate defect injection & fix evidence (`docs/Task-10...`) | **Completed** |
| **Task 11** | Docker Image & Container Lifecycle | Multi-stage `Dockerfile`, complete container lifecycle commands (build, run, inspect, stop, remove), `docker-compose.yml` (`docs/Task-11...`) | **Completed** |
| **Task 12** | Jenkins-Docker CD Pipeline | Versioned Docker image build, Docker Hub push, end-to-end commit-to-container pipeline (`docs/Task-12...`) | **Completed** |
| **Task 13** | Configuration Management (Ansible) | Server prerequisites specification, Ansible inventory, YAML playbook execution (`docs/Task-13...`) | **Completed** |
| **Task 14** | Automated Provisioning & Reliability | Clean provisioning, idempotency rerun demonstration (`changed=0`), health check, rollback demonstration (`docs/Task-14...`) | **Completed** |
| **Task 15** | Consolidated Project Report | End-to-end report, artifact index, architecture validation, and evaluation rubric summary (`docs/Task-15...`) | **Completed** |

---

## 3. Key Project Artifacts Index

- **Application Source Code**:
  - Backend: `src/main/java/com/mananc/road_helper/` (44 Java files)
  - Frontend: `frontend/src/` (21 React/JSX files)
- **Automated Tests**:
  - `src/test/java/com/mananc/road_helper/service/IncidentServiceTest.java` (Unit tests)
  - `src/test/java/com/mananc/road_helper/selenium/RoadHelperSeleniumIT.java` (Selenium WebDriver tests)
  - `src/test/java/com/mananc/road_helper/selenium/SeleniumScreenshotUtil.java` (Failure screenshot utility)
- **Continuous Integration / Delivery Pipelines**:
  - `Jenkinsfile` (Tomcat deployment pipeline)
  - `Jenkinsfile.docker` (Docker Hub CD pipeline)
- **Container Infrastructure**:
  - `Dockerfile` (Multi-stage build)
  - `docker-compose.yml` (PostgreSQL + Web Application stack)
- **Configuration Management**:
  - `ansible/inventory.ini` (Host definition)
  - `ansible/playbook.yml` (Provisioning playbook)
  - `ansible/rollback.yml` (Recovery & rollback playbook)
- **Documentation**:
  - `README.md` (Project overview)
  - `BRANCHING.md` (Branch policy)
  - `.github/ISSUE_TEMPLATE/` (Issue templates)
  - `docs/Task-01...` to `docs/Task-15...` (Detailed task reports)
