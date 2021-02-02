# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:01:00 2021

@author: Juan Sebastian
"""

import pandas as pd
import streamlit as st
import numpy as np
import pickle

st.write('''
         
         Author: **Juan Sebastian Roa**
         
         GitHub Profile: https://github.com/jsroa15
         
         ''')


st.title('Churn Prediction App')

st.write("Please fill out the User Input Parameters on the left")

st.write(''' 
         ## **Model Used: Random Forest Classifier**
         ''')

#####Capturing Features from App user#####

st.sidebar.header('User Input Parameters')

def user_input_features():
    
    
    #Scaled feature: I have to use mean and std fit in the StandarScaler
    
    cons_12m=st.sidebar.slider('cons_12m',0,1000,0)
    cons_12m=np.log1p(cons_12m)
    
    cons_gas_12m=st.sidebar.slider('cons_gas_12m',0,1000,0)
    cons_gas_12m=np.log1p(cons_gas_12m)
    
    cons_last_month=st.sidebar.slider('cons_last_month',0,1000,0)
    cons_last_month=np.log1p(cons_last_month)
    
    forecast_cons_12m=st.sidebar.slider('forecast_cons_12m',0,1000,0)
    forecast_cons_12m=np.log1p(forecast_cons_12m)
    
    forecast_cons_year=st.sidebar.slider('forecast_cons_year',0,1000,0)
    forecast_cons_year=np.log1p(forecast_cons_year)
    
    forecast_discount_energy=st.sidebar.slider('forecast_discount_energy',0,1000,0)
    
    forecast_meter_rent_12m=st.sidebar.slider('forecast_meter_rent_12m',0,1000,0)
    
    forecast_price_energy_p1=st.sidebar.slider('forecast_price_energy_p1',0,1000,0)
    
    forecast_price_pow_p1=st.sidebar.slider('forecast_price_pow_p1',0,1000,0)
    forecast_price_pow_p1=np.log1p(forecast_price_pow_p1)
    
    imp_cons=st.sidebar.slider('imp_cons',0,1000,0)
    imp_cons=np.log1p(imp_cons)
    
    margin_gross_pow_ele=st.sidebar.slider('margin_gross_pow_ele',-1000,1000,0)
    
    margin_net_pow_ele=st.sidebar.slider('margin_net_pow_ele',-1000,1000,0)
    
    nb_prod_act=st.sidebar.slider('nb_prod_act',0,1000,0)
    
    net_margin=st.sidebar.slider('net_margin',-1000,1000,0)
    
    num_years_antig=st.sidebar.slider('num_years_antig',0,1000,0)
    
    pow_max=st.sidebar.slider('pow_max',0,1000,0)
    
    years_end=st.sidebar.slider('years_end',0,1000,0)
    years_end=np.log1p(years_end)
    
    years_mod=st.sidebar.slider('years_mod',0,1000,0)
    
    tenure=st.sidebar.slider('tenure',0,1000,0)
    
    total_cons=st.sidebar.slider('total_cons',0,1000,0)
    total_cons=np.log1p(total_cons)
    
    avg_fct_ene=st.sidebar.slider('avg_fct_ene',0,1000,0)
    
    avg_fct_pow=st.sidebar.slider('avg_fct_pow',0,1000,0)
    
    
    channel_sales=st.sidebar.selectbox('channel_sales',(1,2,3,4,5,6,'Other'))
    
    if channel_sales=='1':
        
        channel_sales_1=0 
        channel_sales_2=0
        channel_sales_3=0
        channel_sales_ot=0
        channel_sales_4=0
        channel_sales_5=0
        
    
    elif channel_sales=='2':
        channel_sales_1=1 
        channel_sales_2=0
        channel_sales_3=0
        channel_sales_ot=0
        channel_sales_4=0
        channel_sales_5=0
    
    elif channel_sales=='3':
        channel_sales_1=0 
        channel_sales_2=1
        channel_sales_3=0
        channel_sales_ot=0
        channel_sales_4=0
        channel_sales_5=0
        
    elif channel_sales=='4':
        channel_sales_1=0
        channel_sales_2=0
        channel_sales_3=1
        channel_sales_ot=0
        channel_sales_4=0
        channel_sales_5=0
        
    elif channel_sales=='5':
        channel_sales_1=0
        channel_sales_2=0
        channel_sales_3=0
        channel_sales_ot=0
        channel_sales_4=1
        channel_sales_5=0
    
    elif channel_sales=='6':
        channel_sales_1=0
        channel_sales_2=0
        channel_sales_3=0
        channel_sales_ot=0
        channel_sales_4=0
        channel_sales_5=1
    
        
    else:
        channel_sales_1=0
        channel_sales_2=0
        channel_sales_3=0
        channel_sales_ot=1
        channel_sales_4=0
        channel_sales_5=0
    
    has_gas_t=st.sidebar.selectbox('has_gas',('True','False'))
    if has_gas_t=='True':
        has_gas_t=1
    else:
        has_gas_t=0
    
    origin=st.sidebar.selectbox('Origin',(1,2,3,4,5))
    
    if origin=='1':
        
        origin_up_kamkkxfxxuwbdslkwifmmcsiusiuosws=0 
        origin_up_ldkssxwpmemidmecebumciepifcamkci=0
        origin_up_lxidpiddsbxsbosboudacockeimpuepw=0
        origin_up_usapbepcfoloekilkwsdiboslwaxobdp=0
        
    elif channel_sales=='2':
        
        origin_up_kamkkxfxxuwbdslkwifmmcsiusiuosws=1 
        origin_up_ldkssxwpmemidmecebumciepifcamkci=0
        origin_up_lxidpiddsbxsbosboudacockeimpuepw=0
        origin_up_usapbepcfoloekilkwsdiboslwaxobdp=0

    elif channel_sales=='3':
        
        origin_up_kamkkxfxxuwbdslkwifmmcsiusiuosws=0
        origin_up_ldkssxwpmemidmecebumciepifcamkci=1
        origin_up_lxidpiddsbxsbosboudacockeimpuepw=0
        origin_up_usapbepcfoloekilkwsdiboslwaxobdp=0
        
    elif channel_sales=='4':
        
        origin_up_kamkkxfxxuwbdslkwifmmcsiusiuosws=0
        origin_up_ldkssxwpmemidmecebumciepifcamkci=0
        origin_up_lxidpiddsbxsbosboudacockeimpuepw=1
        origin_up_usapbepcfoloekilkwsdiboslwaxobdp=0
        
    else:
        
        origin_up_kamkkxfxxuwbdslkwifmmcsiusiuosws=0
        origin_up_ldkssxwpmemidmecebumciepifcamkci=0
        origin_up_lxidpiddsbxsbosboudacockeimpuepw=0
        origin_up_usapbepcfoloekilkwsdiboslwaxobdp=1
        
    
    quarter=st.sidebar.selectbox('Quarter transaction',('Q1','Q2','Q3','Q4'))
    
    if quarter=='Q1':
        
        date_end_qtr_Q2=0 
        date_end_qtr_Q3=0
        date_end_qtr_Q4=0
        
        
    elif channel_sales=='Q2':
        
        date_end_qtr_Q2=1 
        date_end_qtr_Q3=0
        date_end_qtr_Q4=0
        
    elif channel_sales=='Q3':
        
        date_end_qtr_Q2=0 
        date_end_qtr_Q3=1
        date_end_qtr_Q4=0
        
    else:
        
        date_end_qtr_Q2=0 
        date_end_qtr_Q3=0
        date_end_qtr_Q4=1
    
    data={
        'cons_12m':cons_12m, 
        'cons_gas_12m':cons_gas_12m,
        'cons_last_month':cons_last_month,
        'forecast_cons_12m':forecast_cons_12m,
        'forecast_cons_year':forecast_cons_year,
        'forecast_discount_energy':forecast_discount_energy,
        'forecast_meter_rent_12m':forecast_meter_rent_12m,
        'forecast_price_energy_p1':forecast_price_energy_p1,
        'forecast_price_pow_p1':forecast_price_pow_p1,
        'imp_cons':imp_cons,
        'margin_gross_pow_ele':margin_gross_pow_ele,
        'margin_net_pow_ele':margin_net_pow_ele,
        'nb_prod_act':nb_prod_act,
        'net_margin':net_margin,
        'num_years_antig':num_years_antig,
        'pow_max':pow_max,
        'years_end':years_end,
        'years_mod':years_mod,
        'tenure':tenure,
        'total_cons':total_cons,
        'avg_fct_ene':avg_fct_ene,
        'avg_fct_pow':avg_fct_pow,
        'channel_sales_ewpakwlliwisiwduibdlfmalxowmwpci':channel_sales_1,
        'channel_sales_foosdfpfkusacimwkcsosbicdxkicaua':channel_sales_2,
        'channel_sales_lmkebamcaaclubfxadlmueccxoimlema':channel_sales_3,
        'channel_sales_other':channel_sales_ot,
        'channel_sales_sddiedcslfslkckwlfkdpoeeailfpeds':channel_sales_4,
        'channel_sales_usilxuppasemubllopkaafesmlibmsdf':channel_sales_5,
        'has_gas_t':has_gas_t,
        'origin_up_kamkkxfxxuwbdslkwifmmcsiusiuosws':origin_up_kamkkxfxxuwbdslkwifmmcsiusiuosws,
        'origin_up_ldkssxwpmemidmecebumciepifcamkci':origin_up_ldkssxwpmemidmecebumciepifcamkci,
        'origin_up_lxidpiddsbxsbosboudacockeimpuepw':origin_up_lxidpiddsbxsbosboudacockeimpuepw,
        'origin_up_usapbepcfoloekilkwsdiboslwaxobdp':origin_up_usapbepcfoloekilkwsdiboslwaxobdp,
        'date_end_qtr_Q2':date_end_qtr_Q2,
        'date_end_qtr_Q3':date_end_qtr_Q3,
        'date_end_qtr_Q4':date_end_qtr_Q4,
       
        }
    
    features=pd.DataFrame(data,index=[0])
    return features




#Here I call the function to get a dataset with features entered by the app user

f=user_input_features()


#Loading the model into the script. I used pickle to save the model

pickle_in=open('model.pickle','rb')
model = pickle.load(pickle_in)

#Here I use sklearn API to use the model and make predictions

prediction=model.predict(f)

#Translating output


st.header('Final Prediction:')


if prediction==0:
    st.header('**User has Retention**')
else:
    st.subheader('**User has Churn!!**')
    
y_proba=model.predict_proba(f)[:,1]
st.subheader('**Probability**')
st.write(y_proba)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

