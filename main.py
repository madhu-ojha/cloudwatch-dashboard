import boto3
import json
import os
from datetime import datetime

def dateandtime():
    now = datetime.now()  # This should be a datetime object
    formatted_now = now.strftime("%Y-%m-%d-%H:%M:%S")
    return formatted_now

def get_cloudwatch_client():
    """Initialize and return a CloudWatch client."""
    return boto3.client('cloudwatch')

def load_metric_widget_from_file(filename):
    """Load metric widget JSON from a file."""
    with open(filename, 'r') as file:
        return json.load(file)

def get_metric_widget_image(client, metric_widget):
    """Get the metric widget image from CloudWatch."""
    try:
        response = client.get_metric_widget_image(MetricWidget=json.dumps(metric_widget))
        return response['MetricWidgetImage']
    except Exception as e:
        print(f"An error occurred while getting the metric widget image: {e}")
        raise

def save_image_to_file(image_data, filename):
    """Save image data to a PNG file."""
    try:
        with open(filename, 'wb') as f:
            f.write(image_data)
        print(f"Image saved successfully to {filename}.")
    except Exception as e:
        print(f"An error occurred while saving the image: {e}")
        raise

def main():
    time = dateandtime()
    source_dir = './Source/'
    output_dir = './Output/'
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Initialize CloudWatch client
    client = get_cloudwatch_client()

    # Process each JSON file in the Source directory
    for filename in os.listdir(source_dir):
        if filename.endswith('.json'):
            dashboard_file = os.path.join(source_dir, filename)
            output_file = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}-{time}.png")

            # Load metric widget
            metric_widget = load_metric_widget_from_file(dashboard_file)
            
            # Get metric widget image
            image_data = get_metric_widget_image(client, metric_widget)
            
            # Save image to file
            save_image_to_file(image_data, output_file)

if __name__ == "__main__":
    main()
