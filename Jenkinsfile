pipeline {
    agent any // Executa no nó padrão do Jenkins (Windows, conforme o log)

    stages {
        stage('Checkout') {
            steps {
                // Faz checkout do repositório Git
                git url: 'https://github.com/ricardobarbieri/jenkinsPipeline.git', branch: 'main'
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
                // Comandos de depuração para verificar ambiente
                bat 'python --version' // Mostra a versão do Python
                bat 'pip --version' // Mostra a versão do pip
                bat 'type requirements.txt' // Mostra o conteúdo do requirements.txt

                // Cria e ativa um ambiente virtual
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate.bat'

                // Atualiza o pip no ambiente virtual
                bat 'python -m pip install --upgrade pip'

                // Instala os pacotes com log detalhado
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
                // Placeholder: Adicione comandos para coletar dados
                echo 'Coletando dados...'
                // Exemplo: bat 'python scripts/collect_data.py'
            }
        }

        stage('Data Preprocessing') {
            steps {
                // Placeholder: Adicione comandos para pré-processamento
                echo 'Pré-processando dados...'
                // Exemplo: bat 'python scripts/preprocess_data.py'
            }
        }

        stage('Model Training') {
            steps {
                // Placeholder: Adicione comandos para treinar o modelo
                echo 'Treinando modelo...'
                // Exemplo: bat 'python scripts/train_model.py'
            }
        }

        stage('Model Evaluation') {
            steps {
                // Placeholder: Adicione comandos para avaliar o modelo
                echo 'Avaliando modelo...'
                // Exemplo: bat 'python scripts/evaluate_model.py'
            }
        }

        stage('Deploy Model') {
            steps {
                // Placeholder: Adicione comandos para deploy
                echo 'Fazendo deploy do modelo...'
                // Exemplo: bat 'python scripts/deploy_model.py'
            }
        }
    }

    post {
        always {
            // Executa sempre, independentemente do resultado
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
