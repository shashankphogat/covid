from flask import Flask, render_template,request
import numpy as np
import joblib

app=Flask(__name__,template_folder='template',static_folder='static')



@app.route('/')
def home():
    return render_template('test.html')

@app.route('/predict/',methods=['POST','GET'])
def predict():
    return render_template('corona.html')

@app.route('/output/',methods=['POST','GET'])
def output():
    with open('saved_model.pkl', 'rb') as f:
        model = joblib.load(f)
    int_features = [x for x in request.form.values()]
    if len(int_features)==11:
        final = [np.array(int_features)]
        predict = model.predict(final)
        output = int(predict)
        if output == 1:
            return render_template('output.html',pred='your severity is of highest class which is EMERGENCY.')
        if output == 2:
            return render_template('output.html',pred='your severity is of 2nd highest class which is EXTREME.')
        if output == 3:
            return render_template('output.html', pred='your severity is of 3rd highest class which is HIGH.')
        if output == 4:
            return render_template('output.html', pred='your severity is of 4th highest class which is LOW.')
        if output == 5:
            return render_template('output.html', pred='your severity is of lowest class which is VERY LOW.')
    else:
        return render_template('corona.html',pred2='You didn\'t attempt all the questions last time. Try again')

if __name__ =='__main__':
    app.run()

