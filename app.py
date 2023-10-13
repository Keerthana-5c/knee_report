from flask import Flask, render_template, request, jsonify
import json
import pandas as pd



app = Flask(__name__)
@app.route('/')
def index():
    return render_template('knee.html')

obs1 = []
imp = []
@app.route('/get_report', methods=['POST'])
def get_report():
    data = request.get_json()
    print(data)
    arthritis = [' Degenerative changes noted in the form of Marginal Osteophytes in the Knee Joint with no Subchondral Sclerosis. ',' Degenerative changes noted in the form of Marginal Osteophytes, Reducing Joint Space in the Knee Joint with no Subchondral Sclerosis. ','Degenerative changes noted in the form of Marginal Osteophytes, Reducing Joint Space in the Knee Joint with Subchondral Sclerosis. ','Degenerative changes noted in the form of Marginal Osteophytes, Reducing Joint Space in the Knee Joint with Subchondral Sclerosis and Cyst. ','Degenerative changes noted in the form of Reducing Joint Space in the Knee Joint with no Subchondral Sclerosis. ','Degenerative changes noted in the form of Reducing Joint Space in the Knee Joint with Subchondral Sclerosis.','Degenerative changes noted in the form of Marginal Osteophytes in the Knee Joint with Subchondral Sclerosis.']
    loosebody = ['Loose Bodies are noted.','Loose Bodies are noted in the Left Knee.','Loose Bodies are noted Right knee.','Loose Bodies are noted in both the knee joints.']
    postop = ['Post Operative changes are noted  with no evidence of any metal implants displacement in present x ray.', 'Post Operative changes are noted  with no evidence of any metal implants displacement in Left Knee. ', 'Post Operative changes are noted  with no evidence of any metal implants displacement in Right Knee.', 'Post Operative changes are noted  with no evidence of any metal implants displacement in both the Knee in the x ray.']
    fabella = ['Incidental Fabella noted in popliteal fossa. ', 'Incidental Fabella noted in popliteal fossa of Left Knee.' ,'Incidental Fabella noted in popliteal fossa of Right Knee. ','Incidental Fabella noted in popliteal fossa of both the Joints. ']
    pts = ['Tibia shows prominent tibial spine. ', 'Tibia of Left knee shows prominent tibial spine.','Tibia Right Knee shows prominent tibial spine. ' ,'Tibia of both knee shows prominent tibial spine. ']
    scleroticchange = ['Sclerotic change is found in the Tibia','Sclerotic change is found in the Left Knee Tibia', 'Sclerotic change is found in the Right Knee Tibia', 'Sclerotic change is found in both knee Tibia']
    tkr = ['Total replacement of Right knee joint with no evidence of any metal implants displacement in present x ray. ','Partial replacement of Right knee joint with no evidence of any metal implants displacement in present x ray. ','Total replacement of Left knee joint with no evidence of any metal implants displacement in present x ray. ','Partial replacement of Left knee joint with no evidence of any metal implants displacement in present x ray. ', 'Total replacement of both knee joint with no evidence of any metal implants displacement in present x ray.  ', 'Partial replacement of both knee joint with no evidence of any metal implants displacement in present x ray. ']
    normal = ['Visualized part of femur and tibia show normal density. ']
    arthritis_imp = ['Suggestive of Mild Knee Osteoarthritis in the knee joint','Suggestive of Grade 1 Knee Osteoarthritis in the knee joint','Suggestive of Grade 2 Knee Osteoarthritis in the knee joint','Suggestive of Grade 3 Knee Osteoarthritis in the knee joint','Suggestive of Grade 4 Knee Osteoarthritis in the knee joint']
    bilateral_imp = ['Suggestive of Mild Knee Osteoarthritis in both the knee joint','Suggestive of Grade 1 Knee Osteoarthritis in both the knee joint','Suggestive of Grade 2 Knee Osteoarthritis in both the knee joint','Suggestive of Grade 3 Knee Osteoarthritis in both the knee joint','Suggestive of Grade 4 Knee Osteoarthritis in both the knee joint']
    right_imp = ['Suggestive of Mild Knee Osteoarthritis in the Right knee joint','Suggestive of Grade 1 Knee Osteoarthritis in the Right knee joint','Suggestive of Grade 2 Knee Osteoarthritis in the Right knee joint','Suggestive of Grade 3 Knee Osteoarthritis in the Right knee joint','Suggestive of Grade 4 Knee Osteoarthritis in the Right knee joint']
    left_imp = ['Suggestive of Mild Knee Osteoarthritis in the left knee joint','Suggestive of Grade 1 Knee Osteoarthritis in the left knee joint','Suggestive of Grade 2 Knee Osteoarthritis in the left knee joint','Suggestive of Grade 3 Knee Osteoarthritis in the left knee joint','Suggestive of Grade 4 Knee Osteoarthritis in the left knee joint']
    norm_imp = ['NO STRUCTURAL ABNORMALITY SEEN.']
    acl = ['Post Operative changes are noted in the form of ACL Reconstruction with no evidence of any metal implants displacement in present x ray.', 'Post Operative changes are noted in the form of ACL Reconstruction with no evidence of any metal implants displacement in Left Knee. ', 'Post Operative changes are noted in the form of ACL Reconstruction with no evidence of any metal implants displacement in Right Knee.', 'Post Operative changes are noted in the form of ACL Reconstruction with no evidence of any metal implants displacement in both the Knee in the x ray.']
    slr = ['Sclerosis found subchondral region of Tibia.','Sclerosis found subchondral region of Tibia of Left Knee','Sclerosis found subchondral region of Tibia of Right Knee','Sclerosis found subchondral region of Tibia of both the Knee Joints']
    obs = []
    obs_r = ["Right Knee:\n"]
    obs_l = ["Left Knee:\n"]
    imp = []

    obs_exist = ['Lower end of the Femur, Patella and Upper ends of the Tibia and Fibula appear normal.','Overlying soft tissues are unremarkable.','No lytic/sclerotic lesion is seen. ']

    

    # Check the 'Anatomy' key
    if 'Anatomy' in data and 'Abnormality' in data and 'Grade' in data:
        anatomy_value = data['Anatomy']
        abnormality_value = data['Abnormality']
        grade_value = data['Grade']
        

        if anatomy_value == 'Right':
            if isinstance(abnormality_value, list)and 'Normal' in abnormality_value :
                obs.append(normal[0])
            elif isinstance(abnormality_value, list)and 'Osteophyte' in abnormality_value and 'Reducing Joint Space' not in abnormality_value and 'Sclerosis' not in abnormality_value and 'Cyst' not in abnormality_value:
                obs.append(arthritis[0])
            elif isinstance(abnormality_value, list)and 'Osteophyte' in abnormality_value and 'Reducing Joint Space' in abnormality_value and 'Sclerosis' not in abnormality_value and 'Cyst' not in abnormality_value :
                obs.append(arthritis[1])
            elif isinstance(abnormality_value, list)and 'Osteophyte' in abnormality_value and 'Reducing Joint Space' in abnormality_value and 'Sclerosis' in abnormality_value and 'Cyst' not in abnormality_value:
                obs.append(arthritis[2])
            elif isinstance(abnormality_value, list)and 'Osteophyte' in abnormality_value and 'Reducing Joint Space' in abnormality_value and 'Sclerosis' in abnormality_value and 'Cyst' in abnormality_value :
                obs.append(arthritis[3])
            elif isinstance(abnormality_value, list)and 'Osteophyte' not in abnormality_value and 'Reducing Joint Space' in abnormality_value and 'Sclerosis' not in abnormality_value and 'Cyst' not in abnormality_value :
                obs.append(arthritis[4])
            elif isinstance(abnormality_value, list)and 'Osteophyte' not in abnormality_value and 'Reducing Joint Space' in abnormality_value and 'Sclerosis' in abnormality_value and 'Cyst' not in abnormality_value :
                obs.append(arthritis[5])
            elif isinstance(abnormality_value, list)and 'Osteophyte' in abnormality_value and 'Reducing Joint Space' not in abnormality_value and 'Sclerosis' in abnormality_value and 'Cyst' not in abnormality_value :
                obs.append(arthritis[6])

            
            if isinstance(abnormality_value, list)and 'Total Knee Replacement' in abnormality_value:
                obs.append(tkr[0])
            if isinstance(abnormality_value, list)and 'Partial Knee Replacement' in abnormality_value:
                obs.append(tkr[1])
            if isinstance(abnormality_value, list)and 'Post OP' in abnormality_value:
                obs.append(postop[0])
            if isinstance(abnormality_value, list)and 'ACL Reconstruction' in abnormality_value:
                obs.append(acl[0])
            if isinstance(abnormality_value, list)and 'Osteophyte' not in abnormality_value and 'Reducing Joint Space' not in abnormality_value and 'Sclerosis' in abnormality_value and 'Cyst' not in abnormality_value :
                obs.append(slr[0])
            if isinstance(abnormality_value, list)and 'Loose Bodies' in abnormality_value:
                obs.append(loosebody[0])
            if isinstance(abnormality_value, list)and 'Sclerotic Changes' in abnormality_value:
                obs.append(scleroticchange[0])
            if isinstance(abnormality_value, list)and 'Prominent Tibial Spike' in abnormality_value:
                obs.append(pts[0])
            if isinstance(abnormality_value, list)and 'Fabella' in abnormality_value:
                obs.append(fabella[0])


        

        elif anatomy_value == 'Left':
            if isinstance(abnormality_value, list)and 'Normal' in abnormality_value :
                obs.append(normal[0])
            elif isinstance(abnormality_value, list)and 'Osteophyte' in abnormality_value and 'Reducing Joint Space' not in abnormality_value and 'Sclerosis' not in abnormality_value and 'Cyst' not in abnormality_value:
                obs.append(arthritis[0])
            elif isinstance(abnormality_value, list)and 'Osteophyte' in abnormality_value and 'Reducing Joint Space' in abnormality_value and 'Sclerosis' not in abnormality_value and 'Cyst' not in abnormality_value :
                obs.append(arthritis[1])
            elif isinstance(abnormality_value, list)and 'Osteophyte' in abnormality_value and 'Reducing Joint Space' in abnormality_value and 'Sclerosis' in abnormality_value and 'Cyst' not in abnormality_value:
                obs.append(arthritis[2])
            elif isinstance(abnormality_value, list)and 'Osteophyte' in abnormality_value and 'Reducing Joint Space' in abnormality_value and 'Sclerosis' in abnormality_value and 'Cyst' in abnormality_value :
                obs.append(arthritis[3])
            elif isinstance(abnormality_value, list)and 'Osteophyte' not in abnormality_value and 'Reducing Joint Space' in abnormality_value and 'Sclerosis' not in abnormality_value and 'Cyst' not in abnormality_value :
                obs.append(arthritis[4])
            elif isinstance(abnormality_value, list)and 'Osteophyte' not in abnormality_value and 'Reducing Joint Space' in abnormality_value and 'Sclerosis' in abnormality_value and 'Cyst' not in abnormality_value :
                obs.append(arthritis[5])
            elif isinstance(abnormality_value, list)and 'Osteophyte' in abnormality_value and 'Reducing Joint Space' not in abnormality_value and 'Sclerosis' in abnormality_value and 'Cyst' not in abnormality_value :
                obs.append(arthritis[6])
            
            if isinstance(abnormality_value, list)and 'Total Knee Replacement' in abnormality_value:
                obs.append(tkr[0])
            if isinstance(abnormality_value, list)and 'Partial Knee Replacement' in abnormality_value:
                obs.append(tkr[1])
            if isinstance(abnormality_value, list)and 'Post OP' in abnormality_value:
                obs.append(postop[0])
            if isinstance(abnormality_value, list)and 'ACL Reconstruction' in abnormality_value:
                obs.append(acl[0]) 
            if isinstance(abnormality_value, list)and 'Osteophyte' not in abnormality_value and 'Reducing Joint Space' not in abnormality_value and 'Sclerosis' in abnormality_value and 'Cyst' not in abnormality_value :
                obs.append(slr[0])                               
            if isinstance(abnormality_value, list)and 'Loose Bodies' in abnormality_value:
                obs.append(loosebody[0])
            if isinstance(abnormality_value, list)and 'Sclerotic Changes' in abnormality_value:
                obs.append(scleroticchange[0])
            if isinstance(abnormality_value, list)and 'Prominent Tibial Spike' in abnormality_value:
                obs.append(pts[0])
            if isinstance(abnormality_value, list)and 'Fabella' in abnormality_value:
                obs.append(fabella[0])

        else:
            if 'Bilateral' in data:
                bilateral_data = data['Bilateral']

                if 'RightKnee' in bilateral_data and 'LeftKnee' in bilateral_data:

                    right_knee_data = bilateral_data['RightKnee']
                    left_knee_data = bilateral_data['LeftKnee']
                    
                    if 'Abnormality' in right_knee_data and 'Abnormality' in left_knee_data and 'Grade' in right_knee_data and 'Grade' in left_knee_data:
                        right_knee_abnormality = right_knee_data['Abnormality']
                        left_knee_abnormality = left_knee_data['Abnormality']
                        right_knee_grade = right_knee_data['Grade']
                        left_knee_grade = left_knee_data['Grade']
                        
                        if isinstance(right_knee_abnormality, list)and 'Osteophyte' in right_knee_abnormality and 'Reducing Joint Space' not in right_knee_abnormality and 'Sclerosis' not in right_knee_abnormality and 'Cyst' not in right_knee_abnormality:
                            obs_r.append(arthritis[0])
                        elif isinstance(right_knee_abnormality, list)and 'Osteophyte' in right_knee_abnormality and 'Reducing Joint Space' in right_knee_abnormality and 'Sclerosis' not in right_knee_abnormality and 'Cyst' not in right_knee_abnormality :
                            obs_r.append(arthritis[1])
                        elif isinstance(right_knee_abnormality, list)and 'Osteophyte' in right_knee_abnormality and 'Reducing Joint Space' in right_knee_abnormality and 'Sclerosis' in right_knee_abnormality and 'Cyst' not in right_knee_abnormality:
                            obs_r.append(arthritis[2])
                        elif isinstance(right_knee_abnormality, list)and 'Osteophyte' in right_knee_abnormality and 'Reducing Joint Space' in right_knee_abnormality and 'Sclerosis' in right_knee_abnormality and 'Cyst' in right_knee_abnormality :
                            obs_r.append(arthritis[3])
                        elif isinstance(right_knee_abnormality, list)and 'Osteophyte' not in right_knee_abnormality and 'Reducing Joint Space' in right_knee_abnormality and 'Sclerosis' not in right_knee_abnormality and 'Cyst' not in right_knee_abnormality :
                            obs_r.append(arthritis[4])
                        elif isinstance(abnormality_value, list)and 'Osteophyte' not in abnormality_value and 'Reducing Joint Space' in abnormality_value and 'Sclerosis' in abnormality_value and 'Cyst' not in abnormality_value :
                            obs_r.append(arthritis[5])
                        elif isinstance(abnormality_value, list)and 'Osteophyte' in abnormality_value and 'Reducing Joint Space' not in abnormality_value and 'Sclerosis' in abnormality_value and 'Cyst' not in abnormality_value :
                            obs_r.append(arthritis[6])
                        
                        if isinstance(right_knee_abnormality, list)and 'Normal' in right_knee_abnormality :
                            obs_r.append(normal[0])
                        if isinstance(right_knee_abnormality, list)and 'Total Knee Replacement' in right_knee_abnormality:
                            obs_r.append(tkr[0])
                        if isinstance(right_knee_abnormality, list)and 'Partial Knee Replacement' in right_knee_abnormality:
                            obs_r.append(tkr[1])
                        if isinstance(right_knee_abnormality, list)and 'Post OP' in right_knee_abnormality:
                            obs_r.append(postop[0])
                        if isinstance(right_knee_abnormality, list)and 'ACL Reconstruction' in right_knee_abnormality:
                            obs_r.append(acl[2])  
                        if isinstance(right_knee_abnormality, list)and 'Osteophyte' not in right_knee_abnormality and 'Reducing Joint Space' not in right_knee_abnormality and 'Sclerosis' in right_knee_abnormality and 'Cyst' not in right_knee_abnormality :
                            obs_r.append(slr[2])                          
                        if isinstance(right_knee_abnormality, list)and 'Loose Bodies' in right_knee_abnormality:
                            obs_r.append(loosebody[0])
                        if isinstance(right_knee_abnormality, list)and 'Sclerotic Changes' in right_knee_abnormality:
                            obs_r.append(scleroticchange[0])
                        if isinstance(right_knee_abnormality, list)and 'Fabella' in right_knee_abnormality:
                            obs_r.append(fabella[0])
                        if isinstance(right_knee_abnormality, list)and 'Prominent Tibial Spike' in right_knee_abnormality:
                            obs_r.append(pts[0])





                        if isinstance(left_knee_abnormality, list)and 'Osteophyte' in left_knee_abnormality and 'Reducing Joint Space' not in left_knee_abnormality and 'Sclerosis' not in left_knee_abnormality and 'Cyst' not in left_knee_abnormality:
                            obs_l.append(arthritis[0])
                        elif isinstance(left_knee_abnormality, list)and 'Osteophyte' in left_knee_abnormality and 'Reducing Joint Space' in left_knee_abnormality and 'Sclerosis' not in left_knee_abnormality and 'Cyst' not in left_knee_abnormality :
                            obs_l.append(arthritis[1])
                        elif isinstance(left_knee_abnormality, list)and 'Osteophyte' in left_knee_abnormality and 'Reducing Joint Space' in left_knee_abnormality and 'Sclerosis' in left_knee_abnormality and 'Cyst' not in left_knee_abnormality:
                            obs_l.append(arthritis[2])
                        elif isinstance(left_knee_abnormality, list)and 'Osteophyte' in left_knee_abnormality and 'Reducing Joint Space' in left_knee_abnormality and 'Sclerosis' in left_knee_abnormality and 'Cyst' in left_knee_abnormality :
                            obs_l.append(arthritis[3])
                        elif isinstance(left_knee_abnormality, list)and 'Osteophyte' not in left_knee_abnormality and 'Reducing Joint Space' in left_knee_abnormality and 'Sclerosis' not in left_knee_abnormality and 'Cyst' not in left_knee_abnormality :
                            obs_l.append(arthritis[4])
                        elif isinstance(abnormality_value, list)and 'Osteophyte' not in abnormality_value and 'Reducing Joint Space' in abnormality_value and 'Sclerosis' in abnormality_value and 'Cyst' not in abnormality_value :
                            obs_l.append(arthritis[5])
                        elif isinstance(abnormality_value, list)and 'Osteophyte' in abnormality_value and 'Reducing Joint Space' not in abnormality_value and 'Sclerosis' in abnormality_value and 'Cyst' not in abnormality_value :
                            obs_l.append(arthritis[6])
                                    
                        if isinstance(left_knee_abnormality, list)and 'Normal' in left_knee_abnormality :
                            obs_l.append(normal[0])
                        if isinstance(left_knee_abnormality, list)and 'Total Knee Replacement' in left_knee_abnormality:
                            obs_l.append(tkr[2])
                        if isinstance(left_knee_abnormality, list)and 'Partial Knee Replacement' in left_knee_abnormality:
                            obs_l.append(tkr[3])
                        if isinstance(left_knee_abnormality, list)and 'Post OP' in left_knee_abnormality:
                            obs_l.append(postop[0])
                        if isinstance(left_knee_abnormality, list)and 'ACL Reconstruction' in left_knee_abnormality:
                            obs_l.append(acl[1]) 
                        if isinstance(left_knee_abnormality, list)and 'Osteophyte' not in left_knee_abnormality and 'Reducing Joint Space' not in left_knee_abnormality and 'Sclerosis' in left_knee_abnormality and 'Cyst' not in left_knee_abnormality :
                            obs_l.append(slr[1]) 

                        if isinstance(left_knee_abnormality, list)and 'Loose Bodies' in left_knee_abnormality:
                            obs_l.append(loosebody[0])
                        if isinstance(left_knee_abnormality, list)and 'Sclerotic Changes' in left_knee_abnormality:
                            obs_l.append(scleroticchange[0])
                        if isinstance(left_knee_abnormality, list)and 'Prominent Tibial Spike' in left_knee_abnormality:
                            obs_l.append(pts[0])                            
                        if isinstance(left_knee_abnormality, list)and 'Fabella' in left_knee_abnormality:
                            obs_l.append(fabella[0])





    if obs_r != ["Right Knee:\n"]:
        obs.append(obs_r)
    if obs_l != ["Left Knee:\n"]:
        obs.append(obs_l)

    obs1 = obs + obs_exist

    print(obs1)



    if 'Anatomy' in data and 'Abnormality' in data and 'Grade' in data:
        abnormality_value = data['Abnormality']
        grade_value = data['Grade']  
        anatomy_value = data['Anatomy']
        if anatomy_value == 'Right' or anatomy_value == 'Left':
            if isinstance(abnormality_value, list) and 'Osteophyte' in abnormality_value or 'Reducing Joint Space' in abnormality_value:
                if grade_value == 'Mild':
                    imp.append(arthritis_imp[0])
                if grade_value == 'grade 1':
                    imp.append(arthritis_imp[1])
                if grade_value == 'grade 2':
                    imp.append(arthritis_imp[2])
                if grade_value == 'grade 3':
                    imp.append(arthritis_imp[3]) 
                if grade_value == 'grade 4':
                    imp.append(arthritis_imp[4])

            if isinstance(abnormality_value, list)and 'Total Knee Replacement' in abnormality_value:
                imp.append(tkr[0])
            if isinstance(abnormality_value, list)and 'Partial Knee Replacement' in abnormality_value:
                imp.append(tkr[1])
            if isinstance(abnormality_value, list)and 'Post OP' in abnormality_value:
                imp.append(postop[0])
            if isinstance(abnormality_value, list)and 'ACL Reconstruction' in abnormality_value:
                imp.append(acl[0])
            # if isinstance(abnormality_value, list)and 'Sclerosis' in abnormality_value:
            #     imp.append(slr[0])                            
            if isinstance(abnormality_value, list)and 'Loose Bodies' in abnormality_value:
                imp.append(loosebody[0])
            if isinstance(abnormality_value, list)and 'Sclerotic Changes' in abnormality_value:
                imp.append(scleroticchange[0])
            if isinstance(abnormality_value, list)and 'Prominent Tibial Spike' in abnormality_value:
                imp.append(pts[0])
            if isinstance(abnormality_value, list)and 'Fabella' in abnormality_value:
                imp.append(fabella[0])



    if 'Bilateral' in data:
        bilateral_data = data['Bilateral']

        if 'RightKnee' in bilateral_data and 'LeftKnee' in bilateral_data:

            right_knee_data = bilateral_data['RightKnee']
            left_knee_data = bilateral_data['LeftKnee']

            if 'Abnormality' in right_knee_data and 'Abnormality' in left_knee_data and 'Grade' in right_knee_data and 'Grade' in left_knee_data:
                right_knee_abnormality = right_knee_data['Abnormality']
                left_knee_abnormality = left_knee_data['Abnormality']
                right_knee_grade = right_knee_data['Grade']
                left_knee_grade = left_knee_data['Grade']

                if (isinstance(right_knee_abnormality, list) and ('Osteophyte' in right_knee_abnormality or 'Reducing Joint Space' in right_knee_abnormality)) and (isinstance(left_knee_abnormality, list) and ('Osteophyte' in left_knee_abnormality or 'Reducing Joint Space' in left_knee_abnormality)):
                    if left_knee_grade == right_knee_grade:
                        if left_knee_grade == 'Mild':
                            imp.append(bilateral_imp[0])
                        if left_knee_grade == 'grade 1':
                            imp.append(bilateral_imp[1])
                        if left_knee_grade == 'grade 2':
                            imp.append(bilateral_imp[2])
                        if left_knee_grade == 'grade 3':
                            imp.append(bilateral_imp[3]) 
                        if left_knee_grade == 'grade 4':
                            imp.append(bilateral_imp[4])
                   
                if(isinstance(right_knee_abnormality, list) and ('Osteophyte' in right_knee_abnormality or 'Reducing Joint Space' in right_knee_abnormality)) or  (isinstance(left_knee_abnormality, list) and ('Osteophyte' in left_knee_abnormality or 'Reducing Joint Space' in left_knee_abnormality)):
                        if left_knee_grade != right_knee_grade:
                            if right_knee_grade == 'Mild':
                                imp.append(right_imp[0])
                            if right_knee_grade == 'grade 1':
                                imp.append(right_imp[1])
                            if right_knee_grade == 'grade 2':
                                imp.append(right_imp[2])
                            if right_knee_grade == 'grade 3':
                                imp.append(right_imp[3]) 
                            if right_knee_grade == 'grade 4':
                                imp.append(right_imp[4])
                            if left_knee_grade == 'Mild':
                                imp.append(left_imp[0])
                            if left_knee_grade == 'grade 1':
                                imp.append(left_imp[1])
                            if left_knee_grade == 'grade 2':
                                imp.append(left_imp[2])
                            if left_knee_grade == 'grade 3':
                                imp.append(left_imp[3]) 
                            if left_knee_grade == 'grade 4':
                                imp.append(left_imp[4])
                
                if (isinstance(right_knee_abnormality, list) and ('Total Knee Replacement' in right_knee_abnormality)) and (isinstance(left_knee_abnormality, list) and 'Total Knee Replaceent' in left_knee_abnormality):
                    imp.append(tkr[4])
                if (isinstance(right_knee_abnormality, list) and ('Partial Knee Replacement' in right_knee_abnormality)) and (isinstance(left_knee_abnormality, list) and 'Partial Knee Replaceent' in left_knee_abnormality):
                    imp.append(tkr[5])
                if (isinstance(right_knee_abnormality, list) and ('Post OP' in right_knee_abnormality)) and (isinstance(left_knee_abnormality, list) and 'Post OP' in left_knee_abnormality):
                    imp.append(postop[3])
                if (isinstance(right_knee_abnormality, list) and ('ACL Reconstruction' in right_knee_abnormality)) and (isinstance(left_knee_abnormality, list) and 'ACL Reconstruction' in left_knee_abnormality):
                    imp.append(acl[3])        
                # if (isinstance(right_knee_abnormality, list) and ('Sclerosis' in right_knee_abnormality)) and (isinstance(left_knee_abnormality, list) and 'Sclerosis' in left_knee_abnormality):
                #     imp.append(slr[3])                                   
                if (isinstance(right_knee_abnormality, list) and ('Loose Bodies' in right_knee_abnormality)) and (isinstance(left_knee_abnormality, list) and 'Loose Bodies' in left_knee_abnormality):
                    imp.append(loosebody[3])
                if (isinstance(right_knee_abnormality, list) and ('Sclerotic Changes' in right_knee_abnormality)) and (isinstance(left_knee_abnormality, list) and 'Sclerotic Changes' in left_knee_abnormality):
                    imp.append(scleroticchange[3]) 
                if (isinstance(right_knee_abnormality, list) and ('Prominent Tibial Spike' in right_knee_abnormality)) and (isinstance(left_knee_abnormality, list) and 'Prominent Tibial Spike' in left_knee_abnormality):
                    imp.append(pts[3])               
                if (isinstance(right_knee_abnormality, list) and ('Fabella' in right_knee_abnormality)) and (isinstance(left_knee_abnormality, list) and 'Fabella' in left_knee_abnormality):
                    imp.append(febella[3])




                else:
                    if (isinstance(right_knee_abnormality, list)and 'Total Knee Replacement' in right_knee_abnormality) and (isinstance(left_knee_abnormality, list)and ('Total Knee Replacement' not in left_knee_abnormality)):
                        imp.append(tkr[2])
                    if (isinstance(right_knee_abnormality, list)and 'Partial Knee Replacement' in right_knee_abnormality) and (isinstance(left_knee_abnormality, list)and ('Partial Knee Replacement' not in left_knee_abnormality)):
                        imp.append(tkr[1])
                    if (isinstance(right_knee_abnormality, list)and 'Post OP' in right_knee_abnormality) and (isinstance(left_knee_abnormality, list)and ('Post OP' not in left_knee_abnormality)):
                        imp.append(postop[2])
                    if (isinstance(right_knee_abnormality, list)and 'ACL Reconstruction' in right_knee_abnormality) and (isinstance(left_knee_abnormality, list)and ('ACL Reconstruction' not in left_knee_abnormality)):
                        imp.append(acl[2])
                    # if (isinstance(right_knee_abnormality, list)and 'Sclerosis' in right_knee_abnormality) and (isinstance(left_knee_abnormality, list)and ('Sclerosis' not in left_knee_abnormality)):
                    #     imp.append(slr[2])
                    if (isinstance(right_knee_abnormality, list)and 'Prominent Tibial Spike' in right_knee_abnormality) and (isinstance(left_knee_abnormality, list)and ('Prominent Tibial Spike' not in left_knee_abnormality)):
                        imp.append(pts[2])
                    if (isinstance(right_knee_abnormality, list)and 'Sclerotic Changes' in right_knee_abnormality) and (isinstance(left_knee_abnormality, list)and ('Sclerotic Changes' not in left_knee_abnormality)):
                        imp.append(scleroticchange[2])                        
                    if (isinstance(right_knee_abnormality, list)and ('Loose Bodies' in right_knee_abnormality)) and (isinstance(left_knee_abnormality, list)and ('Loose Bodies' not in left_knee_abnormality)):
                        imp.append(loosebody[2])                        
                    if (isinstance(right_knee_abnormality, list)and 'Fabella' in right_knee_abnormality) and (isinstance(left_knee_abnormality, list)and ('Fabella' not in left_knee_abnormality)):
                        imp.append(fabella[2])


                    if (isinstance(left_knee_abnormality, list)and 'Total Knee Replacement' in left_knee_abnormality)and (isinstance(right_knee_abnormality, list)and ('Total Knee Replacement' not in right_knee_abnormality)):
                        imp.append(tkr[2])
                    if (isinstance(left_knee_abnormality, list)and 'Partial Knee Replacement' in left_knee_abnormality)and (isinstance(right_knee_abnormality, list)and ('Partial Knee Replacement' not in right_knee_abnormality)):
                        imp.append(tkr[3])
                    if (isinstance(left_knee_abnormality, list)and 'Post OP' in left_knee_abnormality) and (isinstance(right_knee_abnormality, list)and ('Post OP' not in right_knee_abnormality)):
                        imp.append(postop[1])
                    if (isinstance(left_knee_abnormality, list)and 'ACL Reconstruction' in left_knee_abnormality) and (isinstance(right_knee_abnormality, list)and ('ACL Reconstruction' not in right_knee_abnormality)):
                        imp.append(acl[1])
                    # if (isinstance(left_knee_abnormality, list)and 'Sclerosis' in left_knee_abnormality) and (isinstance(right_knee_abnormality, list)and ('Sclerosis' not in right_knee_abnormality)):
                    #     imp.append(slr[1])
                    if (isinstance(left_knee_abnormality, list)and 'Loose Bodies' in left_knee_abnormality)and  (isinstance(right_knee_abnormality, list)and ('Loose Bodies' not in right_knee_abnormality)):
                        imp.append(loosebody[1])
                    if (isinstance(left_knee_abnormality, list)and 'Sclerotic Changes' in left_knee_abnormality) and (isinstance(right_knee_abnormality, list)and ('Sclerotic Changes' not in right_knee_abnormality)):
                        imp.append(scleroticchange[2])                            
                    if (isinstance(left_knee_abnormality, list)and 'Prominent Tibial Spike' in left_knee_abnormality)and (isinstance(right_knee_abnormality, list)and ('Prominent Tibial Spike' not in right_knee_abnormality)):
                        imp.append(pts[1])                                                
                    if (isinstance(left_knee_abnormality, list)and 'Fabella' in left_knee_abnormality)and (isinstance(right_knee_abnormality, list)and ('Fabella' not in right_knee_abnormality)):
                        imp.append(fabella[1])


    if imp == []:
        imp.append(norm_imp[0])
        print(imp)

    # Check the second condition
    for i in range(len(imp)):
        if "Suggestive of" in imp[i]:
            first_occurrence = imp[i].find("Suggestive of")
            if first_occurrence != -1:
                if i == 1:
                    # Replace the second occurrence of "Suggestive of" with "and"
                    imp[i] = imp[i][:first_occurrence] + " and" + imp[i][first_occurrence + len("Suggestive of"):]
                else:
                    # If it's not the second element, you can choose to do something else
                    pass

    
    result = {"observations": obs1, "impressions": imp}
    
    return jsonify(result)
    

if __name__ == '__main__':
    app.run(host = '0.0.0.0')


