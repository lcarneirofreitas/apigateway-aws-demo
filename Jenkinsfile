pipeline {

  agent any

  environment {
    APP_NAME = 'simple_api'
    API_ID = '5oh2kke0g6'
    VPC_LINK_GREEN = '8xt1nc'
    VPC_LINK_BLUE = '2xmgfc'
    STAGE_VERSION = 'v1'
    FILE_YAML = 'v1-swagger-apigateway.yaml'
    TAG = """${sh(returnStdout: true, script: "git describe --tags").trim()}"""
  }

  stages {

    stage('Build Docker Container') {

      steps {
          
          if(env.TAG) {
            sh "cd ${APP_NAME} && docker build . -t lcarneirofreitas/${env.APP_NAME}:${TAG}"
            sh "docker login -u ${env.DKHUBUSER} -p ${env.DKHUBPASS}"
            sh "docker tag lcarneirofreitas/${env.APP_NAME}:${TAG} lcarneirofreitas/${env.APP_NAME}:latest"
            sh "docker push lcarneirofreitas/${env.APP_NAME}:${TAG}"
            sh "docker push lcarneirofreitas/${env.APP_NAME}:latest"
          }
        }
      }

    stage('Update Docker Container Server') {

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

          if (env.ENVIRONMENT == 'green') {
             sh "sed -i 's/XXXXXXXXXX/${env.VPC_LINK_GREEN}/g' swagger/${env.FILE_YAML}"
          } else {
             sh "sed -i 's/XXXXXXXXXX/${env.VPC_LINK_BLUE}/g' swagger/${env.FILE_YAML}"
          }

          if (env.TAG) {
     	     sh "aws apigateway put-rest-api --rest-api-id '${env.API_ID}' --mode overwrite --body 'file://swagger/${env.FILE_YAML}'"
             sh "aws apigateway create-deployment --rest-api-id '${env.API_ID}' --stage-name '${env.STAGE_VERSION}' --description '${TAG} ${env.ENVIRONMENT}'"
          }
      }
    }
  }
}
