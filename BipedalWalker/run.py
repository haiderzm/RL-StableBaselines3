import gym
from stable_baselines3 import PPO

models_dir = "models/PPO"

env = gym.make('BipedalWalker-v3') 
env.reset()

model_path = f"{models_dir}/290000.zip"
model = PPO.load(model_path, env=env)

episodes = 5

for ep in range(episodes):
    obs = env.reset()
    done = False
    total_rewards = 0
    while not done:
        action, _states = model.predict(obs)
        obs, rewards, done, info = env.step(action)
        total_rewards += rewards
        env.render()
    print(total_rewards)