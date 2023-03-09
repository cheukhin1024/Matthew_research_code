import pandas as pd

# merging two csv files
df = pd.concat(map(pd.read_excel, ['G:\Data\156 2021-1959年上市公司专利引用数据\授权专利的被引用信息\授权专利的被引用信息_1', 'G:\Data\156 2021-1959年上市公司专利引用数据\授权专利的被引用信息\授权专利的被引用信息_2', , 'G:\Data\156 2021-1959年上市公司专利引用数据\授权专利的被引用信息\授权专利的被引用信息_3', , 'G:\Data\156 2021-1959年上市公司专利引用数据\授权专利的被引用信息\授权专利的被引用信息_4']), ignore_index=True)
df.head(10)

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
print(find_MaxDepthOfQuotedResearch(df))
