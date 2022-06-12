import streamlit as st
import requests
from PIL import Image
from utils import sex_category,smoker_category,northeast,northwest,southeast,southwest

image=Image.open("umbrella.png")
st.set_page_config(page_title="Medical Insurance",page_icon=image)

st.markdown("""# Medical Insurance Payout""")

# age,bmi,children,sex_category,smoker_category,region_northeast,region_northwest,region_southeast,region_southwest
#female , non smoker = 0

age = st.text_input('Age')
if st.button("Age"):
    if age =="" or not age.isdigit()or int(age) >= 130 or int(age) < 0:
        st.write("Input the correct age")
    else:
        st.write(f"Age is {age}")

bmi = st.text_input('BMI')
if st.button("BMI"):
    # if bmi =="":
    #     st.write("Input the correct BMI")
    # elif bmi==float(bmi):
    #     st.write(f"BMI is {bmi}")
    if bmi =="" or bmi.isalnum() or bmi.isalpha() or int(bmi) >= 40 or int(bmi) <= 18:
        st.write("Input the correct BMI")
    else:
        st.write(f"BMI is {bmi}")

children = st.text_input('Number of Children')
if st.button("Number of Children"):
    if children =="" or not children.isdigit() or int(children)>15:
        st.write("Input the correct number of children")
    else:
        st.write(f"No of children is {children}")

female_male = st.radio('Sex',('Female','Male'))
smoker_nonsmoker = st.radio('Smoke?',('Smoker','Non Smoker'))
region = st.radio('Region', ('Region Northeast', 'Region Northwest', 'Region Southeast', 'Region Southwest'))

# age = "48"
# bmi = "21"
# children = "4"
# female_male = 'Male'
# smoker_nonsmoker = 'Non Smoker'
# region = 'Region Southeast'

data={"age":age,
        "bmi":bmi,
        "children":children,
        "sex_category":sex_category(female_male),
        "smoke":smoker_category(smoker_nonsmoker),
        "ne":northeast(region),
        "nw":northwest(region),
        "se":southeast(region),
        "sw":southwest(region)}

print(data)

url="http://127.0.0.1:8000/evaluation"
features_url="?age="+data.get("age")+"&bmi="+data.get("bmi")+"&children="+data.get("children")+"&sex_category="+data.get("sex_category")+"&smoker_category="+data.get("smoke")+"&region_northeast="+data.get("ne")+"&region_northwest="+data.get("nw")+"&region_southeast="+data.get("se")+"&region_southwest="+data.get("sw")
full_url=url+features_url

# print (full_url)
# a=requests.get(full_url)
# print (a)
# print (a.json()['Annual Medical Expenditure'])

if st.button("Submit"):
    try:
        result=requests.get(full_url)
        final_result=result.json()['Annual Medical Expenditure']
        st.write("Your Annual Medical Expenditure is ")
        st.write(final_result)
        st.write("Your Monthly Medical Expenditure is ")
        st.write(round(final_result/12,2))

    except:
        st.write("Please make sure you input the correct information for all categories")
