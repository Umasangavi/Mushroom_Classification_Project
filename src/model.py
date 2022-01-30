import pandas as pd
import yaml
import argparse
import joblib
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from logger import App_Logger

file_object=open("application_logging/Loggings.txt", 'a+')
logger_object=App_Logger()


def read_params (config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def train_and_evaluate(config_path):
    config = read_params(config_path)
    train_encoder_path=config["encoder"]["train_path"]
    test_encoder_path=config["encoder"]["test_path"]
    random_state=config["base"]["random_state"]
    cache_size=config["estimator"]["SVC"]["params"]['cache_size']
    degree=config["estimator"]["SVC"]["params"]["degree"]
    report_path=config["metrics"]["report"]
    target= config["base"]["target_col"]

    train=pd.read_csv(train_encoder_path)
    test=pd.read_csv(test_encoder_path)

    y_train=train[target]
    y_test=test[target]

    X_train=train.drop(target, axis=1)
    X_test=test.drop(target, axis=1)

    try:
        model= SVC(
            cache_size=cache_size, 
            degree=degree, 
            random_state=random_state)         
        model.fit(X_train,y_train)
        logger_object.log(file_object,'Model is trained')

        y_pred= model.predict(X_test)

        cl_report=pd.DataFrame(classification_report(y_test, y_pred, output_dict=True)).transpose()
        cl_report.to_csv(report_path, index= True)
        logger_object.log(file_object,'Classification report was done')


        joblib.dump(model,open("models/model.pkl", 'wb'))
        logger_object.log(file_object,'model.pkl is saved successfully')


    except Exception as e:
        logger_object.log(file_object,'Exception occurred in train_and_evaluate. Exception message: '+str(e))
        logger_object.log(file_object,'training and evaluation unsuccessful')
        raise Exception()


if __name__ =="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    data=train_and_evaluate(config_path=parsed_args.config)






