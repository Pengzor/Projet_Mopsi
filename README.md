# Puzzle Solving interface

The aim of this app is to solve polyominos pavement problem of size NxN, for N = 3,4,5,6,7 ; with and additional constraint of a fixed "bloc" of size 1x1. The solvers were developped for the MoPSi project and the API for the TDLog project from the respective ENPC courses. 

## Getting Started

These instructions should give you the basics to run the program on your computer.
Please refer to the documentation of the specified librairies for their installation.

### Prerequisites

The following libraries for Python are required:

```
PyQt4
sys
os
numpy
csv
random
```

### Installing

Start with cloning the repository in your folder of choice.

```
git init .
git pull https://github.com/TheoViel/Projet_Mopsi/
```

The libraries for the C++ executable are too heavy to be put on git, download them from the following link :

https://drive.google.com/drive/folders/1FNzrqiQZBRaiTfYuA8jjnXURU6c4HuuP?usp=sharing

and copy them in the folder ```codes```

### Launching

Open ```main.py``` and run it. TADAM ! You can now use the interface

## Authors

* **Théo VIEL** - [GitHub](https://github.com/TheoViel)
* **Matthieu ROUX** - [GitHub](https://github.com/Saint-Venant)


## Acknowledgments

* Thanks to P-A Zitt for the explanation of the maths used here
* Thanks to T. Martinez and P. Monasse for their precious help to include the C++ code in Python
* Hat tip to G. Desforges for helping us with the basics of a MVC interface
