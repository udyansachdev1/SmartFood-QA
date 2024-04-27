# Food Image Recognition and Description Generation

[![CI-Rust](https://github.com/nogibjj/Final_Project_Cloud/actions/workflows/rust.yml/badge.svg)](https://github.com/nogibjj/Final_Project_Cloud/actions/workflows/rust.yml) [![CI-Python](https://github.com/nogibjj/Final_Project_Cloud/actions/workflows/python.yml/badge.svg)](https://github.com/nogibjj/Final_Project_Cloud/actions/workflows/python.yml)

This project is a web application that uses a pre-trained machine learning model to identify images of food items and generate descriptions for them. The application is built with Streamlit and Rust, and is hosted on AWS.

## Overview

1. **Food Image Recognition**: The application accepts an image URL of one of the following food items and identifies it using a pre-trained model:
    - Tiramisu
    - Tuna Tartare
    - Beet Salad
    - Fish and Chips
    - Pancakes
    - Caesar Salad
    - Garlic Bread
    - Carrot Cake
    - Chocolate Mousse
    - Hot Dog
    - Steak

2. **Description Generation**: After identifying the food item, the application uses Rust to connect to [HuggingFace](https://huggingface.co/)'s [Meta Llama](https://huggingface.co/meta-llama/Meta-Llama-3-8B) model and answer questions about the dish.

3. **AWS Hosting**: The application is hosted on [AWS](https://aws.amazon.com/) using [Elastic Container Registry](https://aws.amazon.com/ecr/) with serverless [AWS Fargate](https://aws.amazon.com/fargate/) for Dockerized Image, [Elastic Container Service](https://aws.amazon.com/ecs/) for container orchestration and load balancing, and [Amazon EC2](https://aws.amazon.com/ec2/) for the web server.

4. **CI/CD Pipeline**: The CI/CD pipeline automatically updates the AWS architecture on any changes to the base codes, ensuring rapid iteration and deployment of changes to the service.

Demo Video - [Link]()

## How to Use the App

1. **Access the App**: Visit our Streamlit app [here](http://cf-ecs-lb-162243208.us-east-2.elb.amazonaws.com/).

2. **Image Identification**:
    - In the `Image URL` field on the left sidebar, input the URL of an image featuring any of the listed food items.
    - Press `Enter` to initiate the identification process.
    - The app will analyze the image and display the identified food item.

3. **Question and Answer**:
    - If you have a question or prompt about the identified food item, input it in the `Enter your Query` field on the right.
    - Click on `Submit` to generate a response.
    - The app will use Huggingface's Llama LLM Model to generate and display a response to your query.

Below are a few sample image URLs to get you started with the app:
    - Tiramisu: [https://food.fnr.sndimg.com/content/dam/images/food/fullset/2011/2/4/2/RX-FNM_030111-Sugar-Fix-005_s4x3.jpg.rend.hgtvcom.1280.960.suffix/1371597326801.jpeg](https://food.fnr.sndimg.com/content/dam/images/food/fullset/2011/2/4/2/RX-FNM_030111-Sugar-Fix-005_s4x3.jpg.rend.hgtvcom.1280.960.suffix/1371597326801.jpeg)
    - Hot Dog: [https://img.freepik.com/free-photo/classic-hot-dog-with-ketchup-mustard-sauce-isolated-white-background_123827-29747.jpg?size=626&ext=jpg&ga=GA1.1.1395880969.1710028800&semt=ais](https://img.freepik.com/free-photo/classic-hot-dog-with-ketchup-mustard-sauce-isolated-white-background_123827-29747.jpg?size=626&ext=jpg&ga=GA1.1.1395880969.1710028800&semt=ais)
    - Carrot Cake: [https://bakerjo.co.uk/wp-content/uploads/2022/08/IMG_3525.jpg](https://bakerjo.co.uk/wp-content/uploads/2022/08/IMG_3525.jpg)

## App Development and Architecture

## CI/CD Pipeline

## App Deployment

## Monitoring and Logging

## Team Members
