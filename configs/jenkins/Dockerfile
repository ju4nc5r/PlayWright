FROM jenkins/ssh-agent:latest

ENV JENKINS_AGENT_SSH_PUBKEY="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDKBJAEB8wRY4KW3yZoeaKdFe2IGPlmavUVkprPZKUEygHKclsaYREz2Qsqd4c3R2GRTonQnWecEkeLeO2w1/21ygcR9ie/HvNKibxnMuV0RckVflyBXRsBuDY4+r4+4OksuxrnIUBks9L1+scNiIWBJWLL5ikEskCew1hyt+DchHh0esJGTWvSH+o/qP3dQFn7bFJ+NshW2wpufjxtvRl4yHRYsn5P98lue8e0AliKUaI3xaQXZtwoJavpT/N0WlMUUs2W/XEWx7fzwFfrE6eXVB447m3EpbG/+2koX8L1OaYmDXVrmiGZ95ISufd7DoODLIi2HWHOfr+fppRyKxERX9AnncOXb6VH31+4u567j8EDcQIIOlRF52GN66/ARVDuuH0X7kKB/VYx9QPr/5VbjhqecEz7OwivUPE5Ls75R169/wY3FZcw03BasLbDPvRSOuvKJVFTngd8QS94KY0AXGnoQrvOZVfaqAefN8o9vCarp1H7VW9cejdFss9xWbs= jenkins@4cc2df0f88dc"

# Configuracion de proxy
#ENV http_proxy=""
#ENV https_proxy=""
#ENV no_proxy="localhost, 127.0.0.1"


# Instala Python y Git
RUN apt-get update && \
    apt-get install -y python3 python3-pip git curl vim

# Opcional: Configura el entorno virtual de Python
# RUN python3 -m venv /venv
# ENV PATH="/venv/bin:$PATH"

# Tu resto de instrucciones para configurar el agente Jenkins...
