from transformers import LlamaForCausalLM, LlamaTokenizer
from transformers import pipeline
import torch

tokenizer = LlamaTokenizer.from_pretrained("../../llama_converted")
model = LlamaForCausalLM.from_pretrained(pretrained_model_name_or_path="../../llama_converted",
                                         low_cpu_mem_usage=True, torch_dtype="auto")
llama_pipeline = pipeline(
    task="text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.float16,
    device_map="auto"
)


def get_llama_response(prompt: str) -> None:
    sequences = llama_pipeline(
        prompt,
        do_sample=True,
        top_k=10,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
        max_length=256
    )
    print("chatbot: ", sequences[0]["generated_text"])

input_text = "hi, can you give me an examplary sql query"


# input_text = """
# This is the schema for a relative database:
# CREATE TABLE 'JPK_NAGLOWEK'
# (
# 	'NAGLOWEK_ID' NUMERIC NOT NULL PRIMARY KEY,
# 	'CZAS_WYSLANIA' NUMERIC NOT NULL,
# 	'CZAS_UTWORZENIA' NUMERIC NOT NULL,
# 	'DATA_OD' NUMERIC NOT NULL,
# 	'DATA_DO' NUMERIC NULL,
# 	'ROKMC' NUMERIC NOT NULL
# )
# ;
#
# CREATE TABLE 'JPK_PODMIOT'
# (
# 	'PODMIOT_ID' NUMERIC NOT NULL PRIMARY KEY,
# 	'NAGLOWEK_ID' NUMERIC NOT NULL,
# 	'NIP' TEXT NOT NULL,
# 	'IMIE' TEXT NOT NULL,
# 	'NAZWISKO' TEXT NOT NULL,
# 	'DATA_URODZENIA' NUMERIC NOT NULL,
# 	'TELEFON' NUMERIC NULL,
# 	CONSTRAINT 'FK_JPK_PODMIOT_JPK_NAGLOWEK' FOREIGN KEY ('NAGLOWEK_ID') REFERENCES 'JPK_NAGLOWEK' ('NAGLOWEK_ID') ON DELETE No Action ON UPDATE No Action
# )
# ;
#
# CREATE TABLE 'VAT_SPRZEDAZ'
# (
# 	'SPRZEDAZ_ID' NUMERIC NOT NULL PRIMARY KEY,
# 	'NAGLOWEK_ID' NUMERIC NOT NULL,
# 	'NR_KONTRAHENTA' TEXT NOT NULL,
# 	'DOWOD_SPRZEDAZY' TEXT NOT NULL,
# 	'DATA_WYSTAWIENIA' NUMERIC NOT NULL,
# 	'DATA_SPRZEDAZY' NUMERIC NOT NULL,
# 	'P_6' NUMERIC NULL,
# 	'P_8' NUMERIC NULL,
# 	'P_9' NUMERIC NULL,
# 	'P_11' NUMERIC NULL,
# 	'P_13' NUMERIC NULL,
# 	'P_15' NUMERIC NULL,
# 	'P_16' NUMERIC NULL,
# 	'P_19' NUMERIC NULL,
# 	'P_96' NUMERIC NULL,
# 	CONSTRAINT 'FK_VAT_SPRZEDAZ_JPK_NAGLOWEK' FOREIGN KEY ('NAGLOWEK_ID') REFERENCES 'JPK_NAGLOWEK' ('NAGLOWEK_ID') ON DELETE No Action ON UPDATE No Action
# )
# ;
#
# CREATE TABLE 'VAT_ZAKUP'
# (
# 	'ZAKUP_ID' NUMERIC NOT NULL PRIMARY KEY,
# 	'NAGLOWEK_ID' NUMERIC NOT NULL,
# 	'NR_DOSTAWCY' TEXT NOT NULL,
# 	'DOWOD_ZAKUPU' TEXT NOT NULL,
# 	'DATA_ZAKUPU' NUMERIC NOT NULL,
# 	'DATA_WPLYWU' NUMERIC NOT NULL,
# 	'P_61' NUMERIC NULL,
# 	'P_77' NUMERIC NULL,
# 	'P_78' NUMERIC NULL,
# 	CONSTRAINT 'FK_VAT_ZAKUP_JPK_NAGLOWEK' FOREIGN KEY ('NAGLOWEK_ID') REFERENCES 'JPK_NAGLOWEK' ('NAGLOWEK_ID') ON DELETE No Action ON UPDATE No Action
# )
# ;
#
# Create sql query for:
# "Give me mean value for P_96 column."
# """
# inputs = tokenizer.encode(input_text, return_tensors='pt')
# outputs = model.generate(inputs, max_length=512)
# print("Generated text: ")
# for i, output in enumerate(outputs):
#     print(f"{i}: {tokenizer.decode(output)}")

get_llama_response(prompt=input_text)
