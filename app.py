from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from Model.predict import model, MODEL_VERSION, predict_output
from schema.prediction_response import PredResponse
app=FastAPI()



@app.get("/")
def home_page():
    return {'message':'Insurance Premium prediction model API'}

@app.get("/health")
def health_page():
    return {
        'status':'ok',
        'Model Version': MODEL_VERSION,
        'model_loaded': model is not None
    }

@app.post("/predict",response_model=PredResponse)
def predict_premium(data:UserInput,):

    # req_data=data.model_dump(exclude=["age","weight","height",""])
    input_df={
        'bmi':data.bmi,
        'age_group':data.age_group,
        'lifestyle_risk':data.lifestyle_risk,
        'city_tier':data.city_tier,
        'income_lpa':data.income_lpa,
        'occupation':data.occupation
    }

    try:
        prediction=predict_output(input_df)
        return JSONResponse(status_code=200, content={"response":prediction})

    except Exception as e:
        return JSONResponse(status_code=500,content=(e))






