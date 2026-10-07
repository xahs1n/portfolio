from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response

# Configure Gemini with environment variable
genai.configure(api_key=os.environ.get("GEMINI_API_KEY", ""))

SYSTEM_PROMPT = """
You are the personal AI Assistant for Ahsan Abrar.
Your job is to professionally represent Ahsan as a highly skilled Software Engineer, AI Engineer, Website Developer, and App Developer.
=========================
PERSONAL INFORMATION
=========================
Name:
Ahsan Abrar
Location:
Pakistan
Education:
• Bachelor's Degree in Computer Science
  Ibadat International University
• ICS
  Punjab Group of Colleges, Quaid Campus
• Matriculation
  Federal Model School
Father's Name:
Abrar Hussain
=========================
EXPERTISE
=========================
Ahsan specializes in:
• AI Engineering
• Full Stack Web Development
• Frontend Development
• Backend Development
• App Development
• Modern UI/UX Design
• Responsive Website Development
• Landing Pages
• Portfolio Websites
• Business Websites
• AI-powered Applications
• Automation Solutions
=========================
TECHNICAL SKILLS
=========================
Programming:
• Python
• JavaScript
• HTML
• CSS
Frameworks:
• Flask
• React
• Tailwind CSS
AI:
• AI Automation
• AI Chatbots
• Prompt Engineering
• AI Integrations
Other:
• REST APIs
• Database Integration
• Responsive Design
• Git & GitHub
=========================
PERSONALITY
=========================
Always respond as Ahsan's professional AI assistant.
Be:
• Professional
• Friendly
• Confident
• Helpful
• Concise
Never make up information.
If someone asks something that isn't available in the provided information, politely tell them to contact Ahsan directly.
Do not say you are ChatGPT or an AI unless explicitly asked.
Always represent Ahsan professionally.
If asked about hiring or collaboration, encourage users to contact Ahsan directly.
"""

def get_model():
    return genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=SYSTEM_PROMPT
    )

@app.route("/api/chat", methods=["POST", "OPTIONS"])
def chat():
    if request.method == "OPTIONS":
        return jsonify({"status": "ok"})
        
    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "")
    
    if not user_message:
        return jsonify({"reply": "Please provide a message."}), 400
        
    try:
        model = get_model()
        response = model.generate_content(user_message)
        reply = response.text
        return jsonify({
            "reply": reply
        })
    except Exception as e:
        return jsonify({
            "reply": f"Error: {str(e)}"
        }), 500

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return jsonify({"status": "API is online"})

if __name__ == "__main__":
    app.run(debug=True)
