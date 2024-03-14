import mysql.connector
import pandas as pd
import warnings

from templates import template_invoice, template_tlcf, template_update

warnings.filterwarnings("ignore", message="pandas only supports SQLAlchemy connectable")

class IdTotalLeaseCfReassigner:

    def __init__(self, id_lease_to_check: int) -> None:
        self.valores = {'id': id_lease_to_check,
                        'period': '',
                        'dMonth': None,
                        'new_cashflow_id': None,
                        'old_cashflow_id': None,
                        'invoice_id': None
                        }

    def ejecutar_update(self, query):
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Quantum123!",
                database="quantum1103"
            )

            cursor = conexion.cursor()
            cursor.execute(query)
            conexion.commit()
            print("Query ejecutada exitosamente")

        except mysql.connector.Error as error:
            print("Error al ejecutar el query:", error)
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()


    def ejecutar_select_to_df(self, query):
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Quantum123!",
                database="quantum1103",
                sql_mode=''
            )

            df_result = pd.read_sql(query, conexion)
            print("Query ejecutada exitosamente")
            return df_result
        except mysql.connector.Error as error:
            print("Error al ejecutar el query:", error)
            return None
        finally:
            if conexion.is_connected():
                conexion.close()

    def main(self):
        query =  template_invoice.substitute(self.valores)

        df = self.ejecutar_select_to_df(query)
        self.valores['invoice_id'] = df['id'][0]

        if df['re_sync_status'][0] =='Canceled':
            print(df)
            self.valores['old_cashflow_id'] = df['cashflow_id'][0]
            self.valores['period'] = df['dMonth'][0]
            df_tlcf = self.ejecutar_select_to_df(template_tlcf.substitute(self.valores))
            print(df_tlcf)


            self.valores['new_cashflow_id'] = df_tlcf['idTotalLeaseCF'][0]

            update_q = template_update.substitute(self.valores)
            self.ejecutar_update(update_q)

            print(self.ejecutar_select_to_df(query))
            print(f"""
            Factura de iniciales con invoice_id = {self.valores['invoice_id']} para el id_lease {self.valores['id']}
            Ha sido asignado al Cashflow_id = {self.valores['new_cashflow_id']}
            Anteriormente se tenia asignado al Cashflow_id = {self.valores['old_cashflow_id']}
            """)
        else:
            print(f"No hay facturas de iniciales para el id lease {self.valores['id']}")





