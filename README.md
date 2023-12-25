# News-Articles-Retrieval
                  
                  Topic : Political news(News articles in New York) (News document Retrieval)

1. open the command prompt or Vscode teminal or any terminal

      just navigate it : "cd P17-MiniProject-SAIKU" and then "cd codes" (codes contain all python codes):

Installation:

Ensure you have Python installed on your machine.

Install the necessary libraries using pip:
   

      'pip install nltk scikit-learn textblob tkinter matplotlib'
      


Download NLTK data by running the Python interpreter and executing the following:

        import nltk
        nltk.download('punkt')
        nltk.download('stopwords')


Download any additional pakages require to run code.

Run the Python script Relevence.py to launch the GUI for document searching.

Usage:

    Run the Relevence.py script as "python Relevence.py".
    Enter your query in the provided text field.
    Click the "Search" button to start the search process.
    Review the top 8 relevant documents displayed in the GUI.
    Provide feedback on document relevance using the prompted dialog boxes.(Enter yes if document is relevent and enter no if it is non-relevent)
    Then the top 8 relevant documents displayed
    we have two buttons at bottom of the GUI :
    1.PR-curve It provide the PR-curve based on the Relevence feedback
    2.11-Point Interpolated Precision-Recall Curve based on Precision and Recall

    The Precision and Recall vales for bothPR-curve and 11-point Interpolatedwill print in terminal itself.



-->Relevence.py: The main Python script containing the search functionality and GUI setup.

-->inverted__1.json: JSON file storing the inverted index required for document retrieval.

Link  : https://drive.google.com/file/d/18JILQIumwBQuArT2VBGUAGfDCowRLoLT/view?usp=drive_link

-->Use above link and extract the inverted__1.json file from google drive and replace the path of the file with  inverted__1.json in Relevence.py line number : 168

-->output_folder_2 : folder contain the documents.


Link : https://drive.google.com/file/d/12L31TnhuVCJonpsdPjkU2AlmfRgshmmF/view?usp=drive_link

-->use above link download the zip folder and extract the folder . copy the folder path then replace the output_folder_2 path present in Relevence.py with copied path in line number : 23


Please use above two links the dataset and inverted index present in above links only.

Requirements:

Python 3.x
Libraries: NLTK, scikit-learn, TextBlob


After doing above all things :

                   just run "python Relevence.py"



Simple discription:

A simple information retrieval system using a graphical user interface (GUI) with the help of the Tkinter library. It allows users to enter a query, performs a search within a collection of documents, and uses relevance feedback to refine the search results.

Brief discription of functionalities :


preprocess_text(text)

Description: Converts the input text to lowercase, tokenizes it, removes punctuation and stopwords from the text, and returns the processed text.


read_document(doc_id)

Description: Reads the content of a document based on the provided document ID from a specific file path and returns the text of the document.


calculate_precision_recall()

Description: Calculates precision and recall values based on the top 8 documents retrieved and stores these values in global variables for later analysis or visualization.


display_top_8(sorted_docs)

Description: Clears the text widget and displays the top 8 retrieved documents along with their IDs and contents.


process_relevance_feedback()

Description: Processes relevance feedback for a query entered by the user. It utilizes spell correction, retrieves relevant documents, calculates TF-IDF scores, displays top documents, and gathers feedback on document relevance.

            In terminal I am printing the values of Precision and Recall values of both PR-curve and 11-point interpolation.

calculate_11_point_interpolation()

Description: Calculates the 11-point interpolated precision-recall curve based on stored precision and recall values and visualizes it using Matplotlib.


generate_pr_curve()

Description: Generates and displays the precision-recall curve for the top 8 documents retrieved based on stored precision and recall values.



Examples :

Some queries

            1. Kim Jong-un Says North Korea  Preparing to test Long-Range Missile
            2. Calling on Angels While Enduring the Trials of Job
            3. Airline Pilot, Believed to Be Drunk, Is Pulled From Cockpit in Canada

             And so on ...............
