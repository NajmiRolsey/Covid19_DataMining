import streamlit as st 
import numpy as np
import pandas as pd
import altair as alt 
from streamlit_folium import folium_static
import folium
from bokeh.plotting import figure
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

cases_malaysia = pd.read_csv('cases_malaysia.csv')
cases_malaysia['date'] = pd.to_datetime(cases_malaysia['date'],errors = 'coerce')
tests_malaysia = pd.read_csv('tests_malaysia.csv')
cases_2020 = pd.read_csv('cases_2020.csv')
cases_2021 = pd.read_csv('cases_2021.csv')
finalDf = pd.read_csv('finalDf.csv',index_col=0)

cases_state = pd.read_csv('cases_state.csv')

corelation = pd.read_csv('corelation_q2.csv',index_col=0)

Johor_Boruta = pd.read_csv('Boruta/Johor_Boruta.csv')
Pahang_Boruta = pd.read_csv('Boruta/Pahang_Boruta.csv')
Kedah_Boruta = pd.read_csv('Boruta/Kedah_Boruta.csv')
Selangor_Boruta = pd.read_csv('Boruta/Selangor_Boruta.csv')

Pahang_Boruta = Pahang_Boruta[['Features','Score']]
Johor_Boruta = Johor_Boruta[['Features','Score']]
Kedah_Boruta = Kedah_Boruta[['Features','Score']]
Selangor_Boruta = Selangor_Boruta[['Features','Score']]

rfe_Johor = pd.read_csv('rfe/rfe_Johor.csv')
rfe_Pahang = pd.read_csv('rfe/rfe_Pahang.csv')
rfe_Kedah = pd.read_csv('rfe/rfe_Kedah.csv')
rfe_Selangor = pd.read_csv('rfe/rfe_Selangor.csv')

rfe_Johor = rfe_Johor[['Features','Score']]
rfe_Pahang = rfe_Pahang[['Features','Score']]
rfe_Kedah = rfe_Kedah[['Features','Score']]
rfe_Selangor = rfe_Selangor[['Features','Score']]

regres_Johor = pd.read_csv('regression/johor_regression_score.csv')
regres_Kedah = pd.read_csv('regression/kedah_regression_score.csv')
regres_Pahang = pd.read_csv('regression/pahang_regression_score.csv')
regres_Selangor = pd.read_csv('regression/selangor_regression_score.csv')

class_Johor = pd.read_csv('classification/johor_class.csv')
class_Kedah = pd.read_csv('classification/kedah_class.csv')
class_Pahang = pd.read_csv('classification/pahang_class.csv')
class_Selangor = pd.read_csv('classification/selangor_class.csv')

class_Johor = class_Johor[['Classification Method','Accuracy']]
class_Kedah = class_Kedah[['Classification Method','Accuracy']]
class_Pahang = class_Pahang[['Classification Method','Accuracy']]
class_Selangor = class_Selangor[['Classification Method','Accuracy']]


states = ['Johor','Melaka','Perak','Pulau Pinang', 'Perlis', 'Kedah', 'Kelantan', 'Pahang', 'Terengganu', 'Sabah', 'Sarawak', 'Negeri Sembilan', 'Selangor', 'W.P. Kuala Lumpur', 'W.P. Labuan', 'W.P. Putrajaya']


page_header="""
<div style="background-color:#2E90FF;padding:1.5px">
<h1 style="color:while;text-align:center;">Covid 19 Analysis</h1>
</div><br>
"""

st.markdown(page_header, unsafe_allow_html=True)
st.subheader("Made by:")
st.subheader("Adam (1181101799)")
st.subheader("Yasmin (1181100452)")
st.subheader("Najmi (1181100589)")

page_names = ['Exploratory Data Analysis Q1','Corelation Analysis Q2','Feature Selection Q3', 'Model Training and Evaluation Q4']
#page = st.radio('Page Navigation',page_names, index = 0)

page = st.sidebar.radio(
    'Page Selection',
     page_names)

#============================================================================================================================================
# EDA
if (page == 'Exploratory Data Analysis Q1'):
    st.title('Exploratory Data Analysis')

    st.header('1) What is the trend of new covid 19 cases compared to the trend of recovered cases')
    st.subheader("Covid 19 trends in states")
    # CASES AND RECOVERED CASES
    linePlot = figure(
        title = 'New cases Against Date',
        x_axis_label = 'Date',
        y_axis_label = 'New cases'
    )

    linePlot.line(cases_malaysia['date'],cases_malaysia['cases_new'],legend_label='new cases', line_width=2,color = '#F32B2B')
    linePlot.line(cases_malaysia['date'],cases_malaysia['cases_recovered'],legend_label='recovered', line_width=2,color = '#24E45B')
    st.bokeh_chart(linePlot, use_container_width=True)
    
    st.write('From the chart above we can conclude that the trend for the covid 19 new cases has a similar distribution to the trend of recovered cases from January 2020 to September 2021')
    # CASES FOR EACH STATE
    
    st.header('2) What is the cases trend for all the individual states?')

    left_column, right_column = st.columns(2)

    with left_column:
        state_selection = st.selectbox("Select Your Desired State",states)

    if (state_selection == 'Johor'):

        tempDf = cases_state[cases_state['state'] == 'Johor']
        #df = px.data.gapminder().query("cases_state[cases_state['state'] == 'Johor']")
        fig = px.line(tempDf, x="date", y="cases_new", title='case trends in Johor')
        st.plotly_chart(fig, use_container_width=True)

    elif (state_selection == 'Melaka'):
        tempDf = cases_state[cases_state['state'] == 'Melaka']
        fig = px.line(tempDf, x="date", y="cases_new", title='case trends in Melaka')
        st.plotly_chart(fig, use_container_width=True)

    elif (state_selection == 'Terengganu'):
        tempDf = cases_state[cases_state['state'] == 'Terengganu']
        fig = px.line(tempDf, x="date", y="cases_new", title='case trends in Terengganu')
        st.plotly_chart(fig, use_container_width=True)

    elif (state_selection == 'Pulau Pinang'):
        tempDf = cases_state[cases_state['state'] == 'Pulau Pinang']
        fig = px.line(tempDf, x="date", y="cases_new", title='case trends in Pulau Pinang')
        st.plotly_chart(fig, use_container_width=True)

    elif (state_selection == 'Perak'):
        tempDf = cases_state[cases_state['state'] == 'Perak']
        fig = px.line(tempDf, x="date", y="cases_new", title='case trends in Perak')
        st.plotly_chart(fig, use_container_width=True)

    elif (state_selection == 'Kedah'):
        tempDf = cases_state[cases_state['state'] == 'Kedah']
        fig = px.line(tempDf, x="date", y="cases_new", title='case trends in Kedah')
        st.plotly_chart(fig, use_container_width=True)

    elif (state_selection == 'Perlis'):
        tempDf = cases_state[cases_state['state'] == 'Perlis']
        fig = px.line(tempDf, x="date", y="cases_new", title='case trends in Perlis')
        st.plotly_chart(fig, use_container_width=True)

    elif (state_selection == 'Kelantan'):
        tempDf = cases_state[cases_state['state'] == 'Kelantan']
        fig = px.line(tempDf, x="date", y="cases_new", title='case trends in Kelantan')
        st.plotly_chart(fig, use_container_width=True)

    elif (state_selection == 'Negeri Sembilan'):
        tempDf = cases_state[cases_state['state'] == 'Negeri Sembilan']
        fig = px.line(tempDf, x="date", y="cases_new", title='case trends in Negeri Sembilan')
        st.plotly_chart(fig, use_container_width=True)

    elif (state_selection == 'Pahang'):
        tempDf = cases_state[cases_state['state'] == 'Pahang']
        fig = px.line(tempDf, x="date", y="cases_new", title='case trends in Pahang')
        st.plotly_chart(fig, use_container_width=True)

    elif (state_selection == 'Sabah'):
        tempDf = cases_state[cases_state['state'] == 'Sabah']
        fig = px.line(tempDf, x="date", y="cases_new", title='case trends in Sabah')
        st.plotly_chart(fig, use_container_width=True)

    elif (state_selection == 'Sarawak'):
        tempDf = cases_state[cases_state['state'] == 'Sarawak']
        fig = px.line(tempDf, x="date", y="cases_new", title='case trends in Sarawak')
        st.plotly_chart(fig, use_container_width=True)

    elif (state_selection == 'Selangor'):
        tempDf = cases_state[cases_state['state'] == 'Selangor']
        fig = px.line(tempDf, x="date", y="cases_new", title='case trends in Selangor')
        st.plotly_chart(fig, use_container_width=True)

    elif (state_selection == 'W.P. Kuala Lumpur'):
        tempDf = cases_state[cases_state['state'] == 'W.P. Kuala Lumpur']
        fig = px.line(tempDf, x="date", y="cases_new", title='case trends in Kuala Lumpur')
        st.plotly_chart(fig, use_container_width=True)

    elif (state_selection == 'W.P. Labuan'):
        tempDf = cases_state[cases_state['state'] == 'W.P. Labuan']
        fig = px.line(tempDf, x="date", y="cases_new", title='case trends in Labuan')
        st.plotly_chart(fig, use_container_width=True)

    elif (state_selection == 'W.P. Putrajaya'):
        tempDf = cases_state[cases_state['state'] == 'W.P. Putrajaya']
        fig = px.line(tempDf, x="date", y="cases_new", title='case trends in Putrajaya')
        st.plotly_chart(fig, use_container_width=True)

    
    # TEST DONE AND NEW CASES
    st.header('3) Does the trend of the number of tests conducted follow the trend of the number of positive covid 19 cases?')

    fig = px.line(tests_malaysia, x='date', y=['pcr', 'rtk-ag'], title='number of tests done and new cases per day')
    fig.add_scatter(x=cases_malaysia['date'], y=cases_malaysia['cases_new'],name="new cases")
    st.plotly_chart(fig, use_container_width=True)

    st.write('The trend of the tests does follow closely the trend for the number of new cases. From this data the daily positivity rate can also be calculated. As such we have calculated the daily positivity rate to aid in model training. The positivity rate is calculated using the following fomula:')

    st.subheader('PR = NC / PCR + RTK-AG')
    st.write('PR = Positivity Rate')
    st.write('NC = New cases for that day')
    st.write('PCR = Number of PCR tests held on that day')
    st.write('RTK-AG = Number of RTK-AG tests held on that day')

    #CASES BY MONTH FOR EACH YEAR
    st.header('4) What is the trend of the covid 19 cases per month?')

    fig = px.bar(cases_2020, x='month', y='cases_new', color='cases_import', title='distribution of cases by month in 2020')
    st.plotly_chart(fig, use_container_width=True)

    fig = px.bar(cases_2021, x='month', y='cases_new', color='cases_import', title='distribution of cases by month in 2021')
    st.plotly_chart(fig, use_container_width=True)

    st.header("5) Combining the datasets for model training")

    finalDf

    st.write("To form our final training dataset we decided to merge together the tests_malaysia, cases_malaysia and cases_state dataset to form the final dataset as seen above. Our dataset consists of data from Malaysia as a whole as well as data for each state. Furthermore we also calculated the number of active cases for both Malaysia and each of the states. Moreover we calculated the daily positivity rate to add to our features. The number of active cases is a cumulative value calculated using the following formula:")
    st.subheader('AC = CU + NC - RC')
    st.write("AC = active cases")
    st.write("CU = Cumulative active cases. The initial value of CU is 0 at the begining of the pandemic and is added to everyday")
    st.write("NC = Number of New daily cases")
    st.write("RC = Number of recovery cases")

#============================================================================================================================================
# Corelation
elif (page == 'Corelation Analysis Q2'):
    st.title('Corelation Analysis')

    fig, ax = plt.subplots()
    sns.heatmap(corelation, ax=ax,annot = True)
    st.write(fig)

    st.write("The heatmap above plots out the pearson correlation between the number of cases for each states. Based on the findings we conclude that the states are strongly correlated if they have a pearson correlation coeficient of 0.8 or greater. ")

    st.write('So from this the states that show strong correlation with Pahang are Kedah, Pulau Pinang, Kelantan, Perak, Terengganu, Melaka, Johor, Sabah and Selangor. ')

    st.write('On the other hand the states that show strong correlation with Johor are Perlis, Kedah, Pulau Pinang, Kelantan, Perak, Terengganu, Sabah, Sarawak, Pahang and Labuan')
#============================================================================================================================================
#Feature Selection
elif (page == 'Feature Selection Q3'):
    st.title('Feature Selection')

    states = ['Johor', 'Kedah','Selangor','Pahang']
    state_option = st.radio('State Selection',states, index = 0)

    if (state_option == 'Johor'):
        left_column, right_column = st.columns(2)

        with left_column:
            st.subheader("Boruta Feature Selection")
            Johor_Boruta

        with right_column:
            st.subheader("RFE Feature Selection")
            rfe_Johor
    
        st.write('For the corelation analysis we will be using the features selected by Boruta. This is because Boruta is considered as the industry standard when it comes to feature selection. To select our features we use a threshold of 0.5 and we will be using all features that has a correlation of 0.5 or higher for each of the 4 states.')
        st.write('For predicting the johor cases we will be using new_cases_Negeri Sembilan, active_case_Negeri Sembilan, rtk-ag, active_case_W.P. Kuala Lumpur, new_cases_W.P. Kuala Lumpur, cases_recovered, pcr, new_cases_Sabah, new_cases_Pahang, active_cases, active_case_W.P. Labuan, active_case_Kedah, active_case_Pahang, new_cases_Sarawak, active_case_Selangor, active_case_Kelantan, active_case_Sabah, new_cases_Kedah, new_cases_Melaka, new_cases_Pulau Pinang')

    elif (state_option == 'Kedah'):
        left_column, right_column = st.columns(2)

        with left_column:
            st.subheader("Boruta Feature Selection")
            Kedah_Boruta
            
        with right_column:
            st.subheader("RFE Feature Selection")
            rfe_Kedah

        st.write('For the corelation analysis we will be using the features selected by Boruta. This is because Boruta is considered as the industry standard when it comes to feature selection. To select our features we use a threshold of 0.5 and we will be using all features that has a correlation of 0.5 or higher for each of the 4 states.')
        st.write('For predicting the kedah cases we will be using active_case_W.P. Labuan, cases_recovered, active_cases, active_case_W.P. Kuala Lumpur, active_case_Kelantan, active_case_Melaka, rtk-ag, new_cases_Melaka, active_case_Pahang, active_case_Johor, new_cases_Pahang, new_cases_W.P. Kuala Lumpur, new_cases_Negeri Sembilan, new_cases_Kelantan, pcr, new_cases_W.P. Putrajaya, active_case_Sabah, new_cases_Johor, active_case_Negeri Sembilan, cases_new, active_case_Kedah, new_cases_Selangor, new_cases_Terengganu ')


    elif (state_option == 'Selangor'):
        left_column, right_column = st.columns(2)

        with left_column:
            st.subheader("Boruta Feature Selection")
            Selangor_Boruta
            
        with right_column:
            st.subheader("RFE Feature Selection")
            rfe_Selangor

        st.write('For the corelation analysis we will be using the features selected by Boruta. This is because Boruta is considered as the industry standard when it comes to feature selection. To select our features we use a threshold of 0.5 and we will be using all features that has a correlation of 0.5 or higher for each of the 4 states.')
        st.write('For predicting the selangor cases we will be using  new_cases_Negeri Sembilan, active_case_Negeri Sembilan, active_case_W.P. Labuan, new_cases_W.P. Labuan, rtk-ag, new_cases_Melaka, active_case_W.P. Putrajaya, new_cases_Selangor, new_cases_W.P. Putrajaya, active_cases, active_case_Melaka, cases_new, new_cases_Kelantan, active_case_Sabah, cases_import, new_cases_W.P. Kuala Lumpur, new_cases_Pahang, pcr active_case_Selangor, active_case_Kedah')

    elif (state_option == 'Pahang'):
        left_column, right_column = st.columns(2)

        with left_column:
            st.subheader("Boruta Feature Selection")
            Pahang_Boruta
            
        with right_column:
            st.subheader("RFE Feature Selection")
            rfe_Pahang

        st.write('For the corelation analysis we will be using the features selected by Boruta. This is because Boruta is considered as the industry standard when it comes to feature selection. To select our features we use a threshold of 0.5 and we will be using all features that has a correlation of 0.5 or higher for each of the 4 states.')
        st.write('For predicting the pahang cases we will be using  rtk-ag, new_cases_Melaka, new_cases_Negeri Sembilan, active_case_Melaka, active_case_Negeri Sembilan, active_case_W.P. Kuala Lumpur, new_cases_W.P. Putrajaya, new_cases_W.P. Kuala Lumpur, cases_import, new_cases_Selangor, active_case_W.P. Putrajaya, pcr, active_cases, new_cases_W.P. Labuan, active_case_Kedah, active_case_Selangor, new_cases_Terengganu, active_case_Perak, active_case_Sabah, new_cases_Kedah, active_case_Johor ')

    
#============================================================================================================================================
# Model training
elif (page == 'Model Training and Evaluation Q4'):
    st.title('Model Training and Evaluation')

    left,right = st.columns(2)

    with left:
        classify = st.button("Classification Algorithms")

    with right:
        regress = st.button("Regression Algorithms")
    
    if(classify):
        st.header('Classification')

        left_column, right_column = st.columns(2)

        with left_column:
            st.subheader("Johor")
            class_Johor
        with right_column:
            st.subheader("Pahang")
            class_Pahang

        left_column2, right_column2 = st.columns(2)

        with left_column2:
            st.subheader("Selangor")
            class_Selangor

        with right_column2:
            st.subheader("Kedah")
            class_Kedah
        
        imageClasify = Image.open('AccuracyComparison.jpg')
        st.image(imageClasify)
 
        

        st.header('Johor')
        st.write('We find that the data accuracy collected is also low due to continuous data based on the training and testing process in Johor. The highest accuracy score in Johor was obtained using the KNN-Classification and the Support Vector Machine, both of which had a similar score of 0.215470. Furthermore, with a score of 0.200000, the Logistic Regression is the second best classification approach. The CART Classification Tree, which has a score of 0.198895, is the third approach. Finally, the Naive Bayes algorithm has a score of 0.182320. Based on the data collected in Johor, we can conclude that the KNN and SVM Techniques will be used as classification techniques in the future.')
        
        st.header('Pahang')
        st.write("The Data Accuracy results from Pahang's training and testing process are quite low. This is due to the fact that data is updated on a regular basis. However, we were able to observe and determine which of the five classification methods was the most effective. To begin, the KNN-Classification yielded the highest accuracy score in Pahang, with a value of 0.348066. In addition, with a score of 0.337017, the Naive Bayes Approach is the second best classification method. Now well look at the third approach, Logistic Regression, which has a score of 0.330000. The Support Vector Machine (SVM) comes in second with a score of 0.320442. The CART Classification Tree comes in third with a score of 0.309392. Based on the findings in Pahang, the KNN and Naive Bayes Classification Techniques have been chosen as the classification technique for future use.")

        st.header('Selangor')
        st.write('Furthermore, the next accuracy assessment will be held in Selangor. With a rating of 0.127072, the KNN technique gets the highest accuracy score in Selangor. Furthermore, the SVM and Naive Bayes have a similar score of 0.099448. With a score of 0.088398, the CART Classification Tree comes in third. The Logistic Regression comes in last with a score of 0.070000.  Based on the data collected in Selangor, we may conclude that the KNN and Naive Bayes Approaches will be used as classification techniques in the future.')

        st.header('Kedah')
        st.write('The accuracy testing will take place in Kedah next. The Logistic Regression has the greatest accuracy score in Kedah, with a value of 0.230000. Furthermore, with a score of 0.226519, the KNN - Classification is the second best classification method. The Support Vector Machine (SVM) comes in second with a score of 0.220994. With a score of 0.193370, the CART Classification Treee takes fourth place. Finally, the score of the Naive Bayes method is 0.127072. We may deduce that Logistic Regression and KNN will be employed as classification techniques in the future based on the data obtained in Kedah.')
    
#============================================================================================================================================

    if (regress):

        st.header('Regression')

        left_column, right_column = st.columns(2)

        with left_column:
            st.subheader("Johor")
            regres_Johor

        with right_column:
            st.subheader("Pahang")
            regres_Pahang

        left_column2, right_column2 = st.columns(2)

        with left_column2:
            st.subheader("Selangor")
            regres_Selangor

        with right_column2:
            st.subheader("Kedah")
            regres_Kedah

        imageRegres_R2 = Image.open('Regression_R2.jpg')
        st.image(imageRegres_R2)


        st.header('Johor')
        st.write('For Johor, Linear Regression and KNN Regressor show the best performance out of all four regression models used with an R2 score of 0.9559 and 0.9717 as well as a MAE score of 68.159 and 46.2479 respectively. However, Regressor Tree performed with an R2 score of 0.9476 and a MAE score of 67.1815 and came third in the list. Support Vector Regression (SVR) performed the worst with an R2 score of -0.0243 and a high MAE score of 237.6816 Therefore, only Linear Regression and KNN Regressor were chosen as the models to predict the upcoming cases for Johor')

        st.header('Pahang')
        st.write('For Pahang, Linear Regression and KNN Regressor show the best performance out of all four regression models used with an R2 score of 0.9327 and 0.9482 as well as a MAE score of 27.0322 and 20.1157 respectively. Whereas, Regressor Tree performed with an R2 score of 0.9074 and a MAE score of 33.146 and came third in the list. Support Vector Regression (SVR) performed the worst with an R2 score of only 0.1790 and a high MAE score of 70.0778. Therefore, only Linear Regression and KNN Regressor were chosen as the models to predict the upcoming cases for Pahang ')

        st.header('Selangor')
        st.write('For Selangor, Linear Regression and KNN Regressor show the best performance out of all four regression models used with an R2 score of 0.9603 and 0.9884 as well as a MAE score of 199.6772 and 104.4835 respectively. However, Regressor Tree performed with an R2 score of 0.9595 and a MAE score of 200.2371 and came third in the list. Support Vector Regression (SVR) performed the worst with an R2 score of -0.1740 and a high MAE score of 966.4661. Therefore, only Linear Regression and KNN Regressor were chosen as the models to predict the upcoming cases for Johor')

        st.header('Kedah')
        st.write('For Kedah, KNN Regressor and Regressor Tree show the best performance out of all four regression models used with an R2 score of 0.9676 and 0.9582 as well as a MAE score of 33.7479 and 43.7335 respectively. However, Linear Regression performed with an R2 score of 0.9514 and a MAE score of 45.1151 and came third in the list. Support Vector Regression (SVR) performed the worst with an R2 score of only 0.0011 and a high MAE score of 177.5771. Therefore, only KNN Regressor and Regressor Tree  were chosen as the models to predict the upcoming cases for Kedah')

        st.header('Regression ConClusion')
        st.write('KNN Regressor was chosen as one of the models for Pahang, Johor, Kedah and Selangor whereas Linear Regression was chosen as the other model for Pahang, Johor and Selamgor. Support Vector Regression performed the worst in all four states and Regressor Tree performs well but always comes third to Linear Regression and KNN Regressor except for Kedah where it performed better than Linear Regression.')

        
#============================================================================================================================================









