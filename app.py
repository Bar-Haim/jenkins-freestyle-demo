pipeline {
    agent none  // שולטת מההתחלה על איפה כל שלב ירוץ

    stages {
        stage('Echo') {
            agent any  // השלב הזה ירוץ על כל agent פנוי
            steps {
                echo 'hello world from the testtttt'
            }
        }
    }
}
