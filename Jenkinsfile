pipeline {
    agent none
    environment {
        IMAGENAME = "test_scripts"
    }
    stages {
        stage ('Build') {
            steps {
                sh './django_sites/build.sh'
            }
        }
        stage ('Deploy') {
            steps {
                sh './django_sites/deploy/home/deploy.sh'
            }
        }
    }
}