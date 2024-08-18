import os
from crewai import Crew, Process, Task, Agent
from agents import ReportReader_Agent, Analyzer_Agent, Recommendation_Agent
from tools import searchTool, websiteSearchTool
from tasks import ReportReader_task, Analyze_blood_Sample_task, Find_articles_from_Web_task, Recommendation_task

crew = Crew(
    agents=[ReportReader_Agent, Analyzer_Agent, Recommendation_Agent],
    tasks=[ReportReader_task, Analyze_blood_Sample_task, Find_articles_from_Web_task, Recommendation_task],
    verbose=True
)

results = crew.kickoff()
results_str = str(results)
output_file = "GeneralTestReports.md"
with open(output_file, "w") as file:
    file.write("# Blood_Report_Analysis_Results \n\n")
    file.write(results_str)

print(f"Results have been written to {output_file}")