# Ethereum-Smart-Contract-Analysis-through-chat-gpt-and-other-AI-techniques
(Main.py )This code is written in Python and is using the OpenAI API to analyze smart contract Solidity code for weaknesses. The code sets the API key for OpenAI and sets the path to a directory containing smart contract files. It then retrieves the list of file names in the directory and stores it in a variable called "file_names".
If the directory is empty, the code will print "Directory is Empty". If not, the code opens a .csv file called "resultscontract5.csv" and writes the header row with the column names "File Name" and "ChatGPT Response".

For each file in the directory, the code reads the contents of the file and sends it as a prompt to the OpenAI API with the prompt asking "what is the weaknesses in the following smart contract solidity code?" The API returns a text response, which the code then writes to the .csv file along with the file name. The code uses a try-except block to handle any exceptions that might occur during the API call.
(Topic modelling & Sentiment Analysis.py)This code performs topic modeling and sentiment analysis on text data.
It first loads a CSV file named "combined.csv" into a Pandas dataframe called "data". It then removes any rows with missing values using "data.dropna()".
The code then performs topic modeling on the text data using Latent Dirichlet Allocation (LDA). This involves transforming the text data into a matrix of token counts using the CountVectorizer, fitting the LDA model to the matrix, and extracting the topics and their weights.
Next, it performs sentiment analysis on the text data using the SentimentIntensityAnalyzer from the NLTK library. The sentiment scores are then stored in a list called "sentiments".
Finally, the code writes the topics, sentiments, and other information to a CSV file named "topics_sentiments4.csv".
