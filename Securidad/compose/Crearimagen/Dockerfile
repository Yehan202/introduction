FROM ubuntu:latest

RUN apt-get update && apt-get install -y openssh-server && apt-get install -y iputils-ping net-tools netplan.io
RUN apt-get install -y iptables 
RUN useradd yehan
RUN echo 'yehan:yehan' | chpasswd
RUN mkdir /home/yehan
RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]