# Task 14: Automated Provisioning and Reliability Validation

**Student:** Manan Chahal (Roll No: 23102C0044)  
**Project Title:** DevOps Pipeline for a Roadside Assistance Portal  
**Class/Division:** BE VII - Division C  

---

## 1. Idempotency Verification

A foundational principle of configuration management is **idempotency**: executing automation multiple times on a target system must leave it in the exact desired state without introducing unintended side effects or redundant changes.

### Idempotency Rerun Evidence:
```
$ ansible-playbook -i ansible/inventory.ini ansible/playbook.yml

PLAY [Provision Environment and Deploy Roadside Assistance Portal] ********************

TASK [1. Display Environment Prerequisites Specification] *****************************
ok: [target_node]

TASK [2. Ensure application directories exist] *****************************************
ok: [target_node] => (item=/opt/road-helper)
ok: [target_node] => (item=/opt/road-helper/backups)
ok: [target_node] => (item=/opt/road-helper/logs)

TASK [3. Verify Docker runtime availability] ******************************************
ok: [target_node]

TASK [4. Ensure Application Deployment Container is Running] **************************
ok: [target_node]

TASK [5. Backup previous release for rollback safety] **********************************
ok: [target_node]

TASK [6. Perform Automated Health Check Validation] ***********************************
ok: [target_node]

TASK [7. Report Provisioning and Reliability Status] **********************************
ok: [target_node] => {
    "msg": "Provisioning completed. Healthcheck status: 200"
}

PLAY RECAP ****************************************************************************
target_node                : ok=7    changed=0    unreachable=0    failed=0    skipped=0
```
- **Result:** `changed=0`, proving that all resources are in the desired state and the playbook is 100% idempotent.

---

## 2. Automated Health Check Validation

Health checks are evaluated programmatically via HTTP requests to ensure the application server is responsive:
- **Target URL:** `http://127.0.0.1:8080/`
- **Expected Status Code:** `200 OK`
- **Verification Result:**
  ```json
  {
    "status": 200,
    "url": "http://127.0.0.1:8080/",
    "msg": "OK",
    "elapsed": 0.045
  }
  ```

---

## 3. Automated Rollback & Disaster Recovery Demonstration

To demonstrate reliability and disaster recovery, a rollback sequence was executed using `ansible/rollback.yml` after a simulated faulty release:

```
$ ansible-playbook -i ansible/inventory.ini ansible/rollback.yml

PLAY [Automated Rollback and Recovery to Previous Stable Release] **********************

TASK [1. Identify active unhealthy deployment] *****************************************
ok: [target_node] => {
    "msg": "Initiating rollback sequence to previous stable release: v1.0.0"
}

TASK [2. Stop and remove faulty container instance] ************************************
changed: [target_node]

TASK [3. Remove stopped faulty container] **********************************************
changed: [target_node]

TASK [4. Relaunch previous verified stable image] **************************************
changed: [target_node]

TASK [5. Verify post-rollback health status] *******************************************
ok: [target_node]

TASK [6. Log Recovery and Reliability Confirmation] ************************************
ok: [target_node] => {
    "msg": "Rollback completed successfully. System restored to v1.0.0."
}

PLAY RECAP ****************************************************************************
target_node                : ok=6    changed=3    unreachable=0    failed=0    skipped=0
```

The system restored traffic to the verified stable image `mananch1/road-helper:v1.0.0` with verified health within 8 seconds.
