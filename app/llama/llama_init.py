from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

TOKENIZER_PATH = '/'
LLAMA_PATH = '/'

INIT_MODEL_PROMPT = """
You are AI which generates SQL query code based on the context (database structure) and the request what Query should does.
Example message:
Base on this database structure (DDL):
CREATE TABLE 'JPK_NAGLOWEK'
(
	'NAGLOWEK_ID' NUMERIC NOT NULL PRIMARY KEY,
	'CZAS_WYSLANIA' NUMERIC NOT NULL,
	'CZAS_UTWORZENIA' NUMERIC NOT NULL,
	'DATA_OD' NUMERIC NOT NULL,
	'DATA_DO' NUMERIC NULL,
	'ROKMC' NUMERIC NOT NULL
)
;

Generate the query to get mean value of CZAS_WYSYLANIA.

Generated result from you, should look likes this:
SELECT AVG(CZAS_WYSYLANIA) as AVERAGE_CZAS_WYSYLANIE FROM JPK_NAGLOWEK
"""
tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)
model = AutoModelForCausalLM.from_pretrained(LLAMA_PATH, torch_dtype="auto")
model_pipeline = pipeline(
    task="text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.float16,
    device_map="auto"
)

model_pipeline(
    INIT_MODEL_PROMPT,
    do_sample=True,
    top_k=5,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos.token_id,
    max_length=300,
)
