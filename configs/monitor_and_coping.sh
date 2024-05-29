#!/bin/bash

#Directorio que se va a monitorear
WATCH_DIR="/home/jenkins/workspace"

#Archivo que se va a copiar
git="/home/jenkins/workspace/git.sh"
send_results="/home/jenkins/workspace/send_results.sh"

copy_to_new_dir() {
        local new_dir="$1"
        echo "Nueva carpeta detectada: $new_dir"
        cp -r "$git" "$new_dir"
        cp -r "$send_results" "$new_dir"
        echo "git.sh y send_result.sh se copiaron a $new_dir"
}

inotifywait -m -e create --format '%w%f' "$WATCH_DIR" | while read NEW_PATH
do
    # Verificar si la nueva ruta es un directorio
    if [ -d "$NEW_PATH" ]; then
        copy_to_new_dir "$NEW_PATH"
    fi
done
