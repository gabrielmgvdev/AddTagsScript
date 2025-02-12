import requests
import base64

organization = "sua-organizacao"  
project = "seu-projeto"  
tag_to_add = "sua-tag"  
work_items_ids = [152245, 139951, 139948, 137735, 145922, 146245, 145921, 151279, 137740, 137737, 151282, 151285, 151340]  

pat = "SEU_PERSONAL_ACCESS_TOKEN_AQUI"

auth = base64.b64encode(f":{pat}".encode()).decode()

encoded_project = requests.utils.quote(project)

headers = {
    "Content-Type": "application/json-patch+json",
    "Authorization": f"Basic {auth}"
}

for work_item_id in work_items_ids:
    url = f"https://dev.azure.com/{organization}/{encoded_project}/_apis/wit/workitems/{work_item_id}?api-version=7.1-preview.3"

    body = [
        {
            "op": "add",
            "path": "/fields/System.Tags",
            "value": tag_to_add
        }
    ]

    try:
        response = requests.patch(url, json=body, headers=headers)
        
        if response.status_code == 200:
            print(f" Tag '{tag_to_add}' adicionada ao Work Item ID: {work_item_id}")
        else:
            print(f" Erro ao atualizar Work Item ID {work_item_id}: {response.status_code} - {response.text}")

    except Exception as e:
        print(f" Erro inesperado no Work Item ID {work_item_id}: {str(e)}")