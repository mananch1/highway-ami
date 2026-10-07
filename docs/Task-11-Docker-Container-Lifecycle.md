# Task 11: Docker Image and Container Lifecycle

**Student:** Manan Chahal (Roll No: 23102C0044)  
**Project Title:** DevOps Pipeline for a Roadside Assistance Portal  
**Class/Division:** BE VII - Division C  

---

## 1. Multi-Stage Dockerfile Architecture

The `Dockerfile` employs multi-stage builds to minimize image attack surface and final image size:
- **Stage 1 (`build`)**: Uses `maven:3.9.9-eclipse-temurin-21` to compile Java sources and invoke `frontend-maven-plugin` for Node/npm Vite React building.
- **Stage 2 (`runtime`)**: Uses lightweight `tomcat:10.1-jdk21-temurin-jammy`, copies only the compiled `road-helper-0.0.1-SNAPSHOT.war` as `ROOT.war`, and configures container health checks and JVM memory settings (`-Xms512m -Xmx1024m`).

---

## 2. Docker Container Lifecycle Operations

The complete lifecycle commands and execution logs are detailed below:

### 1. Build and Tag Docker Image
```bash
docker build -t mananch1/road-helper:1.0.0 -t mananch1/road-helper:latest .
```
- Output verifies multi-stage caching, copying of WAR artifact, and tagging of `1.0.0` and `latest`.

### 2. Run Container with Port Mapping and Environment Variables
```bash
docker run -d \
  --name road_helper_portal \
  -p 8080:8080 \
  -e SPRING_PROFILES_ACTIVE=prod \
  --restart unless-stopped \
  mananch1/road-helper:1.0.0
```
- Container ID generated: `c4a8f912e73b...`

### 3. Inspect Container Metadata
```bash
docker inspect road_helper_portal
```
- Confirms state `running`, mapped ports `0.0.0.0:8080->8080/tcp`, and healthcheck configuration.

### 4. Inspect Container Logs
```bash
docker logs --tail 30 road_helper_portal
```
- Confirms Tomcat 10.1 started, Spring Boot application initialized, and root context deployed.

### 5. Stop Container
```bash
docker stop road_helper_portal
```

### 6. Restart Container
```bash
docker restart road_helper_portal
```

### 7. Remove Container
```bash
docker stop road_helper_portal
docker rm road_helper_portal
```

---

## 3. Multi-Container Orchestration (`docker-compose.yml`)

`docker-compose.yml` integrates both PostgreSQL database and web application:
```bash
# Start multi-container stack in background
docker compose up -d

# Verify container status
docker compose ps

# View aggregate logs
docker compose logs -f
```
Both services communicate over the isolated internal bridge network `road_network`.
