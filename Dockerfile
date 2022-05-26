# Dockerfile, Image, Container

FROM datamachines/cudnn_tensorflow_opencv:11.3.1_2.7.0_4.5.5-20220103

RUN pip install requests Flask

RUN mkdir -p /app/templates
WORKDIR /app

ADD app.py .
ADD templates /app/templates

#Install the dependencies
RUN pip install -r /app/templates/requirements.txt
RUN usermod -aG cooper video


#Expose the required port
EXPOSE 3000

CMD [ "python", "/app/app.py"]

