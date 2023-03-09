import pandas as pd

df = pd.read_csv('<file path>')
df.head(10)

#df_column_c = df['column_c'].drop_duplicates 

def find_MaxDepthOfQuotedResearch(df):
  max_depth = 0
  max_depth_of_each_columnC_cell = []
  i = 0
  quoted_research_code = str(df[column_c][i])
  
   for key_e, value_e in df[column_e].iteritems():
     if quoted_research_code == value_e:
        max_depth +=1
        quoted_research_code.replace(value_e)
        
      else:
        max_depth_of_each_columnC_cell.append(max_depth)
        i+=1
        quoted_research_code = str(df[column_c][i])
        max_depth = 0
      
  return max_depth_of_each_columnC_cell         
      
#Test the function
print(find_MaxDepthofQuotedResearch(df))
