# Production-Style CI/CD Pipeline & Monitoring

This project demonstrates a production-oriented DevOps workflow for a containerized Flask application, covering the full lifecycle from code commit to automated deployment and validation.

---

## 🚀 Key Features

- **CI/CD Pipeline:** Automated workflows using GitHub Actions for build, validation, and deployment  
- **Containerization:** Docker-based application packaging for consistent cross-environment execution  
- **Registry Management:** Automated image build and push to Docker Hub  
- **Security:** Secure handling of credentials using GitHub Secrets  
- **Validation:** Automated health checks integrated into the CI pipeline (pipeline fails on service issues)  
- **Monitoring:** Application health endpoint with external uptime monitoring  

---

## 🏗 System Architecture

1. Developer pushes code to repository  
2. CI pipeline is triggered via GitHub Actions  
3. Application dependencies are installed and validated  
4. Docker image is built in an isolated environment  
5. Image is pushed to Docker Hub  
6. Deployment platform pulls and runs the latest image  
7. Health checks validate service availability  

---

## 🛠 Tech Stack

- **Language:** Python (Flask)  
- **CI/CD:** GitHub Actions  
- **Containerization:** Docker  
- **Registry:** Docker Hub  
- **Cloud Deployment:** Render / Railway  
- **Monitoring:** Health checks & UptimeRobot  

---

## 📂 Project Structure
project/
├── .github/workflows/
│ └── ci-cd.yml # CI/CD pipeline definition
├── app.py # Flask app with /health endpoint
├── check_app.py # Automated health validation script
├── Dockerfile # Container definition
├── requirements.txt # Dependencies
└── README.md


---

## 📈 Monitoring & Validation

The application exposes a `/health` endpoint used to verify service availability.

As part of the CI pipeline:
- The application is started
- A health check script is executed
- The pipeline fails automatically if the service is not healthy

This simulates real-world production validation practices.

---

## 🔐 Security

Sensitive credentials (e.g., Docker Hub login) are managed using GitHub Secrets and are never exposed in the codebase.

---

## 🎯 Goal

This project simulates a real-world DevOps lifecycle:

**Code → Build → Test → Validate → Deploy → Monitor**

---
