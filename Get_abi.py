import requests
import json

def get_contract_abi(contract_address):
    url = f"https://api.bscscan.com/api?module=contract&action=getabi&address={contract_address}&apikey=13IE1WTV46K16JRZHA3I7X2PEMU68MKXZE"
    response = requests.get(url)
    data = response.json()
    if data['status'] == '1':
        abi = json.loads(data['result'])
        return abi
    else:
        return None

def write_abi_to_file(abi, filename):
    with open(filename, 'w') as f:
        json.dump(abi, f)

# Example usage:
contract_address = '0x10ED43C718714eb63d5aA57B78B54704E256024E'  # PancakeSwap Router V2 address
abi = get_contract_abi(contract_address)
write_abi_to_file(abi, 'Abi.json')
