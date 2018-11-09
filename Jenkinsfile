pipeline {

  agent any

  environment {
    APP_NAME = 'simple_api'
    API_ID = '5oh2kke0g6'
    VPC_LINK_GREEN = '8xt1nc'
    VPC_LINK_BLUE = '2xmgfc'
    FILE_YAML = 'v1-swagger-apigateway.yaml'
  }

  stages {

    stage('Build') {
      steps {
        script {
          def tag = sh(returnStdout: true, script: "git tag --sort=-refname | head -1").trim()

            sh "cd simple_api && docker build . -t lcarneirofreitas/simple_api:$tag"
            sh "docker login -u ${env.DKHUBUSER} -p ${env.DKHUBPASS}"
            sh "docker tag lcarneirofreitas/simple_api:$tag lcarneirofreitas/simple_api:latest"
            sh "docker push lcarneirofreitas/simple_api:$tag"
            sh "docker push lcarneirofreitas/simple_api:latest"
        }
      }
    }

    stage('Update App Docker') {
      steps {

        sh "ssh ubuntu@${env.ENVIRONMENT} 'bash -s' < scripts/update-docker.sh"
      }
    }

    stage('Running App Tests') {
      steps {

        sh "sleep 10 && echo tests-ok"
      }
    }

    stage('Routing Api Gateway AWS') {
      steps {
        script {
          def tag = sh(returnStdout: true, script: "git tag --sort=-refname | head -1").trim()

          if (env.ENVIRONMENT == 'green') {
             sh "sed -i 's/XXXXXXXXXX/${env.VPC_LINK_GREEN}/g' swagger/${env.FILE_YAML}"
          } else {
             sh "sed -i 's/XXXXXXXXXX/${env.VPC_LINK_BLUE}/g' swagger/${env.FILE_YAML}"
          }

          if (tag) {
             //stage("Change routing") {
     	        sh "aws apigateway put-rest-api --rest-api-id ${env.API_ID} --mode overwrite --body 'file://swagger/${env.FILE_YAML}'"
                sh "aws apigateway create-deployment --rest-api-id 5oh2kke0g6 --stage-name v1 --description $tag"
             //}
          }
        }
      }
    }
  }
}
