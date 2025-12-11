terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

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

  os_type  = "Linux"
  sku_name = "S1"
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
