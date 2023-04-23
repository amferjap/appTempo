pipeline {
    agent { node{label 'master'} }

    environment {
        dockerfilePathback = '/var/lib/jenkins/workspace/appTempo/backend/src/'
        dockerfilePathbackpan = '/var/lib/jenkins/workspace/appTempo/backend/srp/'
        dockerfilePathfront = '/var/lib/jenkins/workspace/appTempo/frontend/'
        registryweb = 'ruvika07/webscrapping:v1'
        regsitryback = 'ruvika07/backend:v1'
        registryfront = 'ruvika07/frontend:v1'
        regsitryCredential = 'Madroño12'
    }

    stages {
        stage ('Build Docker web'){
            steps {
                sh 'docker build -t ${regsitryweb} ${dockerfilePathback}'
            }
        }
        stage ('Build Docker backend'){
            steps {
                sh 'docker build -t ${regsitryback} ${dockerfilePathbackpan}'
            }
        }
        stage ('Build Docker frontend'){
            steps {
                sh 'docker build -t ${regsitryfront} ${dockerfilePathfront}'
            }
        }
        stage ('Push webscrapp'){
            steps {
                sh 'docker login -u ruvika07 -p ${regsitryCredential}'
                sh 'docker push ${registryweb}'
            }
        }
        stage ('Push backend'){
            steps {
                sh 'docker push ${registryback}'
            }
        }
        stage ('Push front'){
            steps {
                sh 'docker push ${registryfront}'
            }
        }
    }
}
