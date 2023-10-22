#2. Retrieve all the words starting with ‘b’ or ‘B’ from the following text.

import re


text = """
Betty bought a bit of butter, But the butter was so bitter, 
So she bought some better butter, To make the bitter butter better.
"""

my_pattern=r'\bB\w+' #b boundry sinir

print(re.findall(my_pattern,text,flags=re.IGNORECASE))
