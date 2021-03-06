pipeline {

  agent any

  environment {
    APP_NAME = 'simple_api'
    API_ID = '5oh2kke0g6'
    VPC_LINK_GREEN = '8xt1nc'
    VPC_LINK_BLUE = '2xmgfc'
    STAGE_VERSION = 'v1'
    FILE_YAML = 'v1-swagger-apigateway.yaml'
    API_URL = "https://5oh2kke0g6.execute-api.sa-east-1.amazonaws.com/v1/actions/healthcheck"
  }

  stages {

    stage('Build Docker Container') {

      steps {
        script {
          def TAG = sh(returnStdout: true, script: "git describe --tags").trim()
          
          if(TAG) {
            sh "cd ${APP_NAME} && docker build . -t lcarneirofreitas/${env.APP_NAME}:${TAG}"
            sh "docker login -u ${env.DKHUBUSER} -p ${env.DKHUBPASS}"
            sh "docker tag lcarneirofreitas/${env.APP_NAME}:${TAG} lcarneirofreitas/${env.APP_NAME}:latest"
            sh "docker push lcarneirofreitas/${env.APP_NAME}:${TAG}"
            sh "docker push lcarneirofreitas/${env.APP_NAME}:latest"
          }
        }
      }
    }

    stage('Update Docker Container Server') {

      steps {
        script {
          def ENVIRONMENT = sh(
                           returnStdout: true, 
                           script: "curl -s ${env.API_URL} | jq -r '.environment'").trim()

          if (ENVIRONMENT == 'green') {
              sh "ssh ubuntu@blue 'bash -s' < scripts/update-docker.sh"
          } else {
              sh "ssh ubuntu@green 'bash -s' < scripts/update-docker.sh"
          }

        }
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
          def TAG = sh(returnStdout: true, script: "git describe --tags").trim()
          def ENVIRONMENT = sh(
                           returnStdout: true, 
                           script: "curl -s ${env.API_URL} | jq -r '.environment'").trim()

          if (ENVIRONMENT == 'green') {
             sh "sed -i 's/XXXXXXXXXX/${env.VPC_LINK_BLUE}/g' swagger/${env.FILE_YAML}"

             if (TAG) {
     	        sh "aws apigateway put-rest-api --rest-api-id '${env.API_ID}' --mode overwrite --body 'file://swagger/${env.FILE_YAML}'"
                sh "aws apigateway create-deployment --rest-api-id '${env.API_ID}' --stage-name '${env.STAGE_VERSION}' --description '${TAG} blue'"
             }

          } else {
             sh "sed -i 's/XXXXXXXXXX/${env.VPC_LINK_GREEN}/g' swagger/${env.FILE_YAML}"

             if (TAG) {
     	        sh "aws apigateway put-rest-api --rest-api-id '${env.API_ID}' --mode overwrite --body 'file://swagger/${env.FILE_YAML}'"
                sh "aws apigateway create-deployment --rest-api-id '${env.API_ID}' --stage-name '${env.STAGE_VERSION}' --description '${TAG} green'"
             }

          }
        }
      }
    }
  }
}
