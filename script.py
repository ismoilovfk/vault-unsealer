import hvac
import os
import requests.exceptions
import time

def main():
    while True:
        vaults = os.getenv('vaults').split(',')
        vault_k = os.getenv('vault_k').split(';')
        
        for vault_name in vaults:
            for i in range(3):  
                vault_url = f"http://{vault_name}-{i}.{vault_name}-internal:8200"
                
                try:
                    client = hvac.Client(url=vault_url)
                    if client.seal_status['sealed']:
                        print(f"{vault_url} is sealed. Attempting to unseal...")
                        
                        for keys in vault_k:
                            keys = keys.split(',')
                            try:
                                client.sys.submit_unseal_keys(keys=keys)
                                print(f"{vault_url} was successfully unsealed.")
                                break  # Exit loop if unsealing is successful
                            except hvac.exceptions.VaultError as e:
                                print(f"Failed to unseal {vault_url} with keys: {keys}. Error: {e}")
                        else:
                            print(f"All unseal attempts failed for {vault_url}.")
                    else:
                        print(f"{vault_url} is already unsealed.")
                except requests.exceptions.ConnectionError as e:
                    print(f"Failed to connect to {vault_url}: {e}")
                except Exception as e:
                    print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()