import base64

class Solution:
    def encode(self, strs: list[str]) -> str:
        # 1. Barcha so'zlarni uzunligi va '#' bilan bitta xom satrga yig'amiz
        raw_string = "".join(f"{len(s)}#{s}" for s in strs)
        
        # 2. Satrni UTF-8 baytlariga o'girib, Base64 ga encode qilamiz
        encoded_bytes = base64.b64encode(raw_string.encode('utf-8'))
        
        # 3. Baytlarni qaytadan string ko'rinishida qaytaramiz
        return encoded_bytes.decode('utf-8')

    def decode(self, s: str) -> list[str]:
        # 1. Base64 matnni qayta dekodlab, asli xom satrni tiklaymiz
        decoded_bytes = base64.b64decode(s.encode('utf-8'))
        raw_string = decoded_bytes.decode('utf-8')
        
        # 2. Xom satrdan Length-Prefix algoritmi bo'yicha so'zlarni ajratib olamiz
        res = []
        i = 0
        while i < len(raw_string):
            j = raw_string.find('#', i)
            length = int(raw_string[i:j])
            
            start = j + 1
            end = start + length
            res.append(raw_string[start:end])
            
            i = end
            
        return res