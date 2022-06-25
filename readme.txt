# Readme - url-short-py

# available at https://url-shortener-py-nmeier.herokuapp.com/


# Running locally - instructions:
# pip install -r requirements.txt
# python3 url-short.py
# connect to localhost:5000
# type in urls in textbox when prompted



#
# notes on current implementation:
#  - originally wanted to do this with AWS lambda and DynamoDB -> arguably outside the scope of this assignment, with more time it could be done
#	- See https://url-shortener-py-nmeier.herokuapp.com/9f508b3 for cloudarch map
#  - decided on a simpler implementation avaliable with python flask web app
#
#  - Could spend time to make front end look better, highly optional for a tool such as this


#
#  - Further features could include the following:
#	- View for all entries in the DB for shortlinks
#	- Tools to delete existing short link entries / tool to remove entry from database
#	- when hosting, a short domain would need to be applied if hosted in a public/cloud network
#		- on an private network this could be configured without a need for a domain iirc and still have a user friendly short sized base url 
#			- IE: instead of https://url-shortener-py-nmeier.herokuapp.com/<short-url> it could probably be https://<internal-ip-addr>/<short-url>
# 	- Should probably make the printed short url a hyperlink (might do that later)
#	
#  - Considerations for maintanence:
#	- The app is currently hosted on heroku
#	- Deployment is done via pushes to a master/main branch --> pushes to heroku origin should be carefully protected to prevent downtime
#	- webapp and db are hosted on same virtual environment, db backups should be considered to avoid losing data
#	- a regular restart on the hostmachine could be implementeted to reduce need for maintanence
#	- with heroku's deployment, near zerodowntime possibly? would need to be researched more
#
