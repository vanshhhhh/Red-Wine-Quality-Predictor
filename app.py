import streamlit as st
import pickle
rfc_model = pickle.load(open('rfc_model.pkl','rb'))
def classify(num):
    if num==1:
        st.success("Predicted Quality of the Red Wine: Good")
    else:
        st.warning("Predicted Quality of the Red Wine: Bad")
def main():
    #st.title("Red Wine Quality Predictor")
    html_temp = """
    <div style='background-color:red ;padding:10px'>
    <h2 style='color:white;text-align:center;'>Red Wine Quality Predictor</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    fa = st.slider('Select the value of Fixed Acidity',4.0,16.0,10.7)
    va = st.slider('Select the value of Volatile Acidity',0.10,2.0,0.35)
    ca = st.slider('Select the value of Citric Acid',0.0,1.0,0.53)
    rs = st.slider('Select the value of Residual Sugar',0.0,16.0,2.61)
    ch = st.slider('Select the value of Chlorides',0.0,1.0,0.07)
    fsd = st.slider('Select the value of Free Sulphur Dioxide',0,75,5)
    tsd = st.slider('Select the value of Total Sulphur Dioxide',0,300,16)
    dn = st.slider('Select the value of Density',0.0,1.50,0.99)
    ph = st.slider('Select the value of pH',0.0,7.0,3.15)
    sp = st.slider('Select the value of Sulphates',0.0,2.0,0.65)
    al =st.slider('Select the value of Alcohol',0.0,15.0,10.92)
    inputs = [[fa, va, ca, rs, ch, fsd,tsd, dn, ph, sp, al]]
    classify(rfc_model.predict(inputs))
if __name__ == "__main__":
    main()
