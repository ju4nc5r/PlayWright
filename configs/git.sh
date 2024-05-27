#!/bin/bash

# Directorio que se va a monitorear
WATCH_DIR="/home/jenkins/workspace"

# Archivo que se va a copiar
git="/home/jenkins/workspace/git.sh"
post_results="/home/jenkins/workspace/send_results.sh"

# Función que se ejecuta cuando se detecta una nueva carpeta
copy_to_new_dir() {
    local new_dir="$1"
    echo "Nueva carpeta detectada: $new_dir"
    cp -r "$git" "$new_dir"
    echo "Carpeta copiada a $new_dir"
}

# Monitorear el directorio en busca de nuevas carpetas
inotifywait -m -e create --format '%w%f' "$WATCH_DIR" | while read NEW_PATH
do
    # Verificar si la nueva ruta es un directorio
    if [ -d "$NEW_PATH" ]; then
        copy_to_new_dir "$NEW_PATH"
    fi
done


# comando para ejecutar el script monitor_and_copy: ./monitor_and_copy.sh > monitor.log 2>&1 &
# comando para matar todos los procesos vincualdos al script monitor_and_copy: pkill -f monitor_and_copy.sh

