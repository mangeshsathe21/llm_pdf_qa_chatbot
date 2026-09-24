import os
import re
from unidecode import unidecode

def sanitize_filename_for_collection(filename : str = 'sanitize_filename_for_collection--my sanitize_filename_for_collectiontext sanitize_filename_for_collection@@ HJj --a     s ^ résumé -__.txt') -> str:
    """
    chromadb compatible file name
    
    3 to 63 chars
    start end with alphanumeric
    can only contain alphanum _ - 
    """
    
    namewithoutextension = os.path.splitext(filename)[0].lower() # only file name
    ascii_name = unidecode(namewithoutextension)
    replaced = re.sub(r"[^a-z0-9_-]+", "-", ascii_name).strip("-_")
    replaced = re.sub(r"-{2,}", "-", replaced)
    
    if len(replaced)<3:
        replaced = replaced+"doc"
    
    if len(replaced) > 63:
        replaced = replaced[:63] 
    
    return replaced

