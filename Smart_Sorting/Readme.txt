
NUTRIGAZE – AI BASED FRUIT & VEGETABLE FRESHNESS SYSTEM

1. PROJECT OVERVIEW
-------------------
NutriGaze is a Deep Learning based web application that detects
whether a fruit or vegetable is Healthy or Rotten using image classification.

The user uploads an image through a web interface, and the system
analyzes the image using a trained Convolutional Neural Network (CNN)
model and displays:

• Fruit / Vegetable Name
• Freshness Status (Healthy or Rotten)
• Prediction Confidence (%)

The goal of this project is to reduce food waste and automate
quality inspection using Artificial Intelligence.




2. PROBLEM STATEMENT
--------------------
Manual inspection of fruits and vegetables can be time-consuming
and inaccurate. There is a need for an automated system that can:

• Identify the type of fruit or vegetable
• Determine its freshness condition
• Provide accurate and fast results

This system solves that problem using Deep Learning.




3. TECHNOLOGIES USED
--------------------

Backend:
• Python
• Flask (Web Framework)
• TensorFlow / Keras
• NumPy
• Pillow

Frontend:
• HTML5
• CSS3

Model:
• VGG16 (Transfer Learning)
• Convolutional Neural Network (CNN)




4. DATASET INFORMATION
----------------------

Dataset Name:
Fruit and Vegetable Disease - Healthy vs Rotten Dataset

Total Classes: 28

Each fruit and vegetable has two categories:
• Healthy
• Rotten

Images were resized to 224x224 for model training.




5. MODEL DETAILS
----------------

Base Model: VGG16 (Pre-trained on ImageNet)
Technique: Transfer Learning
Image Size: 224 x 224
Optimizer: Adam
Loss Function: Categorical Crossentropy

Model Performance:
• Training Accuracy: Above 90%
• Validation Accuracy: Above 90%

The trained model is saved as:
healthy_vs_rotten_model.h5




6. PROJECT STRUCTURE
--------------------

SMART_SORTING
│
├── app.py                      → Main Flask Application
├── healthy_vs_rotten_model.h5  → Trained Deep Learning Model
├── ipython.html                → Training Notebook (HTML Export)
├── Readme.txt                  → Project Documentation
│
├── static/
│   ├── assets/
│   │    └── style.css          → Website Styling
│   ├── uploads/                → Stores Uploaded Images
│   └── forms/
│
└── templates/
    ├── index.html              → Home Page
    ├── blog.html               → About Page
    ├── portfolio-details.html  → Prediction Page
    └── blog-single.html        → Contact Page




7. HOW THE SYSTEM WORKS
-----------------------

Step 1:
User opens the web application.

Step 2:
User navigates to the Predict page.

Step 3:
User uploads an image of a fruit or vegetable.

Step 4:
The image is preprocessed (resized and normalized).

Step 5:
The trained VGG16 model analyzes the image.

Step 6:
The system displays:
• Fruit/Vegetable Name
• Healthy or Rotten Status
• Confidence Score




8. HOW TO RUN THE PROJECT
-------------------------

1. Install Required Libraries:

   pip install flask tensorflow numpy pillow

2. Open project folder:

   cd Smart_Sorting

3. Run the application:

   python app.py

4. Open browser and go to:

   http://127.0.0.1:5000




9. FEATURES
-----------

• Modern Web Interface
• Image Upload Functionality
• Real-time Prediction
• Displays Confidence Percentage
• Clean and Professional UI
• Internship Submission Ready




10. FUTURE IMPROVEMENTS
-----------------------

• Mobile Responsive Enhancement
• Real-time Camera Detection
• Cloud Deployment
• Database Integration
• User Login System
• Model Performance Optimization




11. CONCLUSION
--------------

NutriGaze demonstrates how Artificial Intelligence and Deep Learning
can be applied to solve real-world problems like food quality
inspection and waste reduction.

The system successfully classifies fruits and vegetables as
Healthy or Rotten with high accuracy and provides a simple
web interface for user interaction.




12. DEVELOPER DETAILS
---------------------

Project Name: NutriGaze – Smart Sorting System
Domain: Artificial Intelligence & Machine Learning
Project Type: Internship Project

Developer Name: [KOILADA PAVITRA]




