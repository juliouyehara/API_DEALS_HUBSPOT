import psycopg2 as pg
import psycopg2.extras

def delete_postgres(key_postgre):
    connection = pg.connect(key_postgre)
    curs = connection.cursor()
    postgre_query = """DELETE FROM accountify_omie ROWS"""
    curs.execute(postgre_query)
    connection.commit()
    connection.close()
    curs.close()

def insert_postgre(key_postgre, response):
    try:
        connection = pg.connect(key_postgre)
        curs = connection.cursor()
        postgres_insert_query = """INSERT INTO api_hub  (object_id, 
                                                        deal_name,
                                                        deal_stage,
                                                        pipeline,
                                                        owner_id,
                                                        owner,
                                                        create_date,
                                                        close_date,
                                                        modify_date,
                                                        amount,
                                                        total_contrato,
                                                        implantacao_automatica,
                                                        implantacao_typeform,
                                                        condicoes
                                                                ) 
        VALUES (%(object id)s, 
                %(deal name)s,
                %(deal stage)s,
                %(pipeline)s,
                %(owner id)s,
                %(owner)s,
                %(create date)s,
                %(close date)s,
                %(last date modified)s,
                %(amount)s,
                %(total contrato)s,
                %(implatacao automatica)s,
                %(implatacao typeform)s,
                %(condicoes)s)"""
        pg.extras.execute_batch(curs, postgres_insert_query, response, page_size=len(response))
        connection.commit()
        count = curs.rowcount
        print(count, "Record inserted successfully into mobile table")
        curs.close()
        connection.close()
        print("PostgreSQL connection is closed")
        print(f'Dados inseridos na tabela, a partir de')

    except (Exception, pg.Error) as error:
        print("Failed to insert record into mobile table", error)