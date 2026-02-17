if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    import sys

    class MockDB:
        def __init__(self):
            self.db_path = "voidpos.db"
            if not os.path.exists(self.db_path):
                open(self.db_path, 'a').close()

    app = QApplication(sys.argv)
    mock_db = MockDB()
    try:
        window = AIChatDialog(mock_db)
        window.show()
    except NameError:
        print("Sınıflar eksik kopyalanmış olabilir, ancak kod yapısı incelenebilir.")

    sys.exit(app.exec())        
