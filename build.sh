set -ex
# SET THE FOLLOWING VARIABLES
# docker hub username
USERNAME=codeforafrica
# image name
IMAGE=hurumap
docker build -t $USERNAME/$IMAGE:latest .
