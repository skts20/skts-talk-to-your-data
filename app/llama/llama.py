from app.llama.llama_init import tokenizer, model_pipeline
from app.main import databases
DATABASE_SCHEMA_PLACEHOLDER = "<DATABASE_SCHEMA>"
QUERY_PLACEHOLDER = "<QUERY_PLACEHOLDER>"
LLAMA_PROMPT_TEMPLATE = f"""
Base on this database structure (DDL):
{DATABASE_SCHEMA_PLACEHOLDER}
Generate the query to get: {QUERY_PLACEHOLDER}
"""


def prepare_prompt(db_id: str, lang_query: str):
    db_schema = databases.get_database_schema(db_id)
    print(db_schema)
    return LLAMA_PROMPT_TEMPLATE.replace(DATABASE_SCHEMA_PLACEHOLDER, db_schema).replace(QUERY_PLACEHOLDER, lang_query)


#     TODO handler for llama response

def request_llama(prompt):
    sequences = model_pipeline(
        prompt,
        do_sample=True,
        top_k=5,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos.token_id,
        max_length=300,
    )[0]["generated_text"]
    return sequences
