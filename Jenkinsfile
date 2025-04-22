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
                bat 'mkdir data models'
            }
        }
        stage('Setup Environment') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Data Collection') {
            steps {
                bat 'python scripts\\data_collection.py'
            }
        }
        stage('Data Preprocessing') {
            steps {
                bat 'python scripts\\preprocessing.py'
            }
        }
        stage('Model Training') {
            steps {
                bat 'python scripts\\train_model.py'
            }
        }
        stage('Model Evaluation') {
            steps {
                bat 'python scripts\\evaluate_model.py'
            }
        }
        stage('Deploy Model') {
            steps {
                // Nota: 'start /B' inicia o processo em segundo plano no Windows.
                // Considere Docker ou um servidor WSGI para produção.
                bat 'start /B python scripts\\deploy_model.py'
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
