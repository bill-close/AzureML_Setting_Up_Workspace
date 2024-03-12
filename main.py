# Ensure the 'azureml-core' package is installed via pip

import azureml.core
from azureml.core import Workspace
from azureml.core.authentication import InteractiveLoginAuthentication

print(azureml.core.VERSION)

# Create the workspace using the specified parameters

sub = "90884d79-68d2-4ee8-b32f-9aa53a9a3c4f"
forced_interactive_auth = InteractiveLoginAuthentication(tenant_id="dedd61ab-b77d-444d-8289-15e9ab84ca0f", force=True)

ws = Workspace.create(name='azureml_experiments_workspace',
                      subscription_id=sub,
                      resource_group='azureml_experiments_resource',
                      create_resource_group=True,
                      location='australiaeast'
                     )

