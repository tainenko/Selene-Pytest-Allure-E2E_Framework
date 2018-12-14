# WebAutomation Test With Python  
## Library   
### Selene   
<https://selene-docs-test.readthedocs.io/en/latest/>   

### Pytest 
<https://docs.pytest.org/>  
生成Allure報告  
	$ py.test testcase/ --alluredir ./result/    

指定執行特定features或者stories一部皆測試用例，比如執行"購物車功能"下的"加入購物車"子功能之測試用例：   
	$ py.test testcase/ --allure_features='會員登入功能' --allure_stories='會員登入與登出功能'

### Allure  
@allure.feature # 用於定義被測試的功能，被測產品的需求點 
@allure.story # 用於定義被測功能的用戶場景，即子功能點  
with allure.step # 於用將一個測試用例，分成幾個步驟在報告中輸出  
allure.attach # 用於向測試報告中輸入一些附加的信息，通常是一些測試數據信息   
@pytest.allure.step # 用於將一些通用的函數作為測試步驟輸出到報告，調用此函數的地方會向報告中輸出步驟   

### Baidu-aip
""" 讀取圖片"""   
	def get_file_content(filePath):   
    with open(filePath, 'rb') as fp:   
        return fp.read()   

image = get_file_content('example.jpg')   

""" 調用通用文字識別，圖片參數為本地圖片 """   
client.basicGeneral(image)   		

