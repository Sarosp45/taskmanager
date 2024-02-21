pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from Git repository
                git 'https://github.com/Sarosp45/taskmanager.git'
            }
        }

        stage('Build') {
            steps {

                sh 'python manage.py test'
            }
        }
    }

    post {
        success {
            echo 'Build successful! You can add deployment steps here.'
        }
        failure {
            echo 'Build failed! Take necessary actions for failure.'
        }
    }
}
