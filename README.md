# Learning Lab
Here I will conduct experiments exploring how artificial agents learn, adapt and improve.

# Goals
- Understand learning algorithms through implementation
- Form and test hypotheses about learning
- Explore reinforcement learning and neural networks
- Document experiments, results and failures

### Baseline: Random Agent
I started with an agent that selects a random action at each step, without learning at all from previous experience.

Experiment:
- Episodes: 1000
- Random seed: 42

Results:
- Success rate: 1.4%
- Average steps per successful episode: 13.21

Observations/Next steps:
- A random agent is very poor for such a task, even on a tiny 4x4 grid.
- I will not investigate how an agent could use its previous experiences to make better decisions.
    - This will primarily involve exploring what information an agent should remember and how it could use rewards to improve its decision making.

