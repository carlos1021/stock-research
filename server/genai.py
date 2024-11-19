from flask import Flask, render_template, jsonify, Response
import matplotlib.pyplot as plt
from flask_cors import CORS
from openai import OpenAI
import random
import os
import io

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
MODEL='gpt-4o-mini'
client = OpenAI(api_key=OPENAI_API_KEY)

'''
OpenAI Cookbook: Building a Bring Your Own Browser for real-time information
https://cookbook.openai.com/examples/third_party/web_search_with_google_api_bring_your_own_browser_tool

Zixuan Notes: Create AI that can provide specific methods/models needed for financial problems. eg.Discount cash flow
Generate models in excel or csv file that can be downloaded, user can work directly from there

11/17 Notes (Chatbot)
Data/Technologies/Softwares:
- OpenAI (create conversation; make inferences; feed in large quantities of data)
- yfinance (collect stock data)
- alphavantage (collect news data)
- Website for the generative ai feature

Things we can create:
1. text-based chatbot
	- ask questions about industries
	- ask questions about companies
	- ask to make a prediction
	- ask to analyze data (user uploads, yfinance collects)
	- generate graphs
'''
"""GENERATING GRAPH USING FLASK BACKEND"""

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # HTML file with <img src="/plot">

@app.route('/plot')
def plot():
    import matplotlib.pyplot as plt
    import io

    # Generate the plot
    plt.figure(figsize=(6, 4))
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.title("Sample Plot")

    # Save to a BytesIO object
    with io.BytesIO() as img:
        plt.savefig(img, format='png')
        img.seek(0)
        return Response(img.read(), mimetype='image/png')
    # The context manager ensures `img` is closed after use.


if __name__ == '__main__':
    app.run(debug=True)



"""GENERATING A GRAPH BASED ON INPUT DATA (OPENAI API)"""
# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the CSV data
# file_path = "../data/stock_data.csv"
# data = pd.read_csv(file_path)

# # Convert the 'Date' column to datetime format
# data['Date'] = pd.to_datetime(data['Date'])

# # Plotting
# plt.figure(figsize=(12, 6))

# # Assuming there are five unique companies in the dataset
# unique_companies = data['Company'].unique()

# # Iterate through each company and plot its opening prices
# for company in unique_companies:
#     company_data = data[data['Company'] == company]
#     plt.plot(company_data['Date'], company_data['Open'], label=company)

# # Customize the plot
# plt.title("Opening Prices of Companies Over Time")
# plt.xlabel("Date")
# plt.ylabel("Opening Price")
# plt.legend(title="Company")
# plt.grid(True)
# plt.tight_layout()

# # Show the plot
# plt.show()


"""ALPHA VANTAGE API EXAMPLE"""
# import requests
# from flask import Flask

# app = Flask(__name__)

# # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&apikey=NAPX45F36YMYXH7S'

# @app.route('/')
# def alpha_vantage():
# 	r = requests.get(url)
# 	data = r.json()
# 	return data

# if __name__ == '__main__':
# 	app.run(host='0.0.0.0', port=5000, debug=True)

"""OPENAI API EXAMPLE"""
# OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
# MODEL='gpt-4o-mini'
# client = OpenAI(api_key=OPENAI_API_KEY)
# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}})


# @app.route('/compute', methods=['GET', 'POST'])
# def compute():
# 	try:
# 		random_number = random.randint(1, 100)
# 		return jsonify({'generatedNumber': random_number})
# 	except Exception as e:
# 		return jsonify({'error': str(e)}), 500

# @app.route('/genai', methods=['GET', 'POST'])
# def conversation():
# 	completion = client.chat.completions.create(
# 		model=MODEL,
# 		messages=[
# 			{"role": "system", "content": "You are a helpful assistant that gives the U.S. Stock Market Forecast for a given day."},
# 			{"role": "user", "content": "Hello! Can you provide me information about how the stock market behaved on Tuesday, November 5th, 2024?"}
# 		]
# 	)
# 	return jsonify({'GPT Response': completion.choices[0].message.content})

# if __name__ == '__main__':
# 	app.run(host='0.0.0.0', port=5000, debug=True)
