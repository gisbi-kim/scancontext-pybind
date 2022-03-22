# change the path /home/gskim/Documents/git/scancontext-pybind to your path  
REPOSITORY_PATH='/home/gskim/Documents/git/scancontext-pybind'

# use open3d viewer within docker ps (see http://www.open3d.org/docs/release/docker.html) 
docker run -ti --net=host\
    --device=/dev/dri:/dev/dri \
    -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY \
    -v ${REPOSITORY_PATH}:/root/scancontext-pybind\
    giseopkim/pyicpslam2

