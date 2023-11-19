from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import csv, numpy as np, pandas as pd
import os

data = pd.read_csv(os.path.join("templates", "Training.csv"))
df = pd.DataFrame(data)
cols = df.columns
cols = cols[:-1]
x = df[cols]
y = df['prognosis']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

print("Multinomial Naive Bayes")
mnb = MultinomialNB()
clf_mnb = mnb.fit(x_train, y_train)

indices = [i for i in range(132)]
symptoms = df.columns.values[:-1]

dictionary = dict(zip(symptoms, indices))

def dosomething(symptom):
    user_input_symptoms = symptom
    user_input_label = [0 for i in range(132)]
    for i in user_input_symptoms:
        idx = dictionary[i]
        user_input_label[idx] = 1

    user_input_label = np.array(user_input_label)
    user_input_label = user_input_label.reshape((-1, 1)).transpose()
    return mnb.predict(user_input_label)

# Example usage:
predicted = dosomething(['fatigue', 'headache', 'nausea'])
print("Predicted disease:", predicted)