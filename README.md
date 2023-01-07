# azurerm-data-lake

- this repository has jump start codes to access storage accounts using python, which is a fundamental for learning data lake

- azure storage account has below 4 storages
  
    - blob storage
    - file storage
    - queue storage
    - table storage
  

#### this repo has dedicated folders for each concept and they are self explanatory

- inorder to access table storage we can use below authentication methods

  - Shared Key
  - Connection String
  - Shared Access Signature Token
- In this scenario i will using "connection string"
- inorder to get the connection string of your table storage from the storage account execute the below command from the terminal

`
az storage account keys list -g MyResourceGroup -n MyStorageAccount
`
