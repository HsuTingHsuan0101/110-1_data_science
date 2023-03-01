# 110-1_data_science
110-1 NTU Courses: Programming for Social Science and Data Science

## **I. Web Crawling**
### 01_Counting

* library：`Counter`,  `wikipedia` , `matplotlib`
* 從wilipedia引入英文文本，計算各字詞出現次數並視覺化呈現

### 02_Crawl_json_Dcard

* library：`requests`, `json`, `pandas`
* 爬取Dcard工作版 (https://www.dcard.tw/f/job) 之貼文ID、標題、內容、時間等
* 輸出成CSV檔

### 03_Crawl_json_104網站

* library：`requests`, `json`, `pandas`
* 爬取104網站 (https://www.104.com.tw/jobs/main/) 搜尋頁面
* 關鍵字輸入「數據分析」，爬取所有搜尋結果

### 04_Crawl_html_PTTjob

* library：`requests`, `BeautifulSoup`, `pandas`
* 爬取PTT工作版 (https://www.ptt.cc/bbs/job/index.html) 之作者、標題、內容、時間等

## **II. Text Mining**
### 05_TM01_tokenization_ENG

Loading English Data from Wiki then tokenize
library：`wikipedia`, `string`, `nltk`, `counter`
* Tokenization
* Counting
* Stopword and Punctuation Removal
* Stemming and Lemmatization
* Application: WordCloud 文字雲
