pipeline {
    agent any

    stages {
        stage('Echo') {
            steps {
                echo 'hello world from the testtttt'
            }
        }
    }
}
