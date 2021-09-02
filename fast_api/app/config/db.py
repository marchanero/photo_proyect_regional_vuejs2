from sqlalchemy import create_engine, MetaData

engine = create_engine ("mysql+pymysql://root:orangepi.@emosys.site:3306/usuarios")

meta = MetaData()
conn=engine.connect()