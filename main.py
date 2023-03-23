import sys

from pyRDDLGym import RDDLEnv
from pyRDDLGym import ExampleManager

############################################################
# IMPORT THE AGENT AND OTHER DEPENDENCIES OF YOUR SOLUTION #
############################################################
from pyRDDLGym.Policies.Agents import NoOpAgent


#########################
# MAIN INTERACTION LOOP #
#########################
def main(env, inst, method_name=None, episodes=1):
    print(f'preparing to launch instance {inst} of domain {env}...')

    # get the environment info
    EnvInfo = ExampleManager.GetEnvInfo(env)

    # set up the environment class, choose instance 0 because every example has at least one example instance
    log = False if method_name is None else True
    myEnv = RDDLEnv.RDDLEnv(domain=EnvInfo.get_domain(),
                            instance=EnvInfo.get_instance(inst),
                            enforce_action_constraints=False,
                            debug=False,
                            log=log,
                            simlogname=method_name)

    # set up the agent object:
    agent = NoOpAgent(action_space=myEnv.action_space,
                        num_actions=myEnv.numConcurrentActions)

    for episode in range(episodes):
        total_reward = 0
        state = myEnv.reset()
        for step in range(myEnv.horizon):

            ##################################################
            # change following line for your sampling method #
            ##################################################
            action = agent.sample_action()

            next_state, reward, done, info = myEnv.step(action)
            total_reward += reward

            # prints can be removed for final submission
            print()
            print(f'step       = {step}')
            print(f'state      = {state}')
            print(f'action     = {action}')
            print(f'next state = {next_state}')
            print(f'reward     = {reward}')
            state = next_state
            if done:
                break
        print(f'episode {episode+1} ended with reward {total_reward}')

    myEnv.close()
    # CLEAN UP ANY RESOURCES YOU HAVE USED



##########################################
# DO NOT CHANGE THIS PART OF THE CODE!!! #
##########################################
if __name__ == "__main__":
    args = sys.argv
    print(args)
    method_name = None
    episodes = 1
    if len(args) == 2:
        if args[0] == '-h':
            print('python GymExample.py <domain> <instance> <method name> <num episodes>')
    if len(args) < 3:
        env, inst = 'HVAC', '1'
    elif len(args) < 4:
        env, inst = args[1:3]
    elif len(args) < 5:
        env, inst, method_name = args[1:4]
    else:
        env, inst, method_name, episodes = args[1:5]
        try:
            episodes = int(episodes)
        except:
            raise ValueError("episode must be an integer value argument, received: " + episodes)
    main(env, inst, method_name, episodes)

