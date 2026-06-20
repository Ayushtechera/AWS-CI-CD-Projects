# 🎓 Student Performance Prediction — CI/CD Pipeline

An end-to-end ML project with a **fully automated CI/CD pipeline** — push your code and the app automatically builds into a Docker container and deploys to AWS EC2.

![App Preview](./templates/preview.png)

---

## 🚀 Tech Stack

`Python` `Flask` `scikit-learn` `CatBoost` `XGBoost` `Docker` `GitHub Actions` `AWS EC2` `AWS ECR`

---

## ⚙️ ML Pipeline Overview

| Step | What happens |
|---|---|
| Data Ingestion | Loads dataset, splits into train/test, saves artifacts |
| Data Transformation | `StandardScaler` + `OneHotEncoder` via `ColumnTransformer` |
| Model Training | Trains 8 models, picks best by R² score |
| Prediction | User input → preprocessor → model → predicted score |

---

## 🔄 CI/CD Flow

```
Code Push (GitHub)
      ↓
GitHub Actions Triggered
      ↓
Docker Image Built
      ↓
Image Pushed to AWS ECR
      ↓
EC2 Pulls & Runs Container ✅
```

**3 things needed to set this up:**
1. Docker build configured
2. GitHub Actions workflow (`.github/workflows/`)
3. IAM User in AWS with ECR & EC2 permissions

---

## ☁️ AWS EC2 — Docker Setup

SSH into your EC2 instance and run these commands:

```bash
# Update packages
sudo apt-get update -y
sudo apt-get upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add user to docker group
sudo usermod -aG docker ubuntu
newgrp docker
```

Then configure EC2 as a **self-hosted GitHub Actions runner** from:
`GitHub Repo → Settings → Actions → Runners → New self-hosted runner`

---

## 🔐 GitHub Secrets Required

Go to `Repo → Settings → Secrets → Actions` and add:

| Secret | Value |
|---|---|
| `AWS_ACCESS_KEY_ID` | Your IAM user access key |
| `AWS_SECRET_ACCESS_KEY` | Your IAM user secret key |
| `AWS_REGION` | `us-east-1` |
| `AWS_ECR_LOGIN_URI` | `<account-id>.dkr.ecr.ap-south-1.amazonaws.com` |
| `ECR_REPOSITORY_NAME` | `simple-app` |

---

## 📁 Project Structure

```
src/
├── components/
│   ├── data_ingestion.py
│   ├── data_transformation.py
│   └── model_trainer.py
├── pipeline/
│   ├── train_pipeline.py
│   └── predict_pipeline.py
├── exception.py
├── logger.py
└── utils.py
Dockerfile
app.py                         # Flask entry point
.github/workflows/main.yaml    # CI/CD pipeline
```

---

## 🖥️ Run Locally

```bash
git clone https://github.com/Ayushtechera/StudentScore-CICD-AWS.git
cd StudentScore-CICD-AWS
pip install -r requirements.txt
python app.py
```

Open `http://localhost:8080`

---

## 📊 Dataset

[Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams) — Kaggle

**Features:** gender, race/ethnicity, parental education, lunch, test prep course, reading score, writing score
**Target:** math score

---

## 💡 What I Built / Learned

- End-to-end CI/CD pipeline from scratch
- Dockerized a Flask + ML app
- Pushed Docker images to AWS ECR
- Set up EC2 as a self-hosted GitHub Actions runner
- Managed AWS IAM roles and GitHub Secrets

---

**Ayush Kashyap** · [GitHub](https://github.com/Ayushtechera)