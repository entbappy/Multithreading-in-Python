from flask import Flask, render_template, request, jsonify
import time
import threading


app = Flask(__name__)



def trainModel():
    print("Loading data..")


def loadData():
    time.sleep(30)
    print("Load..")

class TrainModel (threading.Thread):
    def __init__(self, data):
        threading.Thread.__init__(self)
        self.data = data
    def run(self):
        # return model loss
        self._return = trainModel()    
    def join(self):
        threading.Thread.join(self)
        return self._return


class LoadData (threading.Thread):
    def __init__(self, filenames):
        threading.Thread.__init__(self)
        self.filenames = filenames
    def run(self):        
        # return data
        self._return = loadData()
    def join(self):
        threading.Thread.join(self)
        return self._return



@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')


@app.route('/train', methods=['POST'])  # This will be called from UI
def train_model():
    if (request.method=='POST'):
          for _ in range(10):
            # loadData
            loadThread = LoadData(None)
            loadThread.start()
            
            # trainModel
            trainThread = TrainModel(None)
            trainThread.start()
            
            # only continue if both threads are done
            modelLoss = trainThread.join()
            data = loadThread.join()

            return jsonify({'status': 'success'})



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000,debug=True)
