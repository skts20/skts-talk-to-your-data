# from transformers import LlamaForCausalLM, LlamaTokenizer
# from transformers import pipeline
# import torch
#
# tokenizer = LlamaTokenizer.from_pretrained("../../llama_converted")
# model = LlamaForCausalLM.from_pretrained(pretrained_model_name_or_path="../../llama_converted",
#                                          low_cpu_mem_usage=True, torch_dtype="auto")
# llama_pipeline = pipeline(
#     task="text-generation",
#     model=model,
#     tokenizer=tokenizer,
#     torch_dtype=torch.float16,
#     device_map="auto"
# )
#
#
# def get_llama_response(prompt: str) -> None:
#     sequences = llama_pipeline(
#         prompt,
#         do_sample=True,
#         top_k=10,
#         num_return_sequences=1,
#         eos_token_id=tokenizer.eos_token_id,
#         max_length=256
#     )
#     print("chatbot: ", sequences[0]["generated_text"])
#
# # input_text = "hi, can you give me an examplary sql query"
#
#
# input_text = "You are the SQL queries generator. Your task is to generate SQL query from the input I put you (question) and context (ddl of database). For this database: CREATE TABLE 'JPK_NAGLOWEK'('NAGLOWEK_ID' NUMERIC NOT NULL PRIMARY KEY,'CZAS_WYSLANIA' NUMERIC NOT NULL,'CZAS_UTWORZENIA' NUMERIC NOT NULL,'DATA_OD' NUMERIC NOT NULL,'DATA_DO' NUMERIC NULL,'ROKMC' NUMERIC NOT NULL);Generate a simple SQL query for given problem: Average value for CZAS_UTWORZENIA column"
# # inputs = tokenizer.encode(input_text, return_tensors='pt')
# # outputs = model.generate(inputs, max_length=512)
# # print("Generated text: ")
# # for i, output in enumerate(outputs):
# #     print(f"{i}: {tokenizer.decode(output)}")
#
# get_llama_response(prompt=input_text)
#
# # while True:
# #     print("you:")
# #     prompt = input()
#
# #     if prompt == "stop chat":
# #         break
# #     else:
# #         try:
# #             get_llama_response(prompt)
# #         except Exception as e:
# #             print(e)