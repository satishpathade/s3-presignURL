# S3 Pre-Signed URL Generator (AWS Lambda + Boto3)

This project provides an **AWS Lambda function** that generates secure **pre-signed URLs** for Amazon S3.  
These URLs let clients **upload (PUT)** or **download (GET)** files directly to/from S3 **without exposing AWS credentials**.

---

## Why Use Pre-Signed URLs?
- **Secure:** Temporary access to specific files only  
- **Time-limited:** URLs expire automatically (default: 1 hour)  
- **Simple:** No need to expose AWS access keys  
- **Scalable:** Works with API Gateway, mobile apps, or web apps  

---

## Setup
### 1. Create an S3 Bucket
Create an S3 bucket in the AWS Management Console to store your files.

### 2. Deploy Lambda Function
- Create a new Lambda function (Python 3.9+ recommended).
- Copy `presignurl.py` into the Lambda console or deploy it via your preferred deployment method.
- Add an environment variable:
- **BUCKET_NAME** = *your-bucket-name*

### 3. IAM Role Policy
Your Lambda function needs permission to get and put objects in the bucket.  
Here’s an example IAM policy to attach to the Lambda’s execution role:
  [lambda-s3-policy.json](lambda-s3-policy.json)


### Example Request/Response
Input (POST request body to Lambda or API Gateway)
  {
  "file_name": "example.txt",
  "operation": "put_object"
  }
Output :
  {
  "file_name": "example.txt",
  "operation": "put_object",
  "presigned_url": "https://your-bucket-name.s3.amazonaws.com/example.txt?...signature..."
  }
  
