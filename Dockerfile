# Stage 1: Build Frontend and Backend Application
FROM maven:3.9.9-eclipse-temurin-21 AS build

WORKDIR /app

# Copy Maven descriptor
COPY pom.xml .
COPY .mvn .mvn
COPY mvnw mvnw.cmd ./

# Copy source code and frontend
COPY src src
COPY frontend frontend

# Build application WAR (including frontend Vite bundle via frontend-maven-plugin)
RUN mvn clean package -DskipTests

# Stage 2: Deploy to Production Tomcat 10
FROM tomcat:10.1-jdk21-temurin-jammy

LABEL maintainer="Manan Chahal <mananc@roadhelper.com>"
LABEL version="1.0.0"
LABEL description="Roadside Assistance Portal - Spring Boot & React WAR on Tomcat"

# Remove default Tomcat webapps
RUN rm -rf /usr/local/tomcat/webapps/*

# Copy packaged WAR to ROOT.war for root context deployment
COPY --from=build /app/target/road-helper-0.0.1-SNAPSHOT.war /usr/local/tomcat/webapps/ROOT.war

# Expose HTTP port
EXPOSE 8080

# Environment variables
ENV SPRING_PROFILES_ACTIVE=prod
ENV CATALINA_OPTS="-Xms512m -Xmx1024m"

# Healthcheck probe
HEALTHCHECK --interval=30s --timeout=5s --start-period=40s --retries=3 \
  CMD curl -f http://localhost:8080/ || exit 1

# Start Tomcat server
CMD ["catalina.sh", "run"]
