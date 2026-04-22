# Production-Style CI/CD Pipeline & Monitoring

This project demonstrates a professional DevOps workflow for a containerized Flask application. It covers the entire lifecycle from code commit to automated deployment.

## 🚀 Key Features
* **CI/CD Pipeline:** Fully automated workflow using **GitHub Actions**.
* **Containerization:** Multi-stage **Docker** builds for optimized images.
* **Registry Management:** Automated image push to **Docker Hub**.
* **Security:** Sensitive credentials managed via **GitHub Secrets**.
* **Observability:** Health-check endpoints and uptime monitoring.

## 🏗 System Architecture
1. **Developer** pushes code to a feature branch.
2. **Pull Request** triggers automated tests and linting.
3. **Merge to Main** triggers a Docker build.
4. **Image** is tagged and pushed to Docker Hub.
5. **Deployment** (Render/Cloud) pulls the latest image and runs it.

## 🛠 Tech Stack
* **Language:** Python (Flask)
* **DevOps:** GitHub Actions, Docker, Docker Hub
* **Cloud:** Render / Railway
* **Monitoring:** Health Checks & UptimeRobot

## 📂 Project Structure
```text
├── .github/workflows/
│   └── ci-cd.yml      # The "Heart" of the project - Pipeline logic
├── app.py             # Flask application with /health endpoint
├── Dockerfile         # Container definition
├── requirements.txt   # Python dependencies
└── README.md


📈 Monitoring & Health
The application exposes a /health endpoint which returns the system status. This is used by monitoring tools to ensure 100% availability and trigger alerts if the service goes down.