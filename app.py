import streamlit as st
import pickle
import streamlit.components.v1 as components

st.beta_set_page_config(page_title = "App", page_icon = ":wine_glass:")
rfc_model = pickle.load(open('rfc_model.pkl','rb'))
def classify(num):
    if num==1:
        st.success("Predicted Quality of the Red Wine: Good")
    else:
        st.warning("Predicted Quality of the Red Wine: Bad")
def main():
    st.title("Red Wine Quality Predictor")
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>

    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    right,center, left = st.beta_columns(3)
    fa = right.slider('Select the value of Fixed Acidity',4.0,16.0,10.7)
    va = right.slider('Select the value of Volatile Acidity',0.10,2.0,0.35)
    ca = right.slider('Select the value of Citric Acid',0.0,1.0,0.53)
    rs = right.slider('Select the value of Residual Sugar',0.0,16.0,2.61)
    ch = left.slider('Select the value of Chlorides',0.0,1.0,0.07)
    fsd = left.slider('Select the value of Free Sulphur Dioxide',0,75,5)
    tsd = left.slider('Select the value of Total Sulphur Dioxide',0,300,16)
    dn = center.slider('Select the value of Density',0.0,1.50,0.99)
    ph = center.slider('Select the value of pH',0.0,7.0,3.15)
    sp = center.slider('Select the value of Sulphates',0.0,2.0,0.65)
    al =center.slider('Select the value of Alcohol',0.0,15.0,10.92)
    inputs = [[fa, va, ca, rs, ch, fsd,tsd, dn, ph, sp, al]]
    classify(rfc_model.predict(inputs))
    html_link = """
    Made by <a href="https://vanshhhhh.github.io/" style="color:red">Vansh Sharma</a>
    """
    st.markdown(html_link, unsafe_allow_html=True)
if __name__ == "__main__":
    main()
