pipeline {
    agent any
    environment {
        IMAGENAME = "test_scripts"
    }
    stages {
        stage ('Build') {
            steps {
                dir('django_sites') {
                    sh './build.sh'
                }
            }
        }
        stage ('Deploy') {
            steps {
                dir('django_sites/deploy/home') {
                    sh './deploy.sh'
                }
            }
        }
    }
}