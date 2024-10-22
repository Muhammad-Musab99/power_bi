# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'ServicePrincipal'

    # Workspace Id in which the report is present
    WORKSPACE_ID = '712225c1-bb23-471d-aa6a-ec3db8522db7'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = '6e609677-0a66-4e89-9f93-693c1fb144e4'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = '7f7d0b1e-6a07-46f6-ad1c-b8ade86e497c'
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = '3c55f5c4-6ff9-4fbc-a005-e288ed498fce'
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = 'Psy8Q~yXmnt1Ekk-2yiazwHHu4YygBqYigN-qalV'
    
    # Scope Base of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE_BASE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY_URL = 'https://login.microsoftonline.com/organizations'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = ''
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = ''