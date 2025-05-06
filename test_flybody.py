import numpy as np
import matplotlib.pyplot as plt
from flybody.fly_envs import template_task

# Set environment variables in the script
import os
os.environ['MUJOCO_GL'] = 'egl'
os.environ['MUJOCO_EGL_DEVICE_ID'] = '0'

# Create a simple environment
env = template_task()
print("Environment created successfully!")

# Run a few steps
for i in range(10):
    action = np.random.normal(size=env.action_spec().shape)
    timestep = env.step(action)
    print(f"Step {i}, reward: {timestep.reward}")

# Save a render to file
pixels = env.physics.render()
plt.imsave('fly_render.png', pixels)
print("Render saved to fly_render.png")