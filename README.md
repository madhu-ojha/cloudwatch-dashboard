# CloudWatch Metric Widget Image Exporter

This script is designed to load CloudWatch metric widget definitions from JSON files, generate the corresponding images using the AWS CloudWatch service, and save these images as PNG files.

## Prerequisites

### AWS Credentials

Make sure you have your AWS credentials configured properly. The script uses the AWS SDK for Python (`boto3`), which requires access to your AWS credentials. You can configure your credentials using the AWS CLI or by setting up environment variables.

### Python Dependencies

Ensure you have the following Python packages installed:

- `boto3`

You can install the necessary package using `pip`:

```bash
pip install boto3
```
