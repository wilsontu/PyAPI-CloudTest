pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Building the project..."
                // e.g. Docker build, or pip install, etc.
                // sh 'docker build -t my-api-tests:latest .'
            }
        }

        stage('Test') {
            steps {
                echo "Running tests..."
                // e.g. Docker run or pytest
                // sh 'docker run --rm my-api-tests:latest'
                // or, if you're not using Docker:
                // sh 'pytest --maxfail=1 --disable-warnings -v'
            }
        }
    }
    post {
        always {
            echo "Pipeline finished."
        }
    }
}
