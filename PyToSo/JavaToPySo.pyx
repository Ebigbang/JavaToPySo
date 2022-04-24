# FileName: JavaToPySo.pyx
# 接口函数，导出给Java Native的接口
def JNI_API_testFunction(param):
  print("enter JNI_API_test_function")
  print("leave JNI_API_test_function")
  return "234"
# 接口函数企业电量模型
def JNI_API_callentelectFunction(param):
  print("enter JNI_API_test_function")
  print("leave JNI_API_test_function")
  return "123" 