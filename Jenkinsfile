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
                bat 'python --version'
                bat 'pip --version' 
                bat 'type requirements.txt' 


                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate.bat'

                bat 'python -m pip install --upgrade pip'

                script {
                    try {
                        bat 'pip install -r requirements.txt --verbose'
                    } catch (Exception e) {
                        echo "Erro ao instalar dependências: ${e}"
                        error "Falha na instalação do requirements.txt"
                    }
                }
            }
        }

        stage('Data Collection') {
            steps {
                script {
                    if (fileExists('scripts/data_collection.py')) {
                        bat 'venv\\Scripts\\python scripts/data_collection.py'
                        echo 'Coletando dados...'
                    } else {
                        echo 'Script scripts/data_collection.py não encontrado. Pulando etapa...'
                    }
                }
            }
        }

        stage('Data Preprocessing') {
            steps {
                script {
                    if (fileExists('scripts/preprocessing.py')) {
                        bat 'venv\\Scripts\\python scripts/preprocessing.py'
                        echo 'Pré-processando dados...'
                    } else {
                        echo 'Script scripts/preprocessing.py não encontrado. Pulando etapa...'
                    }
                }
            }
        }

        stage('Model Training') {
            steps {
                script {
                    if (fileExists('scripts/train_model.py')) {
                        bat 'venv\\Scripts\\python scripts/train_model.py'
                        echo 'Treinando modelo...'
                    } else {
                        echo 'Script scripts/train_model.py não encontrado. Pulando etapa...'
                    }
                }
            }
        }

        stage('Model Evaluation') {
            steps {
                script {
                    if (fileExists('scripts/evaluate_model.py')) {
                        bat 'venv\\Scripts\\python scripts/evaluate_model.py'
                        echo 'Avaliando modelo...'
                    } else {
                        echo 'Script scripts/evaluate_model.py não encontrado. Pulando etapa...'
                    }
                }
            }
        }

        stage('Deploy Model') {
            steps {
                script {
                    if (fileExists('scripts/deploy_model.py')) {

                        bat 'venv\\Scripts\\python scripts/deploy_model.py'
                        echo 'Fazendo deploy do modelo...'
                    } else {
                        echo 'Script scripts/deploy_model.py não encontrado. Pulando etapa...'
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline concluído. Limpando ou salvando logs...'
        }
        success {
            echo 'Pipeline executado com sucesso!'
        }
        failure {
            echo 'Pipeline falhou. Verifique os logs para detalhes.'
        }
    }
}
