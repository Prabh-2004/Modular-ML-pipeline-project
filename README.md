# End-to-End Machine Learning Pipeline with Deployment

This is an **end-to-end modular Machine Learning project** that I built to understand how real-world ML systems are designed, structured, and deployed.

The project covers the complete ML lifecycle — from data ingestion to model evaluation — and also includes a **Flask-based prediction API and Docker support for deployment**.

---

## 📌 Project Overview

The pipeline is divided into multiple stages:

* Data Ingestion
* Data Validation
* Data Transformation (Feature Engineering + Preprocessing)
* Model Training
* Model Evaluation (MLflow / Dagshub)

In addition to this, I have also built:

* A **Flask app (`app.py`)** for making predictions
* A **Dockerfile** to containerize the application

---

## 🏗️ Project Architecture (Simple View)

```
Config (YAML files)
        ↓
Configuration Manager
        ↓
Entities (Dataclasses)
        ↓
Components (Core Logic)
        ↓
Pipelines (Stage-wise execution)
        ↓
main.py (Training Pipeline)

                + 
           Flask App (app.py)
                ↓
           User Predictions
```

---

## 📂 Project Structure

```
├── .github/
├── artifacts/                  # Models, processed data, outputs
├── config/
│   ├── config.yaml
│   ├── schema.yaml
│   └── params.yaml
│
├── logs/                       # Logging files (not pushed to GIT)
├── mlruns/                     # MLflow tracking (not pushed to GIT)
├── research/                   # Notebooks / experiments
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   └── model_evaluation.py
│   │
│   ├── pipelines/
│   │   ├── stage_01_data_ingestion.py
│   │   ├── stage_02_data_validation.py
│   │   ├── stage_03_data_transformation.py
│   │   ├── stage_04_model_trainer.py
│   │   └── stage_05_model_evaluation.py
│   │
│   ├── entity/
│   │   └── config_entity.py
│   │
│   ├── config/
│   │   └── configuration.py
│   │
│   ├── constants/
│   │   └── __init__.py
│   │
│   ├── utils/
│   │   └── common.py
│
├── templates/                  # HTML templates (if used)
├── venv/                       (not pushed to GIT)
│
├── app.py                      # Flask app for predictions
├── main.py                     # Training pipeline entry point
├── template.py                 # Template generator
├── Dockerfile                  # Docker setup
├── requirements.txt
├── setup.py
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🔄 ML Workflow

1. **Data Ingestion**
   Load data from source

2. **Data Validation**
   Validate schema, missing values, and consistency

3. **Data Transformation**

   * Feature engineering
   * Data preprocessing

4. **Model Training**
   Train the ML model

5. **Model Evaluation**
   Track experiments using MLflow / Dagshub

---

## 🧩 Development Workflow

Whenever a new stage was added, I followed:

1. Update `config.yaml`
2. Update `schema.yaml`
3. Update `params.yaml`
4. Update config entity
5. Update configuration manager
6. Implement component
7. Create/update pipeline
8. Update `main.py`

---

## 🔧 Key Concepts Used

* Modular coding
* YAML-based configuration
* Dataclasses
* Pipeline-based execution
* Experiment tracking (MLflow, Dagshub)
* Flask API development
* Docker containerization

---

## ▶️ How to Run (Training Pipeline)

```bash
conda create -n mlproj python=3.10 -y
conda activate mlproj

pip install -r requirements.txt

python main.py
```

---

## 🌐 Running the Flask App

```bash
python app.py
```

Then open your browser and access:

```
http://localhost:8000
```

---

## 🐳 Running with Docker

```bash
# Build Docker image
docker build -t ml-project .

# Run container
docker run -p 8000:8000 ml-project
```

---

## 📊 Experiment Tracking

* Used **MLflow** for tracking experiments
* Used **Dagshub** for versioning and reproducibility

---

## 🎯 Why I Built This

I created this project to:

* Understand how real ML pipelines work
* Practice writing clean and modular code
* Learn deployment using Flask and Docker
* Prepare for interviews and real-world projects

---

## 👨‍💻 Author

Prabhjot Singh
