-- Esto es un cambio a la base para su funcionamiento correcto con la api

ALTER TABLE powerplantpoint ADD geom_json text NULL;

UPDATE powerplantpoint
SET geom_json=tablaBack.geo_json
FROM (select ST_AsGeoJSON(geom) as geo_json from powerplantpoint) as tablaBack ; 

UPDATE powerplantpoint SET geom_json = ST_AsGeoJSON(geom);

ALTER TABLE natural_protected_areas ADD geom_json text NULL;

UPDATE natural_protected_areas
SET geom_json=tablaBack.geo_json
FROM (select ST_AsGeoJSON(geom) as geo_json from natural_protected_areas) as tablaBack ; 

UPDATE natural_protected_areas SET geom_json = ST_AsGeoJSON(geom);

ALTER TABLE substationpoint ADD geom_json text NULL;

UPDATE substationpoint
SET geom_json=tablaBack.geo_json
FROM (select ST_AsGeoJSON(geom) as geo_json from substationpoint) as tablaBack ; 

UPDATE substationpoint SET geom_json = ST_AsGeoJSON(geom);

ALTER TABLE tranline ADD geom_json text NULL;

UPDATE tranline
SET geom_json=tablaBack.geo_json
FROM (select ST_AsGeoJSON(geom) as geo_json from tranline) as tablaBack ; 

UPDATE tranline SET geom_json = ST_AsGeoJSON(geom);
