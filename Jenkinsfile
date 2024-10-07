pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh '. venv/bin/activate && pytest tests/'
            }
        }
    }

    post {
        always {
            junit 'reports/*.xml'
        }
    }
}
