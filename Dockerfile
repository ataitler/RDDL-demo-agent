FROM python:3.10

WORKDIR /usr/src/RDDL-demo-agent

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# entry point for the docker, this will always run with the docker
# must be FULL PATH for singularity compatibility
ENTRYPOINT ["python", "/usr/src/RDDL-demo-agent/main.py"]

# run the command, this serves as default args to the entrypoint
CMD []



