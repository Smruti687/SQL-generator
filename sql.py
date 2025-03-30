import openai

def generate_sql(description):
    prompt = (
        f"Generate an SQL query based on the following description: \n{description}\n"
        "Also, provide an explanation of the query and suggest possible optimizations."
    )
    
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use the appropriate model
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    description = input("Enter the SQL query description: ")
    output = generate_sql(description)
    print("\nGenerated Output:\n", output)
