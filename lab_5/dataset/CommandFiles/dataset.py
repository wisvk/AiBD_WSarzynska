import pandas as pd


df = pd.read_csv("../OriginalData/earthquake_data.csv")

lut = {"Extremely worried": 4,
       "Not at all worried": 0,
       "Not so worried": 1,
       "Somewhat worried": 2,
       "Very worried": 3
}

lut1 = {"Male": "M",
       "Female": "F",
       None: "No information",
}
lut2 = {"No": "N",
       "Yes": "Y",
}

lut3 = {"Extremely familiar": 4,
       "Not at all familiar": 0,
       "Not so familiar": 1,
       "Somewhat familiar": 2,
       "Very familiar": 3,
       None: "No information",
}

lut4 = {"Extremely familiar": 4,
       "Not at all familiar": 0,
       "Not so familiar": 1,
       "Somewhat familiar": 2,
       "Very familiar": 3,
       None: "No information",
}

lut5 = {"No": "N",
       "Yes": "Y",
       None: "No information",
}

lut6 = {"No": "No",
       "Yes, one or more minor ones": "Minor One",
       "Yes, one or more major ones": "Major One",
       None: "No information",
}

lut7 = {"Extremely worried": 4,
       "Not at all worried": 0,
       "Not so worried": 1,
       "Somewhat worried": 2,
       "Very worried": 3
}

df["Have you or anyone in your household taken any precautions for an earthquake (packed an earthquake survival kit, prepared an evacuation plan, etc.)?"] = df["Have you or anyone in your household taken any precautions for an earthquake (packed an earthquake survival kit, prepared an evacuation plan, etc.)?"].map(lut5)
df["How familiar are you with the San Andreas Fault line?"] = df["How familiar are you with the San Andreas Fault line?"].map(lut4)
df["How familiar are you with the Yellowstone Supervolcano?"] = df["How familiar are you with the Yellowstone Supervolcano?"].map(lut3)
df["What is your gender?"] = df["What is your gender?"].map(lut1)
df['Do you think the "Big One" will occur in your lifetime?'] = df['Do you think the "Big One" will occur in your lifetime?'].map(lut2)
df["Have you ever experienced an earthquake?"] = df["Have you ever experienced an earthquake?"].map(lut6)
df["In general, how worried are you about earthquakes?"] = df["In general, how worried are you about earthquakes?"].map(lut)
df["How worried are you about the Big One, a massive, catastrophic earthquake?"] = df["How worried are you about the Big One, a massive, catastrophic earthquake?"].map(lut7)

df["Personal Data"]=df["What is your gender?"]+df["Age"]+" "+df['Do you think the "Big One" will occur in your lifetime?']

print(df.head()["Personal Data"])
df = df[ ["Personal Data"] + [ col for col in df.columns if col != "Personal Data" ] ]
df = df[  [ col for col in df.columns if col != "Age" ] ]
df = df[[ col for col in df.columns if col != 'Do you think the "Big One" will occur in your lifetime?' ] ]
df = df[ [ col for col in df.columns if col != "What is your gender?" ] ]


df.rename(columns = {'US Region':'Region'}, inplace = True)
df.rename(columns = {'How much total combined money did all members of your HOUSEHOLD earn last year?':'Annual income'}, inplace = True)
df.rename(columns = {'How familiar are you with the Yellowstone Supervolcano?':'Knowledge of the Yellowstone Supervolcano'}, inplace = True)
df.rename(columns = {'How familiar are you with the San Andreas Fault line?':'Knowledge of the San Andreas Fault line'}, inplace = True)
df.rename(columns = {'Have you or anyone in your household taken any precautions for an earthquake (packed an earthquake survival kit, prepared an evacuation plan, etc.)?':'Precautions for an earthquake'}, inplace = True)
df.rename(columns = {'How worried are you about the Big One, a massive, catastrophic earthquake?':'How worried are you about the Big One?'}, inplace = True)
df.rename(columns = {'In general, how worried are you about earthquakes?':'How worried are you about earthquakes'}, inplace = True)

for col in df.columns:
    print(col)
print(df.head())
print(df.head()["Have you ever experienced an earthquake?"])

from pathlib import Path
filepath = Path('../AnalysisData/AnalysisData.csv')
df.to_csv(filepath)


