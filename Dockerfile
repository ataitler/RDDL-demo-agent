FROM python:3.10

WORKDIR /usr/src/RDDLagent

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# define the port number the container should expose
EXPOSE 5000

# run the command
CMD ["python", "./main2.py"]

# docker run -i -t -v $(pwd):/usr/share/nginx/html:ro rddl-random-agent /bin/bash
# docker run -i -t -v /home/test/Documents/pyRDDLGym-main:/usr/share/pyRDDLGym -e PATH="$PATH:/usr/share/pyRDDLGym" rddl-random-agent /bin/bash
# docker run -i -t -v /home/test/Documents/pyRDDLGym-logging4comp:/usr/share/pyRDDLGym -e PATH="$PATH:/usr/share/pyRDDLGym" rddl-random-agent-volume /bin/bash

# docker build -t rddl-random-agent-volume .

