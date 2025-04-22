pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ricardobarbieri/jenkinsPipeline.git'
            }
        }
        stage('Setup Directories') {
            steps {
                sh 'mkdir -p data models'
            }
        }
        stage('Setup Environment') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Data Collection') {
            steps {
                sh 'python3 scripts/data_collection.py'
            }
        }
        stage('Data Preprocessing') {
            steps {
                sh 'python3 scripts/preprocessing.py'
            }
        }
        stage('Model Training') {
            steps {
                sh 'python3 scripts/train_model.py'
            }
        }
        stage('Model Evaluation') {
            steps {
                sh 'python3 scripts/evaluate_model.py'
            }
        }
        stage('Deploy Model') {
            steps {
                // Nota: 'nohup' é mantido, mas considere Docker para produção
                sh 'nohup python3 scripts/deploy_model.py &'
            }
        }
    }
    post {
        success {
            echo 'Pipeline concluído com sucesso!'
        }
        failure {
            echo 'Pipeline falhou. Verifique os logs.'
        }
    }
}