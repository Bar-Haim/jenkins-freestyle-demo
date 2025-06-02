pipeline {
    agent any

    stages {
        stage('Run Hello Script') {
            steps {
                sh 'chmod +x hello.sh'
                sh './hello.sh'
            }
        }
    }
}

