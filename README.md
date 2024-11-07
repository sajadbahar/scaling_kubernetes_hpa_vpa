[![Deploy to Kubernetes](https://github.com/sajadbahar/scaling_kubernetes_hpa_vpa/actions/workflows/deploy.yaml/badge.svg)](https://github.com/sajadbahar/scaling_kubernetes_hpa_vpa/actions/workflows/deploy.yaml)
# Kubernetes Scaling with HPA and VPA

This repository demonstrates the setup and configuration of Kubernetes Horizontal Pod Autoscaler (HPA) and Vertical Pod Autoscaler (VPA) to achieve efficient scaling in a microservice environment. It includes manifests and configurations for deploying a sample application on Kubernetes with scaling capabilities.

## Overview

This project provides:
- **Horizontal Pod Autoscaling (HPA)** to scale pods based on CPU usage.
- **Vertical Pod Autoscaling (VPA)** to adjust pod resource requests automatically.
- Examples of CI/CD integration using GitHub Actions and Docker images.

## Project Structure

```plaintext
├── k8s-manifests          # Kubernetes deployment and service manifests
├── examples               # Contain Exanple for VPA, HPA and combined one
├── .github/workflows      # GitHub Actions workflows for CI/CD pipeline
└── README.md              # Project documentation
```

### Key Files
- **k8s-manifests/deployment.yaml** - Configures deployment with autoscaling.
- **k8s-manifests/hpa.yaml** - Sets up Horizontal Pod Autoscaling (HPA).
- **k8s-manifests/vpa.yaml** - Sets up Vertical Pod Autoscaling (VPA).
- **.github/workflows** - CI/CD pipeline to build and push Docker images.

## Features
- Horizontal Pod Autoscaling (HPA): Automatically scales the number of pod replicas based on CPU utilization.
- Vertical Pod Autoscaling (VPA): Dynamically adjusts CPU and memory resource requests and limits for containers.
- Example manifests for deploying and scaling a sample application.

## Requirements

- **Kubernetes Cluster** - Minimum version 1.18.
- **kubectl** - To apply manifests and manage the cluster.
- **Docker** - For building images.
- **GitHub CLI** - Recommended for managing GitHub Actions locally.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/sajadbahar/scaling_kubernetes_hpa_vpa.git
cd scaling_kubernetes_hpa_vpa
```

### 2. Configure Docker Registry and CI/CD

Make sure to update the Docker image reference in `.github/workflows` with your Docker registry credentials.

### 3. Deploy the Application

Use `kubectl` to apply the manifests:

```bash
kubectl apply -f k8s-manifests/
```

### 4. Verify Deployment and Scaling

Check the status of your deployments and autoscaling:

```bash
kubectl get pods
kubectl describe hpa
kubectl describe vpa
```

## Environment Variables

To facilitate flexible configuration, use environment variables for sensitive data and deployment-specific values.

## Metrics Collection

To enable metrics collection for autoscaling, you will need a metrics server in your Kubernetes cluster.
You can deploy Prometheus as a Helm chart for collecting metrics or use any other preferred setup.

## CI/CD Pipeline

The repository is set up with GitHub Actions CI/CD, which automates the process of building and pushing the Docker image.
Make sure to review and configure the `.github/workflows` file to set up your specific repository, image, and credentials.

## Environment Variables

To make image configuration dynamic, specify the Docker image repository as an environment variable:

```yaml
containers:
  - name: worker
    image: ${DOCKER_REPO:-your-default-image}
```
Update the deployment YAML files with environment variables as required by your CI/CD setup.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for discussion.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE.md) file for details.

---

This repository is a demonstration of Kubernetes autoscaling features and is intended for learning purposes.
