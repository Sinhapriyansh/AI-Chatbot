import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


API_KEY = "AIzaSyC200mLb4VolbkemhUQ53dhZDR0B73hcDs"

def get_local_response(text):
    text = text.lower()
    if "hi" in text or "hello" in text:
        return "Hello Sir! I am AI CHATBOT. How can I assist you today?"
    if "who are you" in text:
        return "I am AI CHATBOT, your Neuro-Logic Assistant."
    if "code" in text:
        return "Sure! Here is a sample logic:\n\nprint('Hello from AI CHATBOAT')"
    return "I am currently in smart-sync mode. How else can I help you, Sir?"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_text = request.form["msg"]
    
    
    model_name = "gemini-1.0-pro" 
    url = f"https://generativelanguage.googleapis.com/v1/models/{model_name}:generateContent?key={API_KEY}"
    
    try:
        response = requests.post(url, json={"contents": [{"parts": [{"text": user_text}]}]}, timeout=5)
        
        if response.status_code == 200:
            return jsonify({"response": response.json()['candidates'][0]['content']['parts'][0]['text']})
        else:
            
            return jsonify({"response": get_local_response(user_text)})
            
    except:
        
        return jsonify({"response": get_local_response(user_text)})

if __name__ == "__main__":
    app.run(debug=True)