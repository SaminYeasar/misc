import torch
import os
import random
from collections import namedtuple

def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def save_weights(policy, discriminator, args, directory='./preTrained'):
    # see if the folder exit if note create one
    create_folder(directory)
    print("Saving weights")
    torch.save(policy.actor.state_dict(), '{}/{}_{}_{}_actor.pth'.format(directory, args.algo, args.policy_name, args.env_name))
    torch.save(policy.critic.state_dict(), '{}/{}_{}_{}_critic.pth'.format(directory, args.algo, args.policy_name, args.env_name))
    torch.save(discriminator.state_dict(), '{}/{}_{}_{}_discriminator.pth'.format(directory, args.algo, args.policy_name, args.env_name))


def load_weights(policy, discriminator, args, directory='./preTrained'):
    if os.path.exists(directory):
        print("Loading PreTrained Weights")
        policy.actor.load_state_dict(torch.load('{}/{}_{}_{}_actor.pth'.format(directory, args.algo, args.policy_name, args.env_name)))
        policy.critic.load_state_dict(torch.load('{}/{}_{}_{}_critic.pth'.format(directory, args.algo, args.policy_name, args.env_name)))
        discriminator.load_state_dict(torch.load('{}/{}_{}_{}_discriminator.pth'.format(directory, args.algo, args.policy_name, args.env_name)))
    else:
        print("PreTrained Weights don't exists. Training Agent from scratch")




# Taken from
# https://github.com/pytorch/tutorials/blob/master/Reinforcement%20(Q-)Learning%20with%20PyTorch.ipynb

Transition = namedtuple('Transition', ('state', 'action', 'mask', 'next_state',
                                       'reward'))


class Memory(object):
    def __init__(self):
        self.memory = []

    def push(self, *args):
        """Saves a transition."""
        self.memory.append(Transition(*args))

    def sample(self):
        return Transition(*zip(*self.memory))

    def __len__(self):
        return len(self.memory)
