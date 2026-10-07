# Task 3: Requirements, Architecture and Technology Setup

**Student:** Manan Chahal (Roll No: 23102C0044)  
**Project Title:** DevOps Pipeline for a Roadside Assistance Portal  
**Class/Division:** BE VII - Division C  

---

## 1. System Requirements Specification (SRS) Summary

### Functional Requirements
- **FR-01 (Authentication & Access)**: User registration and login with BCrypt password hashing and JWT issuance. Role-based authorization (`CUSTOMER`, `TECHNICIAN`, `ADMIN`).
- **FR-02 (Guest Emergency Request)**: Direct assistance submission requiring only name, contact number, location, and incident category without pre-registration.
- **FR-03 (Automated Dispatch)**: Round-robin queue allocation matching pending incidents to available field technicians.
- **FR-04 (Role-Based Status Management)**: Enforced state transitions (`REQUESTED` -> `AUTO_ASSIGNED` -> `IN_PROGRESS` -> `RESOLVED` -> `CLOSED` / `CANCELLED`).
- **FR-05 (Search & Filter)**: Keyword query support over incident descriptions and geographic locations.
- **FR-06 (Analytics Dashboard)**: Aggregated KPI calculations for administrators (totals, status distributions, category distributions, average resolution time).
- **FR-07 (Live Chat)**: Real-time STOMP WebSocket pub/sub message exchange per incident session.

### Non-Functional Requirements
- **NFR-01 (Portability)**: Cross-platform deployment via standard WAR on Apache Tomcat 10 and multi-stage Docker container.
- **NFR-02 (Stateless Scalability)**: Stateless REST API secured by JWT tokens, allowing horizontal scaling.
- **NFR-03 (Automated Testing)**: Unit and E2E Selenium regressions executable in headless mode in local and CI environments.

---

## 2. Use-Case Diagram

```mermaid
flowchart TD
    Guest((Guest Driver))
    Cust((Registered Customer))
    Tech((Field Technician))
    Admin((Administrator))

    subgraph System_Use_Cases ["Roadside Assistance Portal"]
        UC1([Submit Emergency Request])
        UC2([Track Incident Status])
        UC3([Register / Login])
        UC4([Create Authenticated Incident])
        UC5([Live Chat with Technician])
        UC6([Toggle Availability])
        UC7([Update Status: IN_PROGRESS / RESOLVED])
        UC8([View Analytics Dashboard])
        UC9([Search Incidents])
        UC10([Manage Users & Dispatches])
    end

    Guest --> UC1
    Guest --> UC2
    Guest --> UC5

    Cust --> UC3
    Cust --> UC4
    Cust --> UC2
    Cust --> UC5

    Tech --> UC3
    Tech --> UC6
    Tech --> UC7
    Tech --> UC5

    Admin --> UC3
    Admin --> UC8
    Admin --> UC9
    Admin --> UC10
```

---

## 3. Minimum Application Architecture Diagram

```mermaid
flowchart TD
    subgraph Client_Tier ["Presentation Layer"]
        Vite["React 18 SPA (Vite Bundle)"]
        Components["Components: Navbar, IncidentCard, StatusBadge, Chat"]
        Pages["Pages: Landing, Login, Dashboards, Search"]
    end

    subgraph Container_Tier ["Web & Application Container"]
        TomcatServer["Apache Tomcat 10 (Port 8080)"]
        Dispatcher["Spring DispatcherServlet"]
        SecurityFilter["JwtAuthFilter (Security Chain)"]
        SpaResolver["SpaWebMvcConfigurer (SPA Path Forwarder)"]
    end

    subgraph Service_Tier ["Business & Application Services"]
        AuthCtrl["AuthController"]
        EmergCtrl["EmergencyController"]
        IncCtrl["IncidentController"]
        DashCtrl["DashboardController"]
        ChatCtrl["ChatController (STOMP / SockJS)"]
        
        IncSvc["IncidentService (Dispatch Engine)"]
        UserSvc["UserService"]
        NotifSvc["NotificationService"]
        DashSvc["DashboardService"]
    end

    subgraph Persistence_Tier ["Data Layer"]
        JPA["Spring Data JPA / Hibernate"]
        PG[(PostgreSQL Database)]
        H2[(H2 In-Memory for Automated Tests)]
    end

    Vite --> TomcatServer
    TomcatServer --> Dispatcher
    Dispatcher --> SecurityFilter
    Dispatcher --> SpaResolver
    SecurityFilter --> AuthCtrl & EmergCtrl & IncCtrl & DashCtrl & ChatCtrl
    AuthCtrl --> UserSvc
    EmergCtrl & IncCtrl --> IncSvc
    IncSvc --> NotifSvc
    DashCtrl --> DashSvc
    IncSvc & UserSvc & DashSvc --> JPA
    JPA --> PG
    JPA -.-> H2
```

---

## 4. Data Model Specification

```mermaid
erDiagram
    app_users {
        bigint id PK
        varchar name
        varchar email UK
        varchar password
        varchar role
        boolean is_available
        timestamp created_at
    }

    incident {
        bigint id PK
        varchar type
        varchar description
        varchar status
        varchar location
        varchar guest_name
        varchar guest_phone
        varchar guest_token UK
        bigint customer_id FK
        bigint technician_id FK
        timestamp created_at
        timestamp updated_at
        timestamp resolved_at
    }

    chat_message {
        bigint id PK
        bigint incident_id FK
        bigint sender_id FK
        varchar sender_name
        varchar message
        timestamp timestamp
    }

    zone {
        varchar zone_id PK
        varchar name
        double_precision x
        double_precision y
    }

    app_users ||--o{ incident : "customer / technician"
    incident ||--o{ chat_message : "contains"
    app_users ||--o{ chat_message : "sends"
```

---

## 5. API Endpoints Catalog

| HTTP Method | URI Endpoint | Authentication | Purpose |
|-------------|--------------|----------------|---------|
| `POST` | `/api/v1/auth/register` | Public | Register new user account |
| `POST` | `/api/v1/auth/login` | Public | Authenticate user, receive JWT token |
| `POST` | `/api/v1/emergency` | Public | Submit emergency request, receive tracking token |
| `GET` | `/api/v1/emergency/status?token=` | Public | View guest incident status |
| `GET` | `/api/v1/incidents` | JWT (`CUSTOMER`, `TECH`, `ADMIN`) | List incidents filtered by role |
| `POST` | `/api/v1/incidents` | JWT (`CUSTOMER`) | Create authenticated incident |
| `GET` | `/api/v1/incidents/{id}` | JWT / Guest | Retrieve incident detail |
| `PATCH` | `/api/v1/incidents/{id}/status` | JWT (`TECH`, `ADMIN`) | Transition workflow status |
| `GET` | `/api/v1/incidents/search?query=` | JWT (`ADMIN`, `TECH`) | Search by query string |
| `GET` | `/api/v1/dashboard/summary` | JWT (`ADMIN`) | Get operational analytics and KPIs |
| `GET` | `/api/v1/users` | JWT (`ADMIN`) | List technicians |
| `PATCH` | `/api/v1/users/{id}/availability` | JWT (`TECH`) | Toggle technician active status |
| `GET` | `/api/v1/incidents/{id}/chat` | JWT / Guest | Fetch chat message history |
| `WS` | `/ws` -> `/app/chat/{id}` | STOMP / SockJS | Send real-time chat message |
