# RDDL-demo-agent
RDDL docker demo agent for the 2023 IPPC


## Getting started
1. get this demo agent template:
`git clone https://github.com/ataitler/RDDL-demo-agent.git`
2. Install all pyRDDLGym requirements:
`pip install -r requirements.txt`
3. Go to '/usr/share/' and run `git clone https://github.com/ataitler/pyRDDLGym.git`
4. Build docker:
`docker build -t RDDL-demo-agent-image .`
Replace the *RDDL-demo-agent-image* with a name of your choosing.
5. Run docker container with the pyRDDLGym external volume: `docker run -v /usr/share/pyRDDLGym:/usr/share/pyRDDLGym RDDL-demo-agent-image`