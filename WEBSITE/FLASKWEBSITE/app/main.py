# import requirements needed
from flask import Flask, render_template, request
from utils import get_base_url
from flask import url_for, request
import numpy as np
# setup the webserver
# port may need to be changed if there are multiple flask servers running on same server
port = 12345
base_url = get_base_url(port)
# url_for('static', filename='style.css')


    
    
#load the model

import pickle
filename = 'rf.pkl'
loaded_model = pickle.load(open(filename, 'rb'))

#get the inputs from the front end

#Encoding 

# predict

# return the predictions on the main website
    
    
   


# if the base url is not empty, then the server is running in development, and we need to specify the static folder so that the static files are served
if base_url == '/':
    app = Flask(__name__)
else:
    app = Flask(__name__, static_url_path=base_url+'static')





# set up the routes and logic for the webserver
@app.route(f'{base_url}')
def home():
    test_flag = 0
    return render_template('index.html')


@app.route(f"{base_url}", methods=['GET','POST'])
def main():
    
    if request.method == 'GET':
        return render_template('index.html', classification_text = "")

    if request.method == 'POST':
        result = [thing for thing in request.form.values()]
#         print('The results are ',result)
        result = np.array(result)
        predictions = loaded_model.predict(result.reshape(1,-1))[0]
        if predictions == 0:
            predictions_text = "you are safe"
            test_flag = 1
        else:
            predictions_text = "you need HELP : Please call 988 for any help"
            test_flag = 2
        print("the predicctio isssss brooo",type(predictions))
        return render_template("index.html",classification_text = predictions_text,image_flag = test_flag)
    

#         else:
#             return render_template("index.html")
#         result = request.form.values([thing for thing in result]) 
#         results_final = model.predict(results_reshaped)


@app.route(f'{base_url}/team_members')
def team_members():
    return render_template('team_members.html') # would need to actually make this page

if __name__ == '__main__':
    # IMPORTANT: change url to the site where you are editing this file.
    website_url = 'https://cocalc2.ai-camp.dev'
    
    print(f'Try to open\n\n    https://{website_url}' + base_url + '\n\n')
    app.run(host = '0.0.0.0', port=port, debug=True)
