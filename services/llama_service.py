import requests
import json

def generate_summary(student):
    try:
        llama_url = "http://localhost:11434/api/generate"
        payload = {
            "model": "llama3.2",
            "prompt": f"Generate a short hypothetical professional 2-3 lines summary for student {student.name}, age {student.age}, email {student.email}. don't include anything like here is summary etc...    "
        }

        response = requests.post(llama_url, json=payload, stream=True)
        response.raise_for_status()

        summary = ""
        for line in response.iter_lines():
            if line:
                try:
                    chunk = json.loads(line)
                    summary += chunk.get("response", "")
                except ValueError:
                    continue
        return summary.strip()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to generate summary: {str(e)}")
