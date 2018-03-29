#!/bin/sh
jupyter_password=`python -c 'import IPython; print(IPython.lib.passwd("zhouminhao007"));'`
echo $jupyter_password

cd
mkdir certs
cd certs
sudo openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.pem -out mycert.pem <<!
CN
china
shanghai
.
.
peter
zhou_00009@126.com
!

cd ~/.jupyter
cert_num=$(grep -n "c.NotebookApp.certfile =" jupyter_notebook_config.py | head -n 1 | cut -d: -f1)
password_num=$(grep -n "c.NotebookApp.password =" jupyter_notebook_config.py | head -n 1 | cut -d: -f1)
ip_num=$(grep -n "c.NotebookApp.ip =" jupyter_notebook_config.py | head -n 1 | cut -d: -f1)
port_num=$(grep -n "c.NotebookApp.port =" jupyter_notebook_config.py | head -n 1 | cut -d: -f1)
browser_num=$(grep -n "c.NotebookApp.open_browser =" jupyter_notebook_config.py | head -n 1 | cut -d: -f1)

sed -i "${cert_num}s@.*@c.NotebookApp.certfile = u\"/home/ubuntu/certs/mycert.pem\"@g" ./jupyter_notebook_config.py
sed -i "${password_num}s@.*@c.NotebookApp.password = \"${jupyter_password}\"@g" ./jupyter_notebook_config.py
sed -i "${ip_num}s@.*@c.NotebookApp.ip = \"*\"@g" ./jupyter_notebook_config.py
sed -i "${port_num}s@.*@c.NotebookApp.port = 8888@g" ./jupyter_notebook_config.py
sed -i "${browser_num}s@.*@c.NotebookApp.open_browser = False@g" ./jupyter_notebook_config.py

cd
mkdir .terminal-config
cd .terminal-config
wget https://raw.githubusercontent.com/Peter-Chou/dotfiles/master/.terminal-config/git-completion.bash
wget https://raw.githubusercontent.com/Peter-Chou/dotfiles/master/.terminal-config/git-prompt.sh
cd
wget https://raw.githubusercontent.com/Peter-Chou/dotfiles/master/.bash_profile
echo "source ~/.bash_profile" >> .bashrc
sed -i '/cygdrive/d' ./.bash_profile
sed -i '/emacsclientw/d' ./.bash_profile 
