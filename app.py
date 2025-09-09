from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load the financial data
df = pd.read_csv('financial-data.csv')

# Convert numeric columns to float
numeric_columns = ['Total Revenue', 'Net Income', 'Total Assets', 'Total Liabilities', 'Cash Flow from Ops']
for col in numeric_columns:
    df[col] = df[col].replace(',', '', regex=True).astype(float)

# Define supported queries
supported_queries = [
    "What is the total revenue of [company] in [year]?",
    "What is the net income of [company] in [year]?",
    "What are the total assets of [company] in [year]?",
    "What is the debt-to-assets ratio of [company] in [year]?",
    "How has net income changed for [company] from [previous_year] to [year]?"
]

@app.route('/', methods=['GET', 'POST'])
def chatbot():
    response = "Welcome to the Financial Chatbot! Ask about financial data for Apple, Microsoft, or Tesla.<br>Examples:<br>" + "<br>".join(supported_queries)
    if request.method == 'POST':
        user_input = request.form['query'].lower().strip()
        
        # Parse input
        company = None
        year = None
        metric = None
        
        if "apple" in user_input:
            company = "apple"
        elif "microsoft" in user_input:
            company = "microsoft"
        elif "tesla" in user_input:
            company = "tesla"
        
        for y in [2022, 2023, 2024, 2025]:
            if str(y) in user_input:
                year = y
        
        if "total revenue" in user_input or "revenue" in user_input:
            metric = "Total Revenue"
        elif "net income" in user_input or "profit" in user_input:
            metric = "Net Income"
        elif "total assets" in user_input or "assets" in user_input:
            metric = "Total Assets"
        elif "debt-to-assets ratio" in user_input or "debt ratio" in user_input:
            metric = "Debt-to-Assets Ratio"
        elif "how has net income changed" in user_input:
            metric = "Net Income Change"
        
        # Fetch and respond
        if company and year and metric:
            if metric == "Debt-to-Assets Ratio":
                result = df[(df['Company'] == company) & (df['Year'] == year)]
                if not result.empty:
                    value = result['Total Liabilities'].values[0] / result['Total Assets'].values[0]
                    response = f"The debt-to-assets ratio for {company.capitalize()} in {year} was {value:.2f}."
                else:
                    response = f"No data found for {company.capitalize()} in {year}."
            elif metric == "Net Income Change":
                current = df[(df['Company'] == company) & (df['Year'] == year)]
                previous = df[(df['Company'] == company) & (df['Year'] == year-1)]
                if not current.empty and not previous.empty:
                    current_val = current['Net Income'].values[0]
                    previous_val = previous['Net Income'].values[0]
                    change = ((current_val - previous_val) / previous_val) * 100
                    direction = "increased" if change > 0 else "decreased"
                    response = f"Net income for {company.capitalize()} {direction} by {abs(change):.2f}% from {year-1} to {year}."
                else:
                    response = f"Data not available for {company.capitalize()} for both {year} and {year-1}."
            else:
                result = df[(df['Company'] == company) & (df['Year'] == year)][metric]
                if not result.empty:
                    value = result.values[0] / 1000  # Convert to billions
                    response = f"{metric} for {company.capitalize()} in {year} was {value:.3f} billion USD."
                else:
                    response = f"No data found for {company.capitalize()} in {year}."
        else:
            response = "Sorry, I didn't understand your question. Try one of these:<br>" + "<br>".join(supported_queries)
    
    return render_template('chatbot.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)