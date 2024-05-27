# Accede a los parámetros pasados desde Jenkins
user=$1
pass=$2
DIR="$PWD"
FOLDER='sap-crm-tests'
FULL_PATH="$DIR/$FOLDER"

echo "${DIR}"
echo "${FULL_PATH}"

url="https://${user}:${pass}@gitlab.sis.ad.bia.itau/homologacion/sap-crm-tests.git"
#git -c http.sslVerify=false clone -b dev "${url}"


if [ -e "$FULL_PATH" ]; then
     echo "La carpeta '${FOLDER}' existe en '${DIR}'. Haciendo git pull..."
     cd 'sap-crm-tests'
     git config http.sslVerify false
     git pull
else
     echo "La carpeta '$FOLDER' no existe en '$DIR'. Clonando rama dev..."
     git -c http.sslVerify=false clone -b dev "${url}"
     git config --global --add safe.directory "${FULL_PATH}"
 fi

