# PTT Beauty Notify
PTT表特版定時通知程式，搭配Line Notify服務進行通知。

## 檔案內容
- getBeaury.py 主程式
- crawlFunc.py 爬蟲程式
- sendNotify.py LINE Notify通知程式
- requirements.txt 本次使用的python套件

## 使用方式
首先必須先安裝相關套件，請參見requirements.txt。

`pip install -r requirements.txt`

### 執行命令
`python getBeaury.py`

可搭配排程執行

### 可自訂部分
約60行的地方可以找到下列程式：

    #edge
    token = 'your line notify api token'

    #default message
    message = '\n{你的預設文字}\n'+article_detail

    tz_Taipei = pytz.timezone('Asia/Taipei') 
    now = datetime.now(tz_Taipei).strftime("%H")
    
    statment = {
        '07': '早安！該起床囉！',
        '09': '有沒有認真工作啊！',
        '11': '加油！快吃午餐了！',
        '13': '起床囉！認真工作！',
        '15': '今天下午茶吃什麼呢？',
        '17': '下班囉！',
        '19': '晚餐吃了嗎？還沒吃可以先運動！',
        '21': '追劇時間',
        '23': '準備洗洗睡！晚安！',
        '01': '還不快睡覺'
    }

- 變數token你在line notify取得的token。
- 變數defaut message為你的預設文字，article_detail為文章網址。
- 變數tz_Taipei 為時區的設定。
- dictionary statment的key為「時」，07代表上午七點，value為訊息文字。
