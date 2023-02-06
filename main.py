import os
import openai
import csv

openai.api_key = "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"
path='C:/Users/39349/Desktop/contract_dataset_ethereum/contract5/'
file_names= os.listdir(path)

ask="what is the weaknesses in the following smart contract solidity code?\n\n"

if not file_names:
    print("Directory is Empty")
else:
    with open("resultscontract5.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["File Name", "ChatGPT Response"])
        for i in file_names:
            try:
                print('\nChatGPT Response for file '+i)
                with open(path+i) as my_file:
                    response = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=ask+ my_file.read(),
                        temperature=0.9,
                        max_tokens=2048,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0.6,
                        stop=[" Human:", " AI:"]
                    )
                    text = response['choices'][0]['text']
                    print (text)
                    writer.writerow([i, text])
            except:
                pass
