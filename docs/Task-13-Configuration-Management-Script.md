# Task 13: Configuration Management Script

**Student:** Manan Chahal (Roll No: 23102C0044)  
**Project Title:** DevOps Pipeline for a Roadside Assistance Portal  
**Class/Division:** BE VII - Division C  

---

## 1. Server Prerequisites Specification

Before deployment, the target node must satisfy the following configuration baseline:

| Prerequisite Category | Requirement Specification | Purpose |
|-----------------------|---------------------------|---------|
| **Operating System** | Linux (Ubuntu 22.04 LTS / Debian 12) or Windows Server | Host operating system |
| **Runtime Packages** | `curl`, `git`, `openjdk-21-jdk`, `docker.io`, `docker-compose-v2` | Execution & container runtimes |
| **System Users & Groups** | User `roadhelper`, group `docker` | Non-root privilege separation |
| **Directory Hierarchy** | `/opt/road-helper`, `/opt/road-helper/backups`, `/opt/road-helper/logs` | Artifact and log persistence |
| **Network Ports** | `8080/tcp` (Application HTTP), `5432/tcp` (PostgreSQL Database) | Ingress traffic and data access |
| **Services** | `docker.service`, `postgresql.service` | Daemons active and enabled on boot |

---

## 2. Ansible Inventory & Playbook Structure

- **Inventory File (`ansible/inventory.ini`)**: Defines target host groups, IP addresses, connection drivers, and environment variables.
- **Playbook File (`ansible/playbook.yml`)**:
  - Enforces directory existence with appropriate permission masks (`0755`).
  - Verifies Docker engine daemon status.
  - Pulls the verified container image (`mananch1/road-helper:latest`).
  - Launches the containerized application on mapped port `8080`.
  - Captures release metadata and backups for rollback protection.
  - Executes automated HTTP health checks.

---

## 3. Initial Execution Log Evidence

```
$ ansible-playbook -i ansible/inventory.ini ansible/playbook.yml

PLAY [Provision Environment and Deploy Roadside Assistance Portal] ********************

TASK [1. Display Environment Prerequisites Specification] *****************************
ok: [target_node] => {
    "msg": [
        "Target Port: 8080",
        "Database Port: 5432",
        "Application Name: road-helper",
        "Deployment Mode: container"
    ]
}

TASK [2. Ensure application directories exist] *****************************************
changed: [target_node] => (item=/opt/road-helper)
changed: [target_node] => (item=/opt/road-helper/backups)
changed: [target_node] => (item=/opt/road-helper/logs)

TASK [3. Verify Docker runtime availability] ******************************************
ok: [target_node]

TASK [4. Ensure Application Deployment Container is Running] **************************
changed: [target_node]

TASK [5. Backup previous release for rollback safety] **********************************
changed: [target_node]

TASK [6. Perform Automated Health Check Validation] ***********************************
ok: [target_node]

TASK [7. Report Provisioning and Reliability Status] **********************************
ok: [target_node] => {
    "msg": "Provisioning completed. Healthcheck status: 200"
}

PLAY RECAP ****************************************************************************
target_node                : ok=7    changed=4    unreachable=0    failed=0    skipped=0
```
The node was configured and provisioned with zero errors.
