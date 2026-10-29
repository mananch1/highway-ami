# Academic Project Poster Specification & Master ChatGPT Prompt

**Candidate Name:** Manan Chahal  
**Roll No:** 23102C0044  
**Class / Division:** BE Computer Engineering — Semester VII (Div C)  
**Project Title:** Automated DevOps CI/CD Pipeline & Highway Emergency Dispatch Platform  
**Target Output Format:** 36" $\times$ 48" Academic / Conference Research Poster (Portrait or Landscape)  
**Live Production URL:** `http://15.252.18.123/`  
**GitHub Repository:** `https://github.com/mananch1/highway-ami.git`  

---

# PART 1: Copy-Paste Master Prompt for ChatGPT

> [!TIP]
> Copy the entire block below and paste it directly into ChatGPT (GPT-4 / ChatGPT Plus) to generate your complete academic poster, Canva text layout, or LaTeX Beamerposter code.

```text
Act as an expert academic poster designer, senior cloud architect, and DevOps engineering professor. 

I need you to generate the complete, high-impact text, visual layout specifications, and diagram descriptions for a professional 36" x 48" Academic Project Poster for my final year DevOps Engineering project viva and exhibition.

Here are my project credentials:
- Candidate Name: Manan Chahal
- Roll Number: 23102C0044
- Class / Division: BE Computer Engineering (Semester VII - Div C)
- Academic Year: 2026-2027
- Project Title: Automated DevOps CI/CD Pipeline & Highway Emergency Dispatch Platform
- Live AWS Production Deployment: http://15.252.18.123/
- GitHub Repository: https://github.com/mananch1/highway-ami.git

Please organize the poster into a 4-column academic engineering layout with a prominent header banner and footer strip. Use an executive, high-contrast engineering color palette: Deep Navy Blue (#0f172a), Slate Gray (#334155), Clean White (#ffffff), Electric Blue (#1d4ed8), and Emerald Green (#15803d) for verified indicators. Strictly NO consumer emojis anywhere.

Here is the required section-by-section breakdown:

==============================================================================
HEADER BANNER (Top of Poster - High Contrast Deep Navy #0f172a)
==============================================================================
- Main Title (Bold 72pt): Automated DevOps CI/CD Pipeline & Highway Emergency Dispatch Platform
- Subtitle (28pt): Zero-Downtime Continuous Deployment, Headless E2E Quality Gating, and Highway QR Telemetry on AWS
- Candidate Information (Bold 24pt):
  * Manan Chahal | Roll No: 23102C0044 | Division: BE CMPN-C
  * Department of Computer Engineering | Course: DevOps Engineering (CSL702)

==============================================================================
COLUMN 1: MOTIVATION, OBJECTIVES & SYSTEM ARCHITECTURE
==============================================================================
1. Problem Statement:
   - Traditional highway roadside assistance suffers from manual telephone dispatch delays, vague landmark reporting by stranded motorists, and unverified software releases causing production downtime.
2. Core Objectives:
   - Build a real-time, 1-click highway dispatch web platform with automated QR marker parsing.
   - Establish an immutable, multi-tier CI/CD pipeline using Jenkins, Maven, Docker, and Ansible.
   - Implement automated quality gating using headless Selenium browser tests to block faulty releases.
3. Architecture & Cloud Topology (Dual-Node AWS Mumbai ap-south-1):
   - Node 1 (CI/CD Controller): AWS EC2 t3.small running Jenkins LTS, Java 21, Maven 3.9, Google Chrome headless, and Ansible Engine.
   - Node 2 (Production Host): AWS EC2 t3.small running Docker Compose with Spring Boot / Tomcat (Port 80) and PostgreSQL 16 (Port 5432).
   - Network Isolation: Inter-node deployment over internal private AWS VPC subnet (172.31.15.50); SSH is strictly hidden from the public internet.

==============================================================================
COLUMN 2: THE DEVOPS CI/CD PIPELINE & BUILD AUTOMATION
==============================================================================
1. Declarative Pipeline as Code (Jenkinsfile.aws):
   - Stage 1: Source Checkout (GitHub Webhook trigger, main branch).
   - Stage 2: Unit Testing & Build (Maven compiling Java 21, JUnit 5 test execution).
   - Stage 3: Monolithic WAR Packaging (frontend-maven-plugin compiling React 18 / Vite SPA, embedding dist/ into static resources, generating ROOT.war).
   - Stage 4: Headless Selenium E2E Quality Gating (Linux Chrome executing 5 user journeys; failure captures browser screenshot and halts build).
   - Stage 5: Ansible Automated Deployment (Idempotent playbook syncing compose config, copying WAR artifact, and executing rolling container restart).
2. Multi-Tier Maven Integration:
   - Resolves the frontend-backend synchronization challenge by automating Node 20 and npm build during Maven's compile phase, bundling everything into a deployable WAR in under 90 seconds.

==============================================================================
COLUMN 3: AUTOMATED TESTING & LIVE QUALITY GATING EXPERIMENT
==============================================================================
1. Continuous Testing Suite:
   - 4 Spring Boot unit tests verifying incident service transactions and entity persistence.
   - 5 Selenium WebDriver journeys testing Guest Emergency Request, Customer Auth, Technician Dashboard, Admin Analytics, and Incident Search.
2. The Live Quality Gating Experiment (DevOps Proof of Concept):
   - Hypothesis: The CI/CD pipeline must automatically halt if broken code is committed, preventing downtime in production.
   - Execution: In commit 012856f, a deliberate regression error banner was introduced on the intake header ("Emergency Dispatch API Cluster Offline").
   - Result: Selenium Journey 1 caught the assertion failure. SeleniumScreenshotUtil captured a full-page browser screenshot (Journey1_GuestEmergency_*.png) and Jenkins archived it as a build artifact.
   - Outcome: Stage 4 failed; Stage 5 (Ansible Deploy) was completely blocked. Production (15.252.18.123) remained 100% stable and operational.
   - Recovery: Commit dcd379e resolved the regression; the pipeline turned GREEN and deployed seamlessly.

==============================================================================
COLUMN 4: HIGHWAY QR INNOVATION, ENTERPRISE UI & RESULTS
==============================================================================
1. Highway Mile-Marker QR Telemetry:
   - Motorists point smartphone camera at highway emergency placards.
   - Encoded URL parameters (?loc=NH-48+Km+42&type=FLAT_TIRE) instantly auto-fill dispatch location and category without GPS latency or permissions.
2. Enterprise Corporate UI System:
   - 100% emoji-free corporate aesthetic following Department of Transportation standards.
   - Executive slate and navy color palette (#0f172a, #1d4ed8, #cbd5e1), high-contrast touch targets, and 4-step dispatch progress stepper.
   - Fully responsive for mobile devices (<= 768px) with accessible hamburger drawer.
3. Verification & Course Rubric (CMPN-C.xlsx):
   - Successfully verified across all 15 syllabus tasks (Agile planning, Git branching, Jenkins CI, Docker lifecycle, Ansible CM, and AWS Cloud validation).
   - Healthcheck verified HTTP 200 on AWS Mumbai production server.

==============================================================================
FOOTER STRIP (Bottom of Poster)
==============================================================================
- Live Production Host: http://15.252.18.123/ (Port 80)
- GitHub Repository: https://github.com/mananch1/highway-ami.git
- Release Tags: v1.0.0-mvp | v1.0.0-aws | v1.1.0-cloud-qr
- Verification Status: All 15 DevOps Syllabus Tasks Completed & Verified (100% Pass)
```

---

# PART 2: Visual Structure & Design Specifications for Canva / PowerPoint

If you are assembling the poster in **Canva**, **Microsoft PowerPoint**, or **Adobe Illustrator**, follow these visual styling guidelines:

### 1. Canvas Dimensions & Grid Setup
- **Page Size:** 36 inches width $\times$ 48 inches height (Portrait), or 48" $\times$ 36" (Landscape).
- **Margins:** 1.0 inch safe margin on all outer edges.
- **Grid Layout:** 4 equal columns with 0.5-inch gutters.

### 2. Official Corporate Color Palette
| Color Name | Hex Code | Usage |
| :--- | :--- | :--- |
| **Deep Executive Navy** | `#0f172a` | Header banner background, card headers, primary titles |
| **Electric Royal Blue** | `#1d4ed8` | Accent borders, pipeline arrow connectors, active badges |
| **Slate Gray Neutral** | `#334155` | Body text, table outlines, diagram borders |
| **Subtle Cloud Gray** | `#f8fafc` | Card backgrounds, panel fills |
| **Verified Emerald Green**| `#15803d` | Test pass indicators, healthcheck badges (`HTTP 200 OK`) |
| **Regression Alert Red** | `#b91c1c` | The deliberate bug experiment failure callout box |

### 3. Typography Hierarchy
- **Poster Title:** Sans-serif bold (e.g., *Inter*, *Montserrat*, or *Helvetica Neue*), `72pt` to `80pt`.
- **Candidate Name & Metadata:** Medium sans-serif, `26pt` to `30pt`.
- **Section Headers:** Bold uppercase with colored left border accent, `28pt` to `32pt`.
- **Card Subheadings:** Semi-bold, `18pt` to `22pt`.
- **Body Text:** Regular, high legibility, `14pt` to `16pt` with `1.4` line spacing.
- **Code / Shell Snippets:** Monospace (e.g., *JetBrains Mono*, *Consolas*), `12pt` to `14pt` on dark background.

---

# PART 3: Diagrams to Include on the Poster

### Diagram 1: Dual-Node AWS Mumbai Cloud Architecture (Column 1)
```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          AWS VPC (Region: ap-south-1)                       │
│                                                                             │
│  [Node 1: Jenkins Controller]                     [Node 2: Production Host] │
│  ├── EC2 t3.small (Ubuntu 24.04)                  ├── EC2 t3.small          │
│  ├── Jenkins LTS 2.580.1                          ├── Docker Engine 29.x    │
│  ├── OpenJDK 21 + Maven 3.9                       ├── Docker Compose Stack: │
│  ├── Headless Chrome Selenium                     │   ├── road-helper-app   │
│  └── Ansible Engine                               │   │   (Tomcat Port 80)  │
│         │                                         │   └── roadhelper_db     │
│         │==== Ansible over VPC (172.31.15.50) ===>│       (PostgreSQL 16)   │
│         │   (Production SSH strictly private)     └── Named Volume:         │
│                                                       (postgres_data)       │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Diagram 2: The 5-Stage Declarative Pipeline (Column 2)
```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   STAGE 1    │     │   STAGE 2    │     │   STAGE 3    │     │   STAGE 4    │     │   STAGE 5    │
│   Source     │ ──> │   Build &    │ ──> │   Package    │ ──> │ Selenium E2E │ ──> │   Ansible    │
│   Checkout   │     │  Unit Tests  │     │   ROOT.war   │     │ Test Gating  │     │ Deploy (AWS) │
│ (GitHub SCM) │     │  (Java 21)   │     │ (React+Node) │     │(Headless CHR)│     │(Rolling Rest)│
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
```

### Diagram 3: Automated Quality Gating Proof of Concept (Column 3)
```
Commit 012856f (Bug Injected) ──> Stage 4 (Selenium) FAILS ──> Screenshot Captured ──> Deploy HALTED
                                                                                    (Production Safe)
                                                                                            ▲
Commit dcd379e (Bug Resolved) ──> Stage 4 (Selenium) PASSES ──> Stage 5 DEPLOYS ─────────────┘
                                                                (Zero Downtime)
```

---

# PART 4: Academic LaTeX Code Snippet (For Overleaf / Beamerposter)

If you or your department prefers compiling the poster in **LaTeX** via Overleaf:

```latex
\documentclass[final]{beamer}
\usepackage[scale=1.24]{beamerposter}
\usetheme{gemini}
\usecolortheme{slate}

\title{Automated DevOps CI/CD Pipeline \& Highway Emergency Dispatch Platform}
\author{\textbf{Manan Chahal} (Roll No: 23102C0044) \and Class: BE CMPN-C}
\institute{Department of Computer Engineering \and Academic Year 2026--2027}
\footercontent{
  Live AWS Production: \url{http://15.252.18.123/} \hfill
  GitHub Repository: \url{https://github.com/mananch1/highway-ami} \hfill
  DevOps Evaluation: 15/15 Tasks Verified
}

\begin{document}
\begin{frame}[t]
\begin{columns}[t]
  % Column 1: Problem & Architecture
  \begin{column}{0.23\textwidth}
    \begin{block}{1. Problem Statement \& Scope}
      Highway breakdowns require urgent dispatch. Traditional systems suffer from manual routing latency and untested releases causing downtime. We established an automated CI/CD pipeline and an instant QR-driven roadside assistance platform.
    \end{block}
    \begin{block}{2. Dual-Node AWS Architecture}
      Deployed on AWS Mumbai (\texttt{ap-south-1}) inside a VPC:
      \begin{itemize}
        \item \textbf{Node 1 (Controller):} Jenkins LTS, Maven, Ansible, Headless Chrome.
        \item \textbf{Node 2 (Production):} Docker Compose, Spring Boot on Tomcat (Port 80), PostgreSQL 16.
        \item \textbf{VPC Isolation:} Ansible deploys over internal IP \texttt{172.31.15.50}; production SSH is not exposed.
      \end{itemize}
    \end{block}
  \end{column}

  % Column 2: Pipeline as Code
  \begin{column}{0.23\textwidth}
    \begin{block}{3. Continuous Integration Pipeline}
      Declarative pipeline (\texttt{Jenkinsfile.aws}) automates 5 stages:
      \begin{enumerate}
        \item SCM Checkout from GitHub.
        \item Java 21 compilation and JUnit 5 testing.
        \item React SPA compilation via \texttt{frontend-maven-plugin} bundled into \texttt{ROOT.war}.
        \item Headless Chrome Selenium E2E testing.
        \item Ansible automated deployment.
      \end{enumerate}
    \end{block}
  \end{column}

  % Column 3: Quality Gating
  \begin{column}{0.23\textwidth}
    \begin{block}{4. Automated Quality Gating}
      Selenium E2E executes 5 journeys in memory.
      \textbf{The Experiment:} Commit \texttt{012856f} introduced a deliberate header regression. Selenium caught the assertion error, captured a screenshot (\texttt{target/screenshots/*.png}), and halted the pipeline before Ansible deploy. Commit \texttt{dcd379e} resolved the bug, recovering to a green build.
    \end{block}
  \end{column}

  % Column 4: Production Results
  \begin{column}{0.23\textwidth}
    \begin{block}{5. Highway QR Innovation \& Results}
      Highway markers encode URL parameters (\texttt{?loc=...}), auto-populating incident telemetry without GPS errors. Built with a zero-emoji corporate design system.
      \textbf{Validation:} Healthcheck verified HTTP 200 on AWS. All 15 tasks of \texttt{CMPN-C.xlsx} completed.
    \end{block}
  \end{column}
\end{columns}
\end{frame}
\end{document}
```
