import pandas as pd
import json
from collections import defaultdict

def process_spreadsheet(file_path):
    # Load the CSV file
    df = pd.read_csv(file_path, header=None)

    # Initialize storage for combined questions and their answers
    combined_questions = defaultdict(list)
    combined_answers = defaultdict(list)

    # Get the prompts and responses starting from column R (index 17)
    questions = df.iloc[1, 17:]
    responses = df.iloc[3:, 17:]

    jsonl_lines = []

    # Process each column in the responses
    for col in responses:
        qid = df.iloc[0, col]
        if isinstance(qid, str) and '_' in qid:
            # Combine related questions with underscores
            base_qid = qid.split('_')[0]
            combined_questions[base_qid].append(questions[col])
            for response in responses[col].dropna():
                response = response.strip()
                if response:
                    combined_answers[base_qid].append(response)
        else:
            # Process normal questions
            prompt = questions[col]
            for response in responses[col].dropna():
                response = response.strip()
                if response:
                    message = {
                        "messages": [
                            {
                                "role": "system",
                                "content": "You are Jack_Bot, an incredibly funny chatbot designed to always win at the online game 'Quiplash'. The user will present you with a prompt and your goal is to answer it in the most hilarious way possible. Your answer will be pitted against another user's answer, and the audience will determine whose response to the prompt is funnier, so making people laugh is an important part of your job. No topic is off-limits, meaning you should feel free to be as crass and toe the line of what is acceptable to say. Swearing is fine (and even encouraged). Misspelling words also adds to the comedy, so use that when appropriate. Think in the style of 'Cards Against Humanity'. Feel free to use topical references or jokes involving internet culture, well-understood humor, politics, and religion. Remember, your goal is make people laugh!"
                            },
                            {
                                "role": "user",
                                "content": prompt
                            },
                            {
                                "role": "assistant",
                                "content": response
                            }
                        ]
                    }
                    jsonl_lines.append(message)

    # Combine related questions and split answers if necessary
    for base_qid, prompts in combined_questions.items():
        if prompts:
            prompt = prompts[0].split(' - ')[0]
            combined_answer = ' | '.join(combined_answers[base_qid])
            individual_answers = combined_answer.split(' | ')
            valid_answers = [answer for answer in individual_answers if answer]

            # Output combinations of three answers
            for i in range(0, len(valid_answers), 3):
                subset_answers = valid_answers[i:i+3]
                if len(subset_answers) > 0:
                    message = {
                        "messages": [
                            {
                                "role": "system",
                                "content": "You are Jack_Bot, an incredibly funny chatbot designed to always win at the online game 'Quiplash'. The user will present you with a prompt and your goal is to answer it in the most hilarious way possible. Your answer will be pitted against another user's answer, and the audience will determine whose response to the prompt is funnier, so making people laugh is an important part of your job. No topic is off-limits, meaning you should feel free to be as crass and toe the line of what is acceptable to say. Swearing is fine (and even encouraged). Misspelling words also adds to the comedy, so use that when appropriate. Think in the style of 'Cards Against Humanity'. Feel free to use topical references or jokes involving internet culture, well-understood humor, politics, and religion. Remember, your goal is make people laugh!"
                            },
                            {
                                "role": "user",
                                "content": prompt
                            },
                            {
                                "role": "assistant",
                                "content": ' | '.join(subset_answers)
                            }
                        ]
                    }
                    jsonl_lines.append(message)

    # Write to JSONL file
    with open('output.jsonl', 'w') as outfile:
        for line in jsonl_lines:
            json.dump(line, outfile)
            outfile.write('\n')


# Example usage
process_spreadsheet('Quiplash Data/500Responses-7-15-2024.csv')
