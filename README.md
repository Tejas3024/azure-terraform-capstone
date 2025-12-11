# 🚀 Azure Terraform Capstone Project  
## Python Web App Deployment on Azure App Service using Terraform + Deployment Slots  

This project demonstrates full **Infrastructure as Code (IaC)** using **Terraform** to deploy a **Python Flask Application** on **Azure App Service**, with **Staging & Production Deployment Slots** for zero-downtime deployments.

---

## 🏗 Architecture Overview

```
Local Machine
   ├── Python Flask App
   ├── Terraform Scripts
        │
        ▼ (terraform apply)
Azure Cloud
   ├── Resource Group
   ├── App Service Plan (S1)
   ├── Linux Web App (Production)
   ├── Deployment Slot (Staging)
        │
        ▼ (Azure CLI deploy / Slot Swap)
Production Deployment
   ├── Initial deploy via ZIP
   ├── Updates → Staging
   └── Slot Swap → Zero Downtime Release
```

---

## 🎯 Project Objectives

- Provision Azure infrastructure using **Terraform**  
- Deploy a **Python Flask Web App**  
- Create **Staging** + **Production** deployment slots  
- Deploy using **Azure CLI ZIP Deployment**  
- Perform **Blue-Green / Slot Swap deployments**  

---

## 🧰 Technologies Used

| Category | Tools |
|---------|-------|
| Cloud | Azure |
| IaC | Terraform |
| Backend | Python (Flask) |
| Deployment | Azure CLI |
| Hosting | Azure App Service (Linux) |
| Strategy | Blue-Green / Slot Swap |

---

## 📁 Repository Structure

```
azure-terraform-capstone/
│
├── app.py
├── app.zip
│
├── terraform/
│   └── main.tf
│
├── docs/
│   ├── Terraform_Azure_Project_Presentation_Updated.pptx
│   ├── Terraform_Azure_Project_Full_Documentation.docx
│   └── Terraform_Azure_Project_Documentation.pdf
│
└── README.md
```

---

## 🐍 Python Web App (Flask)

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Terraform Azure Web App</h1>
    <p>This application is deployed on Azure App Service using Terraform.</p>
    """
```

---

## 📦 Terraform Configuration (main.tf)

```hcl
provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "rg-terraform-python-webapp"
  location = "Central India"
}

resource "azurerm_service_plan" "appplan" {
  name                = "asp-terraform-python"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  os_type             = "Linux"
  sku_name            = "S1"
}

resource "azurerm_linux_web_app" "webapp" {
  name                = "webapp-terraform-python-tejas-123"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  service_plan_id     = azurerm_service_plan.appplan.id

  site_config {
    application_stack {
      python_version = "3.10"
    }
  }
}

resource "azurerm_linux_web_app_slot" "staging" {
  name           = "staging"
  app_service_id = azurerm_linux_web_app.webapp.id

  site_config {
    application_stack {
      python_version = "3.10"
    }
  }
}
```

---

## 🛠 Terraform Commands

| Command | Purpose |
|--------|---------|
| `terraform init` | Initialize Terraform provider |
| `terraform plan` | See what Terraform will create |
| `terraform apply` | Create Azure resources |
| `terraform destroy` | Delete all resources |

---

## 🚀 Deploying Python App (ZIP Deploy)

### 1️⃣ Create ZIP file  
```powershell
Compress-Archive -Path app.py -DestinationPath app.zip -Force
```

### 2️⃣ Deploy to Web App  
```bash
az webapp deploy \
 --resource-group rg-terraform-python-webapp \
 --name webapp-terraform-python-tejas-123 \
 --src-path app.zip \
 --type zip
```

---

## 🔀 Blue-Green Deployment (Zero-Downtime)

1. Deploy new version → **Staging Slot**  
2. Test in staging  
3. Swap Staging ↔ Production  
4. Traffic shifts instantly → **Zero downtime**  

---

## 🌍 Live URLs

### 🔵 Production  
https://webapp-terraform-python-tejas-123.azurewebsites.net

### 🟡 Staging  
https://webapp-terraform-python-tejas-123-staging.azurewebsites.net

---

## ✅ Final Results

✔ Infrastructure automated using Terraform  
✔ Python Flask app deployed  
✔ Staging + Production slots  
✔ Blue-Green deployment successful  
✔ Ready for real-world DevOps workflows  

---

## 👤 Author  
**Tejas Devendra Sonawane**  
Cloud • Terraform • Azure • DevOps  








