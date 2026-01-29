set -e

sudo apt update
sudo apt install python3

sudo apt install python3-venv

python3 -m venv venv

source venv/bin/activate

pip install fastapi uvicorn numpy pandas flask django

pip freeze > requirement.txt

touch .gitignore

mkdir python_projects

touch main.py
