import streamlit as st
import bs4

# text()
st.text("일반 텍스트 입니다.")
st.text("내가 쓰고 싶은 내용을 쓰면")
st.text("한 줄씩 차례대로 기록됩니다.")

# write()
st.write("---")
st.write("내가 넣는 값에 따라서 알아서 포맷을 예쁘게 만들어줍니다.")
st.write("# 이렇게 글자 크기를 키울 수도 있고")
st.write("## 이렇게 하면 더 작게")
st.write("### 이렇게 하면 더더 작게")
st.write("#### 이렇게 하면 더더더 작게")
st.write("##### 이렇게 하면 더더더더 작게")
st.write("###### 샾 기호를 6개 넣으면 이렇게 연하게 됩니다.")
st.write("> 이런 것도 됩니다.")
st.write(">> 이런 것도 됩니다. 2")
st.write("---")

st.write("https://www.naver.com")

st.write("---")
foo = {"짜장면":5000, "짬뽕":6000, "탕수육":10000}
st.write(foo)

st.write("---")
st.write("1 + 1 = ", 2)

st.write("---")
st.code("print('Hello World')")

st.write("---")
"""
# Magic Commands

매직 커맨드는 굳이 write() 함수를 쓰지 않아도

이렇게 더 직관적으로 코드를 짤 수 있습니다.

---
> 표를 띄우고 싶으면, 그냥 코드에 표를 그리세요.

|         | 수학          | 평가        |  
|---------| --------------|------------|
| 철수    | 90            | 참잘했어요. |  
| 영희    | 50            | 분발하세요. |

https://www.naver.com

```python
print("Hello World")
```
"""
