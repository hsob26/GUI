# 사용할 프로그램 불러오기
from tkinter import font
import tkinter as tk
import random
import time as t 

# GUI 생성
root = tk.Tk()

# 알파벳 목록 및 삭제할 알파벳 추출, 배열

alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alp_txt = ''

def alp_st_all() : # 알파벳 배열 통합
    global alp_txt
    global r_1
    global r_2
    global r_3
    global ans_tr
    global ans_tr_inf 
    global ans_tr_tut 
    r_1, r_2, r_3 = alphabet()
    random.shuffle(alp)
    ans_tr = [r_1, r_2, r_3]
    ans_tr_inf = [r_1, r_2, r_3]
    ans_tr_tut = [r_1, r_2, r_3]
    alp_array()

def alphabet() :  # 삭제할 알파벳 추출 및 중복 제거
    while True :
        r_1 = random.choice(alp)
        r_2 = random.choice(alp)
        r_3 = random.choice(alp)
        if r_1 != r_2 and r_1 != r_3 and r_2 != r_3 :
            return r_1, r_2, r_3

def alp_array() : # 알파벳 배열
    global alp_txt
    alp_txt = ''
    for i in alp : 
        if i != r_1 and i != r_2 and i != r_3 :
            alp_txt = alp_txt + i + ' '


# 함수

def main_window() :  # 메인화면
    frame_main.pack()
    frame_rule.pack_forget()
    frame_level.pack_forget()
    frame_play.pack_forget()
    frame_tut.pack_forget()
    frame_inf.pack_forget()
    frame_end.pack_forget()

def rule_window() :  # 규칙화면
    frame_main.pack_forget()
    frame_rule.pack()
    frame_level.pack_forget()
    frame_play.pack_forget()
    frame_tut.pack_forget()
    frame_inf.pack_forget()
    frame_end.pack_forget()
    btn_mov_lv.place_forget()

def level_window() :  # 시작 후 난이도 화면
    frame_main.pack_forget()
    frame_rule.pack_forget()
    frame_level.pack()
    frame_play.pack_forget()
    frame_tut.pack_forget()
    frame_inf.pack_forget()
    frame_end.pack_forget()
    btn_mov_r.place_forget()

def play_window() :  # 기본 모드 화면
    frame_main.pack_forget()
    frame_rule.pack_forget()
    frame_level.pack_forget()
    frame_play.pack()
    frame_tut.pack_forget()
    frame_inf.pack_forget()
    frame_end.pack_forget()

def tut_window() :  # 연습모드 화면
    frame_main.pack_forget()
    frame_rule.pack_forget()
    frame_level.pack_forget()
    frame_play.pack_forget()
    frame_tut.pack()
    frame_inf.pack_forget()
    frame_end.pack_forget()

def inf_window() :  # 무한모드 화면
    frame_main.pack_forget()
    frame_rule.pack_forget()
    frame_level.pack_forget()
    frame_play.pack_forget()
    frame_tut.pack_forget()
    frame_inf.pack()
    frame_end.pack_forget()

def end_window() :  # 결산 화면
    frame_main.pack_forget()
    frame_rule.pack_forget()
    frame_level.pack_forget()
    frame_play.pack_forget()
    frame_tut.pack_forget()
    frame_inf.pack_forget()
    frame_end.pack()

def entry_clk(event) :  # 기본모드 기입창 표기
    if entry.get() == '사라진 알파벳을 입력해주세요.':
        entry.delete(0, "end")

def entry_clk_inf(event) :  # 무한모드 기입창 표기
    if entry_inf.get() == '사라진 알파벳을 입력해주세요.':
        entry_inf.delete(0, "end")

def entry_clk_tut(event) :  # 연습모드 기입창 표기
    if entry_tut.get() == '사라진 알파벳을 입력해주세요.':
        entry_tut.delete(0, "end")

def font_st(event) :  # 설정 폰트 기입창 표기
    if st_f_et.get() == f'현재폰트 : {n_font}' :
        st_f_et.delete(0, "end")

def timer() : # 제한시간
    global time_left
    global end_rst
    global time

    if time_left > 0 :
        time_left -= 1
        label_time.config(text=f"남은 시간: {time_left} 초", font=(n_font, 15), relief='solid')
        time = root.after(1000, timer)
    else:
        end_rst = 'time over'
        if time is not None :
            root.after_cancel(time)
            time = None
            t.sleep(1)
            rst_()
            end_window() 

def high() : # 난이도 어려움
    global time_left
    global lv
    global life
    global left_alp
    left_alp = 3
    lv = '어려움'
    time_left = 20
    life = 3
    alp_st_all()
    mod_nomal()
    play_window()
    timer()
    answer()

def nomal() : # 난이도 보통
    global time_left
    global lv
    global life
    global left_alp
    left_alp = 3
    lv = '보통'
    time_left = 30
    life = 4
    alp_st_all()
    mod_nomal()
    play_window()
    timer()
    answer()

def easy() : # 난이도 쉬움
    global time_left
    global lv
    global life
    global left_alp
    left_alp = 3
    lv = '쉬움'
    time_left = 40
    life = 6
    alp_st_all()
    mod_nomal()
    play_window()
    timer()
    answer()

def tut() : # 난이도 연습
    global time_left
    global rst_alp
    time_left = 0
    rst_alp = 0
    alp_st_all()
    mod_tut()
    tut_window()

def inf() : # 난이도 무한
    global time_left
    global rst_alp
    global time_aft
    time_left = 10
    rst_alp = 0
    time_aft = 0
    alp_st_all()
    mod_inf()
    inf_window()
    timer_inf()

def program_end() : # 프로그램 종료
    root.destroy()

def update_font(event=None) : # 폰트 변경
    global n_font
    n_font = st_f_et.get()

    # 리벨
    label_alp.config(font=(n_font, 20))
    label_time_inf.config(font=(n_font, 15))
    label_time.config(font=(n_font, 15))
    label_time_tut.config(font=(n_font, 15))
    label_alp_inf.config(font=(n_font, 20))
    label_alp_tut.config(font=(n_font, 20))
    label_alp_txt.config(font=(n_font, 20))
    lab_can_rule.config(font=(n_font, 20))
    lab_end_txt.config(font=(n_font, 30))
    lab_g_name.config(font=(n_font, 60))
    lab_lft_all.config(font=(n_font, 20))
    lab_lv.config(font=(n_font, 31))
    lab_lv_txt.config(font=(n_font, 20))
    lab_rst_alp_inf.config(font=(n_font, 20))
    lab_rst_alp_tut.config(font=(n_font, 20))
    
    # 버튼
    btn_end.config(font=(n_font, 20))
    btn_mov_lv.config(font=(n_font, 20))
    btn_mov_r.config(font=(n_font, 20))
    btn_main_re_tut.config(font=(n_font, 20))
    btn_main_re_lv.config(font=(n_font, 20))
    btn_main_re_rule.config(font=(n_font, 20))
    btn_main_re.config(font=(n_font, 20))
    btn_p.config(font=(n_font, 20))
    btn_rule_game.config(font=(n_font, 20))
    btn_rule_inf.config(font=(n_font, 20))
    btn_rule_play.config(font=(n_font, 20))
    btn_rule_tut.config(font=(n_font, 20))
    btn_r.config(font=(n_font, 20))
    btn_st.config(font=(n_font, 15))
    btn_show_alp.config(font=(n_font, 10))
    btn_start_timer.config(font=(n_font, 10))
    btn_time_ma.config(font=(n_font, 10))
    btn_time_pl.config(font=(n_font, 10))
    bt_lv_n.config(font=(n_font, 20))
    bt_lv_inf.config(font=(n_font, 20))
    bt_lv_tut.config(font=(n_font, 20))
    bt_lv_h.config(font=(n_font, 20))
    bt_lv_e.config(font=(n_font, 20))

    # 기입창
    entry.config(font=(n_font, 15))
    entry_inf.config(font=(n_font, 15))
    entry_tut.config(font=(n_font, 15))
      
def setting_on() : # 설정창 켜기
    global setting_window, st_f_et, n_font

    if not setting_window :
        setting_window = tk.Toplevel(root, width=400, height=300, bg='gray90')
        setting_window.title('설정 창')

        close_st_btn = tk.Button(setting_window, text='설정 창 닫기', font=(n_font, 10), bg='white', command=setting_off)
        close_st_btn.pack()
        close_st_btn.place(x=320, y=0)

        st_label_1 = tk.Label(setting_window, text='폰트 [원하시는 폰트를 입력해주세요]', font=(n_font, 10), bg='white', relief='groove')
        st_label_1.pack()
        st_label_1.place(x=10, y=20)

        st_label_2 = tk.Label(setting_window, text='사용가능한 폰트 목록 보기', font=(n_font, 10), bg='white', fg='blue', relief='groove')
        st_label_2.bind("<Button-1>", lambda event : open_font_list())
        st_label_2.pack()
        st_label_2.place(x=10, y=60)

        st_label_3 = tk.Label(setting_window, text='*폰트 변경시 주의*\n"Times New Roman"을 기본으로 제작 되었기 때문에\n폰트 변경시 창깨짐 현상이 나타날 수 있습니다\n폰트 변경후 글씨가 보이지 않으면\n폰트를 "Times New Roman"으로 변경해주세요', font=(n_font, 10), bg='white', fg='red', relief='groove')
        st_label_3.pack()
        st_label_3.place(x=10, y=80)

        st_f_et = tk.Entry(setting_window, width=40)
        st_f_et.insert(0, f'현재폰트 : {n_font}')
        st_f_et.bind("<FocusIn>", font_st)
        st_f_et.bind("<Return>", update_font)
        st_f_et.pack()
        st_f_et.place(x=10, y=40)

def open_font_list() : # 폰트창 열기
    global font_window
    if not font_window :
        
        font_window = tk.Toplevel(root, width=1500, height=800, bg='white')
        font_window.title('사용 가능한 폰트 목록')

        close_ft_list_btn = tk.Button(font_window, text='닫기', font=(n_font, 10), bg='white', command=close_font_list)
        close_ft_list_btn.pack()
        close_ft_list_btn.place(x=1450, y=0)

        fonts = font.families()

        
        row_count = len(fonts) // 8
        for i in range(row_count + 1) :
            ft_list_label = tk.Label(font_window, text='\n'.join(fonts[i * 59:(i + 1) * 59]), font=('Time New Roman', 10), bg='white')
            ft_list_label.pack()
            ft_list_label.place(x=10 + i * 230, y=20)

def close_font_list() : # 폰트창 닫기
    global font_window
    if font_window :
        font_window.destroy()
        font_window = None

def setting_off() : # 설정창 끄기
    global setting_window
    if setting_window :
        setting_window.destroy()
        setting_window = None

def answer(event=None) : # 답안 처리
    global life
    global left_alp
    global end_rst
    global ans_tr
    global time_left
    global time

    user_input = entry.get()
    user_input = user_input.upper()  

    if user_input in ans_tr :
        ans_tr.remove(user_input)
        left_alp = left_alp - 1
    else:
        life = life - 1

    lab_lft_all.config(text=f'남은 알파벳 : {left_alp}개 / 잔여 목숨 : {life}개')
    entry.delete(0, tk.END)

    if left_alp == 0 :
        end_rst = 'win'
        root.after_cancel(time)        
        t.sleep(1)
        rst_()
        end_window()

    if life == 0 :
        end_rst = 'lose'
        root.after_cancel(time)
        t.sleep(1)
        rst_()
        end_window()

def rst_() : # 승패 판단
    global end_txt
    global end_rst
    global time_aft
    global time_inf
    time_aft_m = 0
    time_aft_s = 0
    
    if time_aft >= 60 :
        time_aft_s = time_aft % 60
        time_aft_m = time_aft // 60
    else :
        time_aft_s = time_aft
        time_aft_m = 0

    if end_rst == 'win' :
        lab_end_txt.config(text=f'난이도 : {lv}\n축하드립니다 !\n전부 맞추셨습니다.')
    elif end_rst == 'lose' :
        lab_end_txt.config(text=f'난이도 : {lv}\n남은 목숨이 없어\n실패하셨습니다.')
    elif end_rst == 'time over' :
        lab_end_txt.config(text=f'난이도 : {lv}\n남은 시간이 없어\n실패하셨습니다.')
    elif end_rst == 'time over inf' :
        lab_end_txt.config(text=f'무한모드 종료\n맞은 알파벳 갯수 : {rst_alp}개\n 유지 시간 : {int(time_aft_m)}분 {int(time_aft_s)} 초')
    else:
        end_txt = ''

def mod_nomal() : # 알파벳 텍스트 라벨 재 실행
    global alp_txt
    alp_txt = ''
    r1, r2, r3 = r_1, r_2, r_3
    for i in alp :
        if i != r1 and i != r2 and i != r3 :
            alp_txt = alp_txt + i + ' '
    label_alp.config(text=alp_txt)

# 난이도 설명 텍스트

def txt_h_on(event) : # 난이도 어려움 설명
    lab_lv_txt.config(text='난이도 : 어려움\n제한시간 : 20초\n목숨 : 2개')
    lab_lv_txt.place(x=300, y=200)
    btn_mov_r.place_forget()

def txt_n_on(event) : # 난이도 보통 설명
    lab_lv_txt.config(text='난이도 : 보통\n제한시간 : 30초\n목숨 : 3개')
    lab_lv_txt.place(x=300, y=200)
    btn_mov_r.place_forget()

def txt_e_on(event) : # 난이도 쉬움 설명
    lab_lv_txt.config(text='난이도 : 쉬움\n제한시간 : 40초\n목숨 : 5개')
    lab_lv_txt.place(x=300, y=200)
    btn_mov_r.place_forget()

def txt_tu_on(event) : # 연습 모드 설명
    lab_lv_txt.config(text='난이도 : 연습\n제한시간 : 없음\n정답을 전부 맞추면 리셋된다')
    lab_lv_txt.place(x=300, y=200)
    btn_mov_r.place_forget()

def txt_inf_on(event) : # 무한 모드 설명
    lab_lv_txt.config(text='난이도 : 무한\n제한시간 : 10초\n자세한건 규칙 참고\n(아래 규칙 버튼을 눌러서 이동)', font=(n_font, 20))
    lab_lv_txt.place(x=300, y=200)
    btn_mov_r.pack()
    btn_mov_r.place(x=505, y=545)
 
def lv_txt_of(event=None) : # 텍스트 숨기기
    lab_lv_txt.place_forget()
    btn_mov_r.place_forget()
 
def lv_txt_of_inf(event) :  # 무한모드 규칙 버튼 제외 텍스트 숨기기
    lab_lv_txt.place_forget()

def mov_inf_rule() : #규칙 창으로 이동하기
    rule_window()
    r_txt_inf_on()
    btn_mov_lv.pack()
    btn_mov_lv.place(x=565, y=545)

def mov_re_lv() : # 난이도 창으로 돌아가기
    level_window()
    lv_txt_of()

# 규칙 설명 텍스트

def r_txt_game_on() : # 기본  게임 설명
    lab_rule_txt.config(text=r_game)
    lab_rule_txt.place(x=150, y=0)
    btn_mov_lv.place_forget()

def r_txt_play_on() : # 기본 모드 설명
    lab_rule_txt.config(text=r_play)
    lab_rule_txt.place(x=150, y=0)
    btn_mov_lv.place_forget()

def r_txt_tut_on() : # 연습 모드 설명
    lab_rule_txt.config(text=r_tut)
    lab_rule_txt.place(x=150, y=0)
    btn_mov_lv.place_forget()

def r_txt_inf_on() : # 무한 모드 설명
    lab_rule_txt.config(text=r_inf)
    lab_rule_txt.place(x=150, y=0)

def r_rule_txt_of() : # 만들었지만 사용 안함(쓸 예정)
    lab_rule_txt.place_forget()

# 무한모드 함수

def alp_reset_inf() : # 무한모드 알파벳 재 배열
    alp_st_all()
    mod_inf()

def answer_inf(event=None) : # 무한모드 답안 처리
    global rst_alp
    global ans_tr_inf
    global time_left

    user_input_inf = entry_inf.get()
    user_input_inf = user_input_inf.upper()
    

    if user_input_inf in ans_tr_inf :
            ans_tr_inf.remove(user_input_inf)
            rst_alp = rst_alp + 1
            time_left = time_left + 3
            entry_inf.delete(0,tk.END)
    else:
        time_left = time_left - 5

    lab_rst_alp_inf.config(text=f'맟힌 알파벳 : {rst_alp}개')
    entry_inf.delete(0, tk.END)

    if not ans_tr_inf :
        time_left = time_left + 5
        alp_reset_inf()

def timer_inf() : # 무한모드 제한시간
    global time_left
    global end_rst
    global time_aft
    global time_inf
    if time_left > 0:
        time_left -= 1
        time_aft += 1
        label_time_inf.config(text=f"남은 시간: {time_left} 초", font=(n_font, 15), relief='solid')
        time_inf = root.after(1000, timer_inf)
    else:
        time_left = 0
        label_time_inf.config(text=f"남은 시간: {time_left} 초", font=(n_font, 15), relief='solid')
        
        end_rst = 'time over inf'
        if time_inf is not None:
            root.after_cancel(time_inf)
            t.sleep(1)
            rst_()
            end_window()   

def mod_inf() : # 무한모드 알파벳 텍스트 라벨 재 실행
    global alp_txt
    alp_txt = ''
    r1, r2, r3 = r_1, r_2, r_3
    for i in alp :
        if i != r1 and i != r2 and i != r3 :
            alp_txt = alp_txt + i + ' '
    label_alp_inf.config(text=alp_txt)

# 연습모드 함수
def tut_time_pl() : # 시간 증가
    global time_left
    time_left += 10
    label_time_tut.config(text=f"남은 시간: {time_left} 초")

def tut_time_ma() : # 시간 감소
    global time_left
    if time_left >= 10:
        time_left -= 10
        label_time_tut.config(text=f"남은 시간: {time_left} 초")

def show_alp() : # 알파벳 보기 버튼 텍스트 변경
    global show_alphabet_state
    if show_alphabet_state :
        label_alp_txt.config(text="", relief=None) 
        btn_show_alp.config(text="사라진 알파벳 보기")
        show_alphabet_state = False
    else :
        label_alp_txt.config(text=ans_tr, relief='groove')
        btn_show_alp.config(text="사라진 알파벳 숨기기")
        show_alphabet_state = True

def start_txt() : # 타이머 버튼 텍스트 변경
    global start_time_txt
    if start_time_txt : 
        btn_start_timer.config(text="타이머 시작")
        start_time_txt = False
    else :
        btn_start_timer.config(text="타이머 중지")
        start_time_txt = True
    
def start_timer() : # 시작 버튼 눌라면 타이머 작동
    global time_left
    if time_left > 0 :
        if time_tut is not None :
            if btn_start_timer.cget('text') == '타이머 중지' :
                root.after_cancel(time_tut)
                start_txt()
            else :
                start_txt()
                timer_tut()
            pass
        else :
            timer_tut()
            start_txt() 

def alp_reset_tut() : # 연습모드 알파벳 재 배열
    alp_st_all()
    label_alp_txt.config(text=ans_tr, relief='groove')
    mod_tut()

def answer_tut(event=None) : # 연습모드 답안 처리
    global rst_alp
    global ans_tr_tut
    global time_left

    user_input_tut = entry_tut.get()
    user_input_tut = user_input_tut.upper()
    

    if user_input_tut in ans_tr_tut :
            ans_tr_tut.remove(user_input_tut)
            rst_alp += 1
            entry_tut.delete(0,tk.END)

    lab_rst_alp_tut.config(text=f'맟힌 알파벳 : {rst_alp}개')
    entry_tut.delete(0, tk.END)

    if not ans_tr_tut :
        alp_reset_tut()
        mod_tut

def timer_tut() : # 연습모드 제한시간
    global time_left
    global end_rst
    global time_aft
    global time_tut
    if time_left > 0:
        time_left -= 1
        time_aft += 1
        label_time_tut.config(text=f"남은 시간: {time_left} 초", font=(n_font, 15), relief='solid')
        time_tut = root.after(1000, timer_tut)    
    else :
        label_time_tut.config(text=f"남은 시간: 0 초", font=(n_font, 15), relief='solid')
        start_txt()
        root.after_cancel(time_tut)
        time_tut = None

def mod_tut() : # 연습모드 알파벳 텍스트 라벨 재 실행
    global alp_txt
    alp_txt = ''
    r1, r2, r3 = r_1, r_2, r_3
    for i in alp :
        if i != r1 and i != r2 and i != r3 :
            alp_txt = alp_txt + i + ' '
    label_alp_tut.config(text=alp_txt)

# 변수 정의 
start_time_txt = False
show_alphabet_state = False
setting_window = None
font_window = None
time = None
time_inf = None
time_tut = None
left_alp = 3
life = 3
time_left = 0
time_aft = 0
time_aft_s = 0
time_aft_m = 0
ans = ''
n_font = 'Times New Roman'
end_txt = ''
end_rst = ''
r_1 = ''
r_2 = ''
r_3 = ''
rst_alp = 0
ans_tr = []
ans_tr_inf = [] 
ans_tr_tut = []
lv = ''
r_play = '기본모드\n난이도 별로 제한시간이 다르고\n난이도에는\n - 어려움[hard] : 제한시간 20초 / 목숨[life] : 2개\n -  보통[nomal] : 제한시간 30초 / 목숨[life] : 3개\n -   쉬움[easy]   : 제한시간 40초 / 목숨[life] : 5개\n가있다'
r_tut = '연습모드\n제한시간을 설정할 수 있다\n(끝나도 결과화면으로 넘어가지 않는다)\n사라진 알파벳보기 버튼으로\n사라진 알파벳을 볼 수 있다\n숨기기 버튼으로 숨길 수 있다\n(3개를 맞춘 후 버튼을 다시 눌러 초기화 해야 한다)'
r_inf = '무한모드\n기본시간 10초를 가지고 시작한다\n사라진 알파벳을 찾으면 제한시간에 변동이 생긴다\n - 맞출경우 : [제한시간] 3초 추가.\n - 틀릴경우 : [제한시간] 5초 감소.\n - 3개 다 찾을경우 : [제한시간] 5초 증가.\n(제한시간은 상한선이 없다)'
r_game = '게임의 기본 설명\n사라진 알파벳 3개를 찾아야 하는 게임이다\n목숨은 틀리면 차감되고\n난이도에 따라 다르게 가지고 시작한다.\n(무한,연습모드에선 목숨이 없고 차감되지 않는다)\n게임 모드에는 일반, 무한, 연습이 있다\n(자새한건 각 모드의 설명에 나와있다)'

# 프레임 (창)
frame_main = tk.Frame(root, width=800, height=600, bg='gray80')
frame_rule = tk.Frame(root, width=800, height=600, bg='white')
frame_level = tk.Frame(root, width=800, height=600, bg='gray80')
frame_play = tk.Frame(root, width=800, height=600, bg='white')
frame_tut = tk.Frame(root, width=800, height=600, bg='white')
frame_inf = tk.Frame(root, width=800, height=600, bg='white')
frame_end = tk.Frame(root, width=800, height=600, bg='white')


# 기본화면
root.title('사라진 알파벳 게임')
root.resizable(False, False)
   
main_window() #기본화면 표시

# 메인화면

# 라벨
lab_g_name = tk.Label(frame_main, text='사라진\n알파벳\n게임', font=(n_font, 60), bg='white', fg='black', relief='solid')
lab_g_name.pack()
lab_g_name.place(x=50, y=150)

# 버튼
btn_r = tk.Button(frame_main, text='규칙', font=(n_font, 20), bg='gray95', fg='black', command=rule_window)
btn_r.pack()
btn_r.place(x=500, y=150)
btn_p = tk.Button(frame_main, text='플레이', font=(n_font, 20), bg='gray95', fg='black', command=level_window)
btn_p.pack()
btn_p.place(x=500, y=250)
btn_st = tk.Button(frame_main, text='설정', font=(n_font, 15), bg='gray95', fg='black', relief='groove', command=setting_on)
btn_st.pack()
btn_st.place(x=742, y=0)
btn_end = tk.Button(frame_main, text='종료', font=(n_font, 20), bg='gray95', fg='black', command=program_end)
btn_end.pack()
btn_end.place(x=500, y=350)



#규칙화면

# 라벨
lab_can_rule = tk.Label(frame_rule, text='', bg='gray95', width=21, height=40, relief='solid')
lab_can_rule.pack()
lab_can_rule.place(x=0, y=0)
lab_rule_txt = tk.Label(frame_rule, text='', font=(n_font, 20), bg='gray95', fg='black',width=43, height=20, relief='solid')
lab_rule_txt.pack()
lab_rule_txt.place(x=150, y=0)

# 버튼
btn_rule_game = tk.Button(frame_rule, text='기본  규칙', font=(n_font, 20), bg='white', fg='black', relief='groove',command=r_txt_game_on)
btn_rule_game.pack()
btn_rule_game.place(x=4, y=3)
btn_rule_play = tk.Button(frame_rule, text='기본  모드', font=(n_font, 20), bg='white', fg='black', relief='groove',command=r_txt_play_on)
btn_rule_play.pack()
btn_rule_play.place(x=4, y=58)
btn_rule_inf = tk.Button(frame_rule, text='무한  모드', font=(n_font, 20), bg='white', fg='black', relief='groove',command=r_txt_inf_on)
btn_rule_inf.pack()
btn_rule_inf.place(x=4, y=113)
btn_rule_tut = tk.Button(frame_rule, text='연습  모드', font=(n_font, 20), bg='white', fg='black', relief='groove',command=r_txt_tut_on)
btn_rule_tut.pack()
btn_rule_tut.place(x=4, y=168)
btn_mov_lv = tk.Button(frame_rule, text='돌아가기', font=(n_font, 20), bg='gray95', fg='black', relief='groove',command=mov_re_lv)
btn_mov_lv.pack_forget()
btn_mov_lv.place_forget()
btn_main_re_rule = tk.Button(frame_rule, text='나가기', font=(n_font, 20), bg='gray95', relief='groove', command=main_window)
btn_main_re_rule.pack()
btn_main_re_rule.place(x=695, y=545)

# 난이도 화면

# 난이도 선택창 테두리
lab_lv_t = tk.Label(frame_level, text=' ', font=(n_font, 380), bg='gray80', relief='solid')
lab_lv_t.pack()
lab_lv_t.place(x=62, y=20)
 
# 라벨
lab_lv = tk.Label(frame_level, text='난이도', font=(n_font, 31), bg='white', fg='black', relief='solid')
lab_lv.pack()
lab_lv.place(x=64, y=21)


# 난이도별 설명 텍스트 - [ 라벨 ]

lab_lv_txt = tk.Label(frame_level, text='', font=(n_font, 25), bg='gray90', fg='black',relief='groove', width=25, height=5)
lab_lv_txt.pack_forget()

# 버튼
bt_lv_h = tk.Button(frame_level, text='어려움', font=(n_font, 20), bg='gray95', fg='black', relief='groove', command=high)
bt_lv_h.bind("<Enter>", txt_h_on)
bt_lv_h.bind("<Leave>", lv_txt_of)
bt_lv_h.pack()
bt_lv_h.place(x=75, y=300)
bt_lv_n = tk.Button(frame_level, text='보통', font=(n_font, 20), bg='gray95', fg='black', relief='groove', command=nomal)
bt_lv_n.bind("<Enter>", txt_n_on)
bt_lv_n.bind("<Leave>", lv_txt_of)
bt_lv_n.pack()
bt_lv_n.place(x=87, y=200)
bt_lv_e = tk.Button(frame_level, text='쉬움', font=(n_font, 20), bg='gray95', fg='black', relief='groove', command=easy)
bt_lv_e.bind("<Enter>", txt_e_on)
bt_lv_e.bind("<Leave>", lv_txt_of)
bt_lv_e.pack()
bt_lv_e.place(x=87, y=100)
bt_lv_tut = tk.Button(frame_level, text='연습', font=(n_font, 20), bg='gray95', fg='black', relief='groove', command=tut)
bt_lv_tut.bind("<Enter>", txt_tu_on)
bt_lv_tut.bind("<Leave>", lv_txt_of)
bt_lv_tut.pack()
bt_lv_tut.place(x=87, y=500)
bt_lv_inf = tk.Button(frame_level, text='무한', font=(n_font, 20), bg='gray95', fg='black', relief='groove', command=inf)
bt_lv_inf.bind("<Enter>", txt_inf_on)
bt_lv_inf.bind("<Leave>", lv_txt_of_inf)
bt_lv_inf.pack()
bt_lv_inf.place(x=87, y=400)
btn_mov_r = tk.Button(frame_level, text='무한모드 규칙', font=(n_font, 20), bg='gray90', fg='black', relief='groove', command=mov_inf_rule)
btn_mov_r.place_forget()
btn_main_re_lv = tk.Button(frame_level, text='나가기', font=(n_font, 20), bg='gray90', relief='groove', command=main_window)
btn_main_re_lv.pack()
btn_main_re_lv.place(x=695, y=545)

# 기본 모드 플레이 화면

# 기입창
entry = tk.Entry(frame_play, width=40, font=(n_font, 15), bg='gray95', relief='groove')
entry.insert(0, '사라진 알파벳을 입력해주세요.')
entry.bind("<FocusIn>", entry_clk)
entry.bind("<Return>", answer)
entry.pack()
entry.place(x=200, y=300)

# 라벨
label_alp = tk.Label(frame_play, text=alp_txt, font=(n_font, 20), bg='white', relief='groove')
label_alp.pack()
label_alp.place(x=100, y=80)
label_time = tk.Label(frame_play, font=(n_font, 15), bg='white')
label_time.pack()
label_time.place(x=0, y=0)
lab_lft_all = tk.Label(frame_play, text=f'남은 알파벳 : {left_alp}개 / 잔여 목숨 : {life}개', font=(n_font, 15), bg='white', relief='groove')
lab_lft_all.pack()
lab_lft_all.place(x=100,y=53)


# 무한모드 플레아 화면

# 기입창
entry_inf = tk.Entry(frame_inf, width=40, font=(n_font, 15), bg='gray95', relief='groove')
entry_inf.insert(0, '사라진 알파벳을 입력해주세요.')
entry_inf.bind("<FocusIn>", entry_clk_inf)
entry_inf.bind("<Return>", answer_inf)
entry_inf.pack()
entry_inf.place(x=200, y=300)

# 라벨
label_alp_inf = tk.Label(frame_inf, text=alp_txt, font=(n_font, 20), bg='white', relief='groove')
label_alp_inf.pack()
label_alp_inf.place(x=100, y=80)
label_time_inf = tk.Label(frame_inf, font=(n_font, 15), bg='white')
label_time_inf.pack()
label_time_inf.place(x=0, y=0)
lab_rst_alp_inf = tk.Label(frame_inf, text=f'맞힌 알파벳 : {rst_alp}개', font=(n_font, 15), bg='white', relief='groove')
lab_rst_alp_inf.pack()
lab_rst_alp_inf.place(x=100,y=53)

# 연습모드 플레이 화면

# 라벨
label_alp_tut = tk.Label(frame_tut, text=alp_txt, font=(n_font, 20), bg='white', relief='groove')
label_alp_tut.pack()
label_alp_tut.place(x=100, y=80)
label_time_tut = tk.Label(frame_tut, text='', font=(n_font, 15), bg='white')
label_time_tut.pack()
label_time_tut.place(x=0, y=0)
lab_rst_alp_tut = tk.Label(frame_tut, text=f'맞힌 알파벳 : {rst_alp}개', font=(n_font, 15), bg='white', relief='groove')
lab_rst_alp_tut.pack()
lab_rst_alp_tut.place(x=100,y=53)
label_alp_txt = tk.Label(frame_tut, text="", font=(n_font, 20), bg='white')
label_alp_txt.pack()
label_alp_txt.place(x=0, y=320)

# 버튼

btn_time_pl = tk.Button(frame_tut, text="시간 추가 (+10초)", font=(n_font, 10), bg='gray90' , relief='groove', command=tut_time_pl)
btn_time_pl.pack()
btn_time_pl.place(x=0, y=200)

btn_time_ma = tk.Button(frame_tut, text="시간 감소 ( -10초)", font=(n_font, 10), bg='gray90' , relief='groove', command=tut_time_ma)
btn_time_ma.pack()
btn_time_ma.place(x=0, y=225)
                  
btn_show_alp = tk.Button(frame_tut, text="사라진 알파벳 보기", font=(n_font, 10), bg='gray90' , relief='groove', command=show_alp)
btn_show_alp.pack()
btn_show_alp.place(x=0, y=300)

btn_main_re_tut = tk.Button(frame_tut, text='나가기', font=(n_font, 20), bg='gray95', relief='groove', command=level_window)
btn_main_re_tut.pack()
btn_main_re_tut.place(x=695, y=545)

btn_start_timer = tk.Button(frame_tut, text="타이머 시작", font=(n_font, 10), bg='gray90' , relief='groove', command=start_timer)
btn_start_timer.pack()
btn_start_timer.place(x=0, y=250)

# 기입창
entry_tut = tk.Entry(frame_tut, width=40, font=(n_font, 15), bg='gray95', relief='groove')
entry_tut.insert(0, '사라진 알파벳을 입력해주세요.')
entry_tut.bind("<FocusIn>", entry_clk_tut)
entry_tut.bind("<Return>", answer_tut)
entry_tut.pack()
entry_tut.place(x=200, y=300)

# 결산 화면

# 라벨
lab_end_txt = tk.Label(frame_end, text='', font=(n_font, 30), bg='gray95', relief='groove', width=35, height=6)
lab_end_txt.pack()
lab_end_txt.place(x=13, y=100)

# 버튼 
btn_main_re = tk.Button(frame_end, text='메인화면으로', font=(n_font, 20), bg='gray95', relief='groove', command=main_window)
btn_main_re.pack()
btn_main_re.place(x=615, y=545)

# 실행
root.mainloop()
