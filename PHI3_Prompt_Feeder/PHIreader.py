import ollama
import os
import matplotlib.pyplot as plt
import numpy as np


class PhiModel:
    
    def __init__(self, model_name="phi3.5"):
        self.model_name = model_name

    def generate_response(self, prompt):
        

        instruction = "Read this review and tell me if it is Positive, negative, or neutral. Use only the word Positive, negative, or neutral."
        full_prompt = f"{instruction} {prompt}"

        message = ""
        stream = ollama.chat(
            model=self.model_name,
            messages=[{'role': 'user', 'content': full_prompt}],
            stream=True,
        )

        # Collects the streamed response
        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)
            message += chunk['message']['content']
        print("\n")
        return message


class PromptProcessor:
    #Handles the processing of prompts from the model
    def __init__(self, output_file, model, additional_directory=None):
        self.output_file = output_file
        self.model = model
        self.additional_directory = additional_directory
        self.file_sentiment_data = []  # To store sentiment counts for each file

    def process_prompts(self):
        
        message_num = 0

        def process_file(file_path):
            nonlocal message_num
            positive = 0
            negative = 0
            neutral = 0

            with open(file_path, "r", encoding="utf-8") as f:
                current_review = ""
                for line in f:
                    line = line.strip()

                    # Skip empty lines and lines starting with certain keywords
                    if not line or line.startswith("#") or line.startswith("-") or line.startswith("Review ID"):
                        continue

                    
                    if line.startswith("Review Content:"):
                        if current_review:
                            # Process the current review content
                            message_num += 1
                            print(f"Processing review {message_num}: {current_review}")
                            response = self.model.generate_response(current_review)
                            with open(self.output_file, "a", encoding="utf-8") as output_f:
                                output_f.write(f"\n\n{message_num}: {response}")

                            # Update counts
                            if "POSITIVE" in response.strip().upper():
                                positive += 1
                            elif "NEGATIVE" in response.strip().upper():
                                negative += 1
                            else:
                                neutral += 1

                            current_review = ""

                        # Start a new review
                        current_review = line.replace("Review Content:", "").strip()
                    else:
                        # Continue building the current review
                        current_review += f" {line}"

                # Process the last review in the file
                if current_review:
                    message_num += 1
                    print(f"Processing review {message_num}: {current_review}")
                    response = self.model.generate_response(current_review)
                    with open(self.output_file, "a", encoding="utf-8") as output_f:
                        output_f.write(f"\n\n{message_num}: {response}")

                    # Update counts
                    if response.strip().upper() == "POSITIVE":
                        positive += 1
                    elif response.strip().upper() == "NEGATIVE":
                        negative += 1
                    else:
                        neutral += 1

            # Append sentiment data for this file
            self.file_sentiment_data.append({
                "file": os.path.basename(file_path),
                "positive": positive,
                "negative": negative,
                "neutral": neutral,
            })

        # Process files in reviews directory
        if self.additional_directory:
            for filename in os.listdir(self.additional_directory):
                if filename.endswith(".txt"):
                    file_path = os.path.join(self.additional_directory, filename)
                    print(f"\nReading reviews from: {file_path}")
                    process_file(file_path)

        # Generate a master bar chart
        self.generate_master_chart()

    def generate_master_chart(self):
        
        files = [data["file"] for data in self.file_sentiment_data]
        positive_counts = [data["positive"] for data in self.file_sentiment_data]
        negative_counts = [data["negative"] for data in self.file_sentiment_data]
        neutral_counts = [data["neutral"] for data in self.file_sentiment_data]

        x = np.arange(len(files))  # the label locations
        width = 0.25  # the width of the bars

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(x - width, positive_counts, width, label="Positive", color="green")
        ax.bar(x, negative_counts, width, label="Negative", color="red")
        ax.bar(x + width, neutral_counts, width, label="Neutral", color="blue")

        # Add labels, title, and legend
        ax.set_xlabel("Files")
        ax.set_ylabel("Counts")
        ax.set_title("Sentiment Analysis by File")
        ax.set_xticks(x)
        ax.set_xticklabels(files, rotation=45, ha="right")
        ax.legend()

        # Save the chart
        plt.tight_layout()
        plt.savefig("sentiment_analysis_master_chart.png")
        plt.close()
        print("Saved master sentiment analysis chart as 'sentiment_analysis_master_chart.png'.")

if __name__ == "__main__":
    
    output_path = "PHI3_Prompt_Feeder/output.txt"
    additional_dir = "Webscraper/Reviews"

    # Initialize the model and processor
    phi_model = PhiModel(model_name="phi3.5")
    processor = PromptProcessor(
        
        output_file=output_path,
        model=phi_model,
        additional_directory=additional_dir
    )

    # Start processing prompts
    processor.process_prompts()
