# Task 4: Git and GitHub Repository Initialization

**Student:** Manan Chahal (Roll No: 23102C0044)  
**Project Title:** DevOps Pipeline for a Roadside Assistance Portal  
**Class/Division:** BE VII - Division C  

---

## 1. Repository Configuration

- **Repository Name:** `highway-ami`
- **Repository Remote URL:** [https://github.com/mananch1/highway-ami.git](https://github.com/mananch1/highway-ami.git)
- **Default Branch:** `main`
- **License:** MIT License
- **Build Descriptor:** Maven `pom.xml` with WAR packaging and `frontend-maven-plugin`

---

## 2. Directory Layout & Folder Structure

```
├── .github/
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md               # GitHub issue template for bugs
│       └── feature_request.md          # GitHub issue template for feature requests
├── .mvn/
│   └── wrapper/                        # Maven wrapper configuration
├── ansible/
│   ├── inventory.ini                   # Target host inventory
│   ├── playbook.yml                    # Provisioning playbook
│   └── rollback.yml                    # Automated rollback playbook
├── docs/                               # 15-Task complete project deliverables
├── frontend/                           # React 18 (Vite) single-page application
│   ├── src/
│   │   ├── api/api.js                  # Axios client with JWT interceptor
│   │   ├── components/                 # UI components (Chat, Navbar, Badges)
│   │   ├── context/AuthContext.jsx     # JWT authentication state management
│   │   ├── pages/                      # Role dashboards and emergency views
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
├── src/
│   ├── main/
│   │   ├── java/com/mananc/road_helper/
│   │   │   ├── config/                 # Security, STOMP WebSocket, SPA routing
│   │   │   ├── controller/             # REST & STOMP controllers
│   │   │   ├── dto/                    # Request/Response data transfer objects
│   │   │   ├── entity/                 # JPA models: User, Incident, Zone, ChatMessage
│   │   │   ├── exception/              # Global error handling
│   │   │   ├── repository/             # Spring Data JPA repositories
│   │   │   ├── security/               # JWT token provider and security filters
│   │   │   ├── service/                # Business logic and dispatch engine
│   │   │   └── RoadHelperApplication.java
│   │   └── resources/
│   │       └── application.properties  # Database and JWT configurations
│   └── test/
│       ├── java/com/mananc/road_helper/
│       │   ├── RoadHelperApplicationTests.java
│       │   ├── selenium/
│       │   │   ├── RoadHelperSeleniumIT.java     # 5 Critical User Journey Tests
│       │   │   └── SeleniumScreenshotUtil.java   # Failure screenshot capture
│       │   └── service/
│       │       └── IncidentServiceTest.java      # Service unit tests
│       └── resources/
│           └── application.properties  # H2 test in-memory configuration
├── .gitignore
├── BRANCHING.md                        # Branching and contribution policy
├── Dockerfile                          # Multi-stage container definition
├── docker-compose.yml                  # Local development multi-container stack
├── Jenkinsfile                         # Declarative CI/CD pipeline
├── Jenkinsfile.docker                  # Docker CD pipeline
├── pom.xml                             # Maven build configuration
└── README.md                           # Comprehensive documentation
```

---

## 3. GitHub Issue Templates & Branch Policy

- Configured `.github/ISSUE_TEMPLATE/bug_report.md` with environment specifications and steps to reproduce.
- Configured `.github/ISSUE_TEMPLATE/feature_request.md` with problem description and acceptance criteria.
- Implemented `BRANCHING.md` defining GitHub Flow conventions:
  - `main` as protected production baseline.
  - `feature/<name>` for feature isolation.
  - Mandatory pull request reviews and automated Jenkins CI status checks before merging.
