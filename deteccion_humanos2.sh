export DARKNET_HOME=/home/cicy2024/darknet4/
export CUDA_HOME=/usr/local/
export PATH=${DARKNET_HOME}:${CUDA_HOME}bin:${PATH}


cd /home/cicy2024/darknet4/
./darknet detector demo cfg/people.data peoplerpeople/people-r-people.cfg peoplerpeople/people-r-people.weights -c 0
