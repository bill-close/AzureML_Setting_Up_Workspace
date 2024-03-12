# Ensure the 'azureml-core' package is installed via pip

import azureml.core
from azureml.core import Workspace
from azureml.core.authentication import InteractiveLoginAuthentication

print(azureml.core.VERSION)

# Create the workspace using the specified parameters

SUBSCRIPTION = "<your-subscription-id>"
forced_interactive_auth = InteractiveLoginAuthentication(tenant_id="<your-tenant-id>", force=True)

ws = Workspace.create(name='<name_your_workspace>',
                      subscription_id=SUBSCRIPTION,
                      resource_group='<name_your_resource>',
                      create_resource_group=True,
                      location='australiaeast'
                     )
