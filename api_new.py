import os, time, re
import ast
from json import loads, dumps, dump
from datetime import datetime, date
from fileOperation import fileOperation
from calling_api import call_textsummerize_api, call_healthtag_api
import streamlit as st

result_path = os.path.join("result")
file_dir = os.path.join("sample")
file_name = "freestate_sample_video.mp4"

fileoperation = fileOperation()

def get_information_from_file(filename):

    #call transcription function
    # filepath = os.path.join(file_dir, filename)
    transcript_result = fileoperation.extract_skim(filename, 'en')
    transcripted_text = transcript_result['text']
    print(transcripted_text)
    st.success('file transcription is completed')

    #payload for text summerization
    payload_textsummerization  = {"wso2_username":"admin","text":transcripted_text,"filesource": "text","source_lang": "English","saveinDB": 'no'}
    summerization_result = call_textsummerize_api(payload_textsummerization)
    print(summerization_result)
    st.success('text Summerization is completed')

    #call healthtag api
    payload_healthtag_api = {
    "filesource": "text",
    "text": transcripted_text,
    "wso2_username":"admin123",
    "medical_condition_tag":"yes",
    "medical_procedure_tag":"yes",
    "medication_tag":"yes",
    "anatomy_tag":"yes",
    "saveinDB": "no"
    }
    healthtag_result = call_healthtag_api(payload_healthtag_api)
    print(healthtag_result)
    result = {"transcription":transcripted_text, "text_summary": summerization_result['response']['result'], "health_tag": healthtag_result['result']}
    st.success('Health-Tagging is completed')
    return result

def save_results(file_name,result):
        """
        Save OCR ranscript results with timestamp.
        """

        final_result ={"filename:":file_name, "result": result, "status": "Api run successfully"}
        final_result1 = dumps(final_result, indent=3, ensure_ascii=False)

        date = datetime.now().strftime("%Y%m%d%I%M%S%p")
        file_name2 = file_name.split(".")[0]
        file_name2 = f"result_{file_name2}_{date}.json"
        try:
            join_path = os.path.join(result_path, file_name2)
            with open(join_path, 'w') as file: 
                dump(final_result, file, indent = 3, ensure_ascii=False)
            
            return final_result
        except Exception as e:
            print("error while saving result :",e)
            return e
            pass




if __name__ == "__main__":
    result=get_information_from_file(file_name)
    print("*"*50)
    print(result)
    print("*"*50)