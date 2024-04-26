
from llama_cpp import Llama
import psycopg2
from tabulate import tabulate

#LLM = Llama(model_path="../models/sqlcoder-7b-2/sqlcoder-7b-q5_k_m.gguf", n_gpu_layers=10, n_ctx=2048, verbose=False)
LLM = Llama(model_path="models/sqlcoder-7b-q5_k_m.gguf", n_gpu_layers=10, n_ctx=2048, verbose=False)


#conn = psycopg2.connect(
#    dbname="yelp",
#    user="postgres",
#    password="postgres",
#    host="localhost",
#    port="5432"
#)
#cur = conn.cursor()

def generate_prompt(question, prompt_file="prompt.md", metadata_file="metadata.sql"):
    with open(prompt_file, "r") as f:
        prompt = f.read()

    with open(metadata_file, "r") as f:
        table_metadata_string = f.read()

    prompt = prompt.format(
        user_question=question, table_metadata_string=table_metadata_string
    )
    return prompt

def query_model(question):
    prompt = generate_prompt(question)
    output = LLM(
        prompt,
        max_tokens=200, # Generate up to 32 tokens
        stop=["Q:", "\n"],
        echo=True # Echo the prompt back in the output
    )
    sql_query = output['choices'][0]['text'].split('[SQL]')[1]
    print("SQL: ", sql_query)
    return execute_query(sql_query)

def execute_query(query):
    pass
    #cur.execute(query)
    #rows = cur.fetchall()
    #headers = [desc[0] for desc in cur.description]
    #return tabulate(rows, headers=headers, tablefmt="grid")


def main():
    print("Welcome to the SQLCoder Chat Interface!")
    print("Type your message and press Enter to get a response.")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("Question: ")
        if user_input.lower() == 'exit':
            print("Exiting...")
            #cur.close()
            #conn.close()
            break
        print("Answer: ")
        response = query_model(user_input)
        print(response)

if __name__ == "__main__":
    main()