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