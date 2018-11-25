set -ex
# SET THE FOLLOWING VARIABLES
# docker hub username
USERNAME=codeforafrica
# image name
IMAGE=hurumap
docker build --target hurumap --no-cache -t $USERNAME/$IMAGE:latest .
docker build --no-cache -t $USERNAME/$IMAGE-dashboard:latest .
