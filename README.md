A.	Installation Guide
1.	Extract the ZIP file
•	Locate the ZIP file you downloaded for this project.
•	Right-click on the ZIP file and select "Extract All..." (Windows) or "Extract Here" (Mac/Linux).
•	Choose an easy-to-find folder (such as your Desktop or Documents folder) as the destination.
•	After extraction, open the extracted folder to ensure all files and subfolders are present.

In Jupyter Notebook, run Step 2 to Step 4:

2.	Data Pre-processing
•	Open Jupyter Notebook 
•	In the Jupyter file browser, navigate to the extracted project folder.
•	Open the notebook named Data Pre-processing.ipynb in Source Codes folder.
•	Run all cells from the beginning to the end.
•	The notebook will process the data and generate a cleaned CSV file in Data folder:
o	Dengue_QA_multilingual_cleaned.csv
•	Confirm that this file appears in your folder when processing is complete.

3.	Knowledge Graph
•	Open the notebook named Knowledge Graph.ipynb in Source Codes folder.
•	Run all cells in this notebook.
•	Upon completion, two files will be created in your Data folder:
o	Dengue_QA_multilingual.json
o	Dengue_QA_multilingual_KG.ttl
•	Ensure these files appear in the project directory.

4.	Model Training
•	In Jupyter, open and run each of the following notebooks in Source Codes folder:
o	Model Training (mpnet-base-v2).ipynb
o	Model Training (MiniLM-L12-v2).ipynb
•	Run all cells in each notebook. These will train the respective models.
•	When finished, ensure the trained model and evaluation results files are created and saved in your Data folder:
o	dengue_qa_model (MiniLM-L12-v2)
o	evaluation_results (MiniLM-L12-v2)
o	dengue_qa_model (mpnet-base-v2)
o	evaluation_results (mpnet-base-v2)

5.	Deploying the Model on Hugging Face Spaces
•	Go to Hugging Face Spaces
o	Open your browser and go to: https://huggingface.co/spaces
•	Create a New Space
1.	Click "New Space" at the top right.
2.	Enter Space Name: Lab1B-G5
3.	Enter Short Description: Briefly describe your project.
4.	Select Space SDK: Choose Gradio.
5.	Choose Gradio Template: Select blank.
6.	Space Hardware: Keep the default option (free version is sufficient).
7.	Select Visibility: Set to Public so anyone can access your app.
8.	Click "Create Space".
•	Upload Project Files to Your Space
1.	Once your space is created, click on the Files tab at the top-right.
2.	Upload the following files:
o	app.py (in Source Codes folder)
o	requirements.txt (in Source Codes folder)
o	dengue_qa_model (mpnet-base-v2).pkl  (in Data folder)
•	Run the Application
1.	After uploading, the system will automatically build and start your app.
2.	Wait for the status to change to "Running" (this may take a few minutes).
3.	When running, click the "App" tab at the top. You will see your deployed web interface and can interact with your system.
Note: If you encounter any errors, check the Logs tab in Hugging Face Spaces for troubleshooting details. 
 B.	How to Use the QA System
1.	Interface
•	Home Page:
When you access the deployed app (via the App tab on Hugging Face Spaces), you’ll see a web page titled “Sistem Soal Jawab Denggi” at the top.
•	Chatbox:
The main feature on the page is a chatbox, where you can type your questions.

2.	Asking Questions
•	Multilingual Support:
You can ask questions in Malay, English, or a mix of both (“rojak” style). The system is designed to understand and respond to all three.
•	System Support Scope:
	Apakah itu denggi (What is dengue)
	Gejala/Simptom (Symptoms of dengue)
	Rawatan dan penjagaan (Treatment and care for dengue)
	Cara pencegahan (Ways to prevent dengue)
You are encouraged to ask any questions related to these topics for the most accurate and relevant answers.
•	How to Ask:
1.	Click on the input box at the bottom of the chat interface.
2.	Type your question in your preferred language.
	Malay example:
Apakah simptom denggi?
	English example:
What are the symptoms of dengue?
	Rojak example:
Denggi symptom macam mana?
3.	Click the “Hantar” button (or press Enter) to submit your question.

3.	Viewing Answers
•	Automated Response:
The system will process your question and display an answer just below your message in the chatbox.
•	Language Consistency:
The reply will be in the same language (or style) as your question, whether it’s Malay, English, or mixed.
•	Reliable Information:
All answers are generated based on the knowledge graph, ensuring that the information provided is accurate, reliable, and relevant to your question.

Quick Tips:
•	Keep your questions short and clear for best results.
•	If the system doesn’t understand your question, try rephrasing or using simpler language.

