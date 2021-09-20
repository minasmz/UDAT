import pickle


def predict_PR_Volume (input):
    loaded_model = pickle.load(open('PR_Volume_model.pkl', 'rb'))
    result = loaded_model.predict([input])
    #print (result[0])
    return result[0]


def predict_AD_Volume (input):
    loaded_model = pickle.load(open('AD_Volume_model.pkl', 'rb'))
    result = loaded_model.predict([input])
    #print (result[0])
    return result[0]


def predict_cure_cycle_total_time (input):
    loaded_model = pickle.load(open('Cure_Cycle_Total_Time_model.pkl', 'rb'))
    result = loaded_model.predict([input])
    #print (result[0])
    return result[0]


def predict_fiber_volume_fraction (input):
    loaded_model = pickle.load(open('Fiber_Volume_Fraction_model.pkl', 'rb'))
    result = loaded_model.predict([input])
    #print (result[0])
    return result[0]


def predict_effective_porosity (input):
    loaded_model = pickle.load(open('Effective_Porosity_model.pkl', 'rb'))
    result = loaded_model.predict([input])
    #print (result[0])
    return result[0]

def predict_PR_prosity (input):
    loaded_model = pickle.load(open('PR_Porosity_model.pkl', 'rb'))
    result = loaded_model.predict([input])
    #print (result[0])
    return result[0]

def predict_AD_prosity (input):
    loaded_model = pickle.load(open('AD_Porosity_model.pkl', 'rb'))
    result = loaded_model.predict([input])
    #print (result[0])
    return result[0]







#predict_AD_prosity([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]])