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
      stage('SonarQube Analysis') {
            steps {
                // Run SonarQube analysis
                sh "mvn clean package"
                sh ''' mvn sonar:sonar -Dsonar.url=http://localhost:9000/ -Dsonar.login=squ_ccf888d69b058e716e7bb6a31ac0fade7d45852c -Dsonar.projectname=FastAPI \
                -Dsonar.java.binaries=. \
                -Dsonar.projectKey=FastAPI '''
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
