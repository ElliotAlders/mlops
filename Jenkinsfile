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
                sh 'venv/bin/pip install -r requirements.txt'
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
                sh 'flake8 --filename=*.py --exclude=venv /var/lib/jenkins/workspace/CI-CD/'
            }
        }
        stage('Docker Build and Push') {
            steps {
                sh 'docker build -t mlops-image -f Dockerfile .'
                sh 'docker tag mlops-image lex77/mlops-image'
                sh 'docker push lex77/mlops-image'
            }
        }
        stage('Deploy to HF Space') {
            steps {
                sh 'rm -rf huggingface'
                sh 'git clone https://alexray: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@huggingface.co/spaces/alexray/btc_predictor huggingface'
                sh 'rsync -av --exclude=README.md /var/lib/jenkins/workspace/CI-CD/* huggingface/'
                dir('huggingface') {
                    sh 'git add .'
                    sh 'git commit -a -m "Update from Jenkins"'
                    sh 'git push origin HEAD:main'
                }
            }
        }
    }
}
