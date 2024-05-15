import openai

# Set OpenAI API key
openai.api_key = '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'

def generate_latex_from_text(text):
    # Generate LaTeX from text using ChatGPT
    response = openai.Completion.create(
        model="gpt-3.5-turbo-0125",
        prompt=text,
        max_tokens=1500,
        temperature=0.7,
        stop="\n\n"
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    # Read input text from file
    with open('analysis_log_SVM.txt', 'r') as f:
        input_text = f.read()

    # Generate LaTeX from input text
    latex_output = generate_latex_from_text(input_text)

    # Write LaTeX output to file
    with open('output_latex.txt', 'w') as f:
        f.write(latex_output)
