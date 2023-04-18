# RDDL-demo-agent
RDDL docker demo agent for the 2023 IPPC


## Getting started

### Prerequisites
1. Get the pyRDDLGym project by *cloning* it or *downloading* the zip of it.
2. Add the <pyRDDLGym folder> path to the PYTHONPATH environment variable.

*DO NOT INSTALL pyRDDLGym VIA PIP, you need to make sure the import is working as in the competition.

### Github
Getting the demo agent:
1. get this demo agent template:
`git clone https://github.com/ataitler/RDDL-demo-agent.git`
2. Install all pyRDDLGym requirements:
`pip install -r requirements.txt`

Do not change the entry point of the agent. main.py must be the entry point of the docker.
Only modify the part of the code as described by the comments in main.py

### Docker
You can pull the docker from Docker-hub and inspect or update it as you like.
-`docker pull ataitler/rddl-demo-agent`

### Build docker
In order to generate a docker from your solution run the following command: 
- `docker build -t <docker_name> .`

Replace the *<docker_name>>* with a name of your choosing.

IMPORTANT! make sure that: 
1. pyRDDLGym in not included in the requirements.txt file.
2. All of pyRDDLGym's dependencies are there (should be unless manually removed).
3. The pyRDDLGym folder does not resides under this project and will not be packaged wit the docker during build. 

5. Run docker container with the pyRDDLGym external volume: `docker run -v /usr/share/pyRDDLGym:/usr/share/pyRDDLGym rddl-demo-agent-image`

## Running the docker
All dockers will be executed with an external binded volume which will include the pyRDDLGym server. \
It is important to make sure that pyRDDLGym is not installed and packaged with the container, to make sure your agent interacts with the correct server.

The docker execution command will be of the form:

```bash
docker run -v <external_pyRDDLGym_folder>:<internal_pyRDDLGym_folder> 
           -e PYTHONPATH="$PYTHONPATH:<internal_pyRDDLGym_folder> 
           <docker_name> 
           <domain>
           <instance>
           <method_name>
           <#iterations>
```

- <external_pyRDDLGym_folder> is the host pyRDDLGym folder that will be externally connected to the docker.
- <internal_pyRDDLGym_folder> is the docker local pyRDDLGym folder mapping.
- the -e flag updates the docker PYTHONPATH environment variable so the import inside the docker will use the correct library.
- <docker_name> is the name of the docker as you named it.
- <domain> is the domain to test on.
- <instance> is the instance number to use.
- <method_name> is your method name, as will be logged in the results logs.
- <#iterations> is the number of episodes to test.




