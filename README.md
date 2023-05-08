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
