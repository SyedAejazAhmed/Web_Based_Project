from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Resume', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_section(self, title, body):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(body)

pdf = PDF()
pdf.add_page()

pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'Syed Aejaz Ahmed A', 0, 1, 'C')
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, 'Email: syed.aejaz.ahmed2006@gmail.com', 0, 1, 'C')
pdf.cell(0, 10, 'Phone: + 1 234 567 890', 0, 1, 'C')
pdf.cell(0, 10, 'LinkedIn: https://www.linkedin.com/in/aejazahmed2006/', 0, 1, 'C')
pdf.cell(0, 10, 'GitHub: https://github.com/SyedAejazAhmed', 0, 1, 'C')
pdf.ln(10)


pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Objective', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
objective = '''Passionate Data Analyst, Web Developer, and Innovator in analyzing data, developing responsive websites, and creating innovative solutions. Dedicated to leveraging technology to drive insights and develop user-friendly digital solutions.'''
pdf.multi_cell(0, 10, objective)
pdf.ln(10)

# Skills
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Skills', 0, 1, 'L')
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Data Analyst', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
data_analyst_skills = '''- Statistical Analysis
- Data Visualization (Tableau, Power BI, D3.js)
- Programming Languages (Python, R, SQL)
- Machine Learning (TensorFlow, scikit-learn)
- Data Cleaning and Preprocessing
- Database Management (MySQL, PostgreSQL, MongoDB)
- Excel'''
pdf.multi_cell(0, 10, data_analyst_skills)
pdf.ln(5)

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Web Developer', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
web_developer_skills = '''- Front-End Development (HTML, CSS, JavaScript, React.js, Angular, Vue.js)
- Back-End Development (Node.js, PHP, Ruby on Rails, Python (Django/Flask))
- Responsive Design
- Version Control (Git, GitHub)
- Web Performance Optimization
- APIs and Web Services (RESTful, GraphQL)
- Security Best Practices'''
pdf.multi_cell(0, 10, web_developer_skills)
pdf.ln(5)

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Innovator', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
innovator_skills = '''- Creative Thinking
- Problem-Solving
- Project Management (Agile, Scrum, Kanban)
- User-Centered Design
- Prototyping (Figma, Sketch, Adobe XD)
- Collaboration
- Continuous Learning'''
pdf.multi_cell(0, 10, innovator_skills)
pdf.ln(10)

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Education', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
education = '''
St. Josephs's College of Engineering, 
Pursuing Bachelor of Technology in Artificial Intelligence and Data Science
Place: Chennai,India,
2023-2027

Excel Matriculation Higher Secondary School
HSC passed with 76%

Excel Matriculation Higher Secondary School
SSLC passed with 80%
'''
pdf.multi_cell(0, 10, education)
pdf.ln(10)


pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Certifications', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
certifications = '''- Python For Data Science, IIT MADRAS,Jan-Feb 2024'''
pdf.multi_cell(0, 10, certifications)
pdf.ln(10)


pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Projects', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
projects = '''Social Media Reputation Monitoring
- Social Media Reputation Monitoring involves tracking and analyzing mentions of a brand, individual, or product across various social media platforms
- Technologies Used: Python, API, Natural Language Processing(NLP), Pandas, Matplotlib/Seaborn, Flask, HTML/CSS/JavaScript, Bootstrap, MySQL 

Social Media Dashboard
- A Social Media Dashboard in web development is a centralized interface that allows users to manage, monitor, and analyze their social media activities across multiple platforms.
- HTML/CSS/JavaScript, Node.js, MySQL, API, CLoud/Azure/Dockers, '''
pdf.multi_cell(0, 10, projects)
pdf.ln(10)


pdf_output_path = 'C:/Users/Enter Your path/resume.pdf'
pdf.output(pdf_output_path)

print(f'Resume saved at: {pdf_output_path}')
