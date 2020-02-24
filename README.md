# Py-OCT-Calibration

This project aims to produce an easy to use tool to calibrate any SD or SS-OCT. By calibrate I mean substracting background - k-linearize spectra - evaluate and compensate dispersion.

## Packages depedencies

In order to use the Py-OCT-Calibration Library, one must have installed the following packages:

```
    - Numpy
    - Scipy
    - json
    - matplotlib
    - sphynx (for developer only)
    - git (for developer only)

```

Using pip3 one can use the following commands:

```console
>>> pip3 install Numpy
>>> pip3 install Scipy
>>> pip3 install matplotlib
>>> pip3 install gitpython
>>> apt-get install python-sphinx (for Unix OS)
>>> sudo port install py27-sphinx (for Mac OS)
```

## Project architecture

The folder architecture is presented as :

```
    PyOCTCalibration/
            - data/                         (contain all data)
                - calibration/
                - img/
            - processing/                
                - calibration.py            (compute the k-linear., dispersion, spectrum shift, noise)
                - Aline.py                  (process one Aline)
                - Bscan.py                  (process one Bscan)
                - Cscan.py                  (process one Cscan)
            - toolbox/                      (contain tools to do all the processing)

            - Doc/                          (not yet added)

```


## Run example

In order to run example one can tape the following command on command prompt:

```console

>>> python3 calibration.py --dispersion=normal --input-dir = ../ --output-file=test.json
>>> python process_Bscan --dispersion=normal --input-file=example

```

Arguments are:

..* Bullet --dispersion : [1] for normal dispersion, [-1] for anormal
..* Bullet --input-dir : directory of the input files for calibration
..* Bullet --output-file : directory for the output .json file containing all the calibration parameters



Here is an example of output give by:

```console

>>> python3 process_Bscan.py -f=cible_6 -d=-1

```

![Alt text](results/example.png?raw=true "Title")

## Pep8 coding convention

In order to keep a clean and consistent code, one can follow the convention as presented in the following link:

https://www.python.org/dev/peps/pep-0008/#documentation-strings
