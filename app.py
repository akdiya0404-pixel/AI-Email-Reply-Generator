import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from google import genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    try:
        if not api_key:
            return jsonify({
                "error": "Gemini API key was not found in the .env file."
            }), 500

        data = request.get_json(silent=True)

        if not data:
            return jsonify({
                "error": "No data was received."
            }), 400

        email = data.get("email", "").strip()
        tone = data.get("tone", "Professional").strip()

        if not email:
            return jsonify({
                "error": "Please enter an email."
            }), 400

        client = genai.Client(api_key=api_key)

        prompt = f"""
You are an intelligent email reply assistant.

Read the received email carefully and write an appropriate reply.

Selected tone: {tone}

Received email:
{email}

Instructions:
- Write only the email reply.
- Do not explain your reasoning.
- Keep the reply clear and natural.
- Do not invent facts, dates, names, or commitments.
- Use a suitable greeting and closing.
"""

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        if not response.text:
            return jsonify({
                "error": "Gemini returned an empty response."
            }), 500

        return jsonify({
            "reply": response.text.strip()
        })

    except Exception as error:
        print("Gemini error:", error)

        return jsonify({
            "error": str(error)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)