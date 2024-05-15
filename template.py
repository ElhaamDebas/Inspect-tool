def generate_latex_from_text(text, output_file):
    # Write LaTeX output to file
    with open(output_file, 'w') as f:
        f.write(text)

if __name__ == "__main__":
    # Read input text from file
    with open('output_latex.txt', 'r') as f:
        latex_content = f.read()

    # Generate LaTeX file
    generate_latex_from_text(latex_content, 'output_latex.tex')
