'''
THIS PROJECT IS THE UNDERGRADUATE THESIS OF DATINGALING, GONZALES, MENDOZA, & SALAZAR
        ENTITLED:
            DESIGN AND DEVELOPMENT OF ACTION RECOGNITION MODEL AND SOFTWARE
                   FOR DIGITIZATION OF BEHAVIORAL CODING SYSTEM
                                DURING EXAMINATION

                    DEVELOPED ON A.Y. 2024-2025 - 2ND SEMESTER
                     THESIS ADVISER: DR. JEFFREY S. SARMIENTO
                     
'''

# AUTHOR: PETER JUSTIN E. DATINGALING 

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import *

from gui_commands import MainWindow

if __name__ == "__main__":
    # Check if a QApplication instance already exists
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    else:
        print("QApplication instance already exists.")

    window = MainWindow()
    window.show()
    sys.exit(app.exec()) 