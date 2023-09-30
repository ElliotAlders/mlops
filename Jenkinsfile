pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Pull Datasets') {
            steps {
                sh 'dvc pull --force'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 data_creation.py'
                sh 'python3 data_preprocessing.py'
                sh 'python3 model_preparation.py'
                sh 'python3 model_testing.py'
            }
        }
        stage('Unit Tests') {
            steps {
                sh 'python3 -m unittest discover -s tests -p "test_*.py"'
            }
        }
        stage('PEP8 Compliance Check') {
            steps {
                sh 'flake8 /var/lib/jenkins/workspace/CI-CD/'
            }
        }
    }
}
