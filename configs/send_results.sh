#!/bin/bash

folder=$1
job_name=$2
folder_lower=$(echo "${folder}" | tr '[:upper:]' '[:lower:]')

ALLURE_RESULTS_DIRECTORY="tests/PlaywrightFramework/projects/${folder}/allure-results"
ALLURE_SERVER="http://domain:port"

# Project ID according to existent projects in your Allure container - Check endpoint for project creation >> `[POST]/projects`
PROJECT_ID=${folder_lower}
echo $folder
echo $folder_lower
#Busca si ya existe el proyecto
response=$(eval curl -X GET "$ALLURE_SERVER/allure-docker-service/projects/search?id=$PROJECT_ID" -H 'accept: */*' | jq -r '.meta_data.message')

echo $response
if [ "${response}" == 'Project not found' ]; then
        echo "El proyecto no existe en Allure. Construyendo..."
        #curl -X 'POST' "$ALLURE_SERVER/allure-docker-service/projects" -H 'accept: */*' -H 'Content-Type: application/json' -d "{'id': $PROJECT_ID}"
        curl -X 'POST' \
          "$ALLURE_SERVER/allure-docker-service/projects" \
          -H 'accept: */*' \
          -H 'Content-Type: application/json' \
          -d "{
          \"id\": \"${PROJECT_ID}\"
  }"

#curl -X 'POST' 'http://testmcil01.sis.ad.bia.itau:5050/allure-docker-service/projects' -H 'accept: */*' -H 'Content-Type: application/json' -d '{"id": "prueba"}'
fi

 DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
 FILES_TO_SEND=$(ls -dp $DIR/$ALLURE_RESULTS_DIRECTORY/* | grep -v /$)
 if [ -z "$FILES_TO_SEND" ]; then
   exit 1
   fi

   FILES=''
   for FILE in $FILES_TO_SEND; do
     FILES+="-F files[]=@$FILE "
     done

     set -o xtrace
     echo "------------------SEND-RESULTS------------------"
     curl -X POST "$ALLURE_SERVER/allure-docker-service/send-results?project_id=$PROJECT_ID" -H 'Content-Type: multipart/form-data' $FILES -ik

#
#
#     #If you want to generate reports on demand use the endpoint `GET /generate-report` and disable the Automatic Execution >> `CHECK_RESULTS_EVERY_SECONDS: NONE`
#     #echo "------------------GENERATE-REPORT------------------"
#     #EXECUTION_NAME='execution_from_my_bash_script'
#     #EXECUTION_FROM='http://google.com'
#     #EXECUTION_TYPE='bamboo'
#
#     #You can try with a simple curl
#     #RESPONSE=$(curl -X GET "$ALLURE_SERVER/allure-docker-service/generate-report?project_id=$PROJECT_ID&execution_name=$EXECUTION_NAME&execution_from=$EXECUTION_FROM&execution_type=$EXECUTION_TYPE" $FILES)
#     #ALLURE_REPORT=$(grep -o '"report_url":"[^"]*' <<< "$RESPONSE" | grep -o '[^"]*$')
#
#     #OR You can use JQ to extract json values -> https://stedolan.github.io/jq/download/
#     #ALLURE_REPORT=$(echo $RESPONSE | jq '.data.report_url')