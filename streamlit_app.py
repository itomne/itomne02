import os
import time
import openai
import streamlit as st
from PIL import Image


# APIキーの設定
openai.api_key = OPENAI_API_KEY
conversation_history_1 = []  # Global scope
conversation_history_2 = []  # Global scope
conversation_history_3 = []  # Global scope
conversation_history_4 = []  # Global scope
conversation_history_5 = []  # Global scope

def main_page():
    
    st.title('chatGPTのwebアプリです')
    st.caption('chatGPTを使ってデザイン思考の入門を網羅します。')
    st.caption('page1~5をの絵を選択して、対話型鑑賞をやってみましょう！')

import requests

def page1():
    prompt = ""  # Initialize your prompt

    st.title('リクリット・ティラバーニャ「“Who’s Afraid of Red, Yellow and Green,」')
    st.caption('感じたことを教えてね！')
    image_1 = Image.open("11.リクリット・ティラバーニャ「“Who’s Afraid of Red, Yellow and Green,」.jpg")
    st.image(image_1, width=400)

    with st.form('qestion_form', clear_on_submit=False):
        st.markdown('### 話しかけてみよう!')
        prompt = st.text_area('テキストエリア')
        submitted = st.form_submit_button("送信")

        if submitted:
            st.text('質問を受け付けました！')
            conversation_history_1.append({"role": "user", "content": prompt})

            # OpenAIのAPIを直接使用
            headers = {
                'Authorization': f'Bearer {openai.api_key}',
                'Content-Type': 'application/json'
            }
            data = {
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "アート思考のデモンストレーションを行います。あなたは[アート思考の専門家]です。相手は[ビジネスパーソン]です。あなたは以下の制約条件に従って、クライアントに問いかけます。"},
                    {"role": "system", "content": "1度の会話で行う質問は必ず1つずつ。"},
                    {"role": "system", "content": "一度の会話で答えられる文字数は、150字以内"},
                    {"role": "system", "content": "説明する時は、あなたが質問を5つ以上行った後とする。"},
                    {"role": "system", "content": "ユーザーが画像を入力したら、あなたはその画像を解釈し解説する。"},
                    {"role": "system", "content": "ユーザーが[絵を描いて]と言ったら、あなたは相手のイメージを質問して画像を出力する"},
                    {"role": "system", "content": "相手が「終了」と言ったら、あなたは「ありがとうございました」と返す"},
                    {"role": "system", "content": "相手との会話で[問題提起力]を評価する。相手の[問題提起力]を100点満点で点数を付ける。講評として相手の考え方・特徴を述べる。"},
                    {"role": "system", "content": "まず、[あなたが人生で影響を受けたアート作品、もしくは映画・音楽・小説などを含む文化的表現物を教えてください]と聞いてください。相手とやり取りを何度か行った後に、下記の質問をしてください。"},
                    {"role": "system", "content": "仕事における問題意識について考えてみましょう。あなたの会社・職場で「当たり前」「常識」とされているようなことで、疑問や違和感を抱いているものはあるでしょうか？ 思いついたものを自由に教えてください。"},
                    {"role": "system", "content": "では、あなたはまず、[あなたが人生で影響を受けたアート作品、もしくは映画・音楽・小説などを含む文化的表現物を教えてください]と聞いてください。相手とやり取りを何度か行った後に、下記の質問をしてください。 "},
                ] + conversation_history_1
            }

            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data).json()

            # レスポンスの処理
            with st.spinner("アート先生の返信を受診中..."):
                time.sleep(3)
            st.markdown('### アート先生より')
            st.info(response["choices"][0]["message"]["content"].strip())
            print(prompt)
            print(response["choices"][0]["message"]["content"].strip())
            conversation_history_1.append({"role": "assistant", "content": response["choices"][0]["message"]["content"].strip()})

    st.markdown('### 会話履歴:')
    for message in conversation_history_1:
        if message["role"] == "user":
            st.write(f"あなた: {message['content']}")
        else:  # if assistant
            st.write(f"アート先生: {message['content']}")


def page2():
    
    st.title('マルセル・デュシャン「泉」')
    st.caption('感じたことを教えてね')
    image_2 = Image.open("4.マルセル・デュシャン「泉」.png")
    st.image(image_2, width=400)
    with st.form('qestion_form',clear_on_submit=False):
       st.markdown('### 話しかけてみよう!')
       prompt = st.text_area('テキストエリア')
       submitted = st.form_submit_button("送信")
       if submitted:
          st.text('質問を受け付けました！')
          conversation_history_2.append({"role": "user", "content": prompt})
          response = openai.ChatCompletion.create(  
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "入力されたキーワードについて最大トークン数で教えてください"}
            ] + conversation_history_2,  # Use conversation_history here
            temperature=1.0,
            presence_penalty=0,
            frequency_penalty=0
          )
          # Process the response
          with st.spinner("アート先生の返信を受診中..."):
             time.sleep(3)
          st.markdown('### アート先生より')
          st.info(response.choices[0]["message"]["content"].strip())
          print(response.choices[0]["message"]["content"].strip())
          # Add GPT-3's response to conversation_history
          conversation_history_2.append({"role": "assistant", "content": response.choices[0]["message"]["content"].strip()})

    

def page3():
    st.title('クリスト＆ジャンヌ＝クロード「「L’Arc de Triomphe, Wrapped」')
    st.caption('感じたことを教えてね！')
    image_3 = Image.open("9.クリスト＆ジャンヌ＝クロード「「L’Arc de Triomphe, Wrapped」.jpg")
    st.image(image_3, width=400)
    with st.form('qestion_form',clear_on_submit=False):
       st.markdown('### 話しかけてみよう!')
       prompt = st.text_area('テキストエリア')
       submitted = st.form_submit_button("送信")
       if submitted:
          st.text('質問を受け付けました！')
          conversation_history_3.append({"role": "user", "content": prompt})
          response = openai.ChatCompletion.create(  
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "対話型鑑賞のデモンストレーションを行います。"},
                {"role": "system", "content": "あなたは[対話型鑑賞のエデュケーター]です。相手は[小学生]です。"},
                {"role": "system", "content": "[クリスト＆ジャンヌ＝クロード「「L’Arc de Triomphe, Wrapped」]について対話します。"},
                {"role": "system", "content": "エデュケーターは以下の４つの制約条件に従って、クライアントに問いかけます。"},
                {"role": "system", "content": "1.あなたが1度の会話で行う質問は必ず1つずつ。"},
                {"role": "system", "content": "2.あなたが一度の会話で答えられる文字数は、150字以内。"},
                {"role": "system", "content": "3.あなたが説明する時は、あなたが質問を10つ以上行った後とする。"},
                {"role": "system", "content": "4.質問を10つ以上行った後、あなたは他の人がこの作品をみた意見を紹介してください。"},
                {"role": "system", "content": "では、あなたはまず、[こんにちは。この作品をご覧になってどんな印象ですか？]と聞いてください。"},
            ] + conversation_history_3,  # Use conversation_history here
            temperature=1.0,
            presence_penalty=0,
            frequency_penalty=0,
          )
          # Process the response
          with st.spinner("アート先生の返信を受診中..."):
             time.sleep(3)
          st.markdown('### アート先生より')
          st.info(response.choices[0]["message"]["content"].strip())
          print(response.choices[0]["message"]["content"].strip())
          # Add GPT-3's response to conversation_history
          conversation_history_3.append({"role": "assistant", "content": response.choices[0]["message"]["content"].strip()})

def page4():
    
    st.title('フェリックス・ゴンザレス＝トレス「無題(ロスの肖像 L.A.にて)')
    st.caption('感じたことを教えてね！')
    image_4 = Image.open("10.フェリックス・ゴンザレス＝トレス「無題(ロスの肖像 L.A.にて)」.jpg")
    st.image(image_4, width=400)
    with st.form('qestion_form',clear_on_submit=False):
       st.markdown('### 話しかけてみよう!')
       prompt = st.text_area('テキストエリア')
       submitted = st.form_submit_button("送信")
       if submitted:
          st.text('質問を受け付けました！')
          conversation_history_4.append({"role": "user", "content": prompt})
          response = openai.ChatCompletion.create(  
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "対話型鑑賞のデモンストレーションを行います。"},
                {"role": "system", "content": "あなたは[対話型鑑賞のエデュケーター]です。相手は[小学生]です。"},
                {"role": "system", "content": "[フェリックス・ゴンザレス＝トレス「無題(ロスの肖像 L.A.にて)」]について対話します。"},
                {"role": "system", "content": "エデュケーターは以下の４つの制約条件に従って、クライアントに問いかけます。"},
                {"role": "system", "content": "1.あなたが1度の会話で行う質問は必ず1つずつ。"},
                {"role": "system", "content": "2.あなたが一度の会話で答えられる文字数は、150字以内。"},
                {"role": "system", "content": "3.あなたが説明する時は、あなたが質問を10つ以上行った後とする。"},
                {"role": "system", "content": "4.質問を10つ以上行った後、あなたは他の人がこの作品をみた意見を紹介してください。"},
                {"role": "system", "content": "では、あなたはまず、[こんにちは。この作品をご覧になってどんな印象ですか？]と聞いてください。"},
            ] + conversation_history_4,  # Use conversation_history here
            temperature=1.0,
            presence_penalty=0,
            frequency_penalty=0,
          )
          # Process the response
          with st.spinner("アート先生の返信を受診中..."):
             time.sleep(3)
          st.markdown('### アート先生より')
          st.info(response.choices[0]["message"]["content"].strip())
          print(response.choices[0]["message"]["content"].strip())
          # Add GPT-3's response to conversation_history
          conversation_history_4.append({"role": "assistant", "content": response.choices[0]["message"]["content"].strip()})
         
def page5():
    st.title('パブロ・ピカソ「アヴィニョンの娘たち」')
    st.caption('感じたことを教えてね')
    image_5 = Image.open("2.パブロ・ピカソ「アヴィニョンの娘たち」.jpg")
    st.image(image_5, width=400)
    with st.form('qestion_form',clear_on_submit=False):
       st.markdown('### 話しかけてみよう!')
       prompt = st.text_area('テキストエリア')
       submitted = st.form_submit_button("送信")
       if submitted:
          st.text('質問を受け付けました！')
          conversation_history_5.append({"role": "user", "content": prompt})
          response = openai.ChatCompletion.create(  
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "対話型鑑賞のデモンストレーションを行います。"},
                {"role": "system", "content": "あなたは[対話型鑑賞のエデュケーター]です。相手は[小学生]です。"},
                {"role": "system", "content": "[パブロ・ピカソ「アヴィニョンの娘たち」]について対話します。"},
                {"role": "system", "content": "エデュケーターは以下の４つの制約条件に従って、クライアントに問いかけます。"},
                {"role": "system", "content": "1.あなたが1度の会話で行う質問は必ず1つずつ。"},
                {"role": "system", "content": "2.あなたが一度の会話で答えられる文字数は、150字以内。"},
                {"role": "system", "content": "3.あなたが説明する時は、あなたが質問を10つ以上行った後とする。"},
                {"role": "system", "content": "4.質問を10つ以上行った後、あなたは他の人がこの作品をみた意見を紹介してください。"},
                {"role": "system", "content": "では、あなたはまず、[こんにちは。この作品をご覧になってどんな印象ですか？]と聞いてください。"},
            ] + conversation_history_5,  # Use conversation_history here
            temperature=1.0,
            presence_penalty=0,
            frequency_penalty=0,
          )
          # Process the response
          with st.spinner("アート先生の返信を受診中..."):
             time.sleep(1)
          st.markdown('### アート先生より')
          st.info(response.choices[0]["message"]["content"].strip())
          print(response.choices[0]["message"]["content"].strip())
          # Add GPT-3's response to conversation_history
          conversation_history_5.append({"role": "assistant", "content": response.choices[0]["message"]["content"].strip()})
    

    

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 1": page1,
    "Page 2": page2,
    "Page 3": page3,
    "Page 4": page4,
    "Page 5": page5,
    }

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()