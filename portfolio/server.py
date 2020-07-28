from flask import Flask, request, render_template, redirect
import whatsapp_sender
from mailchecker import check_mail_valid
from csv_append import csv_append

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:pages>')
def page(pages):
    try:
        return render_template(pages)
    except:
        return redirect('error.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def form():
    try:
        error = None
        if request.method == 'POST':
            data = request.form.to_dict()
            print(data)
            if check_mail_valid(data['email']):
                return redirect('disposable.html')
            try:
                whatsapp_sender.whatsapp_send(data)
                csv_append(data)
            except:
                pass

        return render_template('./thankyou.html', name=data['user'])
    except:
        return redirect('error.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
