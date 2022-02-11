The setup-files presented here work with Kubernetes >=1.19 (due to the stable version of `ingress`) can be used to setup a JupyterHub-based spawner, creating on-demand NetworKit-Jupyter instances, containing example networks and tutorials for direct usage. Note that for deployment in your own environment slight changes are necessary, mostly concerning final output URL of the service and permanent storage.

The following files contain variables, which have to be set:

- `config/jupyterhub_config.py`: Optional, ony if this custom JupyterHub config should be used. See below for details
- `deployments/jhub-deployment.yaml`: Optional: Reference different container images here
- `ingress/jhub-ingress{-tls}`: Setup public service URL here. Optional: support SSL-certificates.
- `volumes/jhub-pv.yaml`: Setup volume type. Different cloud-provider support different types of storage.


In addition it is possible to provide a `jupyterhub_config.py`. One example can be find under `configs`, using `nativeauthenticator` and `Kubespawner` + several variables to setup JupyterHub. This config has to copied to the Physical Volume as defined in `volumes/jhub-pv.yaml`. If you want to use the default config from JupyterHub, `jhub-deployment.yaml` has to be edited. 

Given the marked variables are set and files are in place, the following procedure sets up a Jupyter-service as described in paper "Interactive Visualization of Protein RINs using NetworKit in the Cloud" (Note: Some names and variables are changed, since the original implementation involves secrets and private container images):

```
git clone https://github.com/networkit/networkit-cloud
cd networkit-cloud
kubectl create namespace my-test-jhub
kubectl config set-context --current --namespace=my-test-jhub
. accounts/create_podedit_role.sh
kubectl apply -f accounts/jhub-namespace-user.yaml
kubectl apply -f volumes/jhub-pv.yaml
kubectl apply -f volumes/jhub-pvc.yaml

# Optional step: Copy config/jupyterhub_config.py to the pv (process depending on type of pv)
# Example:
# cp configs/jupyterhub_config.py /nfs-destination-folder-with-pv

kubectl apply -f deployments/jhub-deployment
kubectl apply -f services/jhub-services.yaml
```

Service export is heavily depending on the infrastructure (bare-metal, provisioner, AWS, Azure, etc.). For standard Kubernetes it should be enough to expose the service via an ingress object. Note that the definition also consists of a SSL-certificate, which has to be provided externally.

```
kubectl apply -f ingress/jhub-ingress-tls.yaml
```

For testing or development purposes (like `minikube`) it also suffices to create an ingress object without SSL-certificate:

```
kubectl apply -f ingress/jhub-ingress.yaml
```
