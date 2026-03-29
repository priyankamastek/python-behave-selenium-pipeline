AWS Cloud - Upload reports to S3 (Simple Storage Service) Service
To create user in AWS for accessing services
 - AWS Management Console
 - AWS IAM USER (Access Key + Secret Key) 
 - 
 - 

Python Scripts for Automation - Boto3
Python - Python-AWS Library Boto3

Upload the 

To install Allure tool for reports
=========================================
 - Install Java
 - Install NodeJS
 - npm install -g allure-commandline
 - allure --version
 - In python project - pip install allure-behave
 - Run command - behave -f allure_behave.formatter:AllureFormatter -o Reports/features
 - It will run all the feature files and generate Reports folder with json
 - Run command - allure serve Reports/features 

To upload allure reports to AWS S3
==================================================
To push Python Selenium Allure reports to AWS S3, 

First generate the static HTML report files and then upload the entire report directory 
to your S3 bucket using either the AWS CLI or the boto3 Python SDK.

1. AWS Credentials: Configure your AWS credentials (access key and secret key) on your system, 
or use an IAM role if running on an AWS service like EC2.

2. Allure Command-line tool: Install the Allure CLI tool (requires Java) to generate the HTML report 
from test results.

3. Python Boto3 Library: Install the AWS SDK for Python using pip install boto3.

For project with only selenium
After running your Selenium tests with a Python test framework like pytest, 
generate the raw Allure results in a specific directory. 
1. pytest your_tests.py --alluredir allure-results

2. Generate the Allure HTML Report 
2. allure generate Reports/features -o allure-report-html --clean              

3. **Upload the Report to AWS S3 **
4. You can use the AWS CLI's :
5. aws s3 sync command for a simple and effective way to upload an entire directory. 
# Upload the entire directory to your S3 bucket
aws s3 sync allure-report-html/ s3://your-allure-report-bucket-name/your-report-path/

aws s3 sync allure-report-html/ s3://testing-reports-s3-25-mar-26/

Programmatic way:
import boto3
import os

def upload_allure_report_to_s3(local_directory, bucket_name, s3_prefix=''):
    s3_client = boto3.client('s3')
    for root, dirs, files in os.walk(local_directory):
        for file in files:
            local_path = os.path.join(root, file)
            # Create the S3 object name (key) by maintaining the directory structure
            relative_path = os.path.relpath(local_path, local_directory)
            s3_key = os.path.join(s3_prefix, relative_path).replace("\\", "/")

            print(f"Uploading {local_path} to s3://{bucket_name}/{s3_key}")
            try:
                s3_client.upload_file(local_path, bucket_name, s3_key)
            except Exception as e:
                print(f"Error uploading file: {e}")

# Usage example:
upload_allure_report_to_s3('allure-report-html', 'your-allure-report-bucket-name', 'latest-report')

Allure requirement - but rather are static HTML websites 
that can be easily hosted on any web server 

AWS 
 - S3 :
    * General Storage space - Code files, logs , html reports..
    * Host a static Website with a webserver
    *  static
      *  html
      *  css
 * Website created by S3 - user
 *   upload allure-report-html  - user manual
 *   python script using boto3  - Automation

S3 components
==================
 - buckets (Logical Containers)
 - objects (Files)

AWS Infrastructure
  - Regions - Area where AWS physical data centers are provided
  - Regions have AZ (Availability Zones)
  -  EC2, lambda, RDS, VPC
  - Global - common for all regions
    -  IAM, Billing

 Bucket Level permissions
 Object Level permissions

AWS S3 - Bucket, uploaded objects, assign permissions, static Website
AWS IAM - Creating user, applying permissions and generating access + secret key.

AWS EC2 - Setup Jenkins - Run test application

