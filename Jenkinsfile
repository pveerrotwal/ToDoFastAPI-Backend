pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                // Install Python dependencies
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Lint') {
            steps {
                // Lint the Python code (optional)
                sh 'flake8 .'
            }
        }
        stage('Test') {
            steps {
                // Run backend tests (e.g., using pytest)
                sh 'pytest'
            }
        }
        stage('Security Scan') {
            steps {
             sh 'curl -fsSL https://raw.githubusercontent.com/ZupIT/horusec/main/deployments/scripts/install.sh | bash -s latest'
             sh 'horusec start -p="./" -e="true"'
            }
        }
        stage('Deploy') {
            steps {
                // Deploy the backend code (e.g., to a server)
                // Replace 'python deploy.py' with your actual deployment command
                sh 'python deploy.py'
            }
        }
    }
}
