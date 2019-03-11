set -x
# SET THE FOLLOWING VARIABLES
# docker hub username
USERNAME=codeforafrica
# image name
IMAGE=hurumap
docker build --target $IMAGE --no-cache -t $USERNAME/$IMAGE:latest .
