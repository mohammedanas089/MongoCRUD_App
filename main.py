from flask import Flask,render_template,flash,redirect,url_for,request
from forms import *
from bson import ObjectId
'''
import secrets
secrets.token_hex(16)
'''
app = Flask(__name__)
app.config['SECRET_KEY']='a6117d75525f998d655339b828aa727e'

import pymongo
myclient = pymongo.MongoClient("mongodb://172.17.0.2:27017/")
db = myclient['hospitalDb']


@app.route("/")
@app.route("/home")
def home():
    collection_names = db.list_collection_names()
    return render_template('home.html', colList=collection_names)




@app.route("/crt",methods=['GET','POST'])
def create():
    col = request.args.get("value")
    if col == "patientCol":
        createForm=Patient()
        collection = db['patientCol']
        if createForm.validate_on_submit():
            collection.insert_one({
                'name':createForm.username.data,
                'mail':createForm.email.data,
                'pass':createForm.pin.data,
            })
            flash('Data Entry done')
            return redirect(url_for('create',value=col))
        return render_template('create.html',title="Create",form=createForm,data=collection.find())
    elif col=="doctorCol":
        createForm=Doctor()
        collection = db['doctorCol']
        if createForm.validate_on_submit():
            collection.insert_one({
                'name':createForm.username.data,
                'mail':createForm.email.data,
                'pass':createForm.pin.data,

            })
            flash('Data Entry done')
            return redirect(url_for('create'))
        return render_template('create.html',value=collection,title="Create",form=createForm,data=collection.find())
    


@app.route('/edit/<string:record_id>', methods=['GET', 'POST'])
def edit_record(record_id):
    collection = db['patientCol']
    record = collection.find_one({'_id': ObjectId(record_id)})

    if not record:
        return "Record not found."

    editForm = Patient(obj=record)  # Prepopulate the form with the existing data

    if request.method == 'POST':
        collection.update_one({'_id': ObjectId(record_id)}, {
        '$set': {
            'name': editForm.username.data,
            'mail': editForm.email.data,
            'pass': editForm.pin.data,
        }
        })
        return redirect(url_for('create',value="patientCol"))
    if request.method=='GET':

            # Update the record in MongoDB with the edited data
    
        return render_template('create.html', title="Edit", form=editForm, record=record)


@app.route('/del/<string:record_id>')
def delete_record(record_id):
    collection = db['patientCol']
    # Use PyMongo to delete the record from MongoDB
    collection.delete_one({'_id': ObjectId(record_id)})
    # Redirect back to the page displaying the records after deletion
    return redirect(url_for('create',value="patientCol"))



if __name__=="__main__":
    app.run(debug=True)
