pipeline {
    agent { node{label 'master'} }

/* Creación de variables de entorno */

    environment {
/* Ruta de los Dockerfiles de cada programa, se depe especificar la ruta absoluta de cada Dockerfile después de que el servdor clone el repositorio de GitHub*/
        dockerfilePathback = '/var/lib/jenkins/workspace/appTempo/backend/src/'
        dockerfilePathbackpan = '/var/lib/jenkins/workspace/appTempo/backend/srp/'
        dockerfilePathfront = '/var/lib/jenkins/workspace/appTempo/frontend/'
/* Nombres de los repsitorios donde se subirán las imagenes a DockerHub*/
        registryweb = 'ruvika07/webscrapping:v1'
        registryback = 'ruvika07/backend:v1'
        registryfront = 'ruvika07/frontend:v1'
        regsitryCredential = 'Madroño12'
    }

    stages {
/* Compilación de las imagenes, hay un stage por cada programa*/
        stage ('Build Docker web'){
            steps {
/*sh Indica que es un comando que realizará el usuario jenkins en el propio servidor*/
                sh 'docker build -t $registryweb $dockerfilePathback'
            }
        }
        stage ('Build Docker backend'){
            steps {
                sh 'docker build -t $registryback $dockerfilePathbackpan'
            }
        }
        stage ('Build Docker frontend'){
            steps {
                sh 'docker build -t $registryfront $dockerfilePathfront'
            }
        }
/* Una vez terminada la fase de compilación, inicia la subida de las imagenes. Se realiza un stage por cada programa*/
        stage ('Push webscrapp'){
            steps {
/* En el primer stage se hace el login a DockerHub en el servidor, con una vez basta para poder realizar el resto de docker push*/
/*                sh 'docker login -u ruvika07 -p $regsitryCredential' */
                sh 'docker push $registryweb'
            }
        }
        stage ('Push backend'){
            steps {
                sh 'docker push $registryback'
            }
        }
        stage ('Push front'){
            steps {
                sh 'docker push $registryfront'
            }
        }
    }
}
