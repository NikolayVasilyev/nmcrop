#
#	Micropsi work test
#

NAME=micropsi
MOUNT=/home/nikolay/mount_hall/docker_share
TARGET=micropsi

ifndef TUSER
	TUSER=root
endif

.PHONY: build
build:
	docker build -t $(TARGET) .

.PHONY: start
start:
	docker run \
		-ti \
		-u $(TUSER) \
		--name $(NAME) \
		$(ARGS) \
		$(TARGET)

.PHONY: run
run:
	docker exec \
		-ti \
		-u $(TUSER) \
		$(TARGET) \
		"/run" \
		$(ARGS) \
		$(TARGET)


.PHONY: attach
attach:
	docker start $(NAME)
	docker attach $(NAME)

.PHONY: spawn
spawn:
	docker exec -it -u $(TUSER) $(NAME) bash

.PHONY: stop
stop:
	-docker stop $(TARGET)
	-docker rm $(TARGET)
