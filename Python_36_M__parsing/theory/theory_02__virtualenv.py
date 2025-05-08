"""
установка виртуального окружения
pip install virtualenv

=== устанавливаем версию python 3.12 (если её ещё нет)
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.12
sudo apt install libpython3.12-dev
sudo apt install python3.12-venv
sudo apt-get install python3.12-distutils

virtualenv venv -p python3.12
source venv/bin/activate

##### в моей ситуации необходима установка pip прямо с сервера
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.12

"""


