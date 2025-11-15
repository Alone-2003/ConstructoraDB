CREATE INDEX ix_ing_material_material ON ingreso_material(material_id);
CREATE INDEX ix_ent_mat_material      ON entrega_material(material_id);
CREATE INDEX ix_prestamo_herramienta  ON prestamo_herramienta(herramienta_id);
CREATE INDEX ix_avances_actividad     ON avances(actividad_id, fecha);
CREATE INDEX ix_ajustes_material      ON ajustes_stock(material_id, fecha);
CREATE INDEX ix_entregas_proy_act     ON entregas(proyecto_id, actividad_id, fecha);
