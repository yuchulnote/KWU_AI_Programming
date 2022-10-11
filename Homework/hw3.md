```python
import os
import wordcloud
import matplotlib.pyplot as plt
print(f"현재 디렉토리 위치: {os.getcwd()}")
```

    현재 디렉토리 위치: /Users/yuchul/Anaconda/AI Programming/Web_Crawler_HW



```python
from selenium.webdriver.common.by import By
```


```python
from selenium import webdriver

driver = webdriver.Chrome('/Users/yuchul/Downloads/chromedriver')
driver.get('https://yuchulnote.github.io/deep_learning_study/Optimizer/')
driver.implicitly_wait(time_to_wait=10)
```

    /Users/yuchul/opt/anaconda3/envs/torch/lib/python3.7/site-packages/ipykernel_launcher.py:3: DeprecationWarning: executable_path has been deprecated, please pass in a Service object
      This is separate from the ipykernel package so we can avoid doing imports until



```python
element = driver.find_element(By.XPATH, r'//*[@id="main"]/article/div[1]/section[1]').text
```


```python
s_words = wordcloud.STOPWORDS.union({'합니다', '것 같습니다', '됩니다', '입니다', 'self', 'key', 'lr', 'grads', 'params', 'v', 'h'})
image = wordcloud.WordCloud(width = 1000, height = 700, stopwords = s_words, font_path='/Users/yuchul/Downloads/Gothic_A1/GothicA1-Black.TTF').generate(element)

plt.figure(figsize = (40, 30))
plt.imshow(image)
plt.show()
```


    
![png](output_4_0.png)
    

