pipeline {
    agent {
        docker { image 'python:3.5.1'}
    }
    stages {
        stage ('show python version') {
            steps {
                sh 'python --version'
            }
        }
    }
}