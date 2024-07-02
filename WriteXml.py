


def write(id,name,step,step_icom_link):
    file=open("./res/"+id+".json","wb")
    id:id
    name:name[0]
    step_josn=[]
    for step_mun in range(0,len(step)):
        step1=step_mun[step_mun][0]
        link=step_icom_link[step_mun]
        step_str="{dss_id:"+str(step_mun+1)+"\nstep:"+step1+"\nicom_link:"+link+"}"
        step_josn.append(step_str)
    data=''
    for str_data in step_josn:
        data=str_data+",\n"
    teep_source:[
        data
    ]





