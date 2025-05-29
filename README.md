# CKD-Prediction-using-ML-and-DL

# Project Name

A brief description of your project goes here.

## Environment Setup

This project uses a dedicated Python environment to manage dependencies. The following instructions detail how to create a Conda environment with Python 3.9.18 and install the required packages.

### Step 1: Create a Conda Environment

Open your terminal and run:

```bash
conda create -n env python==3.9.18
```

This command will create a new Conda environment named `env` with Python version 3.9.18.

### Step 2: Activate the Environment

Activate the created environment by running:

```bash
conda activate env
```

### Step 3: Install Required Packages

With your environment activated, install the necessary packages using pip:

```bash
pip install tensorflow==2.15.0
pip install seaborn
pip install social-auth-app-django
pip install pillow==11.2.1
```

> **Note:**  
> - Make sure that your internet connection is active when installing these packages.  
> - The package versions are fixed based on the requirements of this project. If updates or changes are needed, adjust the version numbers accordingly.

## Additional Information

- For any troubleshooting or further instructions regarding package installations, refer to the [official documentation](https://www.tensorflow.org/) of the respective packages.
- To deactivate the Conda environment when you're done working, simply run:

  ```bash
  conda deactivate
  ```

## Contributing

If you wish to contribute to this project, please open an issue or submit a pull request.

## License

Specify your project's license here.
