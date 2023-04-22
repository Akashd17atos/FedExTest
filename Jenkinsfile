pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Build app'
            }
        }
        stage('Test') {
            steps {
                echo 'Test app'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy app'
            }
        }        
        
    }
	
    post {
        always {
            echos "The Pipeline Succeed :)"
        }
        failure {
            echo "Subject: The Pipeline failed :("
        }
    }	
	
}
