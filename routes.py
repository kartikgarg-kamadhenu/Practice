from flask import request,jsonify,Blueprint
from project_colordetection import app
from project_colordetection.functions.functions import allowed_file,top_colors1,create_logger
from werkzeug.utils import secure_filename
import os
import requests

logger=create_logger()
upload=Blueprint('upload',__name__)

@upload.route('/upload', methods=['POST'])
def upload_file():  
    
    
    
    
    if request.method=='POST':
        
        try:
        
            if request.form['url']:
                
                url=request.form['url']
                fn,fext=os.path.splitext(url)
                filename=secure_filename(fn)+fext
                
                try:
                    response=requests.get(url)
                    file=os.path.join(app.config['UPLOAD_FOLDER'],filename)
                    with open (file,'wb') as f:
                        f.write(response.content)
                    a=top_colors1(file)
                    output=a
                    logger.debug("The input file was valid.")
                    return jsonify(output)
        
                except:
                    return jsonify("Image is not downloadable")
            
        except:
            
            if 'file' not in request.files:
                logger.warning("key 'file' was missing")
                return jsonify({"error":"no file part"})
            
            file = request.files['file']
            if file.filename=='' or not(file.filename.strip()):
                logger.warning("no file was selected")
                return jsonify({"error":"no selected file"})
            
            
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                #output = predict(file_path)
                
                try:
                    
                    a=top_colors1(file)
                    output=a
                    logger.debug("The input file was valid.")
                    return jsonify(output)
                
                except:
                
                    logger.error("some error in the code or file error")
                    return jsonify({"error":"file error"})
            
            else:
            
                logger.warning("the file input was not in the allowed extensions")
                return jsonify({"error":"invalid file"})
            
        else:
            
            logger.error("code failed")
            return jsonify({"message":"some error occured."})
    
#    except:
#        
#        logger.warning("Invalid json or some key value pair were missing")
#        return jsonify({"Message":"Data is invalid/missing"})
#    