from fpdf import FPDF

# Create a PDF class
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "AWS CDK CLI Commands", border=False, ln=True, align="C")
        self.ln(5)

    def table_header(self):
        self.set_font("Arial", "B", 10)
        self.cell(35, 10, "Command", 1)
        self.cell(55, 10, "Meaning", 1)
        self.cell(40, 10, "Example", 1)
        self.cell(60, 10, "Notes", 1)
        self.ln()

    def table_row(self, command, meaning, example, notes):
        self.set_font("Arial", "", 9)
        self.cell(35, 10, command, 1)
        self.cell(55, 10, meaning, 1)
        self.cell(40, 10, example, 1)
        self.cell(60, 10, notes, 1)
        self.ln()

# Create PDF
pdf = PDF()
pdf.add_page()

# Table header
pdf.table_header()

# CDK commands list
commands = [
    ("cdk init", "Initialize CDK project", "cdk init app --language python", "Choose a language"),
    ("cdk synth", "Generate CloudFormation template", "cdk synth", "Outputs template"),
    ("cdk deploy", "Deploy resources to AWS", "cdk deploy", "Creates/updates resources"),
    ("cdk destroy", "Remove deployed resources", "cdk destroy", "Be careful!"),
    ("cdk diff", "Show what will change", "cdk diff", "Useful before deploy"),
    ("cdk list", "List stacks in app", "cdk list", "Also works as cdk ls"),
    ("cdk doctor", "Check setup health", "cdk doctor", "Run if errors occur"),
    ("cdk bootstrap", "Prepare AWS account", "cdk bootstrap", "One-time setup"),
    ("cdk context", "Manage cached values", "cdk context --clear", "Clear outdated info"),
    ("cdk metadata", "Inspect deployed stack", "cdk metadata", "Advanced usage"),
    ("cdk deploy stack-name", "Deploy specific stack", "cdk deploy MyStack", "For multi-stack apps"),
    ("cdk destroy stack-name", "Destroy specific stack", "cdk destroy MyStack", "Avoid full wipe"),
    ("cdk synth > file", "Export template to file", "cdk synth > template.yaml", "For review/export"),
]

# Add rows
for cmd in commands:
    pdf.table_row(*cmd)

# Save the PDF
pdf.output("aws_cdk_commands.pdf")
print("PDF created: aws_cdk_commands.pdf")
