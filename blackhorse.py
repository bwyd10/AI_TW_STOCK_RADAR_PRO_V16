
import pandas as pd
def calculate_blackhorse(result):
    score=0
    if float(result.get("營收成長%",0) or 0)>=15: score+=20
    if float(result.get("RS強度",0) or 0)>=1.2: score+=20
    if float(result.get("法人籌碼分",0) or 0)>=15: score+=20
    if str(result.get("VCP通過","")).lower() in ["yes","true","1","通過"]: score+=15
    if float(result.get("AI冠軍分數",0) or 0)>=80: score+=15
    if float(result.get("ROE%",0) or 0)>=15: score+=10
    score=min(100,score)
    stars="★★★★★" if score>=90 else "★★★★☆" if score>=75 else "★★★☆☆"
    return {"blackhorse_score":score,"blackhorse_rating":stars}
