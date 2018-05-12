pipeline {
    agent {
        docker { image 'python:3.5.1'}
    }
    environment {
        VAR1 = 'this is var1'
    }
    stages {
        stage ('show python version') {
            steps {
                sh 'python --version'
            }
        }
        stage ('test environment') {
            sh './print_environment.sh'
        }
    }
}