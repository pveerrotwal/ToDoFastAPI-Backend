pipeline {
    agent any
    environment {
        DOCKER_COMPOSE_VERSION = '1.29.2'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build and Run Backend') {
            steps {
                script {
                    // Install Docker Compose (if not already installed)
                    sh "curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose"
                    sh 'chmod +x /usr/local/bin/docker-compose'

                    // Build and run the backend Docker container
                    sh 'docker-compose -f docker-compose.yml up -d --build'
                }
            }
        }
        stage('Test Backend') {
            steps {
                // Run backend tests if applicable
                // Example: sh 'docker-compose -f docker-compose.backend.yml exec <backend_service_name> pytest'
            }
        }
        stage('Security Scan') {
            steps {
            sh 'curl -fsSL https://raw.githubusercontent.com/ZupIT/horusec/main/deployments/scripts/install.sh | bash -s latest'
            sh 'horusec start -p="./" -e="true"'
          }
        }
    }
    post {
        always {
            // Clean up backend Docker container after pipeline execution
            sh 'docker-compose -f docker-compose.yml down'
        }
    }
}
