# Fly_Sim
Simulating fruit-fly drosophilia from first principles

[![nature](https://img.shields.io/badge/publication-8A2BE2)][paper]

<img src="fly-white.png" width="65%">

## 🎯 Overview

This project implements the first full brain-body upload of the fruit-fly, incorporating:
- **🧠 Neural Connectome**: Structural and functional brain modeling
- **🦴 Body Physics**: MuJoCo-based biomechanical simulation  
- **🌍 Environment**: Interactive environmental responses
- **🔬 Data Integration**: Real connectome data and experimental validation

`flybody` is an anatomically-detailed body model of the fruit fly [_Drosophila melanogaster_][drosophila_wikipedia] for [MuJoCo][mujoco] physics simulator and reinforcement learning applications. 


## Getting Started

The fruit fly body model lives in [this directory][fly-home]. To visualize it, you can drag-and-drop `fruitfly.xml` or `floor.xml` to MuJoCo's `simulate` viewer.

Interacting with the fly via Python is as simple as:

```python
import numpy as np
import mediapy

from flybody.fly_envs import walk_imitation

# Create walking imitation environment.
env = walk_imitation()

# Run environment loop with random actions for a bit.
for _ in range(100):
   action = np.random.normal(size=59)  # 59 is the walking action dimension.
   timestep = env.step(action)

# Generate a pretty image.
pixels = env.physics.render(camera_id=1)
mediapy.show_image(pixels)
```

The quickest way to get started with `flybody` is to take a look at a [tutorial notebook][tutorial] or [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)][tutorial-colab].

Also, [this notebook][envs] shows examples of the flight, walking, and vision-guided flight RL task environments designed by Deepmind. 

## Installation

Follow these steps to install `flybody`:

### Option 1: Installation from cloned local repo

1. Clone this repo and create a new conda environment:
   ```bash
   git clone "link to repo"
   cd flybody
   conda create --name fly_sim_env -c conda-forge python=3.10 pip ipython cudatoolkit=11.8.0
   conda activate fly_sim_env
   ```
   `flybody` can be installed in one of the three modes described next. Also, for installation in editable (developer) mode, use the commands as shown. For installation in regular, not editable, mode, drop the `-e` flag.
   
2. **Core installation**: minimal installation for experimenting with the
   fly model in MuJoCo or prototyping task environments. ML dependencies such as [Tensorflow][tf] and [Acme][acme] are not included and policy rollouts and training are not automatically supported.
   ```bash
   pip install -e .
   ```
   
3. **ML extension (optional)**: same as core installation, plus ML dependencies (Tensorflow, Acme) to allow running
   policy networks, e.g. for inference or for training using third-party agents not included in this library.
   ```bash
   pip install -e .[tf]
   ```

4. **Ray training extension (optional)**: same as core installation and ML extension, plus [Ray][ray] to also enable
   distributed policy training in the fly task environments.
   ```bash
   pip install -e .[ray]
   ```

### Option 2: Installation from remote repo
1. Create a new conda environment:
   ```bash
   conda create --name flybody -c conda-forge python=3.10 pip ipython cudatoolkit=11.8.0
   conda activate flybody
   ```
   Proceed with installation in one of the three modes (described above):
2. **Core installation**:
   ```bash
   pip install git+https://github.com/TuragaLab/flybody.git
   ```
3. **ML extension (optional)**:
   ```bash
   pip install "flybody[tf] @ git+https://github.com/TuragaLab/flybody.git"
   ```
5. **Ray training extension (optional)**:
   ```bash
   pip install "flybody[ray] @ git+https://github.com/TuragaLab/flybody.git"
   ```
   
### Additional configuring

1. You may need to set [MuJoCo rendering][mujoco-rendering] environment varibles, e.g.:
   ```bash
   export MUJOCO_GL=egl
   export MUJOCO_EGL_DEVICE_ID=0
   ```
2. Also, for the ML and Ray extensions, `LD_LIBRARY_PATH` may require an update, e.g.:
   ```bash
   CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/:$CUDNN_PATH/lib
   ```

3. You may want to run `pytest` to test the main components of the `flybody` installation.

## Citing `flybody`
See our accompanying [publication][paper]. Thank you for your interest in our fly model:)
```bibtex
@article{flybody,
  title = {Whole-body physics simulation of fruit fly locomotion},
  author = {Roman Vaxenburg and Igor Siwanowicz and Josh Merel and Alice A Robie and
            Carmen Morrow and Guido Novati and Zinovia Stefanidi and Gert-Jan Both and
            Gwyneth M Card and Michael B Reiser and Matthew M Botvinick and
            Kristin M Branson and Yuval Tassa and Srinivas C Turaga},
  journal = {Nature},
  doi = {https://doi.org/10.1038/s41586-025-09029-4},
  url = {https://www.nature.com/articles/s41586-025-09029-4},
  year = {2025},
}
```
