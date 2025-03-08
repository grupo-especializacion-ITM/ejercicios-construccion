class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def print_report(self):
        print(f"Report: {self.title}")
        print(self.content)

# Uso
report = Report("Sales Report", "Total Sales: $5000")
report.print_report()  # Violación de Pure Fabrication


## Challenge
# Separa la lógica de impresión en una nueva clase ReportPrinter.
# Haz que Report solo contenga los datos.
# Permite agregar diferentes formas de salida (ej. PDF, consola, etc.) sin modificar Report.