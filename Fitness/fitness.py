import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import altair as alt


exercise_images = {
    "Running": "images/running.jpg",
    "Cycling": "images/cycling.jpg",
    "Yoga": "images/yoga.jpg",
    "Weightlifting": "images/weightlifting.jpg",
    "Sports": "images/sports.jpeg",
    "Light": "images/light.jpg",
    "Moderate": "images/moderate.jpg",
    "Intense": "images/intense.jpg"
}

exercise_dict = {
        "Light": {
            "Running": {"Duration": "20 mins", "Image": "images/running.jpg", "Suggestions": ["- 11 minute mile pace", "- Flat terrain", "- Treadmill"]},
            "Cycling": {"Duration": "30 mins", "Image": "images/cycling.jpg", "Suggestions": ["- 7:30 minute mile pace", "- Flat terrain", "- Bike Machine"]},
            "Yoga": {"Duration": "30 mins", "Image": "images/yoga.jpg", "Suggestions": ["- Full body stretch warmup", "- 3 beginner standing/balancing poses", "- 3 beginner seated/resting poses"]},
            "Weightlifting": {"Duration": "30 mins", "Image": "images/weightlifting.jpg", "Suggestions": {"Push": ["- 2 sets bench press", "- 2 sets dumbbell shoulder press", "- 2 sets tricep pushdowns"],
                                                                     "Pull": ["- 2 sets lat pulldowns", "- 2 sets rear deltoid flies", "- 2 sets dumbbell bicep curls"],
                                                                     "Legs": ["- 2 sets barbell squats", "- 2 sets machine hamstring curls", "- 2 sets calf raises"]}},
            "Sports": {"Duration": "30 mins", "Image": "images/sports.jpeg", "Suggestions": ["- Dodgeball", "- Badminton", "- Bowling"]}
                               },
        "Moderate": {
            "Running": {"Duration": "35 mins", "Image": "images/running.jpg", "Suggestions": ["- 9 minute mile pace", "- Moderately hilly terrain", "- Neighborhoods"]},
            "Cycling": {"Duration": "45 mins", "Image": "images/cycling.jpg", "Suggestions": ["- 6 minute mile pace", "- Moderately hilly terrain", "- Roads and sidewalks"]},
            "Yoga": {"Duration": "45 mins", "Image": "images/yoga.jpg", "Suggestions": ["- Full body stretch warmup", "- 4 intermediate standing/balancing poses", "- 4 intermediate seated/resting poses"]},
            "Weightlifting": {"Duration": "45 mins", "Image": "images/weightlifting.jpg", "Suggestions": {"Push": ["- 2 sets bench press", "- 2 sets dumbbell shoulder press", "- 2 sets tricep pushdowns", "- 2 sets cable lateral raises"],
                                                                     "Pull": ["- 2 sets lat pulldowns", "- 2 sets rear deltoid flies", "- 2 sets dumbbell bicep curls", "- 2 sets seated lateral rows"],
                                                                     "Legs": ["- 2 sets barbell squats", "- 2 sets machine hamstring curls", "- 2 sets calf raises", "- 2 sets hip abductors/adductors"]}},
            "Sports": {"Duration": "45 mins", "Image": "images/sports.jpeg", "Suggestions": ["- Tennis", "- Volleyball", "- Basketball"]}
                               },
        "Intense": {
            "Running": {"Duration": "50 mins", "Image": "images/running.jpg", "Suggestions": ["- 7:30 minute mile pace", "- Hilly terrain", "- Hiking trails"]},
            "Cycling": {"Duration": "60 mins", "Image": "images/cycling.jpg", "Suggestions": ["- 5 minute mile pace", "- Hilly terrain", "- Mountain biking trails"]},
            "Yoga": {"Duration": "60 mins", "Image": "images/yoga.jpg", "Suggestions": ["- Full body stretch warmup", "- 4 advanced standing/balancing poses", "- 4 advanced seated/resting poses"]},
            "Weightlifting": {"Duration": "75 mins", "Image": "images/weightlifting.jpg", "Suggestions": {"Push": ["- 3 sets bench press", "- 3 sets dumbbell shoulder press", "- 3 sets tricep pushdowns", "- 3 sets cable lateral raises", "- 3 sets incline dumbbell press"],
                                                                     "Pull": ["- 3 sets lat pulldowns", "- 3 sets rear deltoid flies", "- 3 sets dumbbell bicep curls", "- 3 sets seated lateral rows", "- 3 sets cable hammer curls"],
                                                                     "Legs": ["- 3 sets barbell squats", "- 3 sets machine hamstring curls", "- 3 sets calf raises", "- 3 sets hip abductors/adductors", "- 3 sets leg extensions"]}},
            "Sports": {"Duration": "60 mins", "Image": "images/sports.jpeg", "Suggestions": ["- Soccer", "- Ultimate Frisbee", "- Boxing"]}
                               }
                                }


# User profile section

def display_user_profile():
    st.title("Fitness Tracker 🏋️")
    st.image("images/gym.jpg")

    age = st.number_input("Enter your age", min_value=1, value=18)
    weight = st.number_input("Enter your weight in lbs", min_value=1, value=150)

    calories = st.slider("How many calories do you consume per day on average?", min_value=1000, max_value=3000, value=2000, step=100) #NEW
    if calories < 2000:
        st.write("You are likely currently eating in a calorie deficit. If you are trying to lose weight, keep it up!")
    elif calories >= 2000 and calories <= 2200:
        st.write("You are likely currently eating at a calorie balance. Maybe consider going on a bulk to build some more muscle?")
    elif calories > 2200:
        st.write("You are likely currently eating in a calorie surplus. Get that bulk going!") 

    intensity = st.radio("**Select your desired exercise intensity level**🔥", ["Light", "Moderate", "Intense"]) #NEW
    st.session_state.intensity = intensity #NEW
    
    if intensity == "Light":
        st.image(exercise_images["Light"], width = 200)
    elif intensity == "Moderate":
        st.image(exercise_images["Moderate"], width = 200)
    elif intensity == "Intense":
        st.image(exercise_images["Intense"], width = 200)
    st.subheader("Navigate to the Activity Tracker section to view your recommended exercises based on your desired intensity!")


# Activity tracker section

def display_activity_tracker():
    st.header("Activity Tracker ⏱️")
    st.image("images/tracker.jpg", width = 250)
    st.write("---")

    intensity = st.session_state.intensity
    st.subheader(f"Selected exercise intensity: {intensity}")

    exercise_type = st.selectbox("Select an Exercise", ["Running", "Cycling", "Yoga", "Weightlifting", "Sports"]) #NEW
    imgurl = exercise_dict[intensity][exercise_type]["Image"]

    st.image(imgurl, width = 450)
    if exercise_type == "Weightlifting":
        muscle_group = st.radio("Which muscle group (typical Push Pull Legs split) would you like to exercise?", ["Push", "Pull", "Legs"])
    
    st.subheader("Workout Recommendations📓")
    recommendation_dict = exercise_dict[intensity][exercise_type]
    
    st.write(f"**Duration**: {recommendation_dict['Duration']}")
    if exercise_type != "Weightlifting":
        expander = st.expander("**Exercise Recommendations**")
        regimen = recommendation_dict["Suggestions"]
        for bullet in regimen:
            expander.write(bullet)
    else:
        expander = st.expander("**Regimen Recommendations**")
        regimen = recommendation_dict["Suggestions"][muscle_group]
        for bullet in regimen:
            expander.write(bullet)
    

# Function to visualize progress
def display_progress_visualization():
    intensity = st.session_state.intensity
    st.header("Progress Visualization 📈")
    progress_data = {
        "Light": {
            "Date": [datetime.now() - timedelta(days=4), datetime.now() - timedelta(days=3), datetime.now() - timedelta(days=2), datetime.now() - timedelta(days=1), datetime.now()],
            "Progress": [2, 5, 10, 8, 12]
        },
        "Moderate": {
            "Date": [datetime.now() - timedelta(days=4), datetime.now() - timedelta(days=3), datetime.now() - timedelta(days=2), datetime.now() - timedelta(days=1), datetime.now()],
            "Progress": [5, 8, 7, 11, 18]
        },
        "Intense": {
            "Date": [datetime.now() - timedelta(days=4), datetime.now() - timedelta(days=3), datetime.now() - timedelta(days=2), datetime.now() - timedelta(days=1), datetime.now()],
            "Progress": [8, 7, 15, 19, 25]
        }
    }

    # line chart for the selected intensity level
    if intensity in progress_data:
        st.subheader(f"Model Progress Visualization for {intensity} Intensity")
        
        # Create a DataFrame from dummy data
        df = pd.DataFrame(progress_data[intensity])
        df['Date'] = pd.to_datetime(df['Date'])
        
        # Create an Altair line chart with axis labels
        chart = alt.Chart(df).mark_line().encode(
            x=alt.X('Date:T', title='Date', axis=alt.Axis(format='%m/%d')),
            y=alt.Y('Progress:Q', title='Percent Growth')
        ).properties(
            width=600,
            height=500
        )

        st.altair_chart(chart, use_container_width=True)
    else:
        st.warning("No progress data available for the selected intensity level.")
    
    st.write("---")
    st.subheader("Keep up the good work! 👍")

# Main function for app structure
def main():
    st.sidebar.title("🔥Fitness App🔥")
    navigation_choice = st.sidebar.radio("Select an Page", ["Profile", "Activity Tracker", "Progress"])

    if navigation_choice == "Profile":
        display_user_profile()
    elif navigation_choice == "Activity Tracker":
        display_activity_tracker()
    elif navigation_choice == "Progress":
        display_progress_visualization()


main()
