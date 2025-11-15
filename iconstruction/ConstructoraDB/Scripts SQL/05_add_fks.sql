ALTER TABLE usuarios
  ADD CONSTRAINT fk_usuarios_rol FOREIGN KEY (rol_id) REFERENCES roles(id);

ALTER TABLE actividades
  ADD CONSTRAINT fk_act_proy FOREIGN KEY (proyecto_id) REFERENCES proyectos(id);

ALTER TABLE avances
  ADD CONSTRAINT fk_avances_actividad FOREIGN KEY (actividad_id) REFERENCES actividades(id);

ALTER TABLE ingresos
  ADD CONSTRAINT fk_ingresos_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id);

ALTER TABLE ingreso_material
  ADD CONSTRAINT fk_ing_mat_ingreso  FOREIGN KEY (ingreso_id)  REFERENCES ingresos(id),
  ADD CONSTRAINT fk_ing_mat_material FOREIGN KEY (material_id) REFERENCES materiales(id);

ALTER TABLE entregas
  ADD CONSTRAINT fk_entregas_proyecto FOREIGN KEY (proyecto_id) REFERENCES proyectos(id),
  ADD CONSTRAINT fk_entregas_actividad FOREIGN KEY (actividad_id) REFERENCES actividades(id),
  ADD CONSTRAINT fk_entregas_usuario  FOREIGN KEY (usuario_id)  REFERENCES usuarios(id);

ALTER TABLE entrega_material
  ADD CONSTRAINT fk_ent_mat_entrega  FOREIGN KEY (entrega_id)  REFERENCES entregas(id),
  ADD CONSTRAINT fk_ent_mat_material FOREIGN KEY (material_id) REFERENCES materiales(id);

ALTER TABLE prestamo_herramienta
  ADD CONSTRAINT fk_prestamo_entrega     FOREIGN KEY (entrega_id)     REFERENCES entregas(id),
  ADD CONSTRAINT fk_prestamo_herramienta FOREIGN KEY (herramienta_id) REFERENCES herramientas(id);

ALTER TABLE devolucion_herramienta
  ADD CONSTRAINT fk_devh_prestamo FOREIGN KEY (prestamo_id) REFERENCES prestamo_herramienta(id);

ALTER TABLE devolucion_material
  ADD CONSTRAINT fk_devm_entrega_material FOREIGN KEY (entrega_material_id) REFERENCES entrega_material(id);

ALTER TABLE ajustes_stock
  ADD CONSTRAINT fk_ajuste_material   FOREIGN KEY (material_id)   REFERENCES materiales(id),
  ADD CONSTRAINT fk_ajuste_autorizado FOREIGN KEY (autorizado_por) REFERENCES usuarios(id);

ALTER TABLE auditoria
  ADD CONSTRAINT fk_auditoria_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id);
