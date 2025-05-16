"""
https://it4each.com/blog/reguliarnye-vyrazheniia-predislovie/

pip install lorem-text
"""

from lorem_text import lorem

# print(lorem.paragraph())

text = """Consequatur est quos repellat obcaecati, corporis corrupti cupiditate qui 
tempore nesciunt possimus dolores animi voluptates culpa suscipit, eum excepturi 
laboriosam nemo commodi ullam? Odit placeat nemo sint voluptatum in illum accusamus 
saepe asperiores, distinctio odio harum? Dignissimos necessitatibus quaerat modi, 
magni ex debitis voluptas, neque error totam odit, molestias odio voluptatem obcaecati 
minus vel nostrum repudiandae iure, blanditiis corporis corrupti ducimus aperiam.
"""

patten = r'mo'

print(text.count(patten))