from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Terraform Azure Web App</title>
        </head>
        <body>
            <h1>Terraform Azure Web App Project</h1>

            <h2>Terraform Commands Used</h2>
            <ul>
                <li>terraform init</li>
                <li>terraform validate</li>
                <li>terraform plan</li>
                <li>terraform apply</li>
                <li>terraform destroy</li>
            </ul>

            <h2>Azure Resources Created Using Terraform</h2>
            <ul>
                <li>Resource Group</li>
                <li>App Service Plan</li>
                <li>Azure Web App (Python)</li>
                <li>Deployment Slots (Staging & Production)</li>
            </ul>

            <h2>Deployment Slot Concept</h2>
            <p>
                This application is deployed using Azure Deployment Slots.
                First it is deployed to the Staging slot and then swapped to Production
                for zero-downtime deployment.
            </p>

            <p>
                This Web Application is deployed on Azure using Terraform as
                Infrastructure as Code.
            </p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
