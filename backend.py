from flask import Flask, request, render_template, Response,json
from flask_cors import CORS
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from analyser import analyse
import yfinance as yf


app = Flask(__name__, template_folder='static_file')
cors = CORS(app)
cors = CORS(app, origins=["*"])
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print("File modified")

# get frontpage
@app.route("/",methods=['GET'])
def frontpage():
    return render_template('frontend.html')

def start_task(entered_data):
    # analyse function is imported from analyser.py
    final_output,optimised_final_output=analyse(entered_data)
    return final_output,optimised_final_output

@app.route("/submit",methods=['POST'])
def submitted():
    entered_data = request.get_json()    
    # get entered ticker symbol
    ticker_symbol = entered_data['symbol']
    ticker = yf.Ticker(str(ticker_symbol))
    try:
        # send input for analysis
        final_output,optimised_final_output = start_task(entered_data)
        response_data = {
            'final_output': final_output,
            'optimised_final_output': optimised_final_output
        } 

    except:
        # error if ticker symbol is not valid
        response_data={
            'error': 'Please Enter Valid Ticker Symbol.'
            }
    return Response(json.dumps(response_data, sort_keys=False))
         
          
        
        



if __name__=="main":
    observer = Observer()
    event_handler = MyHandler()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()
    app.run(debug=True)    
        

