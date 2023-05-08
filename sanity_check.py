import gym
import mani_skill2.envs
import matplotlib.pyplot as plt
from pathlib import Path


def save_camera_view(obs_camera, title, save_path):
    Path(save_path).mkdir(parents=True, exist_ok=True)
    plt.figure()
    rgb, depth = obs_camera['rgb'], obs_camera['depth']
    plt.subplot(1, 2, 1)
    plt.title(f"{title} - RGB")
    plt.imsave(f"{save_path}/rgb.png", rgb)
    plt.subplot(1, 2, 2)
    plt.title(f"{title} - Depth")
    plt.imsave(f"{save_path}/depth.png", depth[:, :, 0], cmap="gray")


env = gym.make(
    "OpenCabinetDrawer-v1",
    obs_mode="rgbd",
    control_mode="base_pd_joint_vel_arm_pd_joint_delta_pos"
)
print("Observation space", env.observation_space)
print("Action space", env.action_space)

env.seed(0)
obs = env.reset()
print(obs["image"].keys())
for camera in obs["image"].keys():
    save_camera_view(obs['image'][camera], f"{camera} view", f"vis/{camera}")

done = False
while not done:
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)
env.close()
