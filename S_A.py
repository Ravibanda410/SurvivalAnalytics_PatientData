
import pandas as pd
# Loading the the survival un-employment data
patient = pd.read_csv("C:/RAVI/Data science/Assignments/Survival Analytics/Patient.csv/Patient.csv")
patient.head()
patient.describe()

patient = patient.drop(["PatientID"], axis = 1)

patient["Followup"].describe()

# Spell is referring to time 
Time = patient.Followup

# Importing the KaplanMeierFitter model to fit the survival analysis
pip install lifelines
from lifelines import KaplanMeierFitter

# Initiating the KaplanMeierFitter model
kmf = KaplanMeierFitter()

# Fitting KaplanMeierFitter model on Time and Events for death 
kmf.fit(Time, patient.Eventtype)

# Time-line estimations plot 
kmf.plot()


