#  Sarvagyaata AI Streamlit Application

# Live Demo : 
<https://github.com/user-attachments/assets/e78cccf0-929f-4d2b-b554-1f9db2f4636b>

# WEBSITE LINK 1:https://sarvagyaataai.streamlit.app/
# WEBSITE LINK 2:https://sarvagyaata-ai-u6z4.onrender.com/

## Table of Contents
1. [Introduction](#introduction)
2. [Features and its Explaination](#features)
3. [Installation](#installation)
4. [Running the Application](#running-the-application)
5. [Application Structure](#application-structure)
6. [About Us](#about-us)
7. [License](#license)

## Introduction
Welcome to Sarvagyaata AI, your all-in-one intelligent business solution. This application is built using Streamlit and offers a variety of business intelligence features. Our team of passionate third-year engineering students in Artificial Intelligence and Data Science (AIDS) is dedicated to revolutionizing business intelligence through innovative solutions.

## Features
The application offers the following features:

1. **Personalized Content Chatbot**
2. **Chat with any PDF**
3. **Personalized Computer Vision**
4. **Movie Recommendation System**
5. **Business Analyst Dashboard**
6. **Causal Inference of Blockchain**
7. **Sentiment Analysis of Twitter**
8. **Stock Price Predictive Analytics**
9. **CryptoCurrency Predictive Analytics**
10. **Company Chat Analyser**
11. **AutoML for Auto EDA**

# Explaination 
## 1.Personalized Content Chatbot Feature

The **Personalized Content Chatbot** is designed to help users generate creative writing prompts based on their input, such as a genre, tone, or initial plot point. Leveraging the `gpt-3.5-turbo` model from OpenAI, this feature aids writers in overcoming writer's block and finding inspiration for their projects.

### How It Works

1. **User Input**: Users provide a genre, tone, or initial plot point for the desired writing prompt.
2. **AI Model Invocation**: The application uses the `gpt-3.5-turbo` model to generate a creative writing prompt based on the user's input.
3. **Response Display**: The generated writing prompt is displayed to the user, providing inspiration for their writing task.

### User Interface

- **Main Interface**: Includes a title and description, a text area for user input, and a "Generate Prompt" button.
- **Sidebar**: Contains options, settings, and example prompts to guide the user.

This feature is ideal for writers and anyone looking for creative inspiration for their writing projects.

## 2.Chat with any PDF Feature

The **"Chat with any PDF"** feature enables users to interact with and extract information from a PDF document related to the Diamante Net Hackathon. By uploading a PDF guide, users can ask questions about the hackathon, and the system provides relevant answers based on the content of the PDF and additional pre-defined information.

### How It Works

1. **Upload PDF**: Users can upload a PDF document related to the Diamante Net Hackathon.

2. **Extract and Process Text**: The content from the uploaded PDF is extracted and combined with pre-defined hackathon information.

3. **Question Handling**: Users can input questions about the hackathon. The system processes these questions and provides answers by:
   - Splitting the text into manageable chunks.
   - Finding the most relevant chunks based on the question.
   - Classifying the type of question (e.g., person, location, date).
   - Extracting relevant entities and information from the text.

4. **Answer Display**: The system presents the most relevant information or answers based on the user's question.

### User Interface

- **Title**: "Diamante Net Hackathon Assistant"
- **Subtitle**: "Your personal guide to the Diamante Net Hackathon"
- **PDF Uploader**: Allows users to upload a PDF guide for additional information.
- **Text Input**: Users enter their questions about the hackathon.
- **Answer Display**: Shows the answer or relevant information extracted from the PDF and pre-defined content.

This feature provides a user-friendly way to interact with and extract useful details from hackathon-related documents.

## 3.Personalized Computer Vision Feature

The **Personalized Computer Vision** feature focuses on **object detection and tracking** using the YOLOv8 model. This feature allows users to detect and track objects in images and videos by selecting different model configurations and input sources.

### How It Works

1. **Model Selection**: Users can choose between object detection and segmentation tasks. The system loads the corresponding pre-trained YOLOv8 model based on the user's selection.

2. **Confidence Level**: Users can adjust the model's confidence threshold via a slider, which determines the minimum confidence level required for object detection.

3. **Source Selection**:
   - **Image**: Users can upload an image from their local files. The system displays both the original and detected images, showing the results of object detection with bounding boxes and additional information.
   - **Video**: Users can process and analyze a video file for object detection and tracking.
   - **YouTube**: Users can provide a YouTube video URL to analyze video content for object detection.

4. **Output Display**: The system displays the processed results, including detected objects and bounding boxes, as well as the option to view detection results in an expandable section.

### User Interface

- **Main Page**: Displays the title and description for object detection and tracking.
- **Sidebar**: Contains options for selecting the model type (detection or segmentation), confidence level, and input source (image, video, YouTube).
- **Image/Video Upload**: Users can upload images or provide video URLs for processing. 
- **Detection Results**: Shows the detected objects and their details.

This feature is designed for users needing to perform advanced computer vision tasks such as object detection and tracking in various types of media.

## 4.Movie Recommender Engine

The **Movie Recommender Engine** feature provides users with personalized movie recommendations based on their selected movie. This feature leverages a recommendation system to suggest similar movies, offering an engaging and interactive experience.

### How It Works

1. **Movie Selection**:
   - Users can select a movie from a dropdown menu or type the movie’s name into a text box.

2. **Recommendation Generation**:
   - The system uses a pre-trained recommendation model to find and suggest movies similar to the selected one. It fetches these recommendations based on similarity metrics.

3. **Poster Retrieval**:
   - For each recommended movie, the system fetches movie posters from an external API to visually present the recommendations.

4. **Display Recommendations**:
   - Recommended movies, along with their posters, are displayed in a grid layout for easy viewing. This visual display helps users quickly identify and explore new movies.

### User Interface

- **Movie Selection Dropdown**:
  - Allows users to select a movie from a list or input its name manually.

- **Recommendation Display**:
  - Shows recommended movies and their posters in a visually appealing format, helping users to explore new movie options based on their preferences.

This feature enhances the user experience by providing tailored movie suggestions and leveraging visual elements to engage users effectively.

### 5.Bussiness Dashboard

The dashboard offers a comprehensive platform for data analytics and visualization, built using Streamlit and various Python libraries.

#### Key Features

1. **Data Loading and Filtering**:
   - Loads data from an Excel file (or MySQL database).
   - Users can filter data by region, location, and construction type via sidebar options.

2. **Descriptive Analytics**:
   - Provides statistics like mean, mode, sum, and median of investment amounts.
   - Displays metrics using visually appealing cards.

3. **Data Visualization**:
   - **Bar Graphs**: Investment by business type.
   - **Line Graphs**: Investment trends by state.
   - **Pie Charts**: Ratings distribution by region.
   - **Histograms**: Variable distributions.
   - **Box Plots**: Investment quartiles by business type.

4. **Interactive Features**:
   - **Data Viewing**: Filter and view datasets within the dashboard.
   - **Progress Bar**: Tracks earnings against a target.

5. **Advanced Analytics Pages**:
   - Includes pages for Covariance, Frequency Distribution, Hypothesis Testing, Python Query, Advanced Regression, Business Locations, Descriptive Statistics, Regression Analysis, and Sales by Date.

This dashboard is ideal for interactive data exploration and visualization, providing a powerful tool for gaining insights from data.

### 6. Causal Inference in Blockchain Transactions Feature

This feature demonstrates causal inference in blockchain transactions using synthetic data. It aims to understand the causal effects of different transaction features on confirmation times.

#### Key Components

1. **Data Generation and Loading**:
   - Synthetic data is generated with features like transaction ID, fee, size, number of inputs, outputs, and confirmation time.
   - Data is cached for efficient loading.

2. **Exploratory Data Analysis (EDA)**:
   - **Correlation Heatmap**: Visualizes the correlation between transaction features.
   - **Scatter Plot Matrix**: Shows relationships between multiple transaction features.
   - **Distribution Plots**: Displays the distribution of each transaction feature.

3. **Causal Inference Analysis**:
   - Utilizes the `DoWhy` library to build a causal model.
   - **Causal Graph**: Attempts to visualize the causal relationships between features.
   - **Identified Estimand**: Presents the causal estimand identified by the model.
   - **Causal Estimate**: Estimates the causal effect using linear regression.

4. **Intervention Analysis**:
   - Allows users to select a feature for intervention.
   - Simulates the effect of doubling the selected feature on confirmation time.
   - **Causal Model for Intervened Data**: Builds a new causal model for the intervened data.
   - **Intervention Effect Visualization**: Shows the effect of intervention on confirmation time using scatter plots.

This feature provides an interactive and educational experience for understanding causal relationships in blockchain transactions, leveraging advanced statistical methods and visualizations.

### 7.Twitter Sentiment Analysis Feature

This feature allows users to perform sentiment analysis on tweets using a pre-trained model and visualize the data distributions and word clouds based on the sentiment of tweets.

#### Key Components

1. **Model Loading**:
   - Loads a pre-trained sentiment analysis model from a pickle file.

2. **Data Visualization**:
   - Loads a dataset of tweets with their sentiments and text.
   - **3D Scatter Plot**: Visualizes the relationship between tweet length, word count, and sentiment using a 3D scatter plot.
   - **Sentiment Distribution Pie Chart**: Shows the distribution of different sentiments in the dataset.
   - **Word Clouds by Sentiment**: Generates word clouds for each sentiment category, highlighting the most frequent words in tweets of each sentiment.

3. **Prediction**:
   - Allows users to enter a tweet and predict its sentiment using the pre-trained model.
   - Displays the prediction result and the time taken to make the prediction.

4. **About Page**:
   - Provides detailed information about Twitter Sentiment Analysis, including methods used in the application and the benefits of sentiment analysis.
   - Describes the steps involved in data cleaning, feature extraction, model building, and model evaluation.

This feature offers a comprehensive approach to sentiment analysis on Twitter, combining model prediction capabilities with rich data visualizations and user-friendly navigation.

### 8. Stock Index Dashboard Application Overview

#### Tabs and Functionalities
1. **APP INTRODUCTION:**
   - **Markdown:** Overview of app features:
     - **STOCK INDEX DASHBOARD:** Visualize closing prices and volumes.
     - **PORTFOLIO SIMULATION:** Construct Efficient Frontier and simulate portfolios.
     - **CLOSING PRICE PREDICTION:** Predict prices using MLP Regressor.
   - **Date Info:** Current date and time range for analysis.
   - **Stock Indices Description:** Loads and displays indices descriptions from CSV.

2. **STOCK INDEX DASHBOARD:**
   - **Historical Data:** User-specified time range for data analysis.
   - **Data Processing:** Fetches and processes data from Yahoo Finance, extracts risk-free rates, and maps regions to indices.

#### Additional Functionalities
- **Portfolio Simulation:** Constructs Efficient Frontier and simulates portfolio performances.
- **Closing Price Prediction:** Uses historical data to predict prices with MLP Regressor.

#### User Interaction
- **Forms and Inputs:** Date input fields with error handling.

#### Visualization
- **Plotly and Matplotlib:** Interactive and static visualizations for stock index data.
- 
This summary captures the main components and functionalities of the Stock Index Dashboard application, emphasizing its use of various Python libraries for data analysis, visualization, and machine learning within a Streamlit framework.

### 9. Crypto Dashboard Feature

This feature provides a comprehensive cryptocurrency dashboard using Streamlit, displaying real-time price data from the Binance API.

#### Key Components

1. **Loading Market Data**:
   - Fetches real-time cryptocurrency price data from the Binance API and loads it into a DataFrame.

2. **Custom Rounding Function**:
   - Defines a function to round values appropriately based on their magnitude.

3. **Cryptocurrency Selection and Metrics Display**:
   - Provides a list of selected cryptocurrencies with their corresponding symbols from the Binance API.
   - Uses Streamlit's `selectbox` to allow users to choose different cryptocurrencies.
   - Displays the selected cryptocurrencies' prices and percentage changes using Streamlit's `metric` component, organized in three columns for a clean layout.

4. **Data Download Option**:
   - Offers a button to download the entire DataFrame as a CSV file, facilitating further analysis or record-keeping.

5. **Data Display**:
   - Displays the DataFrame containing cryptocurrency data in an expandable section with a large height setting to accommodate extensive data.

6. **Scripts for Enhanced Functionality**:
   - Includes external scripts for potential future enhancements, such as interactive elements using jQuery and Bootstrap.

This feature offers a user-friendly interface for monitoring and analyzing cryptocurrency prices, with options to customize the displayed data and download it for offline use. The use of real-time data from the Binance API ensures users have access to the most current market information.

### 10. Personalized Company Chat Analyzer Feature

This feature provides a comprehensive analysis of chat data, allowing users to gain insights into chat activity and patterns. The app is designed to handle chat data files, preprocess the data, and present various statistical and visual analyses.

#### Key Components

1. **Sidebar Configuration**:
   - Title: "Personalized Chat Analyzer".
   - File Uploader: Allows users to upload a chat data file.

2. **Data Preprocessing**:
   - Uploaded file is read and decoded.
   - Preprocessing is done using a custom `preprocessor` module to convert raw data into a structured DataFrame.

3. **User Selection**:
   - Fetches unique users from the chat data.
   - Provides a dropdown to select a user for analysis, with an option for "Overall" analysis.

4. **Statistics Display**:
   - Displays key statistics such as the total number of messages, words, media shared, and links shared using Streamlit’s `columns` and `header` components.

5. **Monthly Timeline**:
   - Displays a line plot showing the number of messages over time on a monthly basis using Matplotlib.

6. **Daily Timeline**:
   - Similar to the monthly timeline but on a daily basis.

7. **Activity Map**:
   - Shows the busiest days and months using bar plots.
   - Displays a heatmap for weekly activity patterns using Seaborn.

8. **Busiest Users (Group Level)**:
   - If "Overall" is selected, it shows the most active users in the group with a bar chart and a detailed DataFrame.

9. **WordCloud**:
   - Generates and displays a word cloud for the most frequently used words in the chat.

10. **Most Common Words**:
    - Displays a horizontal bar chart of the most common words in the chat.

11. **Emoji Analysis**:
    - Provides a detailed analysis of emojis used, displaying the data in a DataFrame and a pie chart.

This feature offers a detailed and interactive way to analyze chat data, providing both high-level insights and granular details about chat activity, user behavior, and communication patterns.

### 11. Robust AutoML App Feature

This feature provides an end-to-end solution for building, training, and downloading a machine learning model. It includes functionalities for data upload, basic exploratory data analysis (EDA), model training, and model downloading.

#### Key Components

1. **Sidebar Configuration**:
   - Image and title for the sidebar.
   - Radio button options: "Upload Data", "Basic EDA", "Train Model", and "Download Model".
   - Info message guiding the user to upload a dataset.

2. **Functionality to Check Data and Model Availability**:
   - `is_data_uploaded()`: Checks if a dataset has been uploaded.
   - `is_model_trained()`: Checks if a model has been trained.

3. **Upload Data**:
   - Removes existing uploaded data and model files if present.
   - Allows the user to upload a CSV file.
   - Displays the first few rows of the uploaded dataset and its dimensions.

4. **Basic EDA**:
   - Reads the uploaded data and provides basic information about the dataset.
   - Displays dataset info, description, and data types.
   - Visualizations for numeric and categorical data:
     - Histograms for numeric columns.
     - Pair plots for numeric columns.
     - Bar plots for categorical columns.
     - 3D scatter plot if there are at least three numeric columns.

5. **Train Model**:
   - Allows the user to select the problem type (Regression or Classification) and the target variable.
   - Joins text columns for TF-IDF vectorization.
   - Uses a pipeline with TF-IDF vectorizer and RandomForestClassifier.
   - Splits the data into training and testing sets.
   - Trains the model and evaluates it:
     - Displays accuracy.
     - Shows a confusion matrix.
     - Provides a classification report.
   - Saves the trained model using `joblib`.

6. **Download Model**:
   - Provides a download button for the trained model if it exists.

This feature provides a robust and user-friendly interface for building machine learning models, from data upload to model download, making it accessible for users with varying levels of expertise in machine learning.
## Installation
To install and run the application locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/harshchi19/Sarvagyaata-AI.git
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application
To run the application, execute the following command:
```bash
streamlit run app.py
```

## Application Structure
The application is structured as follows:

- `main.py`: The main Streamlit application file.
- `requirements.txt`: The dependencies required to run the application.
- `Personalized chatbot/`: Directory containing the `app.py` for the Personalized Content Chatbot feature.
- `chatwithpdf/`: Directory containing the `app.py` for the Chat with any PDF feature.
- `Object_Detection/`: Directory containing the `app.py` for the Personalized Computer Vision feature.
- `movie_recommendation/`: Directory containing the `app.py` for the Movie Recommendation System feature.
- `Bussiness Dashboard/`: Directory containing the `app.py` for the Business Analyst Dashboard feature.
- `Casual_Inference/`: Directory containing the `app.py` for the Causal Inference of Blockchain feature.
- `Twitter_Sentiment_Analysis/`: Directory containing the `app.py` for the Sentiment Analysis of Twitter feature.
- `Stock_Index_App/`: Directory containing the `app.py` for the Stock Price Predictive Analytics feature.
- `Crypto/`: Directory containing the `app.py` for the CryptoCurrency Predictive Analytics feature.
- `whatsapp-chat-analysis/`: Directory containing the `app.py` for the Company Chat Analyser feature.
- `AutoML/`: Directory containing the `app.py` for the AutoML for Auto EDA feature.

## About Us
We are a team of passionate third-year engineering students in Artificial Intelligence and Data Science (AIDS), dedicated to revolutionizing business intelligence through innovative solutions.

### Team Members
- **Harsh Chitaliya**: Harsh is a creative problem-solver with a keen interest in AI-driven chatbots and natural language processing. His innovative approach to personalized content delivery forms the backbone of our content chatbot feature.
- **Gaurav Singh Khati**: Gaurav excels in computer vision and machine learning. His expertise in developing tailored CV models has been crucial in creating our personalized computer vision solutions for various industry applications.
- **Satyavrat Tiwari**: Satyavrat is passionate about data analytics and predictive modeling. His work on real-time predictive analytics for stock prices and cryptocurrency has added significant value to our financial intelligence offerings.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for using Sarvagyaata AI! We hope our application helps you in making smarter business decisions through intelligent solutions. For any queries or support, please contact us at support@sarvagyaataai.com.
