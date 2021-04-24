if [ ! "$(docker ps -q -f name=flaskapp)" ]; then
    docker-compose -f /vagrant/flaskapp/docker-compose.yml up -d
else 
    docker-compose -f /vagrant/flaskapp/docker-compose.yml down
fi