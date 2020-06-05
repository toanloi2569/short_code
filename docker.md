
# Docker
**list containers**  
`docker ps -a`

**remove container**  
`docker rm $ID`

**list images**  
`docker images`

**remove image**  
`docker rmi $ID`

**network**  
`docker network ls`  
`docker network inspect $ID`

**inspect**  
`docker inspect $ID`

# Docker-compose
**build**  
`docker-compose up -d`

**exec**  
- exec bash : `docker-compose exec -it $ID bash`
- run command of specific service : `docker-compose exec -d SERVICE COMAND`  
ex : `docker-compose exec -d cvparser python server.py`
