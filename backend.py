from flask import Flask, request, render_template,jsonify,make_response
from flask_cors import CORS
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from analyser import analyse
import yfinance as yf
import requests

app = Flask(__name__, template_folder='static_file')
cors = CORS(app)
cors = CORS(app, origins=["*"])
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print("File modified")

@app.route("/",methods=['GET'])
def frontpage():
    return render_template('frontend.html')

def start_task(entered_data):
    final_output,optimised_final_output,final_plot,optimized_final_plot=analyse(entered_data)
    return final_output,optimised_final_output,final_plot,optimized_final_plot

@app.route("/submit",methods=['POST'])
def submitted():
    entered_data = request.get_json()    
    print(entered_data)
    ticker_symbol = entered_data['symbol']
    ticker = yf.Ticker(str(ticker_symbol))
    try:
        final_output,optimised_final_output = start_task(entered_data)
        print('********',final_output)
        response_data = {
            'final_output': final_output,
            'optimised_final_output': optimised_final_output
        } 
        return jsonify(response_data)
    except:
        return jsonify({'error': 'Please Enter Valid Ticker Symbol.'})
         
          
        
        



if __name__=="main":
    observer = Observer()
    event_handler = MyHandler()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()
    app.run(debug=True)    
        

