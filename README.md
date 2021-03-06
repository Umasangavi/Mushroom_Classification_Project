Mushroom Prediction
==============================
The Audubon Society Field Guide to North American Mushrooms contains descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family Mushroom (1981). Each species is labelled as either definitely edible, definitely poisonous, or maybe edible but not recommended. This last category was merged with the toxic category. The Guide asserts unequivocally that there is no simple rule for judging a mushroom's edibility, such as "leaflets three, leave it be" for Poisonous Oak and Ivy. The main goal is to predict which mushroom is poisonous & which is edible.

About Dataset
================================
This dataset includes descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family Mushroom drawn from The Audubon Society Field Guide to North American Mushrooms (1981). Each species is identified as definitely edible, definitely poisonous, or of unknown edibility and not recommended. This latter class was combined with the poisonous one. The Guide clearly states that there is no simple rule for determining the edibility of a mushroom; no rule like "leaflets three, let it be'' for Poisonous Oak and Ivy.

URL: https://www.kaggle.com/uciml/mushroom-classification

Approach:
=================================
* Data Description
  * We will be using Mushrooms Prediction Data Set present in Kaggle Repository. This Data set is satisfying our data requirement. Total 8120 instances present in different        batches of data. Export Data from DB to CSV for training We used MongoDB to push and pull over data for our model.

* Data Splitting
  * We split the data here for our train and test data for further uses.

* Data Preprocessing
  * As our data is full of categorical values, so we convert all those to numerical values by label encoding.
  
* Model Training
  * We trained various model in our notebook and SVC was good on it. We trained with our processed data.
  
* Model Evaluation
  * Model evaluation done by classification and report was saved to .json file.

* Model Saving
  * we will save our modelsso that we can use them for prediction purpose.

* Push to app
  * Here we also create our Streamlit app and user interface and integrate our model with Streamlit and UI

* Data from client side for prediction purpose
  * Now our application on cloud is ready for doing prediction. The prediction data which we receive from client side.

* Data processing and Prediction
  * Client data will also go along the same process Data pre-processing and according to that we will predict those data.

* Export Prediction to CSV
  * Finally, when we get all the prediction for client data, then our final task is toexport prediction to csv file and hand over it to client
  
 Web Deployment
 ===================================
Mushroom Classification Web App : https://mushroom-prediction-api.herokuapp.com/

Screenshots
====================================
**Homepage interface:**

![image](https://user-images.githubusercontent.com/92853376/152312227-bf8d75e1-5169-4669-af01-a46c3a58fcf7.png)

**Prediction:**

![image](https://user-images.githubusercontent.com/92853376/152312323-0e664ff4-e5ab-48f1-a94d-f190ae6d9ad8.png)

**Download csv file:**

![image](https://user-images.githubusercontent.com/92853376/152312423-4f9f4b5a-2149-4a78-87f4-4fc8f150ad6d.png)

**High level design**
======================================
URL: https://drive.google.com/file/d/1S9cW7OYbpTFhXZxlyzTpG1SSmvNDtUQa/view?usp=sharing

**Low level design**
=======================================
URL: https://drive.google.com/file/d/1Teq4gXbu-PJ7YgwATVFhjgd19ftsyYMD/view?usp=sharing

**Architecture**
=======================================
URL: https://drive.google.com/file/d/18tuG3jdrnCdzkN08lpXqN4AtcuB9qmOK/view?usp=sharing

**Detailed project report**
=======================================
URL:https://drive.google.com/file/d/1jw2Xku081WvGizk1TQ9nImSexfr3dQrB/view?usp=sharing

**Wireframe document**
=======================================
URL: https://drive.google.com/file/d/1OKYYBw37wQuB2cNeIzmjCI97Y7Ggi7jk/view?usp=sharing

**Demo video**
=======================================
URL:https://drive.google.com/file/d/1eUfjgxZc36-iSsVw1vN4l_Ru0SQpYv40/view?usp=sharing 

**Linkedin**
========================================
URL: https://www.linkedin.com/in/umasangavi/





