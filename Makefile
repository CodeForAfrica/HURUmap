base:
	docker build --no-cache -t codeforafrica/hurumap-base:0.1.1 contrib/base
	docker build -t codeforafrica/hurumap-base:latest contrib/base
	docker push codeforafrica/hurumap-base:0.1.1
	docker push codeforafrica/hurumap-base:latest

image-latest:
	docker build --no-cache -t codeforafrica/hurumap:latest .
	docker push codeforafrica/hurumap:latest

image-release:
	docker build --no-cache -t codeforafrica/hurumap:1.0.1
	docker push codeforafrica/hurumap:1.0.1
