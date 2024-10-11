pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        credentialsId: 'b995d3dc-0108-4276-a392-018940558c08',  // Replace with your credentials ID
                        url: 'git@github.com:jalts-808/launch101.git'  // Replace with your GitHub SSH URL
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
                sh 'python3 -m venv /var/jenkins_home/jobs/flask-ecommerce-pipeline/workspace/venv'  // Full path to venv
                sh 'chmod +x /var/jenkins_home/jobs/flask-ecommerce-pipeline/workspace/venv/bin/activate'  // Ensure activate is executable
                sh '/var/jenkins_home/jobs/flask-ecommerce-pipeline/workspace/venv/bin/pip install -r requirements.txt'  // Install dependencies
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh '/var/jenkins_home/jobs/flask-ecommerce-pipeline/workspace/venv/bin/python -m unittest discover -s tests'  // Run tests
            }
        }
    }
}


