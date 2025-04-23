# Machine Learning Pipeline with Jenkins

## Overview

This project implements an automated Machine Learning (ML) pipeline using Jenkins, designed to streamline the process of data collection, preprocessing, model training, evaluation, and deployment. The pipeline is defined in a `Jenkinsfile` and integrates with GitHub for continuous integration, enabling automatic builds on code changes via webhooks.

## Features

- **Automated Workflow**: The pipeline handles all stages of an ML project, from data collection to model deployment.
- **Parameterized Builds**: Supports parameters like `BRANCH_NAME` (default: `main`) and `MODEL_TYPE` (options: `logistic_regression`, `random_forest`) for flexible execution.
- **Environment Isolation**: Uses a Python virtual environment to manage dependencies, ensuring reproducibility.
- **Error Handling**: Includes checks for missing scripts and dependency installation errors.
- **GitHub Integration**: Configured to trigger builds automatically on pushes to the repository.

## Pipeline Stages

1. **Clean Workspace**: Clears the workspace to ensure a fresh start for each build.
2. **Checkout**: Clones the specified branch from the GitHub repository.
3. **Setup Directories**: Creates `data` and `models` directories to store datasets and trained models.
4. **Setup Environment**: Sets up a Python virtual environment and installs dependencies from `requirements.txt`.
5. **Data Collection**: Runs `data_collection.py` to gather data (if the script exists).
6. **Data Preprocessing**: Executes `preprocessing.py` to clean and prepare data (if the script exists).
7. **Model Training**: Trains a model using `train_model.py` with the specified `MODEL_TYPE` (if the script exists).
8. **Model Evaluation**: Evaluates the model with `evaluate_model.py` (if the script exists).
9. **Deploy Model**: Deploys the model using `deploy_model.py` (if the script exists).

## Prerequisites

- **Jenkins**: Installed and running (tested on Windows).
- **Git**: Installed and configured in Jenkins.
- **Python**: Version 3.11 or compatible (due to dependency requirements).
- **GitHub Webhook**: Configured to trigger builds on push events (Payload URL: `<Jenkins-URL>/github-webhook/`).

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ricardobarbieri/jenkinsPipeline.git
   cd jenkinsPipeline
