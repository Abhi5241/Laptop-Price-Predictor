import streamlit as st
import pickle
import numpy as np


pipe=pickle.load(open("pipe.pkl","rb"))
df=pickle.load(open("df.pkl","rb"))

st.title("Laptop Predictor")


company=st.selectbox("Brand",df["Company"].unique())
type=st.selectbox("Type",df["TypeName"].unique())
Ram=st.selectbox("Ram",df["Ram"].unique())
gpu=st.selectbox("GPU",df["Gpu"].unique())
os=st.selectbox("OS",df["OpSys"].unique())
weight=st.number_input("Weight")
touchscreen=st.selectbox("Touchscreen",["No","Yes"])
ips=st.selectbox("IPS",["No","Yes"])
screen_size=st.number_input("Screen Size")
resolution=st.selectbox("Screen Resolution",["1920x1080","1366x768","1600x900","3840x1800","3200x1800","2880x1800","2560x1600","2560x1440","2304x1440"])
cpu=st.selectbox("CPU",df["Cpu Brand"].unique())
hdd=st.selectbox("HDD",[0,128,256,512,1024,2048])
ssd=st.selectbox("SSD",[0,128,256,512,1024])
clockspeed=st.number_input("Clock Speed")

if st.button("Predict Price"):
    
    if touchscreen=="Yes":
        touchscreen=1
    else:
        touchscreen=0
    
    if ips=="Yes":
        ips=1
    else:
        ips=0
    x_res=int(resolution.split("x")[0])
    y_res=int(resolution.split("x")[1])
    ppi=((x_res**2)+(y_res**2))**0.5/screen_size
    query=np.array([company,type,Ram,gpu,os,weight,touchscreen,ips,ppi,cpu,clockspeed,hdd,ssd])
    query=query.reshape(1,13)
    st.title("The predicted price for this configuration is "+str(np.exp(pipe.predict(query))))