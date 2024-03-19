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

        stage('Horusec Scan') {
            steps {
                // Install Horusec and run the security scan
                sh 'curl -fsSL https://raw.githubusercontent.com/ZupIT/horusec/main/deployments/scripts/install.sh | bash -s latest'
                sh 'horusec start -p="./" -a 48ae8779421749a4b44393e1c2853163 --disable-docker="true"'
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

