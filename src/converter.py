
import json
import datetime
def create_dict_to_powerplant(powerplant):

	id_plant_point = powerplant[0]
	name_plant = powerplant[1]
	technology_plant = powerplant[2]
	geom_string = powerplant[3]
	cap_effective_mw = powerplant[4]
	status_plant = powerplant[5]
	com_op_date = powerplant[6]

	if com_op_date == None:
		com_op_date = datetime.date.today()	

	geom_dict = json.loads(geom_string)

	powerplant_dict = {"type":"Feature",
		"geometry":geom_dict,
		"properties":{
		"id_plant_point":id_plant_point,
		"plant_name":name_plant,
		"status":status_plant,
		"technology":technology_plant,
		"effective_capacity":cap_effective_mw ,
		"cod":com_op_date.strftime('%d/%m/%Y')}}

	return powerplant_dict


def create_dict_to_substations(substation):

	id_substation_point = substation[0]
	name_plant = substation[1]
	geom_string = substation[2]

	geom_dict = json.loads(geom_string)

	substation_dict = {"type":"Feature",
		"geometry":geom_dict,
		"properties":{
		"id_plant_point":id_substation_point,
		"substation_name":name_plant,
		}}

	return substation_dict


def create_dict_to_tranline(tranline):

	id_tran_line = tranline[0]
	voltage_tran_line = tranline[1]
	color_tran_line = tranline[2]
	geom_string = tranline[3]

	geom_dict = json.loads(geom_string)

	tranline_dict = {"type":"Feature",
		"geometry":geom_dict,
		"properties":{
		"id_plant_point":id_tran_line,
		"voltage_tran_line":voltage_tran_line,
		}}

	return tranline_dict

def create_dict_to_ground_cover_and_vegetation(gcv):
	id_gcv = gcv[0]
	gcv_area = gcv[1]
	gcv_perimeter = gcv[2]
	gcv_grupo_fina =gcv[3]
	geom_string = gcv[4]

	geom_dict = json.loads(geom_string)

	tranline_dict = {"type":"Feature",
		"geometry":geom_dict,
		"properties":{
		"id_plant_point":id_gcv,
		"gcv_area":gcv_area,
		"gcv_perimeter":gcv_perimeter,
		'gcv_grupo_fina':gcv_grupo_fina
		}}

	return tranline_dict


def create_dict_to_natural_protected_areas(gcv):
	id_npa = gcv[0]
	npa_area_type = gcv[1]
	geom_string = gcv[2]

	geom_dict = json.loads(geom_string)

	tranline_dict = {"type":"Feature",
		"geometry":geom_dict,
		"properties":{
		"id_npa":id_npa,
		"npa_area_type":npa_area_type
		}}

	return tranline_dict
	