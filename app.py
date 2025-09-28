import streamlit as st
import pandas as pd
import pickle
st.title("ipl Win predictor")

bat_team = ['Chennai Super Kings', 'Lucknow Super Giants', 'Rajasthan Royals',
       'Punjab Kings', 'Mumbai Indians', 'Kolkata Knight Riders',
       'Royal Challengers Bengaluru', 'Delhi Capitals',
       'Sunrisers Hyderabad', 'Gujarat Titans']
bow_team= ['Royal Challengers Bengaluru', 'Delhi Capitals',
       'Sunrisers Hyderabad', 'Mumbai Indians', 'Gujarat Titans',
       'Punjab Kings', 'Chennai Super Kings', 'Kolkata Knight Riders',
       'Rajasthan Royals', 'Lucknow Super Giants']

citys= ['Chandigarh', 'Lucknow', 'Mumbai', 'Ahmedabad', 'Bengaluru',
       'Hyderabad', 'Chennai', 'Delhi', 'Indore', 'Bangalore', 'Jaipur',
       'Dharamsala', 'Dubai', 'Kolkata', 'Sharjah', 'Cuttack', 'Pune',
       'Abu Dhabi', 'Nagpur', 'Mohali', 'Ranchi', 'Visakhapatnam',
       'Raipur', 'Navi Mumbai', 'Guwahati']

pip = pickle.load(open('pip.pickle','rb'))



st.set_page_config(layout="wide")  # optional

page_bg_img = """
<style>

/* Header/title color */
h1,h2, .stApp h1 {
    color: #ffa500; /* Orange, for IPL vibrance */
    font-weight: bold;
    letter-spacing: 2px;
}

/* Label color and input background */
label, .st-c0, .st-c2, .st-c3 {
    color:  #ffa500 !important; /* Deep blue for contrast */
    font-weight: 700;
}

.stSelectbox, .stTextInput, .stNumberInput > div > input {
    # background-color: #faf3e3 !important; /* Soft cream */
    color:  #ffa500 !important; /* Navy text */
    # border-radius: 8px;
}

.stButton > button {
    background-color: #1e7b6c; /* Teal */
    color:  #ffa500 !important;
    font-weight: 700;
    border-radius: 8px;
    border: none;
    box-shadow: 0 4px 12px rgba(30,123,108,0.2);
    transition: background 0.3s;
}
.stButton > button:hover {
    background-color:  #ffa500;
}

/* Input spacing */
.stSelectbox, .stTextInput, .stNumberInput {
    margin-bottom: 1.5em;
    color: #White
    }

/* Dropdown options color */
div[role="option"] {
    color: black !important;
    font-weight: 700 !important;
}

/* Selected dropdown text color */
.css-1dimb5e-singleValue, .css-1uccc91-singleValue {
    color: black !important;
    font-weight: 700 !important;
}

[data-testid="stAppViewContainer"] {
    background-image: url("https://cdna.artstation.com/p/assets/images/images/062/209/502/large/krishnakant-prajapati-trophy-02.jpg?1682597952");
 background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: absolute;
    top: 0; 
    left: 0; 
    right: 0; 
    bottom: 0;
    background-image: inherit;
    filter: blur(8px);
    z-index: 0;
}
.block-container {
    position: relative;
    z-index: 1;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)





col1 ,col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('batting_Team',sorted(bat_team))
with col2:
    bowling_team = st.selectbox('bowling_Team',sorted(bow_team))

city = st.selectbox('city',sorted(citys))

col1,col2,col3 =st.columns(3)
with col1:
    target_runs = st.number_input("Target runs",0,400)
with col2:
    current_score = st.number_input('current_score',0,400)

with col3:
    wicket_lost = st.number_input('Current Team wickets lost',0,11)

overs= st.number_input("Current over",0,20)

if st.button('predict Probability'):
    

    wicket_left = 10 - wicket_lost
    balls_left= 120 - (overs*6)
    runs_left = target_runs - current_score
    current_run_rate=current_score/ overs
    rrr=runs_left*6/balls_left
    input = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[city] , 'target_runs':[target_runs],'runs_left':[runs_left],'wickets_left':[wicket_left],'balls_left':[balls_left],'current_run_rate':[current_run_rate],'rrr':[rrr]})
    Result = pip.predict_proba(input)
    loss = Result[0][0]
    win = Result[0][1]
    # st.header(str(bowling_team)+" :"+str(round(loss*100,2))+"%")
    # st.header(str(batting_team)+" :"+str(round(win*100,2))+"%")
    st.markdown(f"<h2 style='color:#ffa500'>{bowling_team} : {round(loss*100,2)}%</h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='color:#ffa500'>{batting_team} : {round(win*100,2)}%</h2>", unsafe_allow_html=True)
