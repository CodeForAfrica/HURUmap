set -ex
# SET THE FOLLOWING VARIABLES
# docker hub username
USERNAME=codeforafrica
# image name
IMAGE=hurumap
docker build --target hurumap -t $USERNAME/$IMAGE:latest .
docker build -t $USERNAME/$IMAGE-dashboard:latest .
