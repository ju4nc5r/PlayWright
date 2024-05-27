FROM jenkins/ssh-agent:latest

# Configuracion de proxy
ENV http_proxy="http://eproxy-itau-ar.goskope.com:8081"
ENV https_proxy="http://eproxy-itau-ar.goskope.com:8081"
ENV no_proxy="localhost, 127.0.0.1, localadress, .localdomain.com, .sis.ad.bia.itau"
ENV JENKINS_AGENT_SSH_PUBKEY="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDIxS1d68I/hqLyrYLM0GNHuxRwvJr8VqIq/vLgcU/VlVkL2PXFn/SSmcyeLwulL70EGW2dMFT3M+7q/GDOOT77g9ixx2DTNtTUv2ikDnnNUrcXsyXGVERCqZ4vwjw6XBf6YaAKOZESUhOGvmMQ6Rz9kwc27Mj59rb0DSdnd3LNASLWLv1mnwIZj8EoBbfvoXMJ0yL+7tFA0VFOH1BfE1k7Oezxos0OPAmuz0LH8PMBF9yiy3Ue/ZBD9/MyEsDBzxvMQCiqTonQJYVaSEHndCIaHn7JotOB4WxR/rI3gpmHzLxY3prd9Hmd4z1CuKZRjdTskOp9NzVHmefkKb3VoAE+YHOkdvXeBZanTeja72ZALYLtWPyXriC3abkBzcQu03/hEoy0QSlA6v26Tr5JSvwzNyBkaXakx3W2LWifw1ZK0029oMeFlcwBqELiGKBG13cCF7FWxC+12TElQzMZ/VXUGtd/IDstOwvLnyF31edbA/gWDAjOlN9/RpIyO7UNSls= jenkins@085d90c05939"

# Instala Python y Git
RUN apt-get update && \
    apt-get install -y python3 python3-pip git curl vim

# Opcional: Configura el entorno virtual de Python
# RUN python3 -m venv /venv
# ENV PATH="/venv/bin:$PATH"

# Tu resto de instrucciones para configurar el agente Jenkins...