from flask import Flask, request, Response
import os
from langchain_community.llms.ollama import Ollama
app = Flask(__name__)


llm = Ollama(
    # model="llama3:8b-instruct-q5_K_M",
    # model="mistral:7b-instruct-v0.3-q5_K_M",
    model="qwen2.5:0.5b",
    temperature=0.1,
    top_k=50,
    top_p=0.95,
    repeat_penalty=1.1,
    num_ctx=8192,
    num_predict=4096,
    num_thread=int(os.cpu_count() / 2)
)
def stream(input_text):
    for line in llm.stream(input_text):
        print(line)
        yield line


@app.route('/completion', methods=['GET', 'POST'])
def completion_api():
    if request.method == "POST":
        data = request.get_json()
        input_text = data['input_text']
        return Response(stream(input_text), mimetype='text/event-stream')
    else:
        return Response(None, mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000,debug=True)
