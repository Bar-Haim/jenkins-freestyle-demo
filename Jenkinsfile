pipeline {
    agent any

    stages {
        stage('Run Hello Script') {
            steps {
                sh 'chmod +x app.py'
                sh './app.py'
            }
        }
    }
}

