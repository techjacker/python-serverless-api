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


| Platform       				| Adaptor					| Code/Config				 |
|--------------------------|-----------------------|:----------------------:|
| Local Development			| None				 		| [:floppy_disk:](run.py)	 	 																|
| AWS Lambda Python >= 3.6	| [Flask-Lambda-Python36](https://github.com/techjacker/flask-lambda) | [:floppy_disk:](run_lambda.py)|
| AWS Lambda Python <= 3.6	| [Flask-Lambda](https://github.com/sivel/flask-lambda) | [:floppy_disk:](run_lambda.py) 	 				|
| Azure Functions				| 				 				| 					 			 |
| Google Cloud Functions	| 				 				| 					 			 |

-----------------------------------------------------------
## Setup


#### 1. Create `.env` file and update contents
This is used to set the environment variables required for deployment and local development.
```
$ cp .env.example .env
$ vim .env
```

#### 2. Create a virtualenv then install requirements:
```
$ make env
$ source env/bin/activate
$ make deps
```

-----------------------------------------------------------
## Example Usage

#### 1. Set Environment
Ensure you have created your virtualenv and have the necessary environment variables set (see [setup instructions](#setup) above).
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
Ensure you have created your virtualenv and have the necessary environment variables set (see [setup instructions](#setup) above).

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
## Test
```
$ make test
$ make lint
```
