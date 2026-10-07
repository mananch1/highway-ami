# Task 1: Problem Definition and Scope

**Student:** Manan Chahal (Roll No: 23102C0044)  
**Project Title:** DevOps Pipeline for a Roadside Assistance Portal  
**Class/Division:** BE VII - Division C  

---

## 1. Problem Statement

Vehicular breakdowns and highway emergencies require rapid, coordinated intervention. Traditional roadside assistance services suffer from:
1. **High Latency & Communication Bottlenecks**: Drivers stranded on highways are forced to make lengthy phone calls, manually explain GPS coordinates, and face opaque wait times.
2. **Disconnected Emergency Response**: Drivers requiring urgent multi-agency assistance (police, ambulance, towing) must contact each organization separately during high-stress scenarios.
3. **Inefficient Manual Dispatch**: Dispatchers manually determine technician assignments, resulting in imbalanced workloads, slow response times, and zero real-time status visibility.

The **Roadside Assistance Portal (`road-helper`)** provides an instant, dual-mode web platform enabling drivers to request roadside assistance without mandatory pre-registration in emergencies, leverages automated technician dispatch, provides live status updates, facilitates real-time two-way messaging, and integrates emergency service coordination.

---

## 2. Stakeholder Analysis

| Stakeholder | Role & Responsibility | Key Pain Point Addressed |
|-------------|-----------------------|--------------------------|
| **Stranded Drivers (Customers/Guests)** | Request assistance, report location and incident type, chat with assigned technicians, track resolution. | Eliminates manual phone queues; provides instant dispatch tracking and guest emergency access. |
| **Field Technicians / Mechanics** | Receive automated dispatch assignments, update incident status (`IN_PROGRESS`, `RESOLVED`), chat with drivers. | Real-time queue notifications; automated availability toggling. |
| **Portal Administrators / Dispatchers** | Oversee fleet operations, reassign incidents, analyze service metrics and incident resolution times. | Centralized real-time operational dashboard with Recharts analytics. |
| **Emergency Services (Police, Ambulance, Tow)** | Receive automated incident alerts for critical events (e.g. accidents). | Automated incident triage and dispatch alert logging. |
| **DevOps Engineers / Evaluators** | Maintain automated CI/CD pipelines, containerize workloads, ensure zero-downtime deployments. | Fully automated Git -> Jenkins -> Docker -> Ansible pipeline. |

---

## 3. Measurable Success Criteria

- **Zero-Friction Emergency Access**: Emergency requests submitted and acknowledged in under 15 seconds without user signup.
- **Automated Dispatch**: 100% of newly submitted requests auto-assigned to an available technician via round-robin queue.
- **CI/CD Build Automation**: 100% automated build, packaging, and testing via Jenkinsfile on code commit.
- **Automated Quality Gate**: 5 critical Selenium E2E journeys passing on all releases with automated failure screenshot capture.
- **Container Deployment Time**: Complete container build and launch cycle completed in under 2 minutes.
- **Configuration Idempotency**: Ansible playbook executions achieve `changed=0` on repeated runs.

---

## 4. Approved 15-Task MVP Scope

1. **Task 1**: Problem statement, stakeholder analysis, objectives, constraints, and approved MVP scope.
2. **Task 2**: Agile user stories, backlog, Kanban board, Definition of Done, and DevOps workflow diagram.
3. **Task 3**: System Requirements Specification (SRS), architecture diagram, data model, API endpoints, working local setup.
4. **Task 4**: GitHub repository initialization, README, `.gitignore`, branch naming policy, issue templates, skeleton commit.
5. **Task 5**: Feature branch development (`feature/incident-crud`), commit, push, pull request, code review, and merge into `main`.
6. **Task 6**: MVP completion, feature branch 2 (`feature/dashboard`), merge conflict demonstration and resolution, version tagging (`v1.0.0`).
7. **Task 7**: Jenkins installation, GitHub repository connection, automated build trigger, and WAR artifact archiving.
8. **Task 8**: Declarative `Jenkinsfile` pipeline, parameterized deployment stages, deployment to Tomcat server.
9. **Task 9**: Selenium WebDriver test design (5 critical user journeys), assertions, test data, failure screenshot mechanism, Maven execution.
10. **Task 10**: Jenkins continuous testing integration, automated test reporting, defect injection and correction verification.
11. **Task 11**: Multi-stage `Dockerfile`, container lifecycle commands (build, run, inspect, stop, restart, remove), `docker-compose.yml`.
12. **Task 12**: Jenkins-to-Docker continuous deployment, automated Docker Hub image publishing (`mananch1/road-helper`), container recreation.
13. **Task 13**: Server prerequisites specification, Ansible inventory (`inventory.ini`), and automated provisioning playbook (`playbook.yml`).
14. **Task 14**: Automated node provisioning, idempotency rerun demonstration, health check verification, and rollback playbook (`rollback.yml`).
15. **Task 15**: Consolidated project report, presentation evidence, verification audit, and evaluation summary.
