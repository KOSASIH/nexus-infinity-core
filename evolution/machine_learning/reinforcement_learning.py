import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.distributions import Normal, Categorical
from .utils import ExperienceReplay, PrioritizedExperienceReplay, EpsilonGreedy

class ReinforcementLearning:
    def __init__(self, config):
        self.config = config
        self.env = self.initialize_env()
        self.agent = self.initialize_agent()
        self.experience_replay = self.initialize_experience_replay()
        self.epsilon_greedy = self.initialize_epsilon_greedy()

    def initialize_env(self):
        # Initialize the environment (e.g. gym, mujoco, etc.)
        env = gym.make(self.config['env_name'])
        return env

    def initialize_agent(self):
        # Initialize the agent (e.g. DQN, Policy Gradient, etc.)
        if self.config['agent_type'] == 'dqn':
            agent = DQNAgent(self.config)
        elif self.config['agent_type'] == 'pg':
            agent = PolicyGradientAgent(self.config)
        return agent

    def initialize_experience_replay(self):
        # Initialize the experience replay buffer
        if self.config['experience_replay_type'] == 'uniform':
            experience_replay = ExperienceReplay(self.config)
        elif self.config['experience_replay_type'] == 'prioritized':
            experience_replay = PrioritizedExperienceReplay(self.config)
        return experience_replay

    def initialize_epsilon_greedy(self):
        # Initialize the epsilon-greedy policy
        epsilon_greedy = EpsilonGreedy(self.config)
        return epsilon_greedy

    def train(self):
        for episode in range(self.config['num_episodes']):
            state = self.env.reset()
            done = False
            rewards = 0
            while not done:
                action = self.agent.select_action(state)
                next_state, reward, done, _ = self.env.step(action)
                rewards += reward
                self.experience_replay.add_experience(state, action, reward, next_state, done)
                state = next_state
            self.agent.update_policy(self.experience_replay.sample_batch())
            print(f'Episode {episode+1}, Reward: {rewards}')

    def test(self):
        state = self.env.reset()
        done = False
        rewards = 0
        while not done:
            action = self.agent.select_action(state, epsilon=0.0)
            next_state, reward, done, _ = self.env.step(action)
            rewards += reward
            state = next_state
        print(f'Test Reward: {rewards}')

class DQNAgent:
    def __init__(self, config):
        self.config = config
        self.q_network = self.initialize_q_network()
        self.target_q_network = self.initialize_target_q_network()
        self.optimizer = self.initialize_optimizer()

    def initialize_q_network(self):
        # Initialize the Q-network (e.g. neural network)
        q_network = nn.Sequential(
            nn.Linear(self.config['state_dim'], 128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, self.config['action_dim'])
        )
        return q_network

    def initialize_target_q_network(self):
        # Initialize the target Q-network (e.g. neural network)
        target_q_network = self.initialize_q_network()
        return target_q_network

    def initialize_optimizer(self):
        # Initialize the optimizer (e.g. Adam, RMSProp, etc.)
        optimizer = optim.Adam(self.q_network.parameters(), lr=self.config['learning_rate'])
        return optimizer

    def select_action(self, state, epsilon):
        # Select an action using epsilon-greedy policy
        if np.random.rand() < epsilon:
            action = np.random.randint(self.config['action_dim'])
        else:
            action = self.q_network(state).argmax()
        return action

    def update_policy(self, batch):
        # Update the Q-network using the batch of experiences
        states, actions, rewards, next_states, dones = batch
        q_values = self.q_network(states)
        target_q_values = self.target_q_network(next_states)
        q_values[range(len(actions)), actions] = rewards + self.config['gamma'] * target_q_values.max(dim=1)[0]
        loss = (q_values - self.q_network(states)) ** 2
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

class PolicyGradientAgent:
    def __init__(self, config):
        self.config = config
        self.policy_network = self.initialize_policy_network()
        self.optimizer = self.initialize_optimizer()

    def initialize_policy_network(self):
        # Initialize the policy network (e.g. neural network)
        policy_network = nn.Sequential(
            nn.Linear(self.config['state_dim'], 128),
            nn.ReLU (),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, self.config['action_dim'])
        )
        return policy_network

    def initialize_optimizer(self):
        # Initialize the optimizer (e.g. Adam, RMSProp, etc.)
        optimizer = optim.Adam(self.policy_network.parameters(), lr=self.config['learning_rate'])
        return optimizer

    def select_action(self, state, epsilon):
        # Select an action using the policy network
        action_probs = self.policy_network(state)
        action = Categorical(action_probs).sample()
        return action

    def update_policy(self, batch):
        # Update the policy network using the batch of experiences
        states, actions, rewards, next_states, dones = batch
        action_probs = self.policy_network(states)
        policy_loss = -torch.sum(action_probs * rewards)
        self.optimizer.zero_grad()
        policy_loss.backward()
        self.optimizer.step()
