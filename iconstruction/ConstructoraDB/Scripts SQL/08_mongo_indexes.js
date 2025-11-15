// Ejecutar con: mongosh --file 08_mongo_indexes.js
use iconstruction;

db.evidencias.createIndex({ relacion:1, relacionId:1, creadoEn:-1 });
db.evidencias.createIndex({ tipo:1, creadoEn:-1 });

db.audit_logs.createIndex({ usuarioId:1, fecha:-1 });
db.audit_logs.createIndex({ endpoint:1, fecha:-1 });

db.recepciones.createIndex({ entregaId:1 }, { unique: true });     // una recepción por entrega
db.recepciones.createIndex({ "items.materialCodigo":1 });

db.eventos_avance.createIndex({ actividadId:1, fecha:-1 });
