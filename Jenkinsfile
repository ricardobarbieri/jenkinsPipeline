pipeline {
    agent any // Executa no nó padrão do Jenkins (Windows, conforme logs)

    stages {
        stage('Checkout') {
            steps {
                // Faz checkout do repositório Git
                git branch: 'main', url: 'https://github.com/ricardobarbieri/jenkinsPipeline.git'
            }
        }

        stage('Setup Directories') {
            steps {
                // Cria diretórios "data" e "models"
                bat 'mkdir data models'
            }
        }

        stage('Setup Environment') {
            steps {
                // Comandos de depuração antes da instalação
                bat 'python --version' // Mostra a versão do Python
                bat 'pip --version' // Mostra a versão do pip
                bat 'type requirements.txt' // Mostra o conteúdo do requirements.txt

                // Cria e ativa um ambiente virtual
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate.bat'

                // Atualiza o pip no ambiente virtual
                bat 'python -m pip install --upgrade pip'

                // Instala os pacotes com log detalhado e tratamento de erro
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
                // Verifica se o script existe antes de rodar
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
                        // Evita o uso de start /B, roda diretamente no ambiente virtual
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
