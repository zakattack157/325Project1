#This script takes input from input.txt, processes those inputs as prompts for the phi3.5 model, and then stores the outputs in the output.txt file

#SDK for Ollama models that allows for communication to local models; based on the Ollama restAPI
import ollama



input_file = open("input.txt", "r")

output_file = open("output.txt", "a")

#reads through each line in the input file and feeds the model those lines
message_num = 0
for line in input_file:
    prompt = line.strip()  # Remove leading/trailing whitespace
    

    if not prompt or prompt.startswith('#'):  # Skip empty lines and lines starting with '#'
        continue
    
    print(prompt)
    message_num += 1
    message = ""

    #main point of contact with model where prompt is fed and output is recorded in output.txt
    #the format for this is a key/value pair that reads the role of the prompt asker as well as the prompt itself
    stream = ollama.chat(
        model='phi3.5',
        messages=[{'role': 'user', 'content': prompt}],
        stream=True,
    )

    #output is broken down into readable chunks so the output doesnt wait for the entire response.
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
        message += chunk['message']['content']

    #writes output in output.txt in format of <prompt#>: <response>
    output_file.write('\n\n' + str(message_num) + ': ' + message)  
    print('\n')


input_file.close()
output_file.close()
