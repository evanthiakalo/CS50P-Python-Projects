from fpdf import FPDF
class ShirtificatePDF(FPDF):
    def __init__(self, name):
        super().__init__(orientation= "P", unit= "mm", format= "A4")
        self.name = name
        self.add_page()
        self._header_text()
        self._shirt_image()
        self._user_name_on_shirt()

    def _header_text (self):
        self.set_font("helvetica", "B", 45)
        self.cell (0, 60, "CS50 Shirtificate", align= "C", ln= True)

    def _shirt_image(self):
        self.image ("shirtificate.png", x=10, y=70, w=190)

    def _user_name_on_shirt(self):
        self.set_text_color (255, 255, 255)
        self.set_font ("helvetica", "B", 24)

        self.set_y(140)
        self.cell (0, 10, f"{self.name} took CS50", align= "C")
def main():
    name = input ("Name: ")
    pdf = ShirtificatePDF (name)
    pdf.output ("shirtificate.pdf")

if __name__ == "__main__":
    main()
