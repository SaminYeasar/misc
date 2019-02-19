import torch
import os


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
