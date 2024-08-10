# Mood Predictor App

## Overview

The Mood Predictor App is a React Native application that analyzes song lyrics to predict the emotional mood conveyed by the text. Users can input lyrics, and the app will display predicted moods with a stylish and interactive interface. The app also includes mental health support features to provide resources for users who might be feeling lonely, isolated, or lost.

## Features

- **Predict Mood**: Enter lyrics and get mood predictions.
- **Interactive UI**: Animated and responsive interface for a smooth user experience.
- **Error Handling**: Displays error messages when needed.
- **Mental Health Support**: Provides resources if mood predictions indicate feelings of loneliness, isolation, or being lost.
- **Navigation**: Easy navigation with a bottom navigation bar.

## Technologies Used

- **React Native**: Framework for building the app.
- **React Navigation**: For handling navigation.
- **Animated API**: For creating smooth animations.
- **Fetch API**: For making HTTP requests to the backend.

## Backend Setup

The app communicates with a Flask backend for mood prediction. Ensure that the backend server is running and accessible at `http://10.0.2.2:5000/predict`. 

## Usage

1. **Input Lyrics**: Type or paste song lyrics into the input field.
2. **Predict Mood**: Tap the "Predict Mood" button to get mood predictions.
3. **View Results**: Predicted moods will be displayed with a fade-in animation. If no moods are predicted, an appropriate message will be shown.
4. **Navigate**: Use the bottom navigation bar to access different sections of the app.


