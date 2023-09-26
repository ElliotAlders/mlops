pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                // Create a virtual environment
                sh 'python3 -m venv venv'
                // Activate the virtual environment
                sh '. venv/bin/activate'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install project dependencies from requirements.txt
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Build') {
            steps {
                // Run your project script
                sh 'python3 data_creation.py'
            }
        }
    }
}
