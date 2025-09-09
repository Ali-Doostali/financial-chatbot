# BCG Financial Chatbot

A web-based financial chatbot developed for BCG's GenAI Job Simulation on Forage. This project uses Python, Pandas, and Flask to process financial data and answer queries about companies like Apple, Microsoft, and Tesla, with a vibrant and responsive user interface.

## Features
- **Data Processing**: Uses Pandas to parse and analyze financial data from a CSV file (`financial-data.csv`) based on 10-K reports.
- **Supported Queries**:
  - Total revenue of a company in a specific year.
  - Net income of a company in a specific year.
  - Total assets of a company in a specific year.
  - Debt-to-assets ratio of a company in a specific year.
  - Year-over-year net income change for a company.
- **User Interface**: Responsive and colorful UI with Poppins font, Font Awesome icons, and CSS animations (gradient backgrounds, hover effects).
- **Deployment**: Hosted on GitHub Codespaces for easy online access and testing.
- **Technologies**: Python, Flask, Pandas, HTML, CSS, Git, GitHub Codespaces.

## Project Structure
```
financial-chatbot/
├── .devcontainer/
│   └── devcontainer.json  # Configures Codespaces environment
├── templates/
│   └── chatbot.html       # HTML template for the web interface
├── app.py                 # Main Flask application
├── financial-data.csv     # Financial data for Apple, Microsoft, Tesla
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
```

## Prerequisites
- **Local Setup**:
  - Python 3.11 or higher
  - Git
  - Pip (Python package manager)
- **GitHub Codespaces**:
  - A GitHub account (free tier includes 60 hours/month of Codespaces usage)
  - Access to this repository: [https://github.com/Ali-Doostali/financial-chatbot](https://github.com/Ali-Doostali/financial-chatbot)

## Local Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ali-Doostali/financial-chatbot.git
   cd financial-chatbot
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Application**:
   ```bash
   python app.py
   ```
4. **Access the Chatbot**:
   - Open `http://localhost:5000` in your browser.
   - Try queries like:
     - "What is the total revenue of Apple in 2023?"
     - "What is the debt-to-assets ratio for Tesla in 2022?"

## Running in GitHub Codespaces
1. **Create a Codespace**:
   - Go to [https://github.com/Ali-Doostali/financial-chatbot](https://github.com/Ali-Doostali/financial-chatbot).
   - Click the green **Code** button, then select the **Codespaces** tab.
   - Click **Create codespace on main**.
   - Wait 2-5 minutes for the Codespace to initialize (VS Code will open in your browser).
2. **Install Dependencies**:
   - The `.devcontainer/devcontainer.json` file automatically runs `pip install -r requirements.txt` on Codespace startup.
   - If dependencies don't install, run manually in the Codespace terminal:
     ```bash
     pip install -r requirements.txt
     ```
3. **Run the Application**:
   - In the Codespace terminal:
     ```bash
     python app.py
     ```
   - A notification will appear: "Your application running on port 5000 is available."
   - Click **Open in Browser** to access the chatbot at a URL like `https://[random-id]-5000.preview.app.github.dev`.
4. **Test the Chatbot**:
   - Enter queries like:
     - "What is the total revenue of Apple in 2023?" (Expected: "Total Revenue for Apple in 2023 was 383.285 billion USD.")
     - "How has net income changed for Tesla from 2023 to 2024?" (Expected: "Net income for Tesla decreased by 52.24% from 2023 to 2024.")
   - Save screenshots of responses for documentation.

## Example Queries and Responses
- **Query**: "What is the total revenue of Apple in 2023?"
  - **Response**: "Total Revenue for Apple in 2023 was 383.285 billion USD."
- **Query**: "What is the debt-to-assets ratio for Apple in 2022?"
  - **Response**: "The debt-to-assets ratio for Apple in 2022 was 0.86."
- **Query**: "How has net income changed for Tesla from 2023 to 2024?"
  - **Response**: "Net income for Tesla decreased by 52.24% from 2023 to 2024."

## Limitations
- Limited to predefined queries for Apple, Microsoft, and Tesla.
- Uses static CSV data, no real-time data integration.
- Rule-based parsing, not advanced NLP.

## Future Improvements
- Add support for more companies and financial metrics.
- Integrate real-time data via APIs.
- Enhance query parsing with NLP (e.g., using transformers).

## Author
- **Ali Doostali**
- GitHub: [https://github.com/Ali-Doostali](https://github.com/Ali-Doostali)
- LinkedIn: [Add your LinkedIn URL here]

## License
This project is licensed under the MIT License.
