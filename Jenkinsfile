pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/MuhammadAhsan-DataScientist/i201787_task.git'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t a1_image .'
            }
        }
            }
}
