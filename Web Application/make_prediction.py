import streamlit as st
import pandas as pd
import numpy as np
import pickle

def app():
    # Title for the prediction page
    st.title('Sales Prediction')

    # Load the trained model, scaler, encoder, and PCA model
    model_filename = 'DecisionTreeRegressor_model.pkl'
    scaler_filename = 'scaler.pkl'
    encoder_filename = 'encoder.pkl'
    pca_model_filename = 'pca_model.pkl'

    with open(model_filename, 'rb') as file:
        model = pickle.load(file)

    with open(scaler_filename, 'rb') as file:
        scaler = pickle.load(file)

    with open(encoder_filename, 'rb') as file:
        encoder = pickle.load(file)

    with open(pca_model_filename, 'rb') as file:
        pca = pickle.load(file)

  # Define your numeric and categorical columns as they were during model training
    numeric_cols = ['store_nbr', 'onpromotion', 'month', 'year']
    categorical_cols = ['family', 'day_name', 'city', 'state']

    # Creating input fields for the features your model expects
    store_nbr = st.number_input('Store Number', min_value=1, max_value=54, value=1)
    family = st.selectbox('Product Family', options=['AUTOMOTIVE', 'BABY CARE', 'BEAUTY', 'BEVERAGES', 'BOOKS', 'BREAD/BAKERY',
 'CELEBRATION', 'CLEANING', 'DAIRY', 'DELI', 'EGGS', 'FROZEN FOODS', 'GROCERY I',
 'GROCERY II', 'HARDWARE', 'HOME AND KITCHEN I', 'HOME AND KITCHEN II',
 'HOME APPLIANCES', 'HOME CARE', 'LADIESWEAR', 'LAWN AND GARDEN', 'LINGERIE',
 'LIQUOR,WINE,BEER', 'MAGAZINES', 'MEATS', 'PERSONAL CARE', 'PET SUPPLIES',
 'PLAYERS AND ELECTRONICS', 'POULTRY', 'PREPARED FOODS', 'PRODUCE',
 'SCHOOL AND OFFICE SUPPLIES', 'SEAFOOD'])  
    onpromotion = st.number_input('Number of Products on Promotion', value=0)
    month = st.selectbox('Month', options=list(range(1, 13)))
    year = st.selectbox('Year', options=[2013, 2014, 2015, 2016, 2017])
    day_name = st.selectbox('Day of the Week', options=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    city = st.selectbox('City', options=['Quito', 'Santo Domingo', 'Cayambe', 'Latacunga', 'Riobamba', 'Ibarra',
 'Guaranda', 'Puyo', 'Ambato', 'Guayaquil', 'Salinas', 'Daule', 'Babahoyo',
 'Quevedo', 'Playas', 'Libertad', 'Cuenca', 'Loja', 'Machala', 'Esmeraldas',
 'Manta', 'El Carmen'])
    state = st.selectbox('State', options=['Pichincha', 'Santo Domingo de los Tsachilas', 'Cotopaxi', 'Chimborazo',
 'Imbabura', 'Bolivar', 'Pastaza', 'Tungurahua', 'Guayas', 'Santa Elena',
 'Los Rios', 'Azuay', 'Loja', 'El Oro', 'Esmeraldas', 'Manabi'])

    # Button to make prediction
    if st.button('Predict Sales'):
        # Creating a DataFrame from the input data
        input_data = pd.DataFrame([[store_nbr, family, onpromotion, month, year, day_name, city, state]],
                                  columns=['store_nbr', 'family', 'onpromotion', 'month', 'year', 'day_name', 'city', 'state'])
        
        # Preprocessing numeric columns
        input_data[numeric_cols] = scaler.transform(input_data[numeric_cols])
        
        # Preprocessing categorical columns
        input_data_encoded = encoder.transform(input_data[categorical_cols])
        encoded_feature_names = encoder.get_feature_names_out(categorical_cols)
        input_data_encoded_df = pd.DataFrame(input_data_encoded, columns=encoded_feature_names)
        
        # Combine numeric and encoded categorical features
        final_features = pd.concat([input_data[numeric_cols].reset_index(drop=True), input_data_encoded_df.reset_index(drop=True)], axis=1)
        
        # Apply PCA transformation to match the training data's feature set
        final_features_pca = pca.transform(final_features)
        
        # Predicting using the PCA-transformed features
        prediction = model.predict(final_features_pca)
        
        # Displaying prediction
        st.write(f'Predicted Sales: {prediction[0]}')
        
        # Saving the entry to a history file
        history_file_path = 'prediction_history.txt'
        history_entry = f"Store Number: {store_nbr}, Product Family: {family}, Products on Promotion: {onpromotion}, Month: {month}, Year: {year}, Day of the Week: {day_name}, City: {city}, State: {state}, Predicted Sales: {prediction[0]}\n"
        with open(history_file_path, 'a') as file:
            file.write(history_entry)
