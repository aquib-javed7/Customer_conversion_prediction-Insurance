import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import pandas as pd

st.set_page_config(page_title="Loan Attraction Predictor", page_icon="D:\Customer Convertion Prediction\icon.png",layout='wide')

with open('D:\Customer Convertion Prediction\onehot_encoder.pkl', 'rb') as f:
    loaded_encoder_ohc = pickle.load(f)


st.markdown("<h1 style='text-align:center;text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); color:#33363D; font-size:50px;'>Customer Loan Conversion Predictor | By Akib Javith</h1>", unsafe_allow_html=True)

background_image_url = "https://etimg.etb2bimg.com/photo/109768681.cms"  

# Custom CSS for the submit button
st.markdown(f"""
    <style>
        /* Background and page styling */
        body {{
            background-image: url("{background_image_url}");
            background-size: cover;  /* Ensures the image covers the entire page */
            background-repeat: no-repeat;  /* Ensures the image does not repeat */
            background-attachment: fixed;  /* Makes the background fixed when scrolling */
            color: white;  /* Text color set to white for contrast */
        }}
        .stApp {{
            background-color: transparent;
        }}
        
        /* Option Menu Styling */
        .css-1v0mbp5 {{
            background-color: rgba(255, 255, 255, 0.7);  /* Semi-transparent background for option menu */
            border-radius: 10px;  /* Optional: round the corners */
        }}

        .header {{
            color: #DBC090 !important;
            font-size: 28px;  /* Increased font size */
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);  /* Text shadow effect */
        }}

        /* Styling for content text with text-shadow and increased font size */
        .content-text {{
            color: white;
            font-size: 18px;  /* Increased font size */
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);  /* Light text shadow effect */
        }}
        
        .stColumn {{
            background: rgba(0, 0, 0, 0.3);  /* Semi-transparent black background */
            backdrop-filter: blur(10px);  /* Apply blur effect */
            border-radius: 10px;  /* Optional: round the corners */
            padding: 10px;
        }}

        .button-prompt {{
            color: #FFC300;  /* Custom color */
            font-size: 18px;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }}

        /* Style the form submit button */
        .stForm button {{
            color: white !important;  /* Set text color */
            font-weight: bold !important;
            font-size: 18px !important;
            border-radius: 8px;
            padding: 10px 50px;  /* Make button wider */
            width: 50%;  /* Full width button */
            transition: background-color 0.3s ease;  /* Smooth transition for hover effect */
        }}

        /* Hover effect for the button */
        .stForm button:hover {{
            background-color: #DBC090;  /* Maintain the same color on hover */
            color: #000000 !important;
        }}
    </style>
""", unsafe_allow_html=True)

#option menu

selected = option_menu(
    menu_title=None,
    options=["Home","Loan Prediction"],
    icons=["house", "bar-chart"],
    default_index=0,
    orientation="horizontal",
    styles={
        "nav-link-selected": {
            "background-color": "#DBC090",  # Highlighted option with blue
            "color": "white",  # White text when selected
        },
        "nav-link": {
            "color": "#ffffff",  # white for unselected options
        }
    }
)

age = list(range(18, 96))
day = list(range(1,31))
job = [
    "MANAGEMENT",
    "TECHNICIAN",
    "ENTREPRENEUR",
    "BLUECOLLAR",
    "OTHER",
    "RETIRED",
    "ADMIN",
    "SERVICES",
    "SELFEMPLOYED",
    "UNEMPLOYED",
    "HOUSEMAID",
    "STUDENT",
]
marital = ["MARRIED", "SINGLE", "DIVORCED"]

education_qual = ["TERTIARY", "SECONDARY", "OTHER", "PRIMARY"]

call_type = ["OTHER", "CELLULAR", "TELEPHONE"]

columns_to_scale = ["age", "day", "mon", "dur", "job"]

mon = [
    "JAN",
    "FEB",
    "MAR",
    "APR",
    "MAY",
    "JUN",
    "JUL",
    "AUG",
    "SEP",
    "OCT",
    "NOV",
    "DEC",
]

month_dict = {
    "JAN": 1,
    "FEB": 2,
    "MAR": 3,
    "APR": 4,
    "MAY": 5,
    "JUN": 6,
    "JUL": 7,
    "AUG": 8,
    "SEP": 9,
    "OCT": 10,
    "NOV": 11,
    "DEC": 12,
}

prev_outcome = ["OTHER", "FAILURE", "OTHER", "SUCCESS"]


education_qual_dict = {"TERTIARY": 3, "SECONDARY": 2, "OTHER": 0, "PRIMARY": 1}


outcome_dict = {"NO": 0, "YES": 1}

if selected =='Home':
    col1,col2=st.columns(2)
    with col1:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown('<h2 class="header">Overview</h2>', unsafe_allow_html=True)
        st.markdown('<p class="content-text">In the insurance industry, acquiring new customers and converting leads into sales is crucial for business growth. The dataset provided contains information about a series of marketing calls made to potential customers by an insurance company. The goal is to predict whether a customer will subscribe to an insurance policy based on various attributes of the customer and details of the marketing interactions.</p>', unsafe_allow_html=True)
        st.markdown('<h2 class="header">Deliverables</h2>', unsafe_allow_html=True)
        st.markdown('<p class="content-text">The project will deliver the following deliverables:</p>', unsafe_allow_html=True)
        st.markdown('<p class="content-text">A well-trained machine learning model for Customer loan prediction A user-friendly web application (built with Streamlit). Documentation and instructions for using the application. A project report summarizing the data analysis, model development, and deployment process.</p>', unsafe_allow_html=True)
        st.markdown('<h2 class="header">Technologies Used</h2>', unsafe_allow_html=True)
        st.markdown('<p class="content-text">Python,Pandas,Streamlit,Plotly,Random Search CV,SkLearn,Pickle...</p>', unsafe_allow_html=True)
    with col2:
        st.image('https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEijnnIaq7qsTzTU18aYg-OSLnvt3eUMqOXaXqD6_rJX4wGhTofjPReBTFoPyQ324e-5pnu8xFex55t9IqH8b2dNxo-LW5_tpox9CXDEuAV3Nl6P3nlmBqjqsBTa-tCj0vyLFUyv-xh0im495msok0lTWXZKTxlX1d2LWQ7MmX3YW5nPfpyAgX0DF-nRRg/w631-h355/20220721_185806_0000.png')
        st.image('https://media.licdn.com/dms/image/v2/C4D12AQHIt2funjnANA/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1623913883834?e=1745452800&v=beta&t=haPPrL0iWLrBU28wZ04JGz90c_IIyzLkaDAvlrnJeKY')

if selected == 'Loan Prediction':
    with st.form("Classification"):
        col1,col2=st.columns(2)
        
        with col1:
            age = st.selectbox("Select Age",options=age)
            
            job = st.selectbox("Select Occupation",options=job)
            
            marital = st.selectbox("Select Marital Status",options=marital)
            
            education_qual = st.selectbox("Select Educational Qualification",education_qual)
            
            call_type = st.selectbox("Select Call Type",options=call_type)
        
        with col2:
            
            day = st.selectbox("Select Day",options=day) 
            
            mon = st.selectbox("Select Month",options=mon)
            
            dur = st.number_input("Enter Duration in Seconds",min_value=0,value=0)
            
            num_calls = st.number_input("Enter Number of Calls",min_value=0,value=0)
            
            prev_outcome =st.selectbox("Select Previous Outcome",options=prev_outcome)
            
        with col1:
            st.write(" ")
            submitted = st.form_submit_button("Submit")
            
        if submitted:
            
            try:
                age = age 
                
                education_qual = education_qual_dict[education_qual]
                
                day=day
                
                mon = month_dict[mon]
                
                dur = dur
                
                num_calls = num_calls


                column_names = ['age', 'job', 'marital', 'education_qual', 'call_type', 'day', 'mon', 'dur','num_calls','prev_outcome']

                # Convert 'ip1' into a DataFrame
                ip = pd.DataFrame([[age, job, marital, education_qual, call_type, day, mon, dur,num_calls,prev_outcome]], 
                                columns=column_names)

                # Define categorical and continuous columns
                categorical_cols = ["call_type", "prev_outcome","marital","job"]
                continuous_cols = ['age', 'education_qual', 'day', 'mon', 'dur','num_calls']

                # Encode categorical features
                encoded_user_array = loaded_encoder_ohc.transform(ip[categorical_cols])

                # Convert to DataFrame with proper column names
                encoded_user_df = pd.DataFrame(encoded_user_array, columns=loaded_encoder_ohc.get_feature_names_out(categorical_cols))

                # Concatenate continuous features with encoded categorical features
                final_user_df = pd.concat([ip[continuous_cols], encoded_user_df], axis=1)
                
                with open(r'D:\Customer Convertion Prediction\xgboost_model.pkl','rb') as file:
                    xgb_model = pickle.load(file)

                status_predict = xgb_model.predict(final_user_df)

                outcome = status_predict[0]
                Outcome = "YES" if outcome == 1 else "NO"

                with col2:
                    if outcome == 1:
                        st.markdown(f'<h2 class="header">Prediction is: {Outcome}</h2>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<h2 class="header">Prediction is: {Outcome}</h2>', unsafe_allow_html=True)
                
                
            except ValueError as e:
                st.warning(e)
                st.warning("Please Provide Valid Details")
            except Exception as e:
                st.warning(e)