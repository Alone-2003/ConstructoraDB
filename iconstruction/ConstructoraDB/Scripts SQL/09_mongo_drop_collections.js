// Ejecutar con: mongosh --file 09_mongo_drop_collections.js
use iconstruction;

db.eventos_avance.drop();
db.recepciones.drop();
db.audit_logs.drop();
db.evidencias.drop();
