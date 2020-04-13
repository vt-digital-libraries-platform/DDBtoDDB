# DDBtoDDB

This project contains source code and supporting files for a serverless application - DDBtoDDB - that you can deploy with the SAM CLI. It includes the following files and folders.

- lambda_function.py - Code for the DDBtoDDB's Lambda function.
- template.yaml - A template that defines the DDBtoDDB's AWS resources.

## Deploy the DDBtoDDB application using SAM CLI

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

To build the application for the first time, run the following in your shell:
```bash
sam build --use-container
```
Above command will build the source of the application. The SAM CLI installs dependencies defined in `requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

To package the application, run the following in your shell:
```bash
sam package --output-template-file packaged.yaml --s3-bucket BUCKETNAME
```
Above command will package the application and upload it to the S3 bucket you specified.

Run the following in your shell to deploy the application to AWS:
```bash
sam deploy --template-file packaged.yaml --stack-name STACKNAME --s3-bucket BUCKETNAME --parameter-overrides 'SourceTable=value TargetTable=value Region=us-east-1' --capabilities CAPABILITY_IAM --region us-east-1
```

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.

## Run the DDBtoDDB lamdba function through bash
```bash
aws lambda invoke --function-name LambdaFunctioName out --log-type Tail --query 'LogResult' --output text |  base64 -d
```

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name DDBtoDDB
```

