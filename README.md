# Descarga del proyecto
    git clone https://github.com/minsegjujuy/Adop-1.git

# Tecnologias necesarias
NVM (node version manager)
# instalacion
    sudo apt update
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
    nvm install 16.13.1
    nvm use 16.13.1

Python 3.10.12
# instalacion
    sudo apt install software-properties-common -y
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt install python3.10 -y

# instalacion de python3.10-pip
    sudo apt install python3-pip -y
# instalacion de python3.10-venv
    sudo apt install python3.10-venv -y

# Alta de frontend
    cd frontend
    npm i
    npm start

# Alta de backend
    cd backend
  # creacion de entorno virtual
    python3.10 -m venv envs
  # activacion del entorno virtual
    source envs/bin/activate
  # instalacion de dependencias de python
    pip install -r requirements.txt
  # migracion de las tablas a la base de datos
    python manager.py makemigrations
    python manager.py migrate
  # levantar el servidor
    python manager.py runserver
