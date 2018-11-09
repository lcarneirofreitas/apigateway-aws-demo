pipeline {

  agent any

  environment {
    APP_NAME = 'simple_api'
  }

  stages {

    stage('Build') {
      steps {

        sh 'echo Build'
        sh 'cd simple_api && docker build . -t lcarneirofreitas/simple_api:latest'
      }
    }

  post {

    success {
      sh 'echo Success'
    }

    failure {
      sh 'echo Failure'
    }
  }
}
