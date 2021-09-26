from flask import Flask, request, render_template
import sharemethods
import createbucket
import os
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/upload')
def new_form():
    return render_template('upload.html')

@app.route('/bucket')
def newest_form():
    return render_template('bucket.html')

@app.route('/', methods=['POST'])
def my_form_post():
    bname = request.form['bucket']
    fname = request.form['filename']
    pathname = request.form['path']
    sharemethods.download_files(fname, os.path.join(pathname, fname), bname)
    return 'Go check your folder to see if the file has been downloaded from the cloud!'

@app.route('/bucket', methods=['POST'])
def my_newestform_post():
    bname = request.form['bucket']
    createbucket.create_bucket(bname)
    return "Success!"

@app.route('/upload', methods=['POST'])
def my_newform_post():
    bname = request.form['bucket']
    foname = request.form['folder']
    fname = request.form['filename']
    pathname = request.form['path']
    sharemethods.upload_to_bucket(os.path.join(foname, fname), pathname, bname)
    return 'https://storage.googleapis.com/' + bname + \
            '/' + os.path.join(foname, fname)

