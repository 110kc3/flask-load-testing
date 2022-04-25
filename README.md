# load-testing
Project url: https://oceanic-glazing-347308.lm.r.appspot.com



https://oceanic-glazing-347308.lm.r.appspot.com/view
gets all data in the database 

https://oceanic-glazing-347308.lm.r.appspot.com/api/uuid
generates 1 uuid for each refresh


POST request with form-data:
generate=1

https://oceanic-glazing-347308.lm.r.appspot.com/api/uuid
generates 1 uuid for each request and saves it to the database


When deploying to GCP
# this line from main.py 
if __name__ == '__main__':

deploy with:
gcloud app deploy