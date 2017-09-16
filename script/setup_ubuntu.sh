# install 
sudo apt-get update
sudo apt-get upgrade
sudo add-apt-repository ppa:notepadqq-team/notepadqq
sudo apt-get update
sudo apt-get install notepadqq
sudo apt-get install git

# get the git repository need an authentification
git clone https://github.com/Squallhosika/unicorn.git

sudo apt install python-pi

# Install Kafka
sudo add-apt-repository -y ppa:webupd8team/java
sudo apt-get  update 
sudo apt-get install oracle-java8-installer -y
# in your download folder run the following
wget http://www-eu.apache.org/dist/kafka/0.11.0.0/kafka_2.11-0.11.0.0.tgz
sudo mkdir /opt/kafka/
sudo tar -xvf ~/Documents/kafka_2.11-0.11.0.0.tgz -C /opt/kafka/
sudo nohup /opt/kafka/kafka_2.11-0.11.0.0/bin/kafka-server-start.sh /opt/kafka/kafka_2.11-0.11.0.0/config/server.properties /tmp/kafka.log 2>&1 &
#testing
sudo /opt/kafka/kafka_2.11-0.11.0.0/bin/kafka-server-start.sh /opt/kafka/kafka_2.11-0.11.0.0/config/server.properties
sudo /opt/kafka/kafka_2.11-0.11.0.0/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1  --partitions 1 --topic testing
# Producer
sudo ./kafka-console-producer.sh --broker-list localhost:9092 --topic testing
#consumer
sudo ./kafka-console-consumer.sh --zookeeper localhost:2181 --topic testing --from-beginning


#install postgress
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | sudo apt-key add -
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
# connect to postgress and change password
sudo su - postgres
psql
\password 
# then choose "postgres" as password


#ssh in github
ssh-keygen -t rsa -b 4096 -C "jonathan.lerch@gmail.com"
# just press enter to the following questions
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
sudo apt-get install xclip

https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/
https://stackoverflow.com/questions/1595848/configuring-git-over-ssh-to-login-once
# Important to make ssh work !!!
git config remote.origin.url git@github.com:Squallhosika/unicorn.git


