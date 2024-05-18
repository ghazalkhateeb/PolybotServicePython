## Introduction
This repository contains code for an Image Processing Bot built using Python, Flask, and the Telegram API. The bot allows users to send photos with captions indicating the desired image processing filter to apply, such as blur, contour, rotate, segment, salt and pepper, or concatenation.

## Features
Apply various image processing filters to photos sent by users.
Supported filters include blur, contour, rotate, segment, salt and pepper, and concatenation.
Error handling for graceful user experience.
Telegram webhook integration for real-time interaction.

## Prerequisites
Before running the application, ensure you have the following installed:  <br />
Python (>=3.6)  <br />
Flask  <br />
Matplotlib  <br />
Telebot  <br />
Loguru  <br />

## Installation
1- Clone this repository to your local machine: <br />
```
git clone https://github.com/ghazalkhateeb/PolybotServicePython.git
```
2- Navigate to the project directory: <br />
```
cd directory path
```
3- Install dependencies using pip: <br />
```
pip install -r requirements.txt
```
## Configuration <br />
1- Set up a Telegram bot and obtain the API token. <br />
2- Set the environment variables TELEGRAM_TOKEN and TELEGRAM_APP_URL with your Telegram bot token and your application URL, respectively. <br /> 

## Usage  <br />
1- Run the Flask application by executing app.py: 
```
python app.py
```
2- The application will start running on http://localhost:8443/.  <br /> 
3- Interact with the bot via your Telegram account by sending photos with captions indicating the desired image processing filter.

Example: <br />
Send a photo with the caption "Blur" to apply the blur filter to the image.




