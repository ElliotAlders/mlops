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
        }
        stage('Pull Datasets') {
            steps {
                sh 'dvc pull'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 data_creation.py'
            }
        }
    }
}
