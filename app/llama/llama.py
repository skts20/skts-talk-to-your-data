# from app.llama.llama_init import tokenizer, model_pipeline
from app.main import databases
from app.main import model, tokenizer, llama_pipeline
DATABASE_SCHEMA_PLACEHOLDER = "<DATABASE_SCHEMA>"
QUERY_PLACEHOLDER = "<QUERY_PLACEHOLDER>"
LLAMA_PROMPT_TEMPLATE = f"""
You have access to a database created by this SQL query:
{DATABASE_SCHEMA_PLACEHOLDER}
Please generate only an SQL query to retrieve information from this database.
Task: {QUERY_PLACEHOLDER}
"""


def prepare_prompt(db_id: str, lang_query: str):
    db_schema = databases.get_database_schema(db_id)
    print(db_schema)
    return LLAMA_PROMPT_TEMPLATE.replace(DATABASE_SCHEMA_PLACEHOLDER, db_schema).replace(QUERY_PLACEHOLDER, lang_query)


#     TODO handler for llama response

def request_llama(prompt):

    sequences = llama_pipeline(
        prompt,
        do_sample=True,
        top_k=10,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
        max_length=256
    )
    return sequences[0]["generated_text"]

    # return "SELECT AVG(P_96) AS Srednia_P_96 FROM VAT_SPRZEDAZ WHERE DOWOD_SPRZEDAZY LIKE '%FV%' AND P_96 > 1000;"

