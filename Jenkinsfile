pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        credentialsId: 'b995d3dc-0108-4276-a392-018940558c08',
                        url: 'git@github.com:jalts-808/launch101.git'
                    ]]
                ])
            }
        }
        stage('Check Python Version') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Remove the venv directory if it already exists
                sh 'rm -rf /var/jenkins_home/jobs/flask-ecommerce-pipeline/workspace/venv'

                // Create a new virtual environment
                sh 'python3 -m venv /var/jenkins_home/jobs/flask-ecommerce-pipeline/workspace/venv'

                // Ensure the venv bin is executable
                sh 'chmod +x /var/jenkins_home/jobs/flask-ecommerce-pipeline/workspace/venv/bin/activate'

                // Install dependencies
                sh '/var/jenkins_home/jobs/flask-ecommerce-pipeline/workspace/venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh '/var/jenkins_home/jobs/flask-ecommerce-pipeline/workspace/venv/bin/python -m unittest discover -s tests'
            }
        }
    }
}



