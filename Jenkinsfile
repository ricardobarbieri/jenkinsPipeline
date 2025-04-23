pipeline {
    agent any

    stages {
        stage('Clean Workspace') {
            steps {
                echo 'Limpando o workspace...'
                cleanWs()
            }
        }

        stage('Checkout') {
            steps {
                echo 'Fazendo checkout do repositório...'
                git branch: 'main', url: 'https://github.com/ricardobarbieri/jenkinsPipeline.git'
            }
        }

        stage('Setup Directories') {
            steps {
                echo 'Configurando diretórios...'
                bat '''
                    echo Verificando diretórios existentes...
                    dir
                    rmdir /S /Q data || echo Diretório data não existe, continuando...
                    rmdir /S /Q models || echo Diretório models não existe, continuando...
                    mkdir data models
                    echo Diretórios criados:
                    dir
                '''
            }
        }

        stage('Setup Environment') {
            steps {
                echo 'Configurando ambiente virtual...'
                bat '''
                    python --version
                    pip --version
                    if exist requirements.txt (
                        type requirements.txt
                    ) else (
                        echo requirements.txt não encontrado!
                    )
                    python -m venv venv
                    venv\\Scripts\\activate.bat
                    python -m pip install --upgrade pip
                    if exist requirements.txt (
                        pip install -r requirements.txt --verbose
                    ) else (
                        echo Pulando instalação de dependências, requirements.txt não encontrado.
                    )
                '''
            }
        }

        stage('List Scripts') {
            steps {
                echo 'Listando scripts disponíveis...'
                bat '''
                    dir scripts
                '''
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
