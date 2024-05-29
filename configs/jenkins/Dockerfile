FROM jenkins/ssh-agent:latest

ENV JENKINS_AGENT_SSH_PUBKEY=

# Configuracion de proxy
ENV http_proxy=""
ENV https_proxy=""
ENV no_proxy="localhost, 127.0.0.1"


# Instala Python y Git
RUN apt-get update && \
    apt-get install -y python3 python3-pip git curl vim

# Opcional: Configura el entorno virtual de Python
# RUN python3 -m venv /venv
# ENV PATH="/venv/bin:$PATH"

# Tu resto de instrucciones para configurar el agente Jenkins...
