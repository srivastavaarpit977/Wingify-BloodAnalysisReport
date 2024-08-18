from crewai import Task
import PyPDF2
from agents import researcher_Agent, ReportReader_Agent, Analyzer_Agent, Recommendation_Agent


def extract_text_from_pdf():
    # Prompt the user for the PDF file path
    pdf_path = input("Please enter the path to the PDF file: ")
    
    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as file:
        # Initialize the PDF reader
        reader = PyPDF2.PdfReader(file)
        # Initialize an empty string to store the extracted text
        pdf_text = ""
        # Iterate through each page
        for page_num in range(len(reader.pages)):
            # Extract text from each page
            page = reader.pages[page_num]
            pdf_text += page.extract_text()
    
    return pdf_text


pdf_text = extract_text_from_pdf()
print(pdf_text)



ReportReader_task = Task(
    description=f'''
    Your task is to meticulously read and process the sample blood test report. Follow these steps to ensure that all important information and key components are accurately identified and extracted:
    {pdf_text}

    Instructions for Report Reading:

    1. Extract Personal Details:
       - Identify and extract any personal information included in the report, such as the patient's name, date of birth, and other identifying information.
       - Ensure that this information is handled with care and privacy considerations.

    2. Identify Key Test Information:
       - Locate and extract the names of all tests performed, including their respective results.
       - For each test, identify the following components:
         - Test Name: Clearly state the name of the test.
         - Value: Note the test result value.
         - Normal Range: Record the reference or normal range provided for each test.

    3. Highlight Significant Data:
       - Identify and highlight any values that fall outside the normal range. Pay close attention to these abnormal results, as they are crucial for further analysis.
       - Note any additional observations or comments included in the report that may be relevant to the test results.

    4. Summarize Test Results:
       - Provide a summary of the key findings from the blood test report, including an overview of both normal and abnormal results.
       - Ensure that the summary is clear and includes all relevant details necessary for subsequent analysis.

    5. Prepare Data for Analysis:
       - Format the extracted information in a structured way that can be easily used for further analysis by other agents or tasks.
       - Ensure that the data is accurate and complete, including all relevant details from the report.
    ''',
    expected_output='Provide a detailed extraction of all critical information from the blood test report, including personal details, test names, values, normal ranges, and any notable observations. Ensure that all extracted data is accurate and organized for further analysis.',
    agent=ReportReader_Agent,
)

Analyze_blood_Sample_task = Task(
    description=f'''
    You are supposed to analyze the following blood test report: "{pdf_text}"

    Instructions for Analysis:
    
    1. Review Each Test Result:
       - Compare the test result with the provided normal range.
    
    2. Determine Normality:
       - Within Normal Range:
         - Confirm that the result is normal and explain what this implies about the patient’s health.
       - Outside Normal Range:
         - Identify if the result is higher or lower than the normal range and explain the potential health implications.
    
    3. Provide a Comprehensive Summary:
       - Overview of All Results:
         - Summarize the overall health implications based on the test results.
       - Detailed Analysis of Abnormal Values:
         - Provide in-depth analysis and context for any abnormal values.
       - Implications and Recommendations:
         - Offer suggestions for further investigation, lifestyle changes, or treatments based on the analysis.
       - Simplified Explanation:
         - Ensure the analysis is understandable for non-medical professionals, explaining any medical terms used.
    
    Example Analyses:
    
    1. Test: ALT (SGPT)
       - Normal Range: 10.0 - 49.0 U/L
       - Analysis: If the ALT (SGPT) value is within the range of 10.0 to 49.0 U/L, it indicates normal liver enzyme function. Values above this range may suggest liver damage or inflammation, while values below could indicate a deficiency or other liver conditions.
    
    2. Test: Hemoglobin (Hb)
       - Normal Range: 13.0 - 17.0 g/dL (for males)
       - Analysis: Hemoglobin levels within the normal range indicate a healthy oxygen-carrying capacity of the blood. Levels below 13.0 g/dL may suggest anemia, while levels above 17.0 g/dL could indicate polycythemia or dehydration.
    
    3. Test: White Blood Cell Count (WBC)
       - Normal Range: 4,500 - 11,000 cells/mcL
       - Analysis: A WBC count within this range is normal and indicates a healthy immune response. Elevated levels above 11,000 cells/mcL may indicate an infection, inflammation, or other immune response, while levels below 4,500 cells/mcL could suggest a compromised immune system.
    
    4. Test: Fasting Blood Glucose (FBG)
       - Normal Range: 70 - 99 mg/dL
       - Analysis: Fasting Blood Glucose within this range indicates normal glucose metabolism. Levels between 100 - 125 mg/dL suggest prediabetes, and levels of 126 mg/dL or higher on two separate tests indicate diabetes.
    
    5. Test: Total Cholesterol
       - Normal Range: Less than 200 mg/dL
       - Analysis: Total Cholesterol levels below 200 mg/dL are considered desirable and reduce the risk of heart disease. Levels between 200 - 239 mg/dL are borderline high, and levels of 240 mg/dL or more are high, increasing the risk of cardiovascular disease.
    
    6. Test: Platelet Count
       - Normal Range: 150,000 - 450,000 cells/mcL
       - Analysis: Platelet counts within this range indicate normal blood clotting function. Counts below 150,000 cells/mcL may suggest a risk of excessive bleeding, while counts above 450,000 cells/mcL could indicate an increased risk of clotting.
    ''',
    expected_output='Provide a detailed overview of the blood test results, emphasizing any abnormal values, and include explanations along with potential health implications for each.',
    agent=Analyzer_Agent,
    context=[ReportReader_task]
)

Find_articles_from_Web_task = Task(
    description='''
    Upon completing the analysis of the blood test report, proceed with the following tasks:

    1. Identify Key Health Concerns:
       - Carefully examine the abnormal values in the blood test report.
       - Determine the specific health concerns or issues that these abnormal values indicate. Ensure each concern is clearly identified and described in relation to the specific blood test result.

    2. Conduct a Targeted Web Search:
       - Search for 3-5 recent, high-quality medical articles that directly address each identified health concern. 
       - Prioritize articles published by reputable sources such as peer-reviewed medical journals, well-established health organizations, or leading hospitals (e.g., Mayo Clinic, Cleveland Clinic, Johns Hopkins Medicine).
       - Ensure the articles provide relevant and up-to-date information that enhances the understanding of the identified health concerns.

    3. Provide a Detailed Summary for Each Article:
       - For each selected article, include the following:
         - Full Title and Author(s): Clearly state the title of the article and the names of the authors.
         - Concise Summary: Write a brief, 2-3 sentence summary of the article’s main findings or recommendations. Focus on the key points that are most relevant to the identified health concern.
         - Relevance to Blood Test Results: Explain how the findings of the article relate to the specific abnormal blood test values. Discuss how the article’s insights can be applied to understand the potential implications of the blood test results.

    4. Present Your Findings Clearly:
       - Organize your findings in a format that clearly connects each medical article to the relevant blood test results.
       - Ensure that the connections between the abnormal values and the selected articles are easy to understand, providing a logical flow from the test result to the health concern, and then to the relevant medical research.
    ''',
    expected_output='Curate a list of 3-5 reputable medical articles, each with a brief summary and an explanation of how it relates to the abnormal blood test results. Ensure the articles come from credible sources and offer valuable insights into the identified health concerns.',
    agent=researcher_Agent,
    context=[ReportReader_task, Analyze_blood_Sample_task]
)

Recommendation_task = Task(
    description='''
    Based on the detailed analysis of the blood test report and the insights gathered from relevant medical articles, provide personalized health recommendations. Your recommendations should be clear, actionable, and easy to understand for someone without a medical background. Follow these steps:

    1. Summarize Key Findings:
       - Summarize the most important findings from the blood test report, including any abnormal values and their potential implications.
       - Integrate key insights from the medical articles, focusing on those that directly relate to the individual’s test results.

    2. Identify Main Health Concerns:
       - Clearly outline the primary health concerns highlighted by the blood test results and the related articles.
       - Explain the significance of these concerns, referencing specific test values and relevant research findings.

    3. Recommend Additional Tests or Follow-Ups:
       - Suggest any further diagnostic tests, screenings, or follow-up appointments that may be necessary based on the test results and the identified health concerns.
       - Explain why these additional tests are important, linking them to the specific concerns raised by the blood test results.

    4. Provide Lifestyle Recommendations:
       - Offer practical lifestyle advice that can help address the identified health concerns. This may include dietary changes, exercise routines, stress management techniques, or other healthy habits.
       - Ensure the recommendations are realistic and can be easily integrated into the individual’s daily life.

    5. Suggest Medical Interventions:
       - If appropriate, recommend medical interventions such as medications, treatments, or consultations with specialists.
       - Clearly explain why these interventions may be necessary and how they can help improve the individual’s health outcomes.

    6. Present Information Clearly and Compassionately:
       - Use clear and simple language to ensure that the recommendations are easy to understand.
       - Present the information with empathy and care, recognizing that the individual may be concerned or anxious about their test results.
    ''',
    expected_output='Provide a comprehensive set of health recommendations based on the blood test analysis and relevant medical research. Include clear explanations for each recommendation and ensure they are actionable and easy to follow.',
    agent=Recommendation_Agent,
    context=[ReportReader_task, Analyze_blood_Sample_task, Find_articles_from_Web_task]
)