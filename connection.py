from PySide6 import QtWidgets, QtSql


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('database.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Невозможно создать базу данных",
                                           "Нажмите Cancel для выхода.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec('''
            CREATE TABLE IF NOT EXISTS person  (
                person_id INTEGER PRIMARY KEY,
                person_name TEXT NOT NULL,
                person_description TEXT,
                person_active INTEGER DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        query.exec('''
            CREATE TABLE IF NOT EXISTS contractor  (
                contractor_id INTEGER PRIMARY KEY,
                contractor_name TEXT NOT NULL,
                contractor_description TEXT,
                contractor_active INTEGER DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        query.exec('''
            CREATE TABLE IF NOT EXISTS swap  (
                swap_id INTEGER PRIMARY KEY,
                swap_date TEXT,
                swap_buyer_contractor_id INTEGER,
                swap_buyer_person_id INTEGER,
                swap_seller_contractor_id INTEGER,
                swap_seller_person_id INTEGER,
                swap_sum NUMERIC,
                swap_share_buy NUMERIC,
                swap_share_back NUMERIC,
                swap_description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        query.exec('''
            CREATE TABLE IF NOT EXISTS cash  (
                cash_id INTEGER PRIMARY KEY AUTOINCREMENT,
                cash_giver_id INTEGER,
                cash_receiver_id INTEGER,
                cash_date VARCHAR(20),
                cash_sum REAL,
                cash_status_id INTEGER DEFAULT 1,
                cash_description VARCHAR(512),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()

        return query

    def add_new_transaction_query(self, date, category, description, balance, status):
        sql_query = "INSERT INTO expenses (Date, Category, Description, Balance, Status) VALUES (?, ?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [date, category, description, balance, status])

    def update_transaction_query(self, date, category, description, balance, status, id):
        sql_query = "UPDATE expenses SET Date=?, Category=?, Description=?, Balance=?, Status=? WHERE ID=?"
        self.execute_query_with_params(sql_query, [date, category, description, balance, status, id])

    def delete_transaction_query(self, id):
        sql_query = "DELETE FROM expenses WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])

    def get_total(self, column, filter=None, value=None):
        sql_query = f"SELECT SUM({column}) FROM expenses"

        if filter is not None and value is not None:
            sql_query += f" WHERE {filter} = ?"

        query_values = []

        if value is not None:
            query_values.append(value)

        query = self.execute_query_with_params(sql_query, query_values)

        if query.next():
            return str(query.value(0)) + '$'

        return '0'

    def total_balance(self):
        return self.get_total(column="Balance")

    def total_income(self):
        return self.get_total(column="Balance", filter="Status", value="Income")

    def total_outcome(self):
        return self.get_total(column="Balance", filter="Status", value="Outcome")

    def total_groceries(self):
        return self.get_total(column="Balance", filter="Category", value="Grocery")

    def total_auto(self):
        return self.get_total(column="Balance", filter="Category", value="Auto")

    def total_entertainment(self):
        return self.get_total(column="Balance", filter="Category", value="Entertainment")

    def total_other(self):
        return self.get_total(column="Balance", filter="Category", value="Other")