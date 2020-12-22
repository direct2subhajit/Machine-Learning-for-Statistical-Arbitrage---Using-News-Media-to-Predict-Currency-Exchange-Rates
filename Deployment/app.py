from flask import Flask, render_template,request, redirect, url_for
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
import datetime
from datetime import datetime 
import pandas as pd
from decimal import *

app=Flask(__name__)
@app.route('/')
def FER():
    return render_template('FER.html')

@app.route('/FER',methods=['GET','POST'])
def index():
    extra_line1=''
    extra_line2=''
    if request.method == 'POST':
        From=request.form['From']
        To=request.form['To']
        Amount=request.form['Amount']
        amt = Decimal(Amount)
        Date=request.form['Date']
        #dt = datetime.strptime (Date, "% Y ,% m ,% d")
        dt = pd.datetime.strptime(Date, '%d%b%y')
        c = CurrencyRates(force_decimal=True)
        result = c.convert(From, To, amt,dt)
        c = CurrencyCodes()
        code = c.get_symbol(To)
        extra_line1 = f'The Currency Converted is :{code}'
        extra_line2 = f'{result}'
    return render_template("FER.html",cd = extra_line1,new = extra_line2)
    
if __name__ == "__main__":
    app.run(debug=True)