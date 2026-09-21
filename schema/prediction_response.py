from pydantic import BaseModel,Field
from typing import Dict

class PredResponse(BaseModel):
    predicted_category:str=Field(...,description="Prediction Class",example="High")
    confidence:float=Field(...,description="Confidence of predicted category",example="0.8765",gt=0)
    class_probabilities:Dict[str,float]=Field(...,description="prabbilities of each class",example={"low":0.13,"medium":0.15,"high":72})
