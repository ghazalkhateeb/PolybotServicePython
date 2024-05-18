# Image Processing Telegram Bot <br />

## Introduction
This repository contains code for an Image Processing Bot built using Python, Flask, and the Telegram API.<br />
The bot allows users to send photos with captions indicating the desired image processing filter to apply, such as blur, contour, rotate, segment, salt and pepper, or concatenation.

## Features
Apply various image processing filters to photos sent by users. <br />
Supported filters include blur, contour, rotate, segment, salt and pepper, and concatenation. <br />
Error handling for graceful user experience. <br />
Telegram webhook integration for real-time interaction. <br />

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
   follow this link to create the bot.
   ```
   https://core.telegram.org/bots/features#botfather
   ```
2- Set the environment variables TELEGRAM_TOKEN with your Telegram bot token. <br />
3- Sign up for the Ngrok service:  
   ```
   https://ngrok.com/ 
   ```
   and go over the instructions : <br />
    
    https://dashboard.ngrok.com/get-started/setup 
4- run this command: <br />
   ```
   ngrok http 8443
   ```
   When the command ran, you will see "Forwarding line" with a link.  <br />
  
4- Set the environment variables TELEGRAM_APP_URL with your application URL in the forwarding line. <br /> 

## Usage  <br />
1- Run the Flask application by executing app.py: 
```
python app.py
```
2- The application will start running.  <br /> 
   you can greet the bot using those three words:
   start, hello, hi.
![image](https://github.com/ghazalkhateeb/PolybotServicePython/assets/99688953/ef60df31-a8a5-4cb1-95b4-c442be2185b1)

3- Interact with the bot via your Telegram account by sending photos with captions indicating the desired image processing filter. <br />
example 1: <br />
![image](https://github.com/ghazalkhateeb/PolybotServicePython/assets/99688953/8e3d9757-cb14-46a9-ae84-7827648ef2c4)  <br />
example 2: <br /> 
![image](https://github.com/ghazalkhateeb/PolybotServicePython/assets/99688953/807a44a6-90a3-40fa-9d4c-ce75c8a465e2)  <br />








