FROM jenkins/ssh-agent:latest

ENV JENKINS_AGENT_SSH_PUBKEY="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDFFiHsdNUJ/+a3Jk4bbEU+xkK8E5eLS3b/8ULfn7DezLofSB0H0xcY+BGtc6lsJNDQPksljzLSmqvJ0CkyVcCIyBmtHtaOSNSpXM9MgR8dUkNK3e/ROJUdwQwoYmL3823UXOI2OSKgArwD9hBkEABVusA9bx599MLYp9jSwuUXmFtp+unVx2b83IkHtaWnl5nUFRhiVzBgUuJlxShhwct2sLzkKpLAolZzQox+vKhCqk1Yx4etPsDJiWAjXI4LTiaPpH4UFraxWzQI9XyAVBIrn7jVvha4Br+q1TCX9s96BDehwNHpTDi4bQyqt357ct9rrcSJWBjr9ipjLBO6bGp7xIsox3yQt36cA8FDamVNvVjAoC2LJ1sU1gYrq+YmMygw1hQIgEhyK0sCbJ7gWovvKOLzj2LEu3kyNK9Cx+QUOV4ijHtfcmgkC99TW4htnCumTwepPa2PAhkSlj2Ju09uPVTnzrVzlrY0+uzpH/1GVcZ0GhcN52hMLRggtVawdy8= jenkins@6e9893126644"

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
