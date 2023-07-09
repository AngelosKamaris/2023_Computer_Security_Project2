FROM    ubuntu:latest

# install packages
RUN apt update
RUN apt install -y python3 python3-pip

#add local directory to container
ADD . /root/




# copy script inside container
COPY docker-run.sh /root/
COPY ex.py /root/
#copy attack1 to container

# install dependencies

WORKDIR /root

#pin install requirements
RUN pip3 install -r requirements.txt

# run when container starts
CMD ["bash", "/root/docker-run.sh"]
