# 🚀 End-to-End DevOps Automation Engine

[![DevOps Automated Pipeline](https://github.com/deeputhinks/devops/actions/workflows/ci.yml/badge.svg)](https://github.com/deeputhinks/devops/actions/workflows/ci.yml)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-844FBA?style=flat&logo=terraform&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat&logo=gnu-bash&logoColor=white)

A production-grade, hands-on demonstration of the complete modern DevOps lifecycle: from raw Linux scripting and Docker containerization, to automated CI/CD testing gates, declarative Infrastructure as Code (Terraform), and a self-healing Kubernetes cluster.

---

## 🏛️ System Architecture

```text
 ┌────────────────┐       ┌─────────────────┐       ┌──────────────────┐
 │   Developer    │       │ GitHub Actions  │       │ Container Build  │
 │  (git push)    │ ────> │  (Unit Tests)   │ ────> │  (Docker Image)  │
 └────────────────┘       └─────────────────┘       └──────────────────┘
                                                              │
                                                              ▼
 ┌────────────────┐       ┌─────────────────┐       ┌──────────────────┐
 │ Health Monitor │ <──── │   Kubernetes    │ <──── │ Terraform (IaC)  │
 │  (monitor.sh)  │       │  (5x Replicas)  │       │   (main.tf)      │
 └────────────────┘       └─────────────────┘       └──────────────────┘