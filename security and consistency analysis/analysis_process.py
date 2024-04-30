import analysis_method

item = analysis_method.Json(r"C:\Users\rrm_a\Desktop\test-2.xlsx")
print("-----------step 1:try different url in the same domain ------------")
item.write_down()
item.inital_excel()
item.save_changes()
print('------------step 2:detect manifest file----------------------')

item.handle_list_2(0,'url1')
item.save_changes()
item.handle_list_2(0,'url2')
item.save_changes()
item.handle_list_2(0,'url3')
item.save_changes()
item.handle_list_2(0,'url4')
item.save_changes()
item.handle_list_2(0,'url5')
item.save_changes()

print('---------------------step 3:check api information and request------------------------------')
print("----task 1 get API ----")
item.get_api(0)
item.save_changes()
print("----task 2 get API Information----")
item.get_api_info(0)
item.save_changes()
print("----task 3 request----")
item.clear_path(0)
item.save_changes()
print("----task 4 analysis result ----")
item.request_result(0)
item.save_changes()
print('---------------------step 4:check request with token------------------------------')
print("----task 1 analysis auth ----")
item.check_auth(0)
item.save_changes()
print("----task 2 send request ----")
item.detect_token(0)
item.save_changes()
print("----task 3  analysis result ----")
item.request_result(0)
item.save_changes()

print("---------------------step 5:check name and legal----------------------------")
print("----task 1 compare name ----")
item.check_name(0)
item.save_changes()
print("----task 2 compare legal information ----")
item.check_legal(0)
