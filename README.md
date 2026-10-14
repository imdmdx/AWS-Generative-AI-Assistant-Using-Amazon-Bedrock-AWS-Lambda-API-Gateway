# AWS Generative AI Assistant Using Amazon Bedrock, AWS Lambda & API Gateway

## 📌 Project Overview

The **AWS Generative AI Assistant** is a serverless web application that allows users to ask questions and receive AI-generated responses using Amazon Bedrock and the Amazon Nova Micro foundation model.

The project uses Amazon S3 to host the frontend, Amazon API Gateway to handle HTTP requests, AWS Lambda to process user questions, Amazon Bedrock to generate AI responses, and Amazon DynamoDB to store chat history.

This project demonstrates how to build and deploy a Generative AI application using AWS serverless services.

## 🏗️ Architecture

```text
              User
               |
               v
      Amazon S3 Static Website
         (HTML, CSS, JavaScript)
               |
               v
        Amazon API Gateway
            POST /ask
               |
               v
           AWS Lambda
     (Python Backend Logic)
          /          \
         v            v
 Amazon Bedrock    Amazon DynamoDB
   Nova Micro       Chat History
         |
         v
   AI-Generated Answer
         |
         v
   Response to Frontend
```

**Monitoring and Security:**
- Amazon CloudWatch for logs and troubleshooting.
- AWS IAM for permissions and access control.
- API Gateway CORS configuration for browser access.

## 🚀 AWS Services Used

| AWS Service | Purpose |
|---|---|
| Amazon S3 | Hosts the static frontend website |
| Amazon API Gateway | Provides the HTTP API endpoint |
| AWS Lambda | Processes requests and invokes the AI model |
| Amazon Bedrock | Provides access to the foundation model |
| Amazon Nova Micro | Generates AI responses |
| Amazon DynamoDB | Stores conversation records |
| Amazon CloudWatch | Monitors Lambda execution and logs |
| AWS IAM | Manages service permissions |

## 🛠️ Technologies Used

- HTML5
- CSS3
- JavaScript
- Python
- AWS Lambda
- Amazon API Gateway
- Amazon Bedrock Converse API
- Amazon DynamoDB
- Amazon S3
- Amazon CloudWatch
- AWS IAM

## ✨ Features

- Interactive chat interface with a modern dark theme.
- AI-powered answers using Amazon Nova Micro.
- Serverless backend architecture.
- HTTP POST requests through API Gateway.
- Chat history storage using DynamoDB.
- Loading indicators while the AI generates a response.
- Error handling for failed API requests.
- Static website hosting using Amazon S3.
- Monitoring and debugging through CloudWatch logs.
- IAM-based access control for AWS resources.

## 📂 Project Structure

```text
aws-gen-ai-assistant/
│
├── index.html          # Frontend chat application
├── lambda_function.py  # AWS Lambda backend
├── README.md           # Project documentation
└── screenshots/        # Project screenshots (optional)
```

*Adjust the filenames and folder structure if your actual repository is different.*

## ⚙️ How It Works

1. The user opens the web application hosted on Amazon S3.
2. The user enters a question in the chat interface.
3. JavaScript sends a POST request containing the question to Amazon API Gateway.
4. API Gateway invokes the configured AWS Lambda function.
5. Lambda validates the request and calls Amazon Bedrock using the Converse API.
6. Amazon Nova Micro generates a response.
7. Lambda returns the answer to API Gateway.
8. The frontend displays the answer in the chat window.
9. Lambda stores the question, answer, session ID, and timestamp in DynamoDB, if this functionality is implemented and configured.

## 🔧 Setup and Deployment

### Step 1: Configure Amazon Bedrock

1. Open the Amazon Bedrock console.
2. Select the `us-east-1` AWS Region.
3. Confirm that Amazon Nova Micro (`amazon.nova-micro-v1:0`) is available for your account.
4. Configure the permissions needed to invoke the model.

### Step 2: Create the DynamoDB Table

Create a DynamoDB table named:

`GenAIChatHistory`

Configure the partition key:

- Attribute name: `sessionId`
- Data type: `String`

Ensure the Lambda code and table key schema match. If you plan to store multiple messages for the same session, design a suitable sort key or use a separate unique key for each record.

### Step 3: Create the Lambda Function

1. Create a Python Lambda function named `GenAI-Bedrock-Lambda`.
2. Configure the execution role with the required permissions for Amazon Bedrock and DynamoDB.
3. Add the backend code to parse the incoming question.
4. Use the Amazon Bedrock Converse API to invoke Nova Micro.
5. Return a JSON response containing `success` and `answer`.
6. Configure the required environment variables, if your code uses them.
7. Test the function using a sample JSON event.

Example request:

```json
{
  "question": "Explain AWS Lambda in simple words."
}
```

Example successful response:

```json
{
  "success": true,
  "answer": "AWS Lambda runs code without requiring you to manage servers."
}
```

### Step 4: Configure Amazon API Gateway

1. Create an HTTP API named `GenAI-API`.
2. Integrate the API with `GenAI-Bedrock-Lambda`.
3. Create the route `POST /ask`.
4. Configure the API stage and deployment.
5. Enable CORS for your website origin, the `POST` method, and the `Content-Type` header.
6. Copy the invoke URL.

### Step 5: Configure the Frontend

Open `index.html` and replace the API URL placeholder with your deployed API endpoint:

```javascript
const API_URL = "https://YOUR_API_ID.execute-api.us-east-1.amazonaws.com/ask";
```

Use the correct URL for your API ID and stage.

### Step 6: Host the Website on Amazon S3

1. Create an S3 bucket for the frontend.
2. Upload `index.html`.
3. Enable static website hosting.
4. Configure access according to your hosting approach.
5. Open the S3 website endpoint and test the chat interface.

For production deployments, consider using Amazon CloudFront with appropriate access controls instead of making the S3 bucket publicly readable.

### Step 7: Verify and Monitor

- Test the API with a sample POST request.
- Open the website and submit a question.
- Check Lambda execution logs in Amazon CloudWatch.
- Verify that DynamoDB receives the expected records.
- Check browser developer tools if the frontend reports a network or CORS error.

## 🔐 Security Considerations

- Follow the principle of least privilege when creating IAM policies.
- Do not place AWS access keys or secret credentials in frontend JavaScript.
- Restrict API access as appropriate for your application.
- Configure CORS to allow only trusted origins in production.
- Validate incoming requests and handle errors safely.
- Avoid logging sensitive user data.
- Configure appropriate DynamoDB permissions and encryption.
- Monitor usage and costs for API Gateway, Lambda, Bedrock, and other services.

## 💡 Learning Outcomes

Through this project, I gained practical experience with:

- Building a serverless application on AWS.
- Integrating Generative AI using Amazon Bedrock.
- Invoking foundation models from AWS Lambda.
- Creating HTTP APIs using Amazon API Gateway.
- Hosting static websites using Amazon S3.
- Storing application data using Amazon DynamoDB.
- Configuring IAM permissions and CORS.
- Troubleshooting applications using CloudWatch logs.
- Understanding the architecture of an end-to-end cloud application.

## 🔮 Future Enhancements

- Add persistent conversation history and session management.
- Implement user authentication and authorization.
- Add streaming AI responses.
- Improve the chat interface for mobile devices.
- Add rate limiting and request validation.
- Introduce CloudFront and a custom domain.
- Add automated deployment using AWS SAM or AWS CloudFormation.
- Implement cost monitoring and usage limits.

## 👨‍💻 Author

**Mohd Maaz**

Computer Science Graduate | AWS | Linux | Cloud Computing | DevOps | Python

## 📄 License

This project is intended for educational and portfolio purposes. Add a license file if you want to specify the terms under which others may use or modify the code.
