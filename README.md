# Azure Machine Learning Workspace Creation

This Python script creates a new Azure Machine Learning workspace.

## Requirements

- Python 3.6 or later
- AzureML SDK for Python (`azureml-core` package)

## Installation

Ensure that the `azureml-core` package is installed:

pip install azureml-core

Usage
In the main.py file, replace <your-subscription-id> and <your-tenant-id> with your actual Azure subscription and tenant IDs.

Then, run the script:
python main.py

This will create a new Azure Machine Learning workspace named 'azureml_fridge_items' in the 'azureml_fridge_items' resource group (which will be created if it doesn't exist) in the 'australiaeast' region.

