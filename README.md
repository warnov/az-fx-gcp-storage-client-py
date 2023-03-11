# az-fx-gcp-storage-client-py
An Azure Function that acts as a client of the GCP Storage API written in Python. Useful when you want to access objects in the GCP Storage from Azure.

##### Note for beginners
*If you are new to the develop of Python based Azure Functions it  is useful to follow the [Getting Started Guide](getting_started.md) first. It is also important to understand the concept of [virtual environments](https://code.visualstudio.com/docs/python/environments) for Python Azure Functions in Visual Studio Code so you can configure correctly the packages needed to run your code correctly. Also, if  you are totally new to the Storage API, then I recommend  you to read [this excellent article](https://medium.com/google-cloud/automating-google-cloud-storage-management-with-python-92ba64ec8ea8) to get onboard fast.*

## Packages
You can find in the [requirements](requirements.txt) file the packages required to use this code. If are finding bugs in your development process please be sure that this packages are downloaded to your environment.

## Authentication
For those new to GCP Cloud, the APIs exposed by them can be generally authenticated using a credentials json file that you download from their web console and then make accessible to your code.This is done through the creation of a [service account](https://cloud.google.com/iam/docs/keys-create-delete) in GCP and then the generation of an API Key from there.