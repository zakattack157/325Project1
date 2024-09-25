import ollama


input_file = open("input.txt", "r")

output_file = open("output.txt", "a")

for line in input_file:
    prompt = line.strip()  # Remove leading/trailing whitespace

    if not prompt or prompt.startswith('#'):  # Skip empty lines and lines starting with '#'
        continue

    message = ""

    stream = ollama.chat(
        model='phi3.5',
        messages=[{'role': 'user', 'content': prompt}],
        stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
        message += chunk['message']['content']

    output_file.write(message + '\n')  
    print('\n')


input_file.close()
output_file.close()
