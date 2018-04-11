# Python Serverless API

Boilerplate Flask app that is portable between different serverless platforms.

-----------------------------------------------------------
## Platforms

Deployment and application code adaptors are being added for the following:

<br />

| Platform       				| Deployment				| Status						 |
|--------------------------|-----------------------|:----------------------:|
| AWS Lambda					| AWS SAM 					| 								 |
| AWS Lambda					| Terraform 				| :heavy_check_mark: 	 |
| Azure Functions				| Terraform 				| 					 			 |
| Google Cloud Functions	| Terraform 				| 					 			 |
| Google Kubernetes Engine	| `gcloud` & `kubectl`  | 			 					 |


| Platform       				| Adaptor					| Status						 |
|--------------------------|-----------------------|:----------------------:|
| AWS Lambda Python <= 3.6	| [Flask-Lambda](https://github.com/sivel/flask-lambda) | :heavy_check_mark: 	 |
| AWS Lambda Python >= 3.6	| [Flask-Lambda-Python36](https://github.com/techjacker/flask-lambda) | :heavy_check_mark: 	 |
| Azure Functions				| 				 				| 					 			 |
| Google Cloud Functions	| 				 				| 					 			 |


-----------------------------------------------------------
## Example Usage

#### 1. Set Environment
Ensure you have the necessary environment variables set (see [setup instructions](#setup) above).
```
$ source env/bin/activate
$ source .env
```

#### 2. Run server

##### On host
```
$ make server-debug
```

##### In docker
```
$ docker-compose up
```

#### 3. Manually test development server
```
$ http-prompt localhost:5000
GET /artists
```


-----------------------------------------------------------
## AWS Lambda

### Terraform Deployment
Ensure you have the necessary environment variables set (see [setup instructions](#setup) above).

##### Setup
Create terraform state bucket.
```
$ aws s3 mb --region eu-west-2 s3://<bucket_name>
```

Update bucket name in `/terraform/main.tf`.
```
terraform {
  backend "s3" {
    bucket = "<bucket_name>"
    key    = "terraform.tfstate"
    region = "eu-west-2"
  }
}
```

#### Deploy
Bundle the app into a zip and deploy it using terraform.
```
$ ./bin/deploy
```

#### Manually Test API
```
$ http-prompt $(cd terraform && terraform output api_url)
GET artists
```


-----------------------------------------------------------
## Developer Setup
Set the environment variables required for deployment and local development.

#### 1. Create `.env` file needed for deployment and edit contents.
```
$ cp .env.example .env
$ vim .env
$ source .env
```

#### 2. Create a virtualenv then install requirements:
```
$ make env
$ source env/bin/activate
$ make deps
```

-----------------------------------------------------------
## Test
```
$ make test
$ make lint
```
