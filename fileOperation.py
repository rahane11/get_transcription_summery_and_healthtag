import whisper
from deep_translator import GoogleTranslator
# print(whisper.available_models())
# langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
# print(langs_dict)

model = whisper.load_model('tiny.en')

# instantiate  GoogleTranslator() object with default, 
# reduce cost for reinitatiate every time  
translator = GoogleTranslator(source='auto', target='german')

class fileOperation():
    def extract_skim(self, filepath, lang):
        """take video filepath and language of video and generate skim and return 
        in form {text:sampletext,segment:[{start:0.10, end:0.20, text:sampletext}...{}{}] }"""
        try:
            output={}
            segment=[]
            result = model.transcribe(filepath, language=lang)
            output['text']=result['text']
            for text in result['segments']:
                part_of_speech={}
                part_of_speech['start']=text['start']
                part_of_speech['end']=text['end']
                part_of_speech['text']=text['text']
                segment.append(part_of_speech)
            output['segment']=segment
            return output
        
        except Exception as e:
            return e
    
    def translate_skim(self, text, target_language):
        """take input text as string and target language split on . and translate 
        return as string, maximum 5000 char allowed by translator.translate() function"""
        try:
            if len(text)>=1:
                translator.target = target_language
                #translator = GoogleTranslator(source='auto', target=target_language)
                res=(".").join([translator.translate(sent) for sent in text.split(".")])
                return res
            else:
                return ""
        
        except Exception as e:
            return e
        
    def translate_segment(self, segment, target_language):
        """take segment as input and target language, translate each segment text
        and replace with original segment['text] and return entire segment"""
        try:
            if len(segment)>=1:
                translator.target = target_language
                #translator = GoogleTranslator(source='auto', target=target_language)
                for segment_chunk in segment:
                    if len(segment_chunk['text'])>=1:
                        segment_chunk['text']=translator.translate(segment_chunk['text'])
                    else:
                        segment_chunk['text']=""
                return segment 
            else:
                return ""
        
        except Exception as e:
            return e
        
    def translate_skim_segment(self, segment, target_language):
        """take segment as input and target language, translate each segment text
        and replace with original segment['text] and return entire segment and skim"""
        try:
            if len(segment)>=1:
                translator.target = target_language
                #translator = GoogleTranslator(source='auto', target=target_language)
                texts=[]
                for segment_chunk in segment:
                    if len(segment_chunk['text'])>=1:
                        segment_chunk['text']=translator.translate(segment_chunk['text'])
                        texts.append(segment_chunk['text'])
                    else:
                        segment_chunk['text']=""
                        texts.append(segment_chunk['text'])
                
                translated_text=(" ").join(texts)        
                return translated_text, segment 
            else:
                return "", []
        
        except Exception as e:
            return e, ""