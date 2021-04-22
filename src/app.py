from flask import Flask,jsonify
import converter as cvr
import SQL
from flask_cors import CORS

app= Flask(__name__)
CORS(app)

@app.route('/substations/',methods=['GET'])
def get_substations():

	sql_query = "SELECT id_sbn_point,name_sbn,geom_json from substationpoint"

	substations = SQL.get_result_query(sql_query)
	
	info_substations = []

	for pp in substations:
		info_substations.append(cvr.create_dict_to_substations(pp))

	substations_json = {"type": "FeatureCollection", 
	"features": info_substations
	}
	return jsonify(substations_json)

@app.route('/substations/<string:nothing>',methods=['GET'])
def get_substations_by_nothing(nothing):

	sql_query = "SELECT id_sbn_point,name_sbn,geom_json from substationpoint"

	substations = SQL.get_result_query(sql_query)
	
	info_substations = []

	for pp in substations:
		info_substations.append(cvr.create_dict_to_substations(pp))

	substations_json = {"type": "FeatureCollection", 
	"features": info_substations
	}
	return jsonify(substations_json)


@app.route('/powerplants/',methods=['GET'])
def get_powerplants():

	sql_query = "SELECT id_plant_point,name_plant,technology_plant,geom_json,cap_effective_mw,status_plant,com_op_date from powerplantpoint"

	powerplants = SQL.get_result_query(sql_query)	

	info_powerplants = []

	for pp in powerplants:
		
		info_powerplants.append(cvr.create_dict_to_powerplant(pp))

	powerplants_json = {"type": "FeatureCollection", 
	"features": info_powerplants
	}
	
	return jsonify(powerplants_json)

@app.route('/tranline/',methods=['GET'])
def get_tranline_all():
	sql_query = "SELECT id_tran_line,voltage_tran_line,color_tran_line,geom_json from tranline"
	tranlines = SQL.get_result_query(sql_query)	

	info_tranlines = []

	for pp in tranlines:
		info_tranlines.append(cvr.create_dict_to_tranline(pp))

	tranlines_json = {"type": "FeatureCollection", 
	"features": info_tranlines
	}
	#print(tranlines_json)
	return jsonify(tranlines_json)

@app.route('/tranline/<string:voltage>',methods=['GET'])
def get_tranline_by_voltage(voltage):
	sql_query="SELECT id_tran_line,voltage_tran_line,color_tran_line,geom_json from tranline where voltage_tran_line = " +voltage
	tranlines = SQL.get_result_query(sql_query)	
	##print(tranlines)
	info_tranlines	 = []

	for pp in tranlines:
		info_tranlines.append(cvr.create_dict_to_tranline(pp))

	tranlines_json = {"type": "FeatureCollection", 
	"features": info_tranlines
	}
	#print(powerplants_json)
	return jsonify(tranlines_json)




@app.route('/powerplants/<string:technology>',methods=['GET'])
def get_powerPlants_by_technology_json(technology):
	sql_query = "SELECT id_plant_point,name_plant,technology_plant,geom_json,cap_effective_mw,status_plant,com_op_date from powerplantpoint where technology_plant = '" +technology+"'"
	powerplants = SQL.get_result_query(sql_query)	

	info_powerplants = []

	for pp in powerplants:
		info_powerplants.append(cvr.create_dict_to_powerplant(pp))

	powerplants_json = {"type": "FeatureCollection", 
	"features": info_powerplants
	}
	#print(powerplants_json)
	return jsonify(powerplants_json)




@app.route('/Groud_Cover_and_Vegetation/<string:group>',methods=['GET'])
def get_Groud_Cover_and_Vegetation_by_group_json(group):
	sql_query = "SELECT id_gcv,gcv_area,gcv_perimeter,gcv_grupo_fina,geom_json from ground_cover_and_vegetation where gcv_grupo_fina = " +group
	gcvs = SQL.get_result_query(sql_query)

	info_gcvs= []

	for pp in gcvs:
		info_gcvs.append(cvr.create_dict_to_ground_cover_and_vegetation(pp))

	gcvs_json = {"type": "FeatureCollection", 
	"features": info_gcvs
	}
	#print(powerplants_json)
	return jsonify(gcvs_json)

@app.route('/Groud_Cover_and_Vegetation',methods=['GET'])
def get_Groud_Cover_and_Vegetation_All_json():

	sql_query ="SELECT id_gcv,gcv_area,gcv_perimeter,gcv_grupo_fina,geom_json from ground_cover_and_vegetation"
	gcvs = SQL.get_result_query(sql_query)

	info_gcvs= []

	for pp in gcvs:
		info_gcvs.append(cvr.create_dict_to_ground_cover_and_vegetation(pp))

	gcvs_json = {"type": "FeatureCollection", 
	"features": info_gcvs
	}
	#print(powerplants_json)
	return jsonify(gcvs_json)


@app.route('/natural_protected_areas/',methods=['GET'])
def get_natural_protect_areas_all_json():

	sql_query = "SELECT id_npa,npa_area_type,geom_json from natural_protected_areas"
	natural_protected_areas = SQL.get_result_query(sql_query)	

	info_get_natural_protect_areas_by_area_type= []

	for pp in natural_protected_areas:
		info_get_natural_protect_areas_by_area_type.append(cvr.create_dict_to_natural_protected_areas(pp))

	natural_protected_areas_json = {"type": "FeatureCollection", 
	"features": info_get_natural_protect_areas_by_area_type
	}
	#print(powerplants_json)
	return jsonify(natural_protected_areas_json)


@app.route('/natural_protected_areas/<string:area_type>',methods=['GET'])
def get_natural_protect_areas_all_type(area_type):
	sql_query = "SELECT id_npa,npa_area_type,geom_json from natural_protected_areas where npa_area_type = '" +area_type+"'"
	natural_protected_areas = SQL.get_result_query(sql_query)	

	info_get_natural_protect_areas_by_area_type= []

	for pp in natural_protected_areas:
		info_get_natural_protect_areas_by_area_type.append(cvr.create_dict_to_natural_protected_areas(pp))

	natural_protected_areas_json = {"type": "FeatureCollection", 
	"features": info_get_natural_protect_areas_by_area_type
	}
	#print(powerplants_json)
	return jsonify(natural_protected_areas_json)



if __name__ == '__main__':
	app.run(debug=True)

