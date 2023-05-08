# Articulated Object Manipulation

## Environment setup
```
conda create -n mani-skill2 python=3.7;
conda activate mani-skill2;
pip install mani-skill2 stable_baselines3 chardet tensorboard wandb;
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.6 -c pytorch -c nvidia;
```

## Data setup
```
python -m mani_skill2.utils.download_asset all
```

## Relevant environments
[OpenCabinetDoor-v1](https://haosulab.github.io/ManiSkill2/concepts/environments.html#opencabinetdoor-v1): 42 training cabinets, 10 test cabinets
[OpenCabinetDrawer-v1](https://haosulab.github.io/ManiSkill2/concepts/environments.html#opencabinetdrawer-v1): 25 training cabinets, 10 test cabinets
[TurnFaucet-v0](https://haosulab.github.io/ManiSkill2/concepts/environments.html#turnfaucet-v0): 60 training faucets, 18 test faucets