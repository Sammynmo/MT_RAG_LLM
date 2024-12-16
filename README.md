***MT RAG LLM***

This repository contains the development and testing files for the Master thesis investigating whether LLMs could help students and non-technical users understand and learn SQL by providing translations and explanations in natural language. We set up the experiment with three prompt types: prompt + RAG with SQL query/question pairs and DB schema information, prompt + RAG with SQL query/question pairs, and prompt only. Additionally, we used two LLM types for our experiment, OpenAI's GPT-4o-mini and Google's Gemma with the general-purpose variant Gemma 1.1 and the coding specialised variant CodeGemma 1.1.

![Type_Variant_Overview](https://github.com/user-attachments/assets/f8e0392d-1a11-4af9-8b4d-97f2a1a88710)

The repository has separate folders for the experiment application development, the vector database setup, and the testing.

**A_Apps**

This folder contains all the application files used to obtain natural language translations and explanations. We created separate files for each LLM (i.e., GPT-4o-mini, Gemma, CodeGemma) and their three prompt types (prompt + RAG with SQL query/question pairs and DB schema information, prompt + RAG with SQL query/question pairs, and prompt only). This totals three files per LLM, for a total of nine files overall.

**B_Vector_Stores**

This folder contains separate Jupyter Notebooks for setting up our vector stores: one containing the SQL query/question examples and the other the DB schema information. Additionally, two CSV files with the input information for the two vector stores are included.

**C_Testing**

![Evaluation_Overview_Git](https://github.com/user-attachments/assets/80d2bab0-6dc3-4986-a861-d63e3f5f7d94)

The testing involved various steps; therefore, we divided the files into separate folders.

*5_Testing_Output_Generation*

This folder contains Python scripts for each LLM that iterate through the scripts in the folder "A_Apps" to generate the application output based on our selection of 32 questions (folder 8_Testing_Input_and_Output) used in the testing steps.

*6_LLM_Testing*

This folder contains nine Python scripts for each LLM per prompt type, instructing other LLMs to evaluate the applications' output.

*7_Translation_Testing*

Here are nine Python scripts again, using embedding models to assess the semantic similarity between the Spider question and the application translation output.

*8_Testing_Input_and_Output*

This folder contains the 32 Spider queries in CSV format used for the iterating task in folder "5_Testing_Output_Generation". It also contains nine Python scripts used to extract the scores 1-4 attributed by the LLM evaluation in folder "6_LLM_Testing" into CSV files we used for our analysis and evaluation.
