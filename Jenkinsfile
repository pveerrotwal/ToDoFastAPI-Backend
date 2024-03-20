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

         stage('SonarQube analysis') {
         withSonarQubeEnv(credentialsId: 'squ_7d32eb0bbd7abf76e34409b8cc53c24a40000670', installationName: 'SonarQubeServer') { // You can override the credential to be used
         sh 'mvn org.sonarsource.scanner.maven:sonar-maven-plugin:3.7.0.1746:sonar'
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

