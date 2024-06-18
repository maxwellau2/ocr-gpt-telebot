from openai import OpenAI
client = OpenAI(api_key="")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a student taking an engineers in society and engineering ethics test."},
    {"role": "user", "content": "3, Which of the following best describes ethical concepts?\r\nClear selection\r\npoint\r\nA) Ethics codes are rulesof acceptable personal behaviour and courtesy when\r\no\r\ninteracting with others in a social setting.\r\nO B) Ethics problems havea correct answer that will be arrived at by everyone.\r\nO C) One requiresstrength of character to behave in an ethical manner.\r\nD) Professional ethics is a set of rules that must be followed under all\r\no\r\ncircumstances.?"}
  ])

print(completion.choices[0].message.content)