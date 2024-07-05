# Vault-Unsealer
A simple service for configuring auto-unseal of Vault clusters in Kubernetes clusters. It can operate with both single and multiple clusters.

## HashiCorp offers several options for configuring auto-unseal. You can explore [here](https://developer.hashicorp.com/vault/tutorials/auto-unseal).

If, for any reason, you choose not to utilize HashiCorp's solutions, here is my own approach for configuring auto-unseal in Vault.

## Prerequisites
* Vault Address: Access to the address of your HashiCorp Vault instance.
* Vault Unseal Keys: The unseal keys required to initialize and unseal your Vault instance.
* kubectl Access: Administrative access to your Kubernetes cluster via kubectl.
* Access to Create Resources: Permissions to create necessary resources within your Kubernetes cluster.

Steps to deploy...

1.**Clone the repository:**
```sh
git clone https://github.com/ismoilovfk/vault-unsealer.git
cd vault-unsealer
```

Steps to deploy...

1.**Clone the repository:**
```sh
git clone https://github.com/ismoilovfk/vault-unsealer.git
cd vault-unsealer
```

2.**Update  vault-addresses configmap:**
You shoud list all Vault clusters {fullnameOverride}
```sh
vault-addresses: 'vault,vault-prod,vault-stage'
```

3.**Update  vault-keys secret:**
Keys within one cluster should be separated by commas, with the number ranging from 1 to 5. Keys from cluster A should be separated from those of cluster B by semicolons.
```sh
keys: 'vault1_key1,vault1_key2,vault1_key3;vault2_key1,vault1_key1,vault1_key2,vault1_key3;'
```
4.**Apply manifests:**
```sh
kubectl apply -f manifests
```
