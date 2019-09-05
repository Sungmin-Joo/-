#----------- 나만의 파파고 만들기 프로젝트 ---------
#설명 : https://github.com/Sungmin-Joo/My-own-papago
# -*- coding: utf-8 -*-
import tkinter
import tkinter.font
from tkinter import messagebox
import requests

global target, result, k_e_flag, k_e_radio, e_k_radio

datas = {
    "source" : "ko",
    "target" : "en",
    "text" : None
}

header = {
    'X-Naver-Client-Id' : '-----------------------',
    'X-Naver-Client-Secret' : '-------------'
}
url = 'https://openapi.naver.com/v1/language/translate'

# datas 값 설정
def set_datas(flag, word):
    if flag:
        datas['source'] = 'en'
        datas['target'] = 'ko'
    else:
        datas['source'] = 'ko'
        datas['target'] = 'en'
    datas['text'] = word

#"Enter" 를 누르거나 번역을 누르면 실행
def enter_func(event=None):
    #빈칸이 있으면 경고.
    if target.get() == '':
        messagebox.showinfo("오류","단어를 입력해주세요.")
        return
    else:
        set_datas(k_e_flag.get(),target.get())
    response=requests.post(url = url, headers=header, data=datas).json()
    result.delete(0,len(result.get()))
    result.insert(0,response['message']['result']['translatedText'])

#한글이면 영어 영어면 한글 번역 시작
def cvt_func():
    #빈칸이 있으면 경고.
    if result.get() == '' or target.get() == '':
        messagebox.showinfo("오류","빈 칸이 있으면 안되요.")
        return
    if k_e_flag.get():
        e_k_radio.deselect()
        k_e_radio.select()
    else:
        k_e_radio.deselect()
        e_k_radio.select()
    temp_result = result.get()
    result.delete(0,len(result.get()))
    target.delete(0,len(target.get()))
    set_datas(k_e_flag.get(),temp_result)
    response=requests.post(url = url, headers=header, data=datas).json()
    result.insert(0,response['message']['result']['translatedText'])
    target.insert(0,temp_result)


if __name__ == '__main__':
    global target, result, k_e_flag

    window=tkinter.Tk()
    window.title("Sungmin_Joo_with_PAPAGO")
    window.resizable(False, False)
    window.geometry("+950+500")
    window.configure(bg='white')
    font=tkinter.font.Font(family="맑은 고딕", size=9, weight='bold')
    #라디오 버튼에서 사용할 변수 정의
    k_e_flag=tkinter.IntVar()

    #입력 텍스트 창
    target = tkinter.Entry(window,width=70, bg='white')
    target.pack(pady=5,padx=5,side='top')

    #--------------------------------------- 로고와 버튼들 세팅 ----------------------------------
    frame2=tkinter.Frame(window,bg='white')

    frame2_1=tkinter.Frame(frame2,bg='white')
    #내 로고를 박기 위한 이미지 불러오기
    img=tkinter.PhotoImage(file='./logo/logo.png')
    img_label=tkinter.Label(frame2_1,image=img,bg='white')
    img_label.image=img
    img_label.pack()
    frame2_1.grid(row=0,column=0,ipadx=10)

    #번역과 반전 버튼 세팅
    frame2_2=tkinter.Frame(frame2,bg='white')
    enter_button=tkinter.Button(frame2_2,text='번역',font = font,
                                command = enter_func, width=7, height=2,bg='lime green',relief='ridge')
    enter_button.pack(side='right')
    cvt_button=tkinter.Button(frame2_2,text='↑↓',font = font,
                                command = cvt_func, width=7, height=2,bg='lime green',relief='ridge')
    cvt_button.pack(side='left')
    frame2_2.grid(row=0,column=1,padx=40,ipadx=5)

    #라디오버튼 세팅
    frame2_3=tkinter.Frame(frame2,bg='white')
    k_e_radio=tkinter.Radiobutton(frame2_3, text="한영", value=0,font = font,
                                variable=k_e_flag, bg='lime green', relief='ridge')
    k_e_radio.pack(side='left')
    e_k_radio=tkinter.Radiobutton(frame2_3, text="영한", value=1,font = font,
                                variable=k_e_flag, bg='lime green', relief='ridge')
    e_k_radio.pack(side='right')
    frame2_3.grid(row=0,column=2,padx=10,ipadx=10)
    frame2.pack()
    #--------------------------------------- 로고와 버튼들 세팅 ----------------------------------

    #결과 텍스트 창
    result = tkinter.Entry(window,width=70, bg='white')
    result.pack(pady=5,padx=5,side='bottom')


    #img_label.place(x=40,y=29)
    k_e_radio.select()
    #if you press 'Enter', this line call detect_key
    window.bind('<Return>', enter_func)
    window.mainloop()