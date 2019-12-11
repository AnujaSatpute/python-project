from flask import Flask,request, redirect, render_template,url_for
from functions.models import TourDoModel,Schema

app = Flask(__name__)


@app.route('/hey') 
def hello():
    return "<h1><b>Hello</b></h1>"

@app.route('/') #this is when user hits url
def sql_database():
   
    results = TourDoModel().list_items()
    #print('results',results)
    return render_template('tourdo.html',results=results)


@app.route('/insert',methods = ['POST', 'GET']) #this is when user submits an insert
def insert():
    if request.method == 'POST':
       #cid=request.form['cid']
       cname=request.form['cname']
       pname=request.form['packagename']
       dest=request.form['destination']
       TourDoModel().sql_edit_insert((cname,pname,dest))
       
       return redirect(url_for('sql_database'))
       #return "<h1> Hey in insert</h1>"

@app.route('/delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def delete():
    print("Inside delete")
    if request.method == 'GET':
        ID = request.args.get('ID')
        #print("lname",ID)
        TourDoModel().sql_delete((ID,))
        return redirect(url_for('sql_database'))

@app.route('/query_edit',methods = ['POST', 'GET']) #this is when user clicks edit link
def editlink():
    if request.method == 'GET':
        ID=request.args.get('ID')
        where=' and cid='+ID
        eresults=TourDoModel().list_items(where)
        results=TourDoModel().list_items()
        #print('eresults',eresults)
        return render_template('tourdo.html',eresults=eresults,results=results)

@app.route('/edit',methods = ['POST', 'GET']) #this is when user submits an edit
def edit():
    """old_cid=request.form['old_CID']"""
    cname=request.form['cname']
    packagename=request.form['packagename']
    destination=request.form['destination']  
    cid=request.form['old_CID']
    TourDoModel().sql_edit((cname,packagename,destination,cid))
    return redirect(url_for('sql_database'))

if __name__ == "__main__":
    Schema()
    app.run(debug=True)
