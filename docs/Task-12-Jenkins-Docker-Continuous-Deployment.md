# Task 12: Jenkins-Docker Continuous Deployment

**Student:** Manan Chahal (Roll No: 23102C0044)  
**Project Title:** DevOps Pipeline for a Roadside Assistance Portal  
**Class/Division:** BE VII - Division C  

---

## 1. Automated Commit-to-Container Architecture

`Jenkinsfile.docker` extends the CI pipeline into a fully automated Continuous Delivery workflow:
1. **Source Checkout**: Triggered on code push to `main`.
2. **Build & Quality Gate**: Maven compiles sources and runs headless Selenium E2E suite.
3. **Docker Build & Version Tagging**: Image tagged with dynamic build ID (`mananch1/road-helper:${BUILD_NUMBER}`) and `latest`.
4. **Registry Publication**: Image pushed to public Docker Hub registry under user credentials.
5. **Fresh Container Redeployment**: Gracefully stops the existing container and starts a new container with the fresh image.

---

## 2. End-to-End Pipeline Execution Evidence

```
[Pipeline] stage: Docker Build & Tag
[Docker Build & Tag] Building Docker image mananch1/road-helper:12 and latest...
 > docker build -t mananch1/road-helper:12 -t mananch1/road-helper:latest .
Successfully built e5a4f7819c9a
Successfully tagged mananch1/road-helper:12
Successfully tagged mananch1/road-helper:latest

[Pipeline] stage: Docker Hub Publish
[Docker Hub Publish] Publishing image to Docker Hub...
 > docker login -u mananch1 --password-stdin
Login Succeeded
 > docker push mananch1/road-helper:12
The push refers to repository [docker.io/mananch1/road-helper]
12: digest: sha256:7f49c0d12... size: 2412
 > docker push mananch1/road-helper:latest
latest: digest: sha256:7f49c0d12... size: 2412

[Pipeline] stage: Deploy Fresh Container
[Deploy Fresh Container] Stopping previous container and deploying mananch1/road-helper:12...
road_helper_portal
c91f08a4bb21f3750...
[Pipeline] echo
Successfully built, tested, published to Docker Hub and deployed container!
Finished: SUCCESS
```

- **Docker Hub Repository:** `mananch1/road-helper`
- **Published Tags:** `12`, `latest`, `v1.0.0`
- **Container Name:** `road_helper_portal` (Port 8080)
