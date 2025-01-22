import streamlit as st
import pandas as pd
import numpy as np
# Title of the form

raw_df = pd.read_csv('D:\\GUVI\\visual_studio\\Fligh Data\\Flight_Price.csv')
st.title("Price Predictor")
# Create the form
form = st.form(key='Price_prediction')
# Input fields
airline = form.selectbox("Airline", raw_df.Airline.unique())
source = form.selectbox("source", raw_df.Source.unique())
destination = form.selectbox('destination', raw_df.Destination.unique())
doj = form.date_input('Date of Journey')
dep_time = form.time_input('dep_time')
total_stops = form.slider('Total Stops',min_value = 0, max_value = 4)
additional_info = form.radio('Extra Info',raw_df['Additional_Info'].unique())
i = form.selectbox('Predict for Days', np.arange(10, 105, 5))

# Form submit button
submit_button = form.form_submit_button(label='Submit')
# If the form is submitted
if submit_button:
    # Create a dictionary with the form data
    form_data = {
        'Airline': airline,
        'Source': source,
        'Destination': destination,
        'Date_of_Journey': doj,
        'Dep_Time': dep_time,
        'Total_Stops': total_stops,
        'Additional_Info': additional_info
    }
    
    # Convert the dictionary to a DataFrame
    test_data = pd.DataFrame([form_data])
    test_data1=test_data.copy()
    
    # Display a success message
    st.success("Entry Successful!")
    
    # Display the form data as a table
    st.write("Here are your details:")
    st.table(test_data1)
    
    #creating series of data for price chart
    next_data = test_data1.copy()
    for _ in range (i):
        next_data['Date_of_Journey'] = next_data['Date_of_Journey'] + pd.Timedelta(days = 1)
        test_data1 = pd.concat([test_data1, next_data], ignore_index = True)
    
    import datetime as dt
    #test_data1['Date_of_Journey'] = pd.to_datetime(test_data1['Date_of_Journey'])
    test_data1['Date_of_Journey']=test_data1['Date_of_Journey'].map(dt.datetime.toordinal)

    test_data1['Dep_Time'] = pd.to_datetime(test_data1['Dep_Time'], format='%H:%M:%S')
    test_data1['Dep_Time']=test_data1['Dep_Time'].dt.strftime('%H%M%S').astype(int)

    test_data1 = pd.get_dummies(test_data1, dtype=int)
    
    user_data = pd.DataFrame(columns=['Date_of_Journey', 'Dep_Time', 'Total_Stops', 'Airline_Air Asia',
        'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
        'Airline_Jet Airways', 'Airline_Jet Airways Business',
        'Airline_Multiple carriers',
        'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
        'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
        'Source_Banglore', 'Source_Chennai', 'Source_Delhi', 'Source_Kolkata',
        'Source_Mumbai', 'Destination_Banglore', 'Destination_Cochin',
        'Destination_Delhi', 'Destination_Hyderabad', 'Destination_Kolkata',
        'Destination_New Delhi', 'Additional_Info_1 Long layover',
        'Additional_Info_1 Short layover', 'Additional_Info_2 Long layover',
        'Additional_Info_Business class', 'Additional_Info_Change airports',
        'Additional_Info_In-flight meal not included',
        'Additional_Info_No Info',
        'Additional_Info_No check-in baggage included',
        'Additional_Info_Red-eye flight'])
    user_data['Date_of_Journey'] = test_data1['Date_of_Journey']
    user_data['Dep_Time'] = test_data1['Dep_Time']
    user_data['Total_Stops'] = test_data1['Total_Stops']
    #airline
    try:
        user_data['Airline_Air Asia'] = test_data1['Airline_Air Asia']  
    except:
        pass
    try:
        user_data['Airline_Air India'] = test_data1['Airline_Air India']
    except:
        pass
    try:
        user_data['Airline_GoAir'] = test_data1['Airline_GoAir']
    except:
        pass
    try:
        user_data['Airline_IndiGo'] = test_data1['Airline_IndiGo']
    except:
        pass
    try:
        user_data['Airline_Jet Airways'] = test_data1['Airline_Jet Airways']
    except:
        pass
    try:
        user_data['Airline_Jet Airways Business'] = test_data1['Airline_Jet Airways Business']
    except:
        pass
    try:
        user_data['Airline_Multiple carriers'] = test_data1['Airline_Multiple carriers']
    except:
        pass
    try:
        user_data['Airline_Multiple carriers Premium economy'] = test_data1['Airline_Multiple carriers Premium economy']
    except:
        pass
    try:
        user_data['Airline_SpiceJet'] = test_data1['Airline_SpiceJet']
    except:
        pass
    try:
        user_data['Airline_Trujet'] = test_data1['Airline_Trujet']
    except:
        pass
    try:
        user_data['Airline_Vistara'] = test_data1['Airline_Vistara']
    except:
        pass
    try:
        user_data['Airline_Vistara Premium economy'] = test_data1['Airline_Vistara Premium economy']
    except:
        pass

    #source
    try:
        user_data['Source_Banglore'] = test_data1['Source_Banglore']  
    except:
        pass
    try:
        user_data['Source_Chennai'] = test_data1['Source_Chennai']  
    except:
        pass
    try:
        user_data['Source_Delhi'] = test_data1['Source_Delhi']  
    except:
        pass
    try:
        user_data['Source_Kolkata'] = test_data1['Source_Kolkata']  
    except:
        pass
    try:
        user_data['Source_Mumbai'] = test_data1['Source_Mumbai']  
    except:
        pass


    #destination
    try:
        user_data['Destination_Banglore'] = test_data1['Destination_Banglore']  
    except:
        pass

    try:
        user_data['Destination_Cochin'] = test_data1['Destination_Cochin']  
    except:
        pass

    try:
        user_data['Destination_Delhi'] = test_data1['Destination_Delhi']  
    except:
        pass

    try:
        user_data['Destination_Hyderabad'] = test_data1['Destination_Hyderabad']  
    except:
        pass

    try:
        user_data['Destination_Kolkata'] = test_data1['Destination_Kolkata']  
    except:
        pass

    try:
        user_data['Destination_New Delhi'] = test_data1['Destination_New Delhi']  
    except:
        pass


    #AdditionalInfo
    try:
        user_data['Additional_Info_1 Long layover'] = test_data1['Additional_Info_1 Long layover']  
    except:
        pass

    try:
        user_data['Additional_Info_1 Short layover'] = test_data1['Additional_Info_1 Short layover']  
    except:
        pass

    try:
        user_data['Additional_Info_2 Long layover'] = test_data1['Additional_Info_2 Long layover']  
    except:
        pass

    try:
        user_data['Additional_Info_Business class'] = test_data1['Additional_Info_Business class']  
    except:
        pass

    try:
        user_data['Additional_Info_Change airports'] = test_data1['Additional_Info_Change airports']  
    except:
        pass

    try:
        user_data['Additional_Info_In-flight meal not included'] = test_data1['Additional_Info_In-flight meal not included']  
    except:
        pass

    try:
        user_data['Additional_Info_No Info'] = test_data1['Additional_Info_No Info']  
    except:
        pass

    try:
        user_data['Additional_Info_No check-in baggage included'] = test_data1['Additional_Info_No check-in baggage included']  
    except:
        pass

    try:
        user_data['Additional_Info_Red-eye flight'] = test_data1['Additional_Info_Red-eye flight']  
    except:
        pass

    user_data.replace(np.nan, 0, inplace=True)
        
        
    test_data3 = test_data.copy()
#creating series of data for airline chart
    for _ in range(len(raw_df['Airline'].unique())-1):
        new_row = pd.DataFrame()
        new_row = pd.DataFrame(test_data3.iloc[0]).transpose()
        #new_row = new_row.transpose()
        test_data3 = pd.concat([test_data3, new_row], axis=0, ignore_index=True)
    test_data3['Airline'] = raw_df['Airline'].unique()
    index_data = test_data3['Airline']
    
    test_data3['Total_Stops']=test_data3['Total_Stops'].astype(int)
    import datetime as dt
    #test_data2['Date_of_Journey'] = pd.to_datetime(test_data2['Date_of_Journey'])
    test_data3['Date_of_Journey']=test_data3['Date_of_Journey'].map(dt.datetime.toordinal)

    test_data3['Dep_Time'] = pd.to_datetime(test_data3['Dep_Time'], format='%H:%M:%S')
    test_data3['Dep_Time']=test_data3['Dep_Time'].dt.strftime('%H%M%S').astype(int)

    test_data2 = pd.get_dummies(test_data3, dtype=int)
    
    user_data2 = pd.DataFrame(columns=['Date_of_Journey', 'Dep_Time', 'Total_Stops', 'Airline_Air Asia',
        'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
        'Airline_Jet Airways', 'Airline_Jet Airways Business',
        'Airline_Multiple carriers',
        'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
        'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
        'Source_Banglore', 'Source_Chennai', 'Source_Delhi', 'Source_Kolkata',
        'Source_Mumbai', 'Destination_Banglore', 'Destination_Cochin',
        'Destination_Delhi', 'Destination_Hyderabad', 'Destination_Kolkata',
        'Destination_New Delhi', 'Additional_Info_1 Long layover',
        'Additional_Info_1 Short layover', 'Additional_Info_2 Long layover',
        'Additional_Info_Business class', 'Additional_Info_Change airports',
        'Additional_Info_In-flight meal not included',
        'Additional_Info_No Info',
        'Additional_Info_No check-in baggage included',
        'Additional_Info_Red-eye flight'])
    user_data2['Date_of_Journey'] = test_data2['Date_of_Journey']
    user_data2['Dep_Time'] = test_data2['Dep_Time']
    user_data2['Total_Stops'] = test_data2['Total_Stops']
    #airline
    try:
        user_data2['Airline_Air Asia'] = test_data2['Airline_Air Asia']  
    except:
        pass
    try:
        user_data2['Airline_Air India'] = test_data2['Airline_Air India']
    except:
        pass
    try:
        user_data2['Airline_GoAir'] = test_data2['Airline_GoAir']
    except:
        pass
    try:
        user_data2['Airline_IndiGo'] = test_data2['Airline_IndiGo']
    except:
        pass
    try:
        user_data2['Airline_Jet Airways'] = test_data2['Airline_Jet Airways']
    except:
        pass
    try:
        user_data2['Airline_Jet Airways Business'] = test_data2['Airline_Jet Airways Business']
    except:
        pass
    try:
        user_data2['Airline_Multiple carriers'] = test_data2['Airline_Multiple carriers']
    except:
        pass
    try:
        user_data2['Airline_Multiple carriers Premium economy'] = test_data2['Airline_Multiple carriers Premium economy']
    except:
        pass
    try:
        user_data2['Airline_SpiceJet'] = test_data2['Airline_SpiceJet']
    except:
        pass
    try:
        user_data2['Airline_Trujet'] = test_data2['Airline_Trujet']
    except:
        pass
    try:
        user_data2['Airline_Vistara'] = test_data2['Airline_Vistara']
    except:
        pass
    try:
        user_data2['Airline_Vistara Premium economy'] = test_data2['Airline_Vistara Premium economy']
    except:
        pass

    #source
    try:
        user_data2['Source_Banglore'] = test_data2['Source_Banglore']  
    except:
        pass
    try:
        user_data2['Source_Chennai'] = test_data2['Source_Chennai']  
    except:
        pass
    try:
        user_data2['Source_Delhi'] = test_data2['Source_Delhi']  
    except:
        pass
    try:
        user_data2['Source_Kolkata'] = test_data2['Source_Kolkata']  
    except:
        pass
    try:
        user_data2['Source_Mumbai'] = test_data2['Source_Mumbai']  
    except:
        pass


    #destination
    try:
        user_data2['Destination_Banglore'] = test_data2['Destination_Banglore']  
    except:
        pass

    try:
        user_data2['Destination_Cochin'] = test_data2['Destination_Cochin']  
    except:
        pass

    try:
        user_data2['Destination_Delhi'] = test_data2['Destination_Delhi']  
    except:
        pass

    try:
        user_data2['Destination_Hyderabad'] = test_data2['Destination_Hyderabad']  
    except:
        pass

    try:
        user_data2['Destination_Kolkata'] = test_data2['Destination_Kolkata']  
    except:
        pass

    try:
        user_data2['Destination_New Delhi'] = test_data2['Destination_New Delhi']  
    except:
        pass


    #AdditionalInfo
    try:
        user_data2['Additional_Info_1 Long layover'] = test_data2['Additional_Info_1 Long layover']  
    except:
        pass

    try:
        user_data2['Additional_Info_1 Short layover'] = test_data2['Additional_Info_1 Short layover']  
    except:
        pass

    try:
        user_data2['Additional_Info_2 Long layover'] = test_data2['Additional_Info_2 Long layover']  
    except:
        pass

    try:
        user_data2['Additional_Info_Business class'] = test_data2['Additional_Info_Business class']  
    except:
        pass

    try:
        user_data2['Additional_Info_Change airports'] = test_data2['Additional_Info_Change airports']  
    except:
        pass

    try:
        user_data2['Additional_Info_In-flight meal not included'] = test_data2['Additional_Info_In-flight meal not included']  
    except:
        pass

    try:
        user_data2['Additional_Info_No Info'] = test_data2['Additional_Info_No Info']  
    except:
        pass

    try:
        user_data2['Additional_Info_No check-in baggage included'] = test_data2['Additional_Info_No check-in baggage included']  
    except:
        pass

    try:
        user_data2['Additional_Info_Red-eye flight'] = test_data2['Additional_Info_Red-eye flight']  
    except:
        pass

    user_data2.replace(np.nan, 0, inplace=True)
        





    import mlflow
    import mlflow.pyfunc

    mlflow.set_tracking_uri("http://localhost:5000")

    model_name = 'GradientBoostRegressor'
    model_version = None
    #run_id = '573526c958204d5cbc2be8a60aaf38f4'

    prediction_model = mlflow.pyfunc.load_model(model_uri=f'models:/{model_name}/{model_version}')


    predicted_price_date = prediction_model.predict(user_data)
    st.write("Predicted Price", predicted_price_date[0])

    st.line_chart(predicted_price_date)
    
    predicted_price_flight = prediction_model.predict(user_data2)
    
    flight_rate_df = pd.DataFrame(predicted_price_flight, index_data)
    flight_rate_df = flight_rate_df.reset_index()
    flight_rate_df = flight_rate_df.rename(columns = {0: 'Price'})
    #st.write(flight_rate_df)
    st.bar_chart(flight_rate_df, x = 'Airline', y = 'Price')   
    
    
    
    
