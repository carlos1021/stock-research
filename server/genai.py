from flask import Flask, render_template, jsonify, Response
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import random
import os

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
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
CORS(app, origins=['http://localhost:8000'])

@app.route('/make_decision', methods=['GET', 'POST'])
def conversation():
	completion = client.chat.completions.create(
		model=MODEL,
		messages=[
			{"role": "system", "content": """
                 You are an intelligent assistant tasked with making a decision. You will base your decision 
                on input data that a user sends. The following decisions are as follows:
                A: the user would like textual information about news sentiment; information 
                about a company, industry, or general discipline in finance or economics; general 
                information that can be found through stock news or financial journalist websites.
                B: the user would like a graph visualization generated using the matplotlib.pyplot 
                library. The visualization will be dependent on user query and data received.
                C: the user would like to seek insight from either user input data or data collected 
                from external sources, such as AlphaVantage and/or Yahoo Finance. 
                Your response will be either A,B, or C, depending on which task the user would 
                like accomplished. Here is the following task received from the user: {INSERT_USER_PROMPT_HERE}.
                Return only the label as your response–nothing else.
                      
            """},
			{"role": "user", "content": None}
		]
	)
	return jsonify({'GPT Response': completion.choices[0].message.content})



@app.route('/plot')
def plot():
    import matplotlib.pyplot as plt
    import pandas as pd
    import io

    # Code to generate a graph visualization
    df = pd.read_csv('../data/stock_data.csv')
    df['Date'] = pd.to_datetime(df['Date'])

    # Plotting
    plt.figure(figsize=(12, 6))

    # Assuming there are five unique companies in the dataset
    unique_companies = df['Company'].unique()

    # Iterate through each company and plot its opening prices
    for company in unique_companies:
        company_data = df[df['Company'] == company]
        plt.plot(company_data['Date'], company_data['Open'], label=company)

    # Customize the plot
    plt.title("Opening Prices of Companies Over Time")
    plt.xlabel("Date")
    plt.ylabel("Opening Price")
    plt.legend(title="Company")
    plt.grid(True)
    plt.tight_layout()

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
