import os
from difflib import SequenceMatcher
import pandas as pd

participant_files = os.listdir("Participant_Files/")

original_file = open("1.html").read()

team_details = {
        "Rank": [],
    "Team Name":[],
    "Percentage Similarity" : [],



}

df = pd.DataFrame(team_details)
df = df.astype({"Rank":int})
i = 1

for elem in participant_files:
    text2 = open(os.path.join("Participant_Files",elem)).read()
    m = SequenceMatcher(None, original_file, text2)
    s = pd.Series({'Team Name': f'{elem[:-5]}', 'Percentage Similarity': m.ratio()*100,"Rank":i})
    df = df.append(s,ignore_index=True)
    i+=1

df = df.sort_values(axis=0,ascending=False,by="Percentage Similarity")
i=1
for index,rows in df.iterrows():
    df.loc[index,'Rank'] = i
    i+=1

df.to_csv("Results.csv",index=False)



