import pandas as pd

def rc_seattle(filepath):
    df = pd.read_csv(filepath)
    
    #cleaning basement values
    df.sqft_basement = house_df.sqft_basement.replace('?', '-1.0')
    df.sqft_basement = house_df.sqft_basement.astype(float)
    
    #fixing date dt
    df["date"] = pd.to_datetime(df["date"])

#TODO: see if this is needed at all
def clean(df):
    pass

def create_model(df, x, y):
    #X = df.
    #y = df.
    X = sms.add_constant(X)
    model = sms.OLS(y, X)
    result = model.fit()
    result.summary()

# Executes everything below when '%run -i clean_seattle_df.py' in terminal
if __name__ == "__main__":