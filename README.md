# Store Sales - Time Series Forecasting

## 1) Introduction

Welcome to the "Store Sales - Time Series Forecasting" competition! Hosted by Kaggle, this challenge offers an exciting opportunity to dive into the world of machine learning and time-series forecasting. Our goal is to forecast grocery sales using data from Corporación Favorita, a major grocery retailer based in Ecuador.

### Goal of the Competition
The main goal is predicting the unit sales of thousands of products sold at various Favorita stores. Using a dataset that includes dates, store and item information, promotions, and past sales, your mission is to build a model that forecasts sales more accurately. This is a fantastic way to practice your machine learning skills and get hands-on experience with time-series forecasting.

### Why This Matters
Forecasting is not just for predicting the weather. It's a critical tool for economic planning, scientific research, and business operations. For grocery stores, accurate forecasting can significantly reduce food waste and improve customer satisfaction by ensuring the right amount of products are available at the right time. This competition is your chance to apply machine learning techniques to a real-world problem, enhancing your skills and making a tangible impact.

### Evaluation
Submissions will be evaluated based on the Root Mean Squared Logarithmic Error (RMSLE). This metric is crucial for understanding the accuracy of your predictions, focusing on the logarithmic difference between predicted and actual sales figures.


## 2) How to Install

To get started with this project, follow these steps:

1. Clone this project repository from GitHub
  
2. Install the required packages listed in the requirements.txt file using pip: pip install -r Requirements.txt


## 3) How to Run

After installing the required dependencies, follow these steps to run the application:

1. Open your preferred code editor and navigate to the project directory.

2. Open the terminal or command prompt.

3. Run the following command to start the Streamlit application: streamlit run app.py


## 4) How to Use

Follow these steps to use the "Store Sales - Time Series Forecasting" application:

1. Upon accessing the application, you will see input fields for various features required for sales prediction.

2. Fill in the following information:
   - **Store Number**: Enter the store number for which you want to predict sales.
   - **Product Family**: Select the product family from the dropdown menu.
   - **Number of Products on Promotion**: Enter the number of products on promotion.
   - **Month**: Select the month for which you want to make the prediction.
   - **Year**: Select the year corresponding to the prediction.
   - **Day of the Week**: Select the day of the week.
   - **City**: Select the city where the store is located.
   - **State**: Select the state where the store is located.

3. After providing the required information, click on the "Predict Sales" button.

4. The application will process the input data and display the predicted sales value.

5. You can adjust the input fields and repeat the prediction process as needed to explore different scenarios.

6. To exit the application, simply close the web browser tab or stop the Streamlit server in the terminal/command prompt.

Enjoy using the "Store Sales - Time Series Forecasting" application to forecast sales accurately and efficiently!


