FROM debian:stable-slim
LABEL maintainer="ludovic.desfontaines@gmail.com"

RUN set -x \
	&& apt-get update \
	&& apt-get install --no-install-recommends --no-install-suggests -y python \
	&& apt-get autoremove -y --purge \
	&& apt-get clean -y


COPY content/script.py /root/
COPY content/script.sh /root/

# VOLUME /opt
CMD ["/root/script.sh"]
