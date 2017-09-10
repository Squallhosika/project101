echo "Start setup"
rm -Rf env
virtualenv env --python=python3

#*** Running the following command might be necessary
#*** when mysql is not installed.
#sudo apt-get install mysql-server libmysqlclient-dev
env/bin/pip install -r requirement.txt

echo "Setup done."
