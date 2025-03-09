pipeline {
    agent any 
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                // Example: building the Docker image from a Dockerfile
                sh 'docker build -t my-api-tests:latest .'
            }
        }

        stage('Run Tests') {
            steps {
                // For example, running a container that executes tests
                sh 'docker run --rm my-api-tests:latest'
            }
        }
    }
}
