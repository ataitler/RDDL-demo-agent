import sys
import signal
import time
# sys.path.append('/home/test/pyRDDLGym')

from pyRDDLGym import RDDLEnv
from pyRDDLGym import ExampleManager
from pyRDDLGym.Policies.Agents import NoOpAgent

############################################################
# IMPORT THE AGENT AND OTHER DEPENDENCIES OF YOUR SOLUTION #
from MyAgent.Agent import NoOpAgent as MyRDDLAgent



############################################################


def signal_handler(signum, frame):
    raise Exception("Timed out!")


# MAIN INTERACTION LOOP #
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
    budget = myEnv.Budget

    # default noop agent, do not change
    defaultAgent = NoOpAgent(action_space=myEnv.action_space,
                        num_actions=myEnv.numConcurrentActions)

    ################################################################
    # Initialize your agent here:
    agent = MyRDDLAgent(action_space=myEnv.action_space,
                        num_actions=myEnv.numConcurrentActions)


    ################################################################


    signal.signal(signal.SIGALRM, signal_handler)

    for episode in range(episodes):
        total_reward = 0
        state = myEnv.reset()
        timed_out = False
        elapsed = budget
        finish = start = 0
        for step in range(myEnv.horizon):

            # action selection:
            if not timed_out:
                signal.setitimer(signal.ITIMER_REAL, elapsed)
                try:
                    start = time.time()
                    #################################################################
                    # replace the following line of code with your agent call
                    action = agent.sample_action()



                    #################################################################
                    finish = time.time()
                except:
                    print('Timed out!')
                    print('This episode will continue with default actions!')
                    action = defaultAgent.sample_action()
                    timed_out = True
                    elapsed = 0
                if not timed_out:
                    elapsed = elapsed - (finish-start)
            else:
                action = defaultAgent.sample_action()

            next_state, reward, done, info = myEnv.step(action)
            total_reward += reward

            print()
            print(f'step       = {step}')
            print(f'state      = {state}')
            print(f'action     = {action}')
            print(f'next state = {next_state}')
            print(f'reward     = {reward}')

            state = next_state

            if done:
                break

        print(f'episode {episode+1} ended with reward {total_reward} after {budget-elapsed} seconds')

    myEnv.close()

    ########################################
    # CLEAN UP ANY RESOURCES YOU HAVE USED #


    ########################################


# Command line interface, DO NOT CHANGE
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

