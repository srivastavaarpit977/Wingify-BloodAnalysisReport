# ** Wingify-Blood Report Analysis**

 This project uses CrewAI framework , which act as a agent to analyze blood tests, find health articles, and give personalized health advice. It simplifies medical data to support better health decisions.

## SetUp
Follow the step to setup this project:
1. Clone the repository:
```
git clone https://github.com/srivastavaarpit977/Wingify-BloodAnalysisReport.git

```
2. Create a virtual Environment to avoid conflicts with dependencies
```
python -m venv venv
```
3. Activate Virtual Environment
   - On Windows termial:
    ```
    .\venv\Scripts\activate
    ```
  - On macOS and Linux:
    ```
    source venv/bin/activate
    ```
4. Install Dependencies
```
pip install -r requirements.txt
```
5. Create a .env to avoid API Key leak ans paste this:
```
GOOGLE_API_KEY='your-api-key'
SERPER_API_KEY = 'your-api-key'
```
6. Run the Script:
```
python main.py
```
Now this is create a report and personalized recommendation based on the given blood report, and links for reference.

*****

## Workflow and Approach
#### As the task was to create the blood analysis report and provide personilized recommendation and articles for references from web. For the given task approached with the following agents and tasks for result.
#### AI Agents:
- **ReportReader_Agent:** Read the report or the text extracted from the pdf remembering all the instruction provided to it.
- **researcher_Agent:** Researches the about the medical information in the web to collect reliable sources from online.
- **Analyzer_Agent:** Analyzes the blood report identifying the key compnents to help evaluate the deficiencies and diseases of the person's report.
- **Recommendation_Agent:** Based on the deficiencies and diseases gives personalized and actionable recommendation for the person's healthy life.

#### Tasks:
Now, when the tasks are operated , it used this agent to make perform the task as per given instruction and generates all the output which is then save in the output file.

- **ReportReader Task:** Extract and summarize personal details, test names, values, normal ranges, and significant findings from the blood test report for further analysis.
- **Analyze Blood Sample Task:** Review test results, compare with normal ranges, and provide a summary of health implications, focusing on any abnormal values.
- **Find Articles from Web Task:** Search for credible medical articles related to abnormal test values, summarize them, and explain their relevance to the blood test results.
- **Recommendation Task:** Provide clear, actionable health recommendations based on the blood test analysis and related research, including lifestyle changes and possible medical interventions.

******

Here are the file's description for better understanding
### `main.py`
- **Purpose**: It is the entry point of the application.
- **Functionality**: Initializes and uses the tools and agents defined in other files to perform the main tasks of the application.

### `tools.py`
- **Purpose**: Responsible for initializing and configuring the tools used in the project.
- **Functionality**:
  - Imports `SerperDevTool` and `WebsiteSearchTool` from the `crewai_tools` module.
  - Initializes `searchTool` using `SerperDevTool`.
  - Configures and initializes `WebsiteSearchTool` with specific settings for the language model and embedder, including API keys and model configurations.

### `agents.py`
- **Purpose**: Defines the agents that perform specific tasks within the application.
- **Functionality**:
  - Contains classes and methods to create and manage agents.
  - Agents use the tools and configurations defined in `tools.py` to perform their tasks.

### `tasks.py`
- **Purpose**: Defines the tasks that the agents will perform.
- **Functionality**:
  - Contains functions and classes that outline the specific tasks.
  - Tasks are executed by the agents using the tools and configurations provided.



