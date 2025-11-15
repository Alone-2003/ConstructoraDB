-- Esquema iConstruction: inventario + obra
CREATE TABLE roles (
  id BIGSERIAL,
  nombre TEXT NOT NULL UNIQUE
);

CREATE TABLE usuarios (
  id BIGSERIAL,
  nombre TEXT NOT NULL,
  rut TEXT NOT NULL UNIQUE,
  email TEXT NOT NULL UNIQUE,
  hash_password TEXT NOT NULL,
  rol_id BIGINT NOT NULL,
  estado TEXT NOT NULL DEFAULT 'activo'
);

CREATE TABLE proyectos (
  id BIGSERIAL,
  nombre TEXT NOT NULL,
  mandante TEXT,
  fecha_inicio DATE,
  fecha_fin_comprometida DATE,
  estado TEXT NOT NULL DEFAULT 'en_ejecucion'
);

CREATE TABLE actividades (
  id BIGSERIAL,
  proyecto_id BIGINT NOT NULL,
  nombre TEXT NOT NULL,
  fecha_inicio_plan DATE,
  fecha_fin_plan DATE,
  pct_objetivo NUMERIC(5,2) DEFAULT 100.00
);

CREATE TABLE avances (
  id BIGSERIAL,
  actividad_id BIGINT NOT NULL,
  pct_avance NUMERIC(5,2) NOT NULL,
  fecha TIMESTAMP NOT NULL DEFAULT now(),
  notas TEXT,
  evidencia_url TEXT
);

CREATE TABLE materiales (
  id BIGSERIAL,
  codigo TEXT NOT NULL,
  nombre TEXT NOT NULL,
  unidad TEXT NOT NULL,
  stock NUMERIC(12,2) NOT NULL DEFAULT 0,
  stock_min NUMERIC(12,2) NOT NULL DEFAULT 0,
  vence_el DATE
);

CREATE UNIQUE INDEX ux_materiales_codigo ON materiales(codigo);

CREATE TABLE herramientas (
  id BIGSERIAL,
  codigo TEXT NOT NULL,
  nombre TEXT NOT NULL,
  serie TEXT,
  estado TEXT NOT NULL DEFAULT 'disponible'
);

CREATE UNIQUE INDEX ux_herramientas_codigo ON herramientas(codigo);
CREATE UNIQUE INDEX ux_herramientas_serie  ON herramientas(serie);

CREATE TABLE ingresos (
  id BIGSERIAL,
  proveedor TEXT NOT NULL,
  doc_tipo TEXT NOT NULL,     -- factura/guía
  doc_numero TEXT NOT NULL,
  fecha TIMESTAMP NOT NULL DEFAULT now(),
  usuario_id BIGINT NOT NULL
);

CREATE TABLE ingreso_material (
  id BIGSERIAL,
  ingreso_id BIGINT NOT NULL,
  material_id BIGINT NOT NULL,
  cantidad NUMERIC(12,2) NOT NULL CHECK (cantidad>0)
);

CREATE TABLE entregas (
  id BIGSERIAL,
  fecha TIMESTAMP NOT NULL DEFAULT now(),
  proyecto_id BIGINT NOT NULL,
  actividad_id BIGINT,
  receptor TEXT NOT NULL,
  usuario_id BIGINT NOT NULL
);

CREATE TABLE entrega_material (
  id BIGSERIAL,
  entrega_id BIGINT NOT NULL,
  material_id BIGINT NOT NULL,
  cantidad NUMERIC(12,2) NOT NULL CHECK (cantidad>0)
);

CREATE TABLE prestamo_herramienta (
  id BIGSERIAL,
  entrega_id BIGINT NOT NULL,
  herramienta_id BIGINT NOT NULL,
  estado_entrega TEXT NOT NULL DEFAULT 'operativa'
);

CREATE TABLE devolucion_herramienta (
  id BIGSERIAL,
  prestamo_id BIGINT NOT NULL,
  fecha TIMESTAMP NOT NULL DEFAULT now(),
  estado_devuelta TEXT NOT NULL DEFAULT 'operativa',
  evidencia_url TEXT
);

CREATE TABLE devolucion_material (
  id BIGSERIAL,
  entrega_material_id BIGINT NOT NULL,
  cantidad NUMERIC(12,2) NOT NULL CHECK (cantidad>0),
  fecha TIMESTAMP NOT NULL DEFAULT now()
);

CREATE TABLE ajustes_stock (
  id BIGSERIAL,
  material_id BIGINT NOT NULL,
  cantidad NUMERIC(12,2) NOT NULL,  -- puede ser negativa
  motivo TEXT NOT NULL,             -- merma/pérdida/traspaso
  fecha TIMESTAMP NOT NULL DEFAULT now(),
  autorizado_por BIGINT NOT NULL,
  observacion TEXT
);

CREATE TABLE auditoria (
  id BIGSERIAL,
  usuario_id BIGINT,
  accion TEXT NOT NULL,
  entidad TEXT,
  entidad_id BIGINT,
  created_at TIMESTAMP NOT NULL DEFAULT now(),
  ip TEXT,
  detalles JSONB
);
