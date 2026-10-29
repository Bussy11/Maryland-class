import streamlit as st

# ============================================================
# HUMAN AGE GROUP PREDICTION SYSTEM
# Streamlit web application
# ============================================================

st.set_page_config(
    page_title="Human Age Group Prediction System",
    page_icon="👤",
    layout="centered"
)

st.title("👤 Human Age Group Prediction System")
st.write("Enter your details below to identify your age group.")
st.divider()

# Collect the user's information
with st.form("age_prediction_form"):
    name = st.text_input("Enter your full name")
    age = st.number_input(
        "Enter your age",
        min_value=0,
        max_value=100,
        value=18,
        step=1
    )
    submitted = st.form_submit_button("Predict Age Group")

# Predict the age group after the user submits the form
if submitted:
    if not name.strip():
        st.error("Please enter your full name.")
    else:
        st.success(f"Hello, {name.strip()}!")

        # Age-group boundaries:
        # 0–9 years   = Child
        # 10–18 years = Adolescent
        # 19–49 years = Adult
        # 50–100 years = Grandparent age group
        if age < 10:
            group = "CHILD"
            description = "You belong to the child age group."
        elif age < 19:
            group = "ADOLESCENT"
            description = "You belong to the adolescent age group."
        elif age < 50:
            group = "ADULT"
            description = "You belong to the adult age group."
        else:
            group = "GRANDPARENT AGE GROUP"
            description = "You belong to the 50–100 age group."

        st.subheader("Prediction Result")
        st.info(f"Predicted age group: **{group}**")
        st.write(description)

        st.caption("Thank you for using the Human Age Group Prediction System.")

st.divider()
st.caption(
    "Note: This is a simple rule-based age-group classifier, not a machine-learning model. "
    "The labels are based only on the age ranges defined in this program."
)
