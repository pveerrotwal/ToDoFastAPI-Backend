pipeline {
    agent any

    stages {
        stage('Build Backend') {
            steps {
                // Checkout backend repository
                git branch: 'main', url: 'https://github.com/pveerrotwal/ToDoFastAPI-Backend.git'

                // Build backend Docker image
                script {
                    echo "Building Backend"
                }
            }
        }

        stage('Deploy Backend') {
            steps {
                // Deploy backend Docker containers using docker-compose-backend.yml
                sh 'docker-compose -f docker-compose-backend.yml up -d'
            }
        }

        stage("Sonarqube Analysis "){
            steps{
                withSonarQubeEnv('SonarQubeServer') {
                    sh ''' $SCANNER_HOME/bin/SonarQubeScanner -Dsonar.url=http://localhost:9000/ -Dsonar.login=squ_7d32eb0bbd7abf76e34409b8cc53c24a40000670 -Dsonar.projectName=ToDoFastAPI \
                    -Dsonar.java.binaries=. \
                    -Dsonar.projectKey=ToDoFastAPI '''
    
                }
            }
        }
    }

    post {
        always {
            // Clean up Docker resources
            sh 'docker-compose -f docker-compose-backend.yml down'
        }
    }
}

