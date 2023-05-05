import requests

# importing flask
from flask import Flask, render_template
  
# importing pandas module
import pandas as pd

response = requests.get('https://api.github.com/search/repositories?q=fun+python&s=stars')
jsonout=response.json()
outdata =[]
for x in jsonout['items']:
    listing =[x["full_name"],x["html_url"],x["stargazers_count"]]
    outdata.append(listing)
df=pd.DataFrame(outdata)
print(df)

app = Flask(__name__)

# route to html page - "table"
@app.route('/')
@app.route('/table')
def table():
    
    data = df
    return render_template('table.html', tables=[data.to_html()], titles=[''])

  
if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"))
