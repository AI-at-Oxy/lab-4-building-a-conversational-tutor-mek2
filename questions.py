# questions.py
# Replace this with your own topic and questions (at least 5)!

TOPIC = "Winter Olympics Figure Skating"

QUESTIONS = [
    {
        "question": "Who won the gold medal in women's figure skating at the 2026 Winter Olympics?",
        "answer": "Alysa Liu",
        "misconception": "Students sometimes say Kaori Sakamoto because she won silver! Alysa Liu had a final score of 226.79 and Kaori Sakamoto had a final score of 224.90 so it was pretty close."
    },
    {
        "question": "How many American figure skaters were at the 2026 Winter Olympics?",
        "answer": "16",
        "misconception": "Students sometimes say 18 because some people may confuse 16 and 18."
    },
    {
        "question": "Who won the gold medal in men's figure skating at the 2026 Winter Olympics?",
        "answer": "Mikhail Shaidorov",
        "misconception": "Students sometimes say Nathan because Nathan Chen won gold in 2022."
    },
   
]

# Build the system prompt with your questions baked in
SYSTEM_PROMPT = f"""You are a friendly tutor helping a student learn about {TOPIC}.

Here are the questions you should work through with the student:

"""

for i, q in enumerate(QUESTIONS, 1):
    SYSTEM_PROMPT += f"""Question {i}: {q['question']}
  Correct answer: {q['answer']}
  Common misconception: {q['misconception']}

"""

SYSTEM_PROMPT += """
Work through the questions with the student. How you tutor is up to you,
but make sure the student engages with each question before moving on. Be patient and kind but do not be overly nice - some students get annoyed when there is too much positive reinforcement.
"""
