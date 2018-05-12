pipeline {
    agent any
    environment {
        IMAGENAME = "test_scripts"
    }
    stages {
        stage ('Build') {
            dir('django_sites') {
                steps {
                    sh './build.sh'
                }
            }
        }
        stage ('Deploy') {
            dir('django_sites/deploy/home') {
                steps {
                    sh './deploy.sh'
                }
            }
        }
    }
}