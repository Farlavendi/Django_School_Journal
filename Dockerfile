FROM ubuntu:latest
LABEL authors="Denis"

ENTRYPOINT ["top", "-b"]