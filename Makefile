base:
	docker build -t codeforafrica/hurumap-base:0.1.0 contrib/base
	docker build -t codeforafrica/hurumap-base:latest contrib/base
	docker push codeforafrica/hurumap-base:0.1.0
	docker push codeforafrica/hurumap-base:latest

image-latest:
	docker build -t codeforafrica/hurumap:latest .
	docker push codeforafrica/hurumap:latest

image-release:
	docker build -t codeforafrica/hurumap:1.0.0
	docker push codeforafrica/hurumap:1.0.0
