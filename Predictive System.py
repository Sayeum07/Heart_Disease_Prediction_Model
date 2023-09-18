import numpy as np
import pickle

#loading the saved model 
loaded_model = pickle.load(open('D:/Coding/Data Science Projects/Begineer Level Project/Heart Disease Prediction/trained_model.sav','rb'))


input_data = (41,0,1,130,204,0,0,172,0,1.4,2,0,2)

# change the input data into numpy array

array = np.asarray(input_data)
# reshape the numpy array as we are predicting for only on instance
input_data_reshaped = array.reshape(1,-1)
prediction = loaded_model.predict(input_data_reshaped)
print(prediction)
if (prediction[0]==0):
  print('The person does not have a heart disease')
else:
  print('The person has heart disease')
