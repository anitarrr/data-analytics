# Analysing the Airline Reporting Carrier On-Time Performance Dataset
This code is aimed at analyse the [Airline Reporting Carrier On-Time Performance Dataset](https://developer.ibm.com/data/airline/), as well as getting some trends and insights from the reduced 2 million row sample dataset.

## Installation
To run these Python scripts, you will need to install the required Python modules. It is recommended to create a Python virtual environment before proceeding with the installation.

### Compatibility
These scripts have been tested and verified to work in Python 3.10 and 3.12.

### Creating a Python virtual environment
A Python virtual environment allows you to create an isolated environment for your project, avoiding conflicts with other Python installations and dependencies. To create a virtual environment, follow these steps:

1. Open a terminal/command prompt in the desired directory for your project.
2. Run the following command to create a virtual environment. This will create a new virtual environment named `data_analytics`. You can replace `data_analytics` with your preferred name:

    ```bash
    python3 -m venv data_analytics
    ```

1. Activate the virtual environment. On different operating systems, the activation command varies:
 * Windows:

    ```bash
    # If using cmd.exe
    data_analytics\Scripts\activate.bat

    # If using PowerShell
    data_analytics\Scripts\Activate.ps1
    ```

 * macOS/Linux:
    ```bash
    source data_analytics/bin/activate
    ```

You are now in the virtual environment, and any Python packages you install will be isolated to this environment. When you are done, you can deactivate the virtual environment by running this command in any OS: `deactivate`.

### Installing the required Python modules
To install the required Python modules for running these scripts, follow these steps:

1. Ensure you have activated the virtual environment (if you opted to create one).
2. Run the following command to install the required modules using `pip`. This command will read the `requirements.txt` file and install all the necessary modules automatically.

    ```bash
    pip install -r requirements.txt
    ```

## Usage
Once the code is downloaded and its dependencies are installed, you can run the scripts under the `step_*` folders by running it as usual Python3 scripts. For example:

```bash
python3 step_3_exploring/step_3_1_exploring.py
```

## About the code linting
These Python scripts have been analyzed with [pylint](https://pypi.org/project/pylint/) to ensure that no errors or [code smells](https://martinfowler.com/bliki/CodeSmell.html) are delivered, plus enforcing coding standards.

## Contributing
Contributions to this project are welcome! If you find any issues or have ideas for improvements, you can:
 * Open an issue in the repository.
 * Fork the repository, make your changes, and create a pull request.

## License
This project is licensed under the terms of the [GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/).

The `.gitignore` file is based in the public [GitHub’s collection of .gitignore file templates](https://github.com/github/gitignore).

## Project status
This project is no longer under active development.
