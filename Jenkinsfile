pipeline {
    agent any

    parameters {
        string(name: 'BRANCH_NAME', defaultValue: 'main', description: 'Branch para build')
        choice(name: 'MODEL_TYPE', choices: ['logistic_regression', 'random_forest'], description: 'Tipo de modelo')
    }

    stages {
        stage('Clean Workspace') {
            steps {
                // Limpa o workspace antes de iniciar o build
                cleanWs()
            }
        }

        stage('Checkout') {
            steps {
                git branch: "${params.BRANCH_NAME}", url: 'https://github.com/ricardobarbieri/jenkinsPipeline.git'
            }
        }

        stage('Setup Directories') {
            steps {
                bat '''
                    rmdir /S /Q data || exit 0
                    rmdir /S /Q models || exit 0
                    mkdir data models
                '''
            }
        }

        stage('Setup Environment') {
            steps {
                // Depuração: Mostra versões e conteúdo do requirements.txt
                bat 'python --version'
                bat 'pip --version'
                bat 'type requirements.txt || echo "requirements.txt não encontrado"'

                // Cria e ativa o ambiente virtual, atualiza pip e instala dependências
                script {
                    try {
                        bat '''
                            python -m venv venv
                            venv\\Scripts\\activate.bat
                            python -m pip install --upgrade pip
                            pip install -r requirements.txt --verbose
                        '''
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
                        bat '''
                            venv\\Scripts\\activate.bat
                            python scripts/data_collection.py
                        '''
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
                        bat '''
                            venv\\Scripts\\activate.bat
                            python scripts/preprocessing.py
                        '''
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
                        bat """
                            venv\\Scripts\\activate.bat
                            python scripts/train_model.py --model-type ${params.MODEL_TYPE}
                        """
                        echo "Treinando modelo (${params.MODEL_TYPE})..."
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
                        bat '''
                            venv\\Scripts\\activate.bat
                            python scripts/evaluate_model.py
                        '''
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
                        bat '''
                            venv\\Scripts\\activate.bat
                            python scripts/deploy_model.py
                        '''
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
