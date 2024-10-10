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
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh './venv/bin/python -m unittest discover -s tests'
            }
        }
    }
}



