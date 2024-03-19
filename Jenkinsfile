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
            steps {
                // Define SonarQube scanner home
                def scannerHome = tool 'SonarScanner 4.0'

                // Run SonarQube scanner
                withSonarQubeEnv('SonarQubeServer') {
                    sh "${scannerHome}/bin/sonar-scanner"
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

