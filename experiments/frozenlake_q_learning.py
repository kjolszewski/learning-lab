import gymnasium as gym
import time

env = gym.make(
    "FrozenLake-v1",
    desc=None,
    map_name="4x4",
    is_slippery=False,
) 

env.action_space.seed(42)

episodes = 1000
successes = 0
successful_steps = []

for episode in range(episodes):
    state, info = env.reset()
    terminated = False
    truncated = False
    steps = 0

    while not terminated and not truncated:
        action = env.action_space.sample()
        state, reward, terminated, truncated, info = env.step(action)
        steps += 1

    if reward == 1:
        successes += 1
        successful_steps.append(steps)

print(f"Success rate: {successes/episodes:.1%}")

if successful_steps:
    average = sum(successful_steps)/len(successful_steps)
    print(f"Average steps when successful: {average:.2f}")

env.close()

