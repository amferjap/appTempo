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
                script {
                    dockerImagweb = docker.build(registryweb, "-f ${dockerfilePathback}/.")
                }
            }
        }
        stage ('Build Docker backend'){
            steps {
                script {
                    dockerImagback = docker.build(registryback, "-f ${dockerfilePathbackpan}/.")
                }
            }
        }
        stage ('Build Docker frontend'){
            steps {
                script {
                    dockerImagfront = docker.build(registryfront, "-f ${dockerfilePathfront}/.")
                }
            }
        }
        stage ('Push webscrapp'){
            steps {
                script {
                    docker.withRegistry('', registryCredential){
                        dockerImagweb.push()
                    }
                }
            }
        }
        stage ('Push backend'){
            steps {
                script {
                    docker.withRegistry('', registryCredential){
                        dockerImagback.push()
                    }
                }
            }
        }
        stage ('Push front'){
            steps {
                script {
                    docker.withRegistry('', registryCredential){
                        dockerImagfront.push()
                    }
                }
            }
        }
    }
}
