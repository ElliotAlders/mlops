pipeline {
  agent any
  stages {
    stage ('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage ('Build') {
      steps {
        sh 'python3 data_creation.py'
      }
    }
  }
}
