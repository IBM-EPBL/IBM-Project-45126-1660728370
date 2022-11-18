
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=;PORT=32328;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=gmz37043;PWD=5eCfk6YOpNcZhK1H",'','')
print(conn)
print("connection successful...")